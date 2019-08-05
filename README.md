# About

I scraped the [University of California's Employee Pay website](https://ucannualwage.ucop.edu/wage/) that provides details on every UC employee and their wages for a given year*.


*While the UCOP reports data begining from 2010, no data from before 2013 has been scraped/parsed yet.

**This project is still a work in progress!**

# Layout

* `\data\` contains a comma-separated text file for each year, representing the entire employee data as reported by the universities.

* `\src` contains source code -- split into two modules -- a retriever, which fetches data from the website, and a parser, that writes it to a CSV file.

* `\tests` contains unit tests. **These are currently in progress!**

