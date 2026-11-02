import argparse
import csv
import json
import logging
import os
import random
import sys
import time

import requests

logger = logging.getLogger(__name__)
logging.basicConfig(filename="ucop.log", encoding="utf-8", level=logging.DEBUG)

BASE_URL = "https://ucannualwage.ucop.edu"
SEARCH_URL = BASE_URL + "/wage/search"

# Keys as returned by the server, and the CSV headers they map to (same order).
FIELDS = ["id", "year", "location", "firstname", "lastname", "title",
          "grosspay", "basepay", "overtimepay", "adjustpay"]
COLUMN_NAMES = ["id", "year", "location", "first name", "last name", "title",
                "gross pay", "regular pay", "overtime pay", "other pay"]

MAX_RETRIES = 3


def refresh_session(session: requests.Session) -> None:
    """Drop old cookies and visit the landing page to get fresh ones."""
    session.cookies.clear()
    resp = session.get(BASE_URL + "/wage/", timeout=60)
    resp.raise_for_status()
    logger.debug("Fresh cookies: %s", session.cookies.get_dict())


def make_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": BASE_URL + "/wage/",
        "Origin": BASE_URL,
        "X-Requested-With": "XMLHttpRequest",
    })
    refresh_session(session)
    return session


def parse_response(response: requests.Response) -> dict:
    try:
        # strict=False tolerates the stray control character the server sometimes emits.
        return json.loads(response.text, strict=False)
    except json.JSONDecodeError:
        return json.loads(response.text.replace("'", '"'), strict=False)


def fetch_page(session: requests.Session, year: int, page: int, page_size: int) -> dict:
    payload = {
        "op": "search",
        "page": page,
        "rows": page_size,        # old parameter name
        "pageSize": page_size,    # name the server now echoes back
        "sidx": "lastname",
        "sord": "asc",
        "count": 0,
        "year": str(year),
        "firstname": "",
        "location": "ALL",
        "lastname": "",
        "title": "",
        "startSal": "1",
        "endSal": "1000000000",
    }

    for attempt in range(1, MAX_RETRIES + 1):
        response = session.post(SEARCH_URL, json=payload, timeout=120)

        if not response.ok:
            print(f"ERROR: HTTP {response.status_code} {response.reason} on page {page}")
            print("Response body (first 1000 chars):", response.text[:1000])
            sys.exit(2)

        data = parse_response(response)
        if data.get("rows"):
            return data

        print(f"WARNING: page {page} came back empty (attempt {attempt}/{MAX_RETRIES}); "
              "refreshing session and retrying...")
        time.sleep(10 * attempt)
        refresh_session(session)

    print(f"ERROR: page {page} still empty after {MAX_RETRIES} attempts. "
          "Rerun the script to resume from saved pages.")
    sys.exit(3)


def acquire_data(year: int, page_size: int) -> list:
    out_dir = f"output_{year}_ps{page_size}"
    os.makedirs(out_dir, exist_ok=True)

    session = make_session()
    all_pages = []
    page_idx = 1
    total_pages = None

    while total_pages is None or page_idx <= total_pages:
        path = os.path.join(out_dir, f"response_data_{page_idx}.json")

        if os.path.exists(path):  # resume: reuse a page saved by an earlier run
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = fetch_page(session, year, page_idx, page_size)
            with open(path, mode="w", encoding="utf-8") as f:
                json.dump(data, f)
            time.sleep(random.uniform(2, 5))  # be polite to the server

        if total_pages is None:
            total_pages = int(data["total"])
            print(f"Server reports {data['records']} records over {total_pages} pages "
                  f"(pageSize={data.get('pageSize')})")
            if data.get("pageSize") != page_size:
                print(f"WARNING: requested {page_size} rows/page but server used "
                      f"{data.get('pageSize')}. The page-size parameter name may have "
                      f"changed; this will take {total_pages} requests.")

        all_pages.append(data)

        with open("progress.txt", mode="w") as progress_file:
            progress_file.write(f"Queried page {page_idx} of {total_pages}")
        if page_idx % 25 == 0:
            print(f"  page {page_idx} / {total_pages}")

        page_idx += 1

    print(f"Finished querying {len(all_pages)} pages for year {year}")
    return all_pages


def parse_salary_data_to_csv(pages: list, year: int) -> None:
    output_csv_filename = f"UCOP_Data_{year}.csv"
    total = 0

    with open(output_csv_filename, mode="w", encoding="utf-8", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(COLUMN_NAMES)

        for page in pages:
            for row in page["rows"]:
                writer.writerow([row[field] for field in FIELDS])
                total += 1

    expected = pages[0]["records"] if pages else 0
    print(f"Wrote {total} records to '{output_csv_filename}' "
          f"({os.path.getsize(output_csv_filename)} bytes)")
    if total != expected:
        print(f"WARNING: server reported {expected} records but only {total} were received.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", type=int, required=True,
                        help="The year you wish to download salary data for.")
    parser.add_argument("-p", "--page-size", type=int, default=1000,
                        help="Rows to request per page (default 1000). Use 20 if larger sizes are ignored.")
    args = parser.parse_args()

    pages = acquire_data(args.year, args.page_size)
    parse_salary_data_to_csv(pages, args.year)