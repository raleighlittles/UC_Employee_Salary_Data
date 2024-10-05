import argparse
import os
import pandas
import sqlalchemy
import pdb
import sys
import locale


def create_database_from_csv(csv_dir_name: str):
    """
    Searches the given directory for CSV files, and combines them all into a single database
    """

    csv_dir = os.fsencode(csv_dir_name)

    combined_dataframe = pandas.DataFrame()

    # needed for logging later
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    for csv_file in os.listdir(csv_dir):

        csv_filename = os.fsdecode(csv_file)

        # the "1" at the end is to remove the period ('.') from the extension
        file_extension = os.path.splitext(csv_filename)[-1][1:]

        if file_extension.lower() == "csv":

            # pdb.set_trace()

            print(f"[DEBUG] Encountered CSV file '{csv_filename}'..")

            # The CSV parsing is a little bit ugly; there's 2 main cases that cause issues:
            # (1) A comma inside of a quoted string -- for example if a user's last name has a suffix
            # their name will appear as 'KENNEDY, JR', 'JOHN'
            # and the parsing engine will sometimes choke thinking it saw 3 columns instead of 2.
            # (2) to solve case 1 we can try to tell pandas to treat an apostrophe (') as the quote character,
            # but this causes issues in cases where an apostrophe appears in a person's last name, e.g. 'O'BRIEN'. To truly get around this we have to tell pandas to ignored escaped apostrophes
            try:
                curr_csv = pandas.read_csv(filepath_or_buffer=os.path.join(
                    csv_dir_name, csv_filename), sep=",", quotechar="'", escapechar="\\")

            except pandas.errors.ParserError as exc_1:
                print(f"[ERROR] Couldn't parse CSV file: '{exc_1}'")
                print("Will now try falling back to double quote as quotechar")

                try:
                    curr_csv = pandas.read_csv(filepath_or_buffer=os.path.join(
                        csv_dir_name, csv_filename), sep=",", quotechar='"')

                except pandas.errors.ParserError as exc_2:
                    print(
                        f"[ERROR] Failed parsing CSV file for a second time. Exception: {exc_2}")
                    sys.exit(1)

            print(
                f"Loaded CSV file successfully! Found '{locale.format_string('%d', curr_csv.size, grouping=True)}' rows and '{len(curr_csv.columns)}' columns")

            combined_dataframe = pandas.concat([combined_dataframe, curr_csv])

        else:
            print(
                f"[WARN] Skipping '{csv_filename}' as it is not a valid CSV file")

    db_engine = sqlalchemy.create_engine(
        f"sqlite:///uc_employee_salaries.sqlite")
    combined_dataframe.to_sql(
        name="salaries", con=db_engine, index=True, index_label="record_id")

    print(
        f"[DEBUG] Finished creating database file with {locale.format_string('%d', combined_dataframe.size, grouping=True)} rows")


if __name__ == "__main__":

    argparse_parser = argparse.ArgumentParser()

    argparse_parser.add_argument("-d", "--directory", type=str,
                                 help="The directory to search for CSV files", required=True)

    argparse_args = argparse_parser.parse_args()

    create_database_from_csv(argparse_args.directory)
