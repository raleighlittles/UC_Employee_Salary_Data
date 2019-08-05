import ast # Used to convert double quotes to single quotes in JSON.
import json

import requests
import re


def acquire_data(year: int) -> dict:
    """
    Issues a POST request to the UC annual website to retrieve all possible employee financial data.

    :return:
    """
    base_url = "https://ucannualwage.ucop.edu"
    search_url : str = base_url + "/wage/search.action"

    # Request headers copied of out Chrome's devtools.
    request_headers = {
        "Host" : re.sub('https://', '', base_url),
        "Content-Length" : '255',
        "Origin" : base_url,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "DNT": "1",
        "Referer": base_url + "/wage/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US, en; q=0.8;q=0.6",
        "Cookie": "JSESSIONID=0000Uq2FDN8doIsM5DBz4pU0xzd:169l0fmr2"
    }

    # Dummy request payload. Searches over all locations to search for any employee receiving between 1 and
    # 1 billion dollars in salary (aka, everyone).
    payload = "_search=false&nd=1497757924608&rows=" + "10000000" + "&page=1&sidx=EAW_LST_NAM&sord=asc&year=" + str(year) + "&location=ALL&firstname=&lastname=&title=&startSal=1&endSal=1000000000"

    session = requests.Session()
    response = session.post(search_url, headers=request_headers, data=payload)

    try:
        response.raise_for_status()

    except requests.HTTPError as e:
        print("ERROR: ", e)
        exit(1)

    valid_json = json.dumps(ast.literal_eval(response.text))

    return json.loads(valid_json)



