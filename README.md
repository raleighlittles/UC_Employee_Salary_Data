# About

I scraped the [University of California's Employee Pay website](https://ucannualwage.ucop.edu/wage/) that provides details on every UC employee and their wages for a given year*.

Data is available for the following years: 2010 thru 2021.

# Usage

Run:

```bash
$ python3 uc_employee_salary_downloader.py <year>
```

and you'll get a file named "UCOP_Data.csv" in the current directory.


# Layout

* `data` contains a comma-separated text file for each year, representing the entire employee data as reported by the universities.

* `analysis` contains graphs of salaries per year (and the corresponding R code used to create it). Here's an example of one such plot:

![2021-graph](./analysis/2021_data.svg)
