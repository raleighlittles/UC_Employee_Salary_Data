import csv

def parse(data : dict):
    """
    Takes a Python object that holds every employee's salary data; extracts that into a CSV file.

    :param data: Python dict. See tests for example JSON format that is expected.
    :return: Nothing
    """
    # These come from website's form.
    column_names = ["id", "year", "location", "first name", "last name", "title", "gross pay", "regular pay", "overtime pay", "other pay"]

    number_of_requests_to_search_over = data['records']

    data_records : list = data["rows"]

    with open("UCOP_Data.csv", "w") as csv_file_object:
        csv_writer = csv.writer(csv_file_object, delimiter=",")

        # Write column names to CSV
        csv_writer.writerow(column_names)

        for employee_record in data_records:

            employee_data : list = employee_record["cell"]

            assert(len(employee_data) == len(column_names))

            csv_writer.writerow(employee_data)
