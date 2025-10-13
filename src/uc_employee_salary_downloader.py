import argparse
import csv
import json
import requests
import time
import os
import random
import sys

import logging

# Can't use requests library with HTTP 2.0 yet as required by the UCOP server

logger = logging.getLogger(__name__)
logging.basicConfig(filename='ucop.log', encoding='utf-8', level=logging.DEBUG)

ONE_MINUTE_TO_SECONDS = 60

def acquire_data(year: int) -> dict:
    """
    Issues a POST request to the UC annual website to retrieve all possible employee financial data.

    :return:
    """
    base_url: str = "https://ucannualwage.ucop.edu"
    search_url: str = base_url + "/wage/search"

    # Request headers copied out of Chrome's devtools.
    request_headers = {
        "Host": "ucannualwage.ucop.edu",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Referer": "https://ucannualwage.ucop.edu/wage/",
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "180",
        "Origin": "https://ucannualwage.ucop.edu",
        "Connection": "keep-alive",
        "Cookie": "JSESSIONID=7432E58D426F2B1E1170E08FA11312A1; AWSALB=5OEZRpd1N+jIHcgFgfya2eiJHVGQyl9vSHr8s/0Ynq7oyh3qggSHTy4n4FovTTuA97J3yNVoWQHmqCqYX61xzvn9rtsftyjAHUDtqqTh3mRjwyhW1V4drtHeM5NZ; AWSALBCORS=5OEZRpd1N+jIHcgFgfya2eiJHVGQyl9vSHr8s/0Ynq7oyh3qggSHTy4n4FovTTuA97J3yNVoWQHmqCqYX61xzvn9rtsftyjAHUDtqqTh3mRjwyhW1V4drtHeM5NZ",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Priority": "u=0",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "trailers"
    }

    response_data_all_pages = list()

    # Have to paginate results
    page_idx = 1
    num_results_per_page = 10000

    while True:

        # Dummy request payload. Searches over all locations to search for any employee receiving between 1 and
        # 1 billion dollars in salary (aka, everyone).
        payload= {"op":"search","page":1,"rows":20,"sidx":"lastname","sord":"asc","count":0,"year":"2024","firstname":"","location":"ALL","lastname":"","title":"","startSal":"1","endSal":"1000000"}

        session = requests.Session()
        response = session.post(
            search_url, headers=request_headers, data=payload, timeout=60)

        try:
            response.raise_for_status()

        except requests.HTTPError as err:
            print("ERROR: ", err)
            import pdb; pdb.set_trace()
            sys.exit(2)

        # Despite the response type being "text/json", calling `response.json()` fails immediately with the following error message:
        # json.errors.JSONDecodeError: Expecting property name enclosed in double quotes: line 2 column 1 (char 2)
        # Thus, we convert the response.text object to have double quotes instead of single quotes.
        # Additionally, there is an errant control character somehow embedded in response.text, which gives the error:
        # json.decoder.JSONDecodeError: Invalid control character at: line 185849 column 69 (char 22761096)
        # To override this, we must set the 'strict' property to false.
        # See: https://docs.python.org/3/library/json.html#json.JSONDecoder
        # 'If strict is false...'

        curr_response_data = json.loads(response.text.replace("\'", "\"").encode('utf-8'),
                                        strict=False)

        # The server returned a response, but the response didn't contain any results -- must've happened because
        # the pagination had reached the end.
        if len(curr_response_data["rows"]) == 0:
            break

        response_data_all_pages.append(curr_response_data)

        # print(f"[DEBUG] Queried page {page_idx}..")
        with open("progress.txt", mode="w") as progress_file:  # overwrite mode, not append
            progress_file.write(f"Queried page {page_idx}..")

        # Log the server's JSON responses for each page, to a directory - in case there's an issue with the server timing out,
        # you can start from that page index next time rather than starting all over again
        server_responses_dir = "output"
        os.mkdir(server_responses_dir)

        server_resp_filename = os.path.join(
            server_responses_dir, f"response_data_{page_idx}.json")

        with open(server_resp_filename, mode="w", encoding="utf-8") as response_file:
            json.dump(curr_response_data, response_file, indent=4)

        page_idx += 1
        # Sleep to avoid overloading server and getting throttled
        time.sleep(ONE_MINUTE_TO_SECONDS / random.randint(2, 6))

    print(f"[DEBUG] Finished querying '{
          page_idx}' pages worth of UCOP data for year '{year}'")

    return response_data_all_pages


def parse_salary_data_to_csv(response_data_list, year: int) -> None:
    """

    """
    # These come from website's form
    column_names = [
        "id", "year", "location", "first name", "last name", "title",
        "gross pay", "regular pay", "overtime pay", "other pay"
    ]

    output_csv_filename = f"UCOP_Data_{year}.csv"
    total_num_records = 0

    with open(file=output_csv_filename, mode="w", encoding="utf-8") as csv_file_object:

        csv_writer = csv.writer(csv_file_object, delimiter=",")
        csv_writer.writerow(column_names)

        for response_data_idx, response_data in enumerate(response_data_list):

            number_of_requests_to_search_over = response_data["records"]
            data_records: list = response_data["rows"]
            total_num_records += len(data_records)

            for employee_record in data_records:

                employee_data: list = employee_record["cell"]

                assert (len(employee_data) == len(column_names))

                csv_writer.writerow(employee_data)

    print(f"[DEBUG]: Finished writing '{total_num_records}' records to file '{
          output_csv_filename}', size='{os.path.getsize(output_csv_filename)}' bytes")


if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()

    argparse_parser.add_argument(
        "-y", "--year", type=int, help="The year you wish to download salary data for.", required=True)

    argparse_args = argparse_parser.parse_args()

    queried_salary_data = acquire_data(argparse_args.year)
    print(f"[DEBUG] Finished querying data for '{argparse_args.year}'")

    parse_salary_data_to_csv(queried_salary_data, argparse_args.year)
