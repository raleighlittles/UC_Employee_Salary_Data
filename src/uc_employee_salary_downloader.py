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
ROWS_PER_PAGE = 10000
OUTPUT_DIR = "output"


def build_session() -> requests.Session:
    """Create a session with browser-like headers and fresh cookies."""
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": BASE_URL + "/wage/",
        "Origin": BASE_URL,
        "X-Requested-With": "XMLHttpRequest",
    })
    # Visit the landing page first so the server issues fresh JSESSIONID / AWSALB cookies.
    resp = session.get(BASE_URL + "/wage/", timeout=60)
    resp.raise_for_status()
    logger.debug("Initial cookies: %s", session.cookies.get_dict())
    return session


def parse_response(response: requests.Response) -> dict:
    """Parse the server's JSON, falling back to the old single-quote hack if needed."""
    try:
        # strict=False tolerates the stray control character the server sometimes emits.
        return json.loads(response.text, strict=False)
    except json.JSONDecodeError:
        return json.loads(response.text.replace("'", '"'), strict=False)


def acquire_data(year: int) -> list:
    """Query every page of results for the given year."""
    session = build_session()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_pages = []
    page_idx = 1

    while True:
        # Searches all locations for anyone earning between $1 and $1 billion (i.e. everyone).
        payload = {
            "op": "search",
            "page": page_idx,
            "rows": ROWS_PER_PAGE,
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

        # json= serializes the body and sets Content-Type/Content-Length correctly.
        response = session.post(SEARCH_URL, json=payload, timeout=120)

        if not response.ok:
            print(f"ERROR: HTTP {response.status_code} {response.reason}")
            print("Response headers:", dict(response.headers))
            print("Response body (first 1000 chars):", response.text[:1000])
            sys.exit(2)

        data = parse_response(response)

        if len(data["rows"]) == 0:
            break

        all_pages.append(data)

        with open("progress.txt", mode="w") as progress_file:
            progress_file.write(f"Queried page {page_idx}..")

        # Save each page so a failure doesn't mean starting over.
        path = os.path.join(OUTPUT_DIR, f"response_data_{page_idx}.json")
        with open(path, mode="w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        # Stop if the server reports this was the last page.
        total_pages = data.get("total")
        if total_pages is not None and page_idx >= int(total_pages):
            break

        page_idx += 1
        time.sleep(60 / random.randint(2, 6))

    print(f"[DEBUG] Finished querying {page_idx} pages of UCOP data for year {year}")
    return all_pages


def parse_salary_data_to_csv(response_data_list, year: int) -> None:
    column_names = [
        "id", "year", "location", "first name", "last name", "title",
        "gross pay", "regular pay", "overtime pay", "other pay",
    ]

    output_csv_filename = f"UCOP_Data_{year}.csv"
    total_num_records = 0

    with open(output_csv_filename, mode="w", encoding="utf-8", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerow(column_names)

        for response_data in response_data_list:
            for employee_record in response_data["rows"]:
                employee_data = employee_record["cell"]
                assert len(employee_data) == len(column_names), employee_data
                csv_writer.writerow(employee_data)
                total_num_records += 1

    size = os.path.getsize(output_csv_filename)
    print(f"[DEBUG] Wrote {total_num_records} records to '{output_csv_filename}', size={size} bytes")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", type=int, required=True,
                        help="The year you wish to download salary data for.")
    args = parser.parse_args()

    queried_salary_data = acquire_data(args.year)
    parse_salary_data_to_csv(queried_salary_data, args.year)
