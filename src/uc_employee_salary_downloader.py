import argparse
import csv
import json
import requests
import time
import os
import random

ONE_MINUTE_TO_SECONDS = 60

def acquire_data(year: int) -> dict:
    """
    Issues a POST request to the UC annual website to retrieve all possible employee financial data.

    :return:
    """
    base_url: str = "https://ucannualwage.ucop.edu"
    search_url: str = base_url + "/wage/search.do"

    # Request headers copied of out Chrome's devtools.
    request_headers = {
        "Content-Length": '255',
        "Origin": base_url,
        "User-Agent":
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": base_url + "/wage/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US, en; q=0.8;q=0.6",
        "Cookie": "JSESSIONID=3BB001A8BF120628A6F641D288077941; AWSALB=GvmQ6hPGjEHx/PVbH1sxDajfAd+y+7trNGbNantJEfsd9NGs7SiaqZTDL8KrXqDIqlujscbyzbHVsEZZBPaKk7/DRWmAR7HxDlcqNqWPe6xjCxNq/GReVErKeQ7A; AWSALBCORS=GvmQ6hPGjEHx/PVbH1sxDajfAd+y+7trNGbNantJEfsd9NGs7SiaqZTDL8KrXqDIqlujscbyzbHVsEZZBPaKk7/DRWmAR7HxDlcqNqWPe6xjCxNq/GReVErKeQ7A"
    }

    response_data = list()

    # Have to paginate results
    page_idx = 1

    while True:

        # Dummy request payload. Searches over all locations to search for any employee receiving between 1 and
        # 1 billion dollars in salary (aka, everyone).
        payload = "_search=false&nd=1724651055477&rows=" + "10000" + f"&page={page_idx}&sidx=EAW_LST_NAM&sord=asc&year=" + str(
            year
        ) + "&location=ALL&firstname=&lastname=&title=&startSal=1&endSal=1000000000"

        session = requests.Session()
        response = session.post(search_url, headers=request_headers, data=payload, timeout=20)

        try:
            response.raise_for_status()

        except requests.HTTPError as err:
            print("ERROR: ", err)
            break

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
        
        response_data.append(curr_response_data)

        # print(f"[DEBUG] Queried page {page_idx}..")
        with open("progress.txt", mode="w") as progress_file: # overwrite mode, not append
            progress_file.write(f"Queried page {page_idx}..")

        output_filename = os.path.join("output", f"response_data_{page_idx}.json")

        with open(output_filename, mode="w") as response_file:
            json.dump(curr_response_data, response_file, indent=4)

        page_idx += 1
        # Sleep to avoid overloading server and getting throttled
        time.sleep(ONE_MINUTE_TO_SECONDS / random.randint(2, 6))

    print(f"[DEBUG] Finished querying '{page_idx}' pages worth of UCOP data for year '{year}'")

    return response_data


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

    print(f"[DEBUG]: Finished writing '{total_num_records}' records to file '{output_csv_filename}', size='{os.path.getsize(output_csv_filename)}' bytes")


if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()

    argparse_parser.add_argument(
        "-y", "--year", type=int, help="The year you wish to download salary data for.", required=True)

    argparse_args = argparse_parser.parse_args()

    queried_salary_data = acquire_data(argparse_args.year)
    print(f"[DEBUG] Finished querying data for '{argparse_args.year}'")

    parse_salary_data_to_csv(queried_salary_data, argparse_args.year)
