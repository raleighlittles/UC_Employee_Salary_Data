# About

I scraped the [University of California's Employee Pay website](https://ucannualwage.ucop.edu/wage/) that provides details on every UC employee and their wages for a given year*.

Data is available for the years **2010* through *2023*. I do a annual Github release that contains a SQL database that combines all salary data for known years, including that previous year, e.g. 2023's release contains 2010 - 2022 data.

# Scraper

The aforementioned UCOP website lets you view or search specific records, but it doesn't have a way to export records at all.

I wrote a Python script that essentially queries the entire database and then saves it to a [CSV file](https://en.wikipedia.org/wiki/Comma-separated_values).

To run the script yourself see the usage info below:

```
usage: uc_employee_salary_downloader.py [-h] [-y YEAR]

options:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR  The year you wish to download salary data for.
```

Example: if you run

`$ python3 uc_employee_salary_downloader.py -y 2022`

you'll get a file named "UCOP_Data_2022.csv" in the current directory containing all salary information for that year.

Here's what that CSV file looks like:

```
id,year,location,first name,last name,title,gross pay,regular pay,overtime pay,other pay
1,2022,ASUCLA,*****,*****,STDT 1,309.00,309.00,0.00,0.00
2,2022,Berkeley,*****,*****,GSR-FULL FEE REM,41705.00,41705.00,0.00,0.00
3,2022,Berkeley,*****,*****,ASSOC IN __ -AY-1/10-GSHIP,3104.00,3104.00,0.00,0.00
```

(see FAQ below)

# Layout

* `data` contains a comma-separated text file for each year, representing the entire employee data as reported by the universities.

* `analysis` contains graphs of salaries per year (and the corresponding R code used to create it). Here's an example of one such plot:

![2021-graph](./analysis/2021_data.svg)

# FAQ

> Q1: When does data get released?

Typically there's about a 9 month lag for the data to be published, i.e the previous year's data is made available by September of the following year.

> Q2: What's up with the weird 'titles'?

The UCOP assigned job titles for student types are odd. See `docs` for a list of them, but you can also just search "Academic Titles UCOP" to figure out what they mean.

> Q3: Why are some of the first and last name fields missing ("*****") ?

Due to [FERPA](https://en.wikipedia.org/wiki/Family_Educational_Rights_and_Privacy_Act) restrictions, the names of students (this includes both undergraduates and graduates!) names are censored, replaced with 5 asterisks instead. In the example CSV I listed you'll see that the titles are all student related.


# Future/Roadmap

- [ ] Tests
- [ ] Parameterize R script
- [ ] Better visualizations (see d3.js)
- [ ] Generate combined database (probably SQL)