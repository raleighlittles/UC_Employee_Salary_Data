import os
import json

import uc_employee_salary_downloader


if __name__ == "__main__":

    json_data = list()

    for filename in os.listdir("output"):
        if filename.endswith(".json"):
            file_path = os.path.join("output", filename)

            with open(file_path, 'r') as f:
                try:
                    json_data.append(json.load(f))

                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from file {filename}: {e}")

    uc_employee_salary_downloader.parse_salary_data_to_csv(json_data, 2023)

