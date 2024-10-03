import csv

def parse_input_to_csv(input_str, output_csv):
    rows = []
    current_row = []

    for line in input_str.splitlines():
        stripped_line = line.strip()

        if stripped_line.startswith(","):
            # Csv row cannot start with commas
            stripped_line = stripped_line[1:]

        # Detect the start of a new row
        if stripped_line == "TR":
            if current_row:  # Save the previous row if any
                rows.append(current_row)
                current_row = []

        # Collect text inside the P (block) lines
        elif stripped_line.startswith('"') and stripped_line.endswith('"'):
            text = stripped_line.strip('"')
            current_row.append(text)

    # Append the last row if it exists
    if current_row:
        rows.append(current_row)

    # Write rows to a CSV file
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(f"CSV saved to {output_csv}")

# Example input
input_str = """
      TR
        TH
          P (block)
            ""
            "ACADEMIC ADMINISTRATOR I "
        TD
          P (block)
            ""
            "001061 "
        TD
          P (block)
            ""
            "34 "
        TD
          P (block)
            ""
            "S56 "
        TD
          P (block)
            ""
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            "ACADEMIC ADMINISTRATOR I NEX "
        TD
          P (block)
            "000961 "
        TD
          P (block)
            "34N "
        TD
          P (block)
            "S56 "
        TD
          P (block)
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            ""
            "ACADEMIC ADMINISTRATOR II "
        TD
          P (block)
            ""
            "001062 "
        TD
          P (block)
            ""
            "34 "
        TD
          P (block)
            ""
            "S56 "
        TD
          P (block)
            ""
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            "ACADEMIC ADMINISTRATOR II NEX "
        TD
          P (block)
            "000962 "
        TD
          P (block)
            "34N "
        TD
          P (block)
            "S56 "
        TD
          P (block)
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            ""
            "ACADEMIC ADMINISTRATOR III "
        TD
          P (block)
            ""
            "001063 "
        TD
          P (block)
            ""
            "34 "
        TD
          P (block)
            ""
            "S56 "
        TD
          P (block)
            ""
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            "ACADEMIC ADMINISTRATOR III NEX "
        TD
          P (block)
            "000963 "
        TD
          P (block)
            "34N "
        TD
          P (block)
            "S56 "
        TD
          P (block)
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            ""
            "ACADEMIC ADMINISTRATOR IV "
        TD
          P (block)
            ""
            "001064 "
        TD
          P (block)
            ""
            "34 "
        TD
          P (block)
            ""
            "S56 "
        TD
          P (block)
            ""
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            "ACADEMIC ADMINISTRATOR IV NEX "
        TD
          P (block)
            "000964 "
        TD
          P (block)
            "34N "
        TD
          P (block)
            "S56 "
        TD
          P (block)
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            ""
            "ACADEMIC ADMINISTRATOR V "
        TD
          P (block)
            ""
            "001065 "
        TD
          P (block)
            ""
            "34 "
        TD
          P (block)
            ""
            "S56 "
        TD
          P (block)
            ""
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            "ACADEMIC ADMINISTRATOR V NEX "
        TD
          P (block)
            "000965 "
        TD
          P (block)
            "34N "
        TD
          P (block)
            "S56 "
        TD
          P (block)
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            ""
            "ACADEMIC ADMINISTRATOR VI "
        TD
          P (block)
            ""
            "001066 "
        TD
          P (block)
            ""
            "34 "
        TD
          P (block)
            ""
            "S56 "
        TD
          P (block)
            ""
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            "ACADEMIC ADMINISTRATOR VI NEX "
        TD
          P (block)
            "000966 "
        TD
          P (block)
            "34N "
        TD
          P (block)
            "S56 "
        TD
          P (block)
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            ""
            "ACADEMIC ADMINISTRATOR VII "
        TD
          P (block)
            ""
            "001067 "
        TD
          P (block)
            ""
            "34 "
        TD
          P (block)
            ""
            "S56 "
        TD
          P (block)
            ""
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            "ACADEMIC ADMINISTRATOR VII NEX "
        TD
          P (block)
            "000967 "
        TD
          P (block)
            "34N "
        TD
          P (block)
            "S56 "
        TD
          P (block)
            "ACADEMIC-ADMINISTRATOR "
      TR
        TH
          P (block)
            ""
            "ACADEMIC ASST TO CHANC "
        TD
          P (block)
            ""
            "000801 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "ACADEMIC ASST TO VICE CHANC "
        TD
          P (block)
            "000800 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "ACADEMIC COORD I-AY "
        TD
          P (block)
            ""
            "000840 "
        TD
          P (block)
            ""
            "35 "
        TD
          P (block)
            ""
            "S46 "
        TD
          P (block)
            ""
            "ACADEMIC COORDINATOR "
      TR
        TH
          P (block)
            "ACADEMIC COORD I-AY NEX "
        TD
          P (block)
            "000850 "
        TD
          P (block)
            "** "
        TD
          P (block)
            "S46 "
        TD
          P (block)
            "ACADEMIC COORDINATOR "
      TR
        TH
          P (block)
            ""
            "ACADEMIC COORD I-FY "
        TD
          P (block)
            ""
            "000841 "
        TD
          P (block)
            ""
            "36 "
        TD
          P (block)
            ""
            "S46 "
        TD
          P (block)
            ""
            "ACADEMIC COORDINATOR "
      TR
        TH
          P (block)
            "ACADEMIC COORD I-FY NEX "
        TD
          P (block)
            "000851 "
        TD
          P (block)
            "36N "
        TD
          P (block)
            "S46 "
        TD
          P (block)
            "ACADEMIC COORDINATOR "
      TR
        TH
          P (block)
            ""
            "ACADEMIC COORD II-AY "
        TD
          P (block)
            ""
            "000842 "
        TD
          P (block)
            ""
            "35 "
        TD
          P (block)
            ""
            "S46 "
        TD
          P (block)
            ""
            "ACADEMIC COORDINATOR "
      TR
        TH
          P (block)
            "ACADEMIC COORD II-AY NEX "
        TD
          P (block)
            "000852 "
        TD
          P (block)
            "** "
        TD
          P (block)
            "S46 "
        TD
          P (block)
            "ACADEMIC COORDINATOR "
      TR
        TH
          P (block)
            ""
            "ACADEMIC COORD II-FY "
        TD
          P (block)
            ""
            "000843 "
        TD
          P (block)
            ""
            "36 "
        TD
          P (block)
            ""
            "S46 "
        TD
          P (block)
            ""
            "ACADEMIC COORDINATOR "
      TR
        TH
          P (block)
            "ACADEMIC COORD II-FY NEX "
        TD
          P (block)
            "000853 "
        TD
          P (block)
            "36N "
        TD
          P (block)
            "S46 "
        TD
          P (block)
            "ACADEMIC COORDINATOR "
      TR
        TH
          P (block)
            ""
            "ACADEMIC COORD III-AY "
        TD
          P (block)
            ""
            "000844 "
        TD
          P (block)
            ""
            "35 "
        TD
          P (block)
            ""
            "S46 "
        TD
          P (block)
            ""
            "ACADEMIC COORDINATOR "
      TR
        TH
          P (block)
            "ACADEMIC COORD III-AY NEX "
        TD
          P (block)
            "000854 "
        TD
          P (block)
            "** "
        TD
          P (block)
            "S46 "
        TD
          P (block)
            "ACADEMIC COORDINATOR "
      TR
        TH
          P (block)
            ""
            "ACADEMIC COORD III-FY "
        TD
          P (block)
            ""
            "000845 "
        TD
          P (block)
            ""
            "36 "
        TD
          P (block)
            ""
            "S46 "
        TD
          P (block)
            ""
            "ACADEMIC COORDINATOR "
      TR
        TH
          P (block)
            "ACADEMIC COORD III-FY NEX "
        TD
          P (block)
            "000855 "
        TD
          P (block)
            "36N "
        TD
          P (block)
            "S46 "
        TD
          P (block)
            "ACADEMIC COORDINATOR "
      TR
        TH
          P (block)
            ""
            "ACT AGRON AES "
        TD
          P (block)
            ""
            "003007 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "534 "
        TD
          P (block)
            ""
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            "ACT AGRON AES-AY "
        TD
          P (block)
            "003064 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "534 "
        TD
          P (block)
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            ""
            "ACT AGRON AES-B/E/E "
        TD
          P (block)
            ""
            "003044 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "534 "
        TD
          P (block)
            ""
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            "ACT AGRON AES-B/E/E-AY "
        TD
          P (block)
            "003066 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "534 "
        TD
          P (block)
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            ""
            "ACT AGRON AES-SFT-VM "
        TD
          P (block)
            ""
            "003009 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "534 "
        TD
          P (block)
            ""
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            "ACT ASSOC AGRON AES "
        TD
          P (block)
            "003017 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "534 "
        TD
          P (block)
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            ""
            "ACT ASSOC AGRON AES-AY "
        TD
          P (block)
            ""
            "003074 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "534 "
        TD
          P (block)
            ""
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            "ACT ASSOC AGRON AES-B/E/E "
        TD
          P (block)
            "003045 "
        TD
          P (block)
            "4 "
        TD
          P (block)
            "534 "
        TD
          P (block)
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            ""
            "ACT ASSOC AGRON AES-B/E/E-AY "
        TD
          P (block)
            ""
            "003076 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "534 "
        TD
          P (block)
            ""
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            "ACT ASSOC AGRON AES-SFT-VM "
        TD
          P (block)
            "003019 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "534 "
        TD
          P (block)
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            ""
            "ACT ASSOC PROF OF TEACH-AY "
        TD
          P (block)
            ""
            "001581 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "214 "
        TD
          P (block)
            ""
            "ACTING PROF OF TEACHING - SOE "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            "ACT ASSOC PROF OF TEACH-FY "
        TD
          P (block)
            "001584 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "214 "
        TD
          P (block)
            "ACTING PROF OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "ACT ASSOC PROF OF TEACH-HCOMP "
        TD
          P (block)
            ""
            "001598 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "214 "
        TD
          P (block)
            ""
            "ACTING PROF OF TEACHING - SOE "
      TR
        TH
          P (block)
            "ACT ASSOC PROF OF TEACH-SFT-VM "
        TD
          P (block)
            "001595 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "214 "
        TD
          P (block)
            "ACTING PROF OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "ACT ASSOC PROF TEACH-AY-B/E/E "
        TD
          P (block)
            ""
            "001587 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "214 "
        TD
          P (block)
            ""
            "ACTING PROF OF TEACHING - SOE "
      TR
        TH
          P (block)
            "ACT ASSOC PROF TEACH-FY-B/E/E "
        TD
          P (block)
            "001590 "
        TD
          P (block)
            "4 "
        TD
          P (block)
            "214 "
        TD
          P (block)
            "ACTING PROF OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "ACT ASSOC PROF-AY "
        TD
          P (block)
            ""
            "001207 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "114 "
        TD
          P (block)
            ""
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            "ACT ASSOC PROF-AY-1/9 "
        TD
          P (block)
            "001201 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "114 "
        TD
          P (block)
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            ""
            "ACT ASSOC PROF-AY-1/9-B/E/E "
        TD
          P (block)
            ""
            "001976 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "114 "
        TD
          P (block)
            ""
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            "ACT ASSOC PROF-AY-B/E/E "
        TD
          P (block)
            "001974 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "114 "
        TD
          P (block)
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            ""
            "ACT ASSOC PROF-FY "
        TD
          P (block)
            ""
            "001217 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "114 "
        TD
          P (block)
            ""
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            "ACT ASSOC PROF-FY-B/E/E "
        TD
          P (block)
            "001975 "
        TD
          P (block)
            "4 "
        TD
          P (block)
            "114 "
        TD
          P (block)
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            ""
            "ACT ASSOC PROF-HCOMP "
        TD
          P (block)
            ""
            "001540 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "114 "
        TD
          P (block)
            ""
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            "ACT ASSOC PROF-SFT-VM "
        TD
          P (block)
            "001900 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "114 "
        TD
          P (block)
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            ""
            "ACT ASST AGRON AES "
        TD
          P (block)
            ""
            "003027 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "534 "
        TD
          P (block)
            ""
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            "ACT ASST AGRON AES-AY "
        TD
          P (block)
            "003084 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "534 "
        TD
          P (block)
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            ""
            "ACT ASST AGRON AES-B/E/E "
        TD
          P (block)
            ""
            "003046 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "534 "
        TD
          P (block)
            ""
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            "ACT ASST AGRON AES-B/E/E/-AY "
        TD
          P (block)
            "003086 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "534 "
        TD
          P (block)
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            ""
            "ACT ASST AGRON AES-SFT-VM "
        TD
          P (block)
            ""
            "003029 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "534 "
        TD
          P (block)
            ""
            "AGRONOMIST-ACTING "
      TR
        TH
          P (block)
            "ACT ASST PROF OF TEACH-AY "
        TD
          P (block)
            "001582 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "224 "
        TD
          P (block)
            "ACTING PROF OF TEACHING - PSOE "
      TR
        TH
          P (block)
            ""
            "ACT ASST PROF OF TEACH-AY-LAW "
        TD
          P (block)
            ""
            "001593 "
        TD
          P (block)
            ""
            "8 "
        TD
          P (block)
            ""
            "224 "
        TD
          P (block)
            ""
            "ACTING PROF OF TEACHING - PSOE "
      TR
        TH
          P (block)
            "ACT ASST PROF OF TEACH-FY "
        TD
          P (block)
            "001585 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "224 "
        TD
          P (block)
            "ACTING PROF OF TEACHING - PSOE "
      TR
        TH
          P (block)
            ""
            "ACT ASST PROF OF TEACH-HCOMP "
        TD
          P (block)
            ""
            "001599 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "224 "
        TD
          P (block)
            ""
            "ACTING PROF OF TEACHING - PSOE "
      TR
        TH
          P (block)
            "ACT ASST PROF OF TEACH-SFT-VM "
        TD
          P (block)
            "001596 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "224 "
        TD
          P (block)
            "ACTING PROF OF TEACHING - PSOE "
      TR
        TH
          P (block)
            ""
            "ACT ASST PROF TEACH-AY-B/E/E "
        TD
          P (block)
            ""
            "001588 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "224 "
        TD
          P (block)
            ""
            "ACTING PROF OF TEACHING - PSOE "
      TR
        TH
          P (block)
            "ACT ASST PROF TEACH-FY-B/E/E "
        TD
          P (block)
            "001591 "
        TD
          P (block)
            "4 "
        TD
          P (block)
            "224 "
        TD
          P (block)
            "ACTING PROF OF TEACHING - PSOE "
      TR
        TH
          P (block)
            ""
            "ACT ASST PROF-AY "
        TD
          P (block)
            ""
            "001307 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "124 "
        TD
          P (block)
            ""
            "ACTING PROFESSOR-NON-SENATE "
      TR
        TH
          P (block)
            "ACT ASST PROF-AY-1/9 "
        TD
          P (block)
            "001301 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "124 "
        TD
          P (block)
            "ACTING PROFESSOR-NON-SENATE "
      TR
        TH
          P (block)
            ""
            "ACT ASST PROF-AY-1/9-B/E/E "
        TD
          P (block)
            ""
            "001979 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "124 "
        TD
          P (block)
            ""
            "ACTING PROFESSOR-NON-SENATE "
      TR
        TH
          P (block)
            "ACT ASST PROF-AY-B/E/E "
        TD
          P (block)
            "001977 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "124 "
        TD
          P (block)
            "ACTING PROFESSOR-NON-SENATE "
      TR
        TH
          P (block)
            ""
            "ACT ASST PROF-FY "
        TD
          P (block)
            ""
            "001317 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "124 "
        TD
          P (block)
            ""
            "ACTING PROFESSOR-NON-SENATE "
      TR
        TH
          P (block)
            "ACT ASST PROF-FY-B/E/E "
        TD
          P (block)
            "001978 "
        TD
          P (block)
            "4 "
        TD
          P (block)
            "124 "
        TD
          P (block)
            "ACTING PROFESSOR-NON-SENATE "
      TR
        TH
          P (block)
            ""
            "ACT ASST PROF-HCOMP "
        TD
          P (block)
            ""
            "001564 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "124 "
        TD
          P (block)
            ""
            "ACTING PROFESSOR-NON-SENATE "
      TR
        TH
          P (block)
            "ACT ASST PROF-SFT-VM "
        TD
          P (block)
            "001898 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "124 "
        TD
          P (block)
            "ACTING PROFESSOR-NON-SENATE "
      TR
        TH
          P (block)
            ""
            "ACT PROF OF TEACH-AY "
        TD
          P (block)
            ""
            "001580 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "214 "
        TD
          P (block)
            ""
            "ACTING PROF OF TEACHING - SOE "
      TR
        TH
          P (block)
            "ACT PROF OF TEACH-AY-B/E/E "
        TD
          P (block)
            "001586 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "214 "
        TD
          P (block)
            "ACTING PROF OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "ACT PROF OF TEACH-AY-LAW "
        TD
          P (block)
            ""
            "001592 "
        TD
          P (block)
            ""
            "8 "
        TD
          P (block)
            ""
            "214 "
        TD
          P (block)
            ""
            "ACTING PROF OF TEACHING - SOE "
      TR
        TH
          P (block)
            "ACT PROF OF TEACH-FY "
        TD
          P (block)
            "001583 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "214 "
        TD
          P (block)
            "ACTING PROF OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "ACT PROF OF TEACH-FY-B/E/E "
        TD
          P (block)
            ""
            "001589 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "214 "
        TD
          P (block)
            ""
            "ACTING PROF OF TEACHING - SOE "
      TR
        TH
          P (block)
            "ACT PROF OF TEACH-HCOMP "
        TD
          P (block)
            "001597 "
        TD
          P (block)
            "5 "
        TD
          P (block)
            "214 "
        TD
          P (block)
            "ACTING PROF OF TEACHING - SOE "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            ""
            "ACT PROF OF TEACH-SFT-VM "
        TD
          P (block)
            ""
            "001594 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "214 "
        TD
          P (block)
            ""
            "ACTING PROF OF TEACHING - SOE "
      TR
        TH
          P (block)
            "ACT PROF-AY "
        TD
          P (block)
            "001107 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "114 "
        TD
          P (block)
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            ""
            "ACT PROF-AY-1/9 "
        TD
          P (block)
            ""
            "001101 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "114 "
        TD
          P (block)
            ""
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            "ACT PROF-AY-1/9-B/E/E "
        TD
          P (block)
            "001973 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "114 "
        TD
          P (block)
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            ""
            "ACT PROF-AY-1/9-LAW "
        TD
          P (block)
            ""
            "001183 "
        TD
          P (block)
            ""
            "8 "
        TD
          P (block)
            ""
            "114 "
        TD
          P (block)
            ""
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            "ACT PROF-AY-B/E/E "
        TD
          P (block)
            "001971 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "114 "
        TD
          P (block)
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            ""
            "ACT PROF-AY-LAW "
        TD
          P (block)
            ""
            "001182 "
        TD
          P (block)
            ""
            "8 "
        TD
          P (block)
            ""
            "114 "
        TD
          P (block)
            ""
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            "ACT PROF-FY "
        TD
          P (block)
            "001117 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "114 "
        TD
          P (block)
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            ""
            "ACT PROF-FY-B/E/E "
        TD
          P (block)
            ""
            "001972 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "114 "
        TD
          P (block)
            ""
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            "ACT PROF-HCOMP "
        TD
          P (block)
            "001542 "
        TD
          P (block)
            "5 "
        TD
          P (block)
            "114 "
        TD
          P (block)
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            ""
            "ACT PROF-SFT-VM "
        TD
          P (block)
            ""
            "001902 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "114 "
        TD
          P (block)
            ""
            "ACTING PROFESSOR-SENATE "
      TR
        TH
          P (block)
            "ACT/INTERIM ASSISTANT DEAN "
        TD
          P (block)
            "001027 "
        TD
          P (block)
            " "
        TD
          P (block)
            "S24 "
        TD
          P (block)
            "ACTING DEAN AND ACTING PROVOST "
      TR
        TH
          P (block)
            ""
            "ACT/INTERIM ASSOC DEAN "
        TD
          P (block)
            ""
            "001017 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "S24 "
        TD
          P (block)
            ""
            "ACTING DEAN AND ACTING PROVOST "
      TR
        TH
          P (block)
            "ACT/INTERIM ASSOC DIRECTOR "
        TD
          P (block)
            "000917 "
        TD
          P (block)
            " "
        TD
          P (block)
            "S34 "
        TD
          P (block)
            "ACTING DIRECTOR "
      TR
        TH
          P (block)
            ""
            "ACT/INTERIM ASSOC VICE CHANC "
        TD
          P (block)
            ""
            "000804 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "ACT/INTERIM ASSOC VICE PROVOST "
        TD
          P (block)
            "001087 "
        TD
          P (block)
            " "
        TD
          P (block)
            "S24 "
        TD
          P (block)
            "ACTING DEAN AND ACTING PROVOST "
      TR
        TH
          P (block)
            ""
            "ACT/INTERIM ASST DIRECTOR "
        TD
          P (block)
            ""
            "000927 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "S34 "
        TD
          P (block)
            ""
            "ACTING DIRECTOR "
      TR
        TH
          P (block)
            "ACT/INTERIM COLLEGE PROVOST "
        TD
          P (block)
            "001047 "
        TD
          P (block)
            " "
        TD
          P (block)
            "S24 "
        TD
          P (block)
            "ACTING DEAN AND ACTING PROVOST "
      TR
        TH
          P (block)
            ""
            "ACT/INTERIM DEAN "
        TD
          P (block)
            ""
            "001007 "
        TD
          P (block)
            ""
            "DEAN "
        TD
          P (block)
            ""
            "S24 "
        TD
          P (block)
            ""
            "ACTING DEAN AND ACTING PROVOST "
      TR
        TH
          P (block)
            "ACT/INTERIM DEPARTMENT CHAIR "
        TD
          P (block)
            "001095 "
        TD
          P (block)
            " "
        TD
          P (block)
            "S64 "
        TD
          P (block)
            "ACTING DEPARTMENT CHAIRPERSON "
      TR
        TH
          P (block)
            ""
            "ACT/INTERIM DIRECTOR "
        TD
          P (block)
            ""
            "000907 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "S34 "
        TD
          P (block)
            ""
            "ACTING DIRECTOR "
      TR
        TH
          P (block)
            "ACT/INTERIM DIVISIONAL DEAN "
        TD
          P (block)
            "001037 "
        TD
          P (block)
            " "
        TD
          P (block)
            "S24 "
        TD
          P (block)
            "ACTING DEAN AND ACTING PROVOST "
      TR
        TH
          P (block)
            ""
            "ACT/INTERIM VICE PROVOST "
        TD
          P (block)
            ""
            "001077 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "S24 "
        TD
          P (block)
            ""
            "ACTING DEAN AND ACTING PROVOST "
      TR
        TH
          P (block)
            "ADDL COMP-HGH&OLIVE VIEW MCS "
        TD
          P (block)
            "003990 "
        TD
          P (block)
            " "
        TD
          P (block)
            "999 "
        TD
          P (block)
            "SUPPLEMENTAL PAY CODES "
      TR
        TH
          P (block)
            ""
            "ADJ INSTR-AY "
        TD
          P (block)
            ""
            "003288 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ADJ INSTR-FY "
        TD
          P (block)
            "003289 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ADJ INSTR-HCOMP "
        TD
          P (block)
            ""
            "001727 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ADJ PROF-AY "
        TD
          P (block)
            "003258 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ADJ PROF-AY-1/10 "
        TD
          P (block)
            ""
            "003367 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ADJ PROF-AY-1/10-BEE "
        TD
          P (block)
            "003380 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ADJ PROF-AY-1/9 "
        TD
          P (block)
            ""
            "003363 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ADJ PROF-AY-1/9-B/E/E "
        TD
          P (block)
            "003379 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ADJ PROF-AY-B/E/E "
        TD
          P (block)
            ""
            "003377 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ADJ PROF-FY "
        TD
          P (block)
            "003259 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ADJ PROF-FY-B/E/E "
        TD
          P (block)
            ""
            "003378 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ADJ PROF-HCOMP "
        TD
          P (block)
            "001730 "
        TD
          P (block)
            "5 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ADJ PROF-SFT-VM "
        TD
          P (block)
            ""
            "001910 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ADMIN STIPEND "
        TD
          P (block)
            "001099 "
        TD
          P (block)
            " "
        TD
          P (block)
            "999 "
        TD
          P (block)
            "SUPPLEMENTAL PAY CODES "
      TR
        TH
          P (block)
            ""
            "AGRON AES "
        TD
          P (block)
            ""
            "003000 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "530 "
        TD
          P (block)
            ""
            "AGRONOMIST-TENURE "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            "AGRON AES-AY "
        TD
          P (block)
            "003060 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "530 "
        TD
          P (block)
            "AGRONOMIST-TENURE "
      TR
        TH
          P (block)
            ""
            "AGRON AES-B/E/E "
        TD
          P (block)
            ""
            "003012 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "530 "
        TD
          P (block)
            ""
            "AGRONOMIST-TENURE "
      TR
        TH
          P (block)
            "AGRON AES-B/E/E-AY "
        TD
          P (block)
            "003062 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "530 "
        TD
          P (block)
            "AGRONOMIST-TENURE "
      TR
        TH
          P (block)
            ""
            "AGRON AES-SFT-VM "
        TD
          P (block)
            ""
            "003001 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "530 "
        TD
          P (block)
            ""
            "AGRONOMIST-TENURE "
      TR
        TH
          P (block)
            "ASSOC ADJ PROF-AY "
        TD
          P (block)
            "003268 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ASSOC ADJ PROF-AY-1/10 "
        TD
          P (block)
            ""
            "003366 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ASSOC ADJ PROF-AY-1/10-BEE "
        TD
          P (block)
            "003369 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ASSOC ADJ PROF-AY-1/9 "
        TD
          P (block)
            ""
            "003362 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ASSOC ADJ PROF-AY-1/9-B/E/E "
        TD
          P (block)
            "003376 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ASSOC ADJ PROF-AY-B/E/E "
        TD
          P (block)
            ""
            "003374 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ASSOC ADJ PROF-FY "
        TD
          P (block)
            "003269 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ASSOC ADJ PROF-FY-B/E/E "
        TD
          P (block)
            ""
            "003375 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ASSOC ADJ PROF-HCOMP "
        TD
          P (block)
            "001729 "
        TD
          P (block)
            "5 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ASSOC ADJ PROF-SFT-VM "
        TD
          P (block)
            ""
            "001909 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ASSOC AGRON AES "
        TD
          P (block)
            "003010 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "530 "
        TD
          P (block)
            "AGRONOMIST-TENURE "
      TR
        TH
          P (block)
            ""
            "ASSOC AGRON AES-AY "
        TD
          P (block)
            ""
            "003070 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "530 "
        TD
          P (block)
            ""
            "AGRONOMIST-TENURE "
      TR
        TH
          P (block)
            "ASSOC AGRON AES-AY-B/E/E "
        TD
          P (block)
            "003072 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "530 "
        TD
          P (block)
            "AGRONOMIST-TENURE "
      TR
        TH
          P (block)
            ""
            "ASSOC AGRON AES-B/E/E "
        TD
          P (block)
            ""
            "003013 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "530 "
        TD
          P (block)
            ""
            "AGRONOMIST-TENURE "
      TR
        TH
          P (block)
            "ASSOC AGRON AES-SFT-VM "
        TD
          P (block)
            "003011 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "530 "
        TD
          P (block)
            "AGRONOMIST-TENURE "
      TR
        TH
          P (block)
            ""
            "ASSOC ASTRONOMER "
        TD
          P (block)
            ""
            "003110 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "520 "
        TD
          P (block)
            ""
            "ASTRONOMER-TENURE "
      TR
        TH
          P (block)
            "ASSOC CLIN PROF-VOL "
        TD
          P (block)
            "002037 "
        TD
          P (block)
            " "
        TD
          P (block)
            "346 "
        TD
          P (block)
            "CLINICAL PROFESSOR - VOLUNTEER "
      TR
        TH
          P (block)
            ""
            "ASSOC COLLEGE PROVOST "
        TD
          P (block)
            ""
            "001052 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "S27 "
        TD
          P (block)
            ""
            "PROVOST "
      TR
        TH
          P (block)
            "ASSOC COOP EXT ADVISOR "
        TD
          P (block)
            "003451 "
        TD
          P (block)
            "28 "
        TD
          P (block)
            "728 "
        TD
          P (block)
            "COOPERATIVE EXTENSION ADVISOR "
      TR
        TH
          P (block)
            ""
            "ASSOC COOP EXT ADVISOR NEX "
        TD
          P (block)
            ""
            "003452 "
        TD
          P (block)
            ""
            "28N "
        TD
          P (block)
            ""
            "728 "
        TD
          P (block)
            ""
            "COOPERATIVE EXTENSION ADVISOR "
      TR
        TH
          P (block)
            "ASSOC COORD PUB PROG NON REP "
        TD
          P (block)
            "003559 "
        TD
          P (block)
            "30A "
        TD
          P (block)
            "927 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            ""
            "ASSOC COORD PUBLIC PROG "
        TD
          P (block)
            ""
            "003560 "
        TD
          P (block)
            ""
            "30B "
        TD
          P (block)
            ""
            "927 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            "ASSOC COORD PUBLIC PROG NEX "
        TD
          P (block)
            "003564 "
        TD
          P (block)
            "30B(N) "
        TD
          P (block)
            "927 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            ""
            "ASSOC COORD PUBPROG NEX NONREP "
        TD
          P (block)
            ""
            "003567 "
        TD
          P (block)
            ""
            "30A(N) "
        TD
          P (block)
            ""
            "927 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            "ASSOC CURATOR "
        TD
          P (block)
            "003651 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "927 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            ""
            "ASSOC DEAN "
        TD
          P (block)
            ""
            "001010 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "S21 "
        TD
          P (block)
            ""
            "DEAN "
      TR
        TH
          P (block)
            "ASSOC DEAN-AY "
        TD
          P (block)
            "001011 "
        TD
          P (block)
            " "
        TD
          P (block)
            "S21 "
        TD
          P (block)
            "DEAN "
      TR
        TH
          P (block)
            ""
            "ASSOC DIRECTOR "
        TD
          P (block)
            ""
            "000910 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "S31 "
        TD
          P (block)
            ""
            "DIRECTOR "
      TR
        TH
          P (block)
            "ASSOC DIVISIONAL DEAN "
        TD
          P (block)
            "001032 "
        TD
          P (block)
            " "
        TD
          P (block)
            "S26 "
        TD
          P (block)
            "DIVISIONAL DEAN "
      TR
        TH
          P (block)
            ""
            "ASSOC FLD PROG SUPV "
        TD
          P (block)
            ""
            "003234 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "927 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            "ASSOC IN __ -AY-1/10-GSHIP "
        TD
          P (block)
            "001508 "
        TD
          P (block)
            "19 "
        TD
          P (block)
            "467 "
        TD
          P (block)
            "ASSOCIATE-STUDENT "
      TR
        TH
          P (block)
            ""
            "ASSOC IN __ -AY-1/9-GSHIP "
        TD
          P (block)
            ""
            "001506 "
        TD
          P (block)
            ""
            "19 "
        TD
          P (block)
            ""
            "467 "
        TD
          P (block)
            ""
            "ASSOCIATE-STUDENT "
      TR
        TH
          P (block)
            "ASSOC IN __- FY-GSHIP "
        TD
          P (block)
            "001511 "
        TD
          P (block)
            "19 "
        TD
          P (block)
            "467 "
        TD
          P (block)
            "ASSOCIATE-STUDENT "
      TR
        TH
          P (block)
            ""
            "ASSOC IN ____-AY-GSHIP "
        TD
          P (block)
            ""
            "001501 "
        TD
          P (block)
            ""
            "19 "
        TD
          P (block)
            ""
            "467 "
        TD
          P (block)
            ""
            "ASSOCIATE-STUDENT "
      TR
        TH
          P (block)
            "ASSOC IN __-AY-NON-GSHIP "
        TD
          P (block)
            "001502 "
        TD
          P (block)
            "19 "
        TD
          P (block)
            "467 "
        TD
          P (block)
            "ASSOCIATE-STUDENT "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            ""
            "ASSOC IN __-FY-NON-GSHIP "
        TD
          P (block)
            ""
            "001512 "
        TD
          P (block)
            ""
            "19 "
        TD
          P (block)
            ""
            "467 "
        TD
          P (block)
            ""
            "ASSOCIATE-STUDENT "
      TR
        TH
          P (block)
            "ASSOC IN__-AY- 1/10 -NON-GSHIP "
        TD
          P (block)
            "001509 "
        TD
          P (block)
            "19 "
        TD
          P (block)
            "467 "
        TD
          P (block)
            "ASSOCIATE-STUDENT "
      TR
        TH
          P (block)
            ""
            "ASSOC IN__-AY- 1/9 -NON-GSHIP "
        TD
          P (block)
            ""
            "001507 "
        TD
          P (block)
            ""
            "19 "
        TD
          P (block)
            ""
            "467 "
        TD
          P (block)
            ""
            "ASSOCIATE-STUDENT "
      TR
        TH
          P (block)
            "ASSOC LAW LIBRARIAN "
        TD
          P (block)
            "003639 "
        TD
          P (block)
            " "
        TD
          P (block)
            "627 "
        TD
          P (block)
            "ASSOC & ASST UNIVERSITY LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "ASSOC LAW LIBRARIAN NEX "
        TD
          P (block)
            ""
            "003640 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "627 "
        TD
          P (block)
            ""
            "ASSOC & ASST UNIVERSITY LIBRARIAN "
      TR
        TH
          P (block)
            "ASSOC LIBRARIAN -CAREER STATUS "
        TD
          P (block)
            "003616 "
        TD
          P (block)
            "26B "
        TD
          P (block)
            "621 "
        TD
          P (block)
            "LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "ASSOC LIBRARIAN-CAREER NEX "
        TD
          P (block)
            ""
            "003666 "
        TD
          P (block)
            ""
            "26A/B(N) "
        TD
          P (block)
            ""
            "621 "
        TD
          P (block)
            ""
            "LIBRARIAN "
      TR
        TH
          P (block)
            "ASSOC LIBRARIAN-CAREER NON REP "
        TD
          P (block)
            "003604 "
        TD
          P (block)
            "26A "
        TD
          P (block)
            "621 "
        TD
          P (block)
            "LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "ASSOC LIBRARIAN-POTLCAR NONREP "
        TD
          P (block)
            ""
            "003605 "
        TD
          P (block)
            ""
            "26A "
        TD
          P (block)
            ""
            "621 "
        TD
          P (block)
            ""
            "LIBRARIAN "
      TR
        TH
          P (block)
            "ASSOC LIBRARIAN-POTNTL CAR NEX "
        TD
          P (block)
            "003667 "
        TD
          P (block)
            "26A/B(N) "
        TD
          P (block)
            "621 "
        TD
          P (block)
            "LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "ASSOC LIBRARIAN-POTNTL CAREER "
        TD
          P (block)
            ""
            "003617 "
        TD
          P (block)
            ""
            "26B "
        TD
          P (block)
            ""
            "621 "
        TD
          P (block)
            ""
            "LIBRARIAN "
      TR
        TH
          P (block)
            "ASSOC LIBRARIAN-TEMP NEX "
        TD
          P (block)
            "003668 "
        TD
          P (block)
            "26A/B(N) "
        TD
          P (block)
            "621 "
        TD
          P (block)
            "LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "ASSOC LIBRARIAN-TEMP STATUS "
        TD
          P (block)
            ""
            "003618 "
        TD
          P (block)
            ""
            "26B "
        TD
          P (block)
            ""
            "621 "
        TD
          P (block)
            ""
            "LIBRARIAN "
      TR
        TH
          P (block)
            "ASSOC PROF IN RES-AY "
        TD
          P (block)
            "003260 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF IN RES-AY-1/10-B/E/E "
        TD
          P (block)
            ""
            "003346 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "ASSOC PROF IN RES-AY-1/9 "
        TD
          P (block)
            "003352 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF IN RES-AY-1/9-B/E/E "
        TD
          P (block)
            ""
            "003386 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "ASSOC PROF IN RES-AY-B/E/E "
        TD
          P (block)
            "003384 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF IN RES-FY "
        TD
          P (block)
            ""
            "003261 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "ASSOC PROF IN RES-FY-B/E/E "
        TD
          P (block)
            "003385 "
        TD
          P (block)
            "4 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF IN RES-HCOMP "
        TD
          P (block)
            ""
            "001725 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "ASSOC PROF IN RES-SFT-VM "
        TD
          P (block)
            "001905 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF OF CLIN-FY "
        TD
          P (block)
            ""
            "001451 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "317 "
        TD
          P (block)
            ""
            "PROFESSOR OF CLINICAL __________ "
      TR
        TH
          P (block)
            "ASSOC PROF OF CLIN-HCOMP "
        TD
          P (block)
            "001454 "
        TD
          P (block)
            "5 "
        TD
          P (block)
            "317 "
        TD
          P (block)
            "PROFESSOR OF CLINICAL __________ "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF OF CLIN-SFT-VM "
        TD
          P (block)
            ""
            "001916 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "317 "
        TD
          P (block)
            ""
            "PROFESSOR OF CLINICAL __________ "
      TR
        TH
          P (block)
            "ASSOC PROF OF TEACH-AY "
        TD
          P (block)
            "001607 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "210 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF OF TEACH-AY-1/10 "
        TD
          P (block)
            ""
            "001614 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "210 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            "ASSOC PROF OF TEACH-AY-1/9 "
        TD
          P (block)
            "001608 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "210 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF OF TEACH-AY-B/E/E "
        TD
          P (block)
            ""
            "001687 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "210 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            "ASSOC PROF OF TEACH-FY "
        TD
          P (block)
            "001617 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "210 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF OF TEACH-FY-B/E/E "
        TD
          P (block)
            ""
            "001690 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "210 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            "ASSOC PROF OF TEACH-HCOMP "
        TD
          P (block)
            "001618 "
        TD
          P (block)
            "5 "
        TD
          P (block)
            "210 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF OF TEACH-SFT-VM "
        TD
          P (block)
            ""
            "001669 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "210 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            "ASSOC PROF TEACH-AY-1/10-B/E/E "
        TD
          P (block)
            "001673 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "210 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF TEACH-AY-1/9-B/E/E "
        TD
          P (block)
            ""
            "001695 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "210 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            "ASSOC PROF TEACH-EMERITUS(WOS) "
        TD
          P (block)
            "001620 "
        TD
          P (block)
            " "
        TD
          P (block)
            "216 "
        TD
          P (block)
            "PROFESSOR OF TEACHING-EMERITUS "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF-AY "
        TD
          P (block)
            ""
            "001200 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "010 "
        TD
          P (block)
            ""
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            "ASSOC PROF-AY-1/9 "
        TD
          P (block)
            "001203 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "010 "
        TD
          P (block)
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF-AY-1/9-B/E/E "
        TD
          P (block)
            ""
            "001245 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "010 "
        TD
          P (block)
            ""
            "PROFESSORIAL-TENURE "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            "ASSOC PROF-AY-B/E/E "
        TD
          P (block)
            "001243 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "010 "
        TD
          P (block)
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF-FY "
        TD
          P (block)
            ""
            "001210 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "010 "
        TD
          P (block)
            ""
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            "ASSOC PROF-FY-B/E/E "
        TD
          P (block)
            "001244 "
        TD
          P (block)
            "4 "
        TD
          P (block)
            "010 "
        TD
          P (block)
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROF-HCOMP "
        TD
          P (block)
            ""
            "001719 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "010 "
        TD
          P (block)
            ""
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            "ASSOC PROF-SFT-VM "
        TD
          P (block)
            "001899 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "010 "
        TD
          P (block)
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            ""
            "ASSOC PROJ SCIENTIST (WOS) "
        TD
          P (block)
            ""
            "003488 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "581 "
        TD
          P (block)
            ""
            "PROJECT SERIES "
      TR
        TH
          P (block)
            "ASSOC PROJ SCIENTIST-FY "
        TD
          P (block)
            "003392 "
        TD
          P (block)
            "37B "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
      TR
        TH
          P (block)
            ""
            "ASSOC PROJ SCIENTIST-FY NEX "
        TD
          P (block)
            ""
            "003492 "
        TD
          P (block)
            ""
            "37B(N) "
        TD
          P (block)
            ""
            "581 "
        TD
          P (block)
            ""
            "PROJECT SERIES "
      TR
        TH
          P (block)
            "ASSOC PROJ SCIENTIST-FY-B/E/E "
        TD
          P (block)
            "003393 "
        TD
          P (block)
            "38B "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
      TR
        TH
          P (block)
            ""
            "ASSOC PROJ SCI-FY NEX NON REP "
        TD
          P (block)
            ""
            "003415 "
        TD
          P (block)
            ""
            "37A(N) "
        TD
          P (block)
            ""
            "581 "
        TD
          P (block)
            ""
            "PROJECT SERIES "
      TR
        TH
          P (block)
            "ASSOC PROJ SCI-FY NON REP "
        TD
          P (block)
            "003405 "
        TD
          P (block)
            "37A "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
      TR
        TH
          P (block)
            ""
            "ASSOC PROJ SCI-FY-B/E/E NONREP "
        TD
          P (block)
            ""
            "003406 "
        TD
          P (block)
            ""
            "38A "
        TD
          P (block)
            ""
            "581 "
        TD
          P (block)
            ""
            "PROJECT SERIES "
      TR
        TH
          P (block)
            "ASSOC PROJ SCNTST-FY-B/E/E NEX "
        TD
          P (block)
            "003493 "
        TD
          P (block)
            "38B(N) "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
      TR
        TH
          P (block)
            ""
            "ASSOC PROJSC-FY-BEE NEX NONREP "
        TD
          P (block)
            ""
            "003416 "
        TD
          P (block)
            ""
            "38A(N) "
        TD
          P (block)
            ""
            "581 "
        TD
          P (block)
            ""
            "PROJECT SERIES "
      TR
        TH
          P (block)
            "ASSOC RES (WOS) "
        TD
          P (block)
            "003212 "
        TD
          P (block)
            " "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASSOC RES PROF-MILLER INST-AY "
        TD
          P (block)
            ""
            "003292 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "566 "
        TD
          P (block)
            ""
            "OTHER RESEARCH "
      TR
        TH
          P (block)
            "ASSOC RES PROF-MILLER INST-FY "
        TD
          P (block)
            "003293 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "566 "
        TD
          P (block)
            "OTHER RESEARCH "
      TR
        TH
          P (block)
            ""
            "ASSOC RES SCRIPPS-AY "
        TD
          P (block)
            ""
            "001936 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASSOC RES-FY "
        TD
          P (block)
            "003210 "
        TD
          P (block)
            "13B "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASSOC RES-FY NEX "
        TD
          P (block)
            ""
            "003180 "
        TD
          P (block)
            ""
            "13B(N) "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASSOC RES-FY NEX NON REP "
        TD
          P (block)
            "003181 "
        TD
          P (block)
            "13A(N) "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASSOC RES-FY-B/E/E "
        TD
          P (block)
            ""
            "001988 "
        TD
          P (block)
            ""
            "14B "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASSOC RES-FY-B/E/E NEX "
        TD
          P (block)
            "001998 "
        TD
          P (block)
            "14B(N) "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASSOC RES-FY-B/E/E NEX NON REP "
        TD
          P (block)
            ""
            "002008 "
        TD
          P (block)
            ""
            "14A(N) "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASSOC RES-FY-B/E/E-NON REP "
        TD
          P (block)
            "001994 "
        TD
          P (block)
            "14A "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASSOC RES-FY-NON REP "
        TD
          P (block)
            ""
            "003217 "
        TD
          P (block)
            ""
            "13A "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASSOC RES-LR SCL-AY "
        TD
          P (block)
            "003213 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASSOC RES-LR SCL-AY-1/9 "
        TD
          P (block)
            ""
            "003215 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASSOC RES-LR SCL-AY-1/9-B/E/E "
        TD
          P (block)
            "001984 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASSOC RES-LR SCL-AY-B/E/E "
        TD
          P (block)
            ""
            "001983 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASSOC RES-LR SCL-FY "
        TD
          P (block)
            "003211 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASSOC RES-LR SCL-FY-B/E/E "
        TD
          P (block)
            ""
            "001991 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASSOC RES-SFT "
        TD
          P (block)
            "003216 "
        TD
          P (block)
            " "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASSOC RES-SFT NEX "
        TD
          P (block)
            ""
            "003186 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASSOC SPECIALIST "
        TD
          P (block)
            "003310 "
        TD
          P (block)
            "24B "
        TD
          P (block)
            "551 "
        TD
          P (block)
            "SPECIALIST "
      TR
        TH
          P (block)
            ""
            "ASSOC SPECIALIST (WOS) "
        TD
          P (block)
            ""
            "003312 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "551 "
        TD
          P (block)
            ""
            "SPECIALIST "
      TR
        TH
          P (block)
            "ASSOC SPECIALIST AES "
        TD
          P (block)
            "003014 "
        TD
          P (block)
            "24A "
        TD
          P (block)
            "557 "
        TD
          P (block)
            "SPECIALIST IN A.E.S. "
      TR
        TH
          P (block)
            ""
            "ASSOC SPECIALIST AES NEX "
        TD
          P (block)
            ""
            "003114 "
        TD
          P (block)
            ""
            "24A(N) "
        TD
          P (block)
            ""
            "557 "
        TD
          P (block)
            ""
            "SPECIALIST IN A.E.S. "
      TR
        TH
          P (block)
            "ASSOC SPECIALIST COOP EXT "
        TD
          P (block)
            "003477 "
        TD
          P (block)
            "29 "
        TD
          P (block)
            "729 "
        TD
          P (block)
            "SPECIALIST IN COOPERATIVE EXTENSION "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            ""
            "ASSOC SPECIALIST COOP EXT NEX "
        TD
          P (block)
            ""
            "003478 "
        TD
          P (block)
            ""
            "29N "
        TD
          P (block)
            ""
            "729 "
        TD
          P (block)
            ""
            "SPECIALIST IN COOPERATIVE EXTENSION "
      TR
        TH
          P (block)
            "ASSOC SPECIALIST NEX "
        TD
          P (block)
            "003311 "
        TD
          P (block)
            "24B(N) "
        TD
          P (block)
            "551 "
        TD
          P (block)
            "SPECIALIST "
      TR
        TH
          P (block)
            ""
            "ASSOC SPECIALIST NEX NON REP "
        TD
          P (block)
            ""
            "003314 "
        TD
          P (block)
            ""
            "24A(N) "
        TD
          P (block)
            ""
            "551 "
        TD
          P (block)
            ""
            "SPECIALIST "
      TR
        TH
          P (block)
            "ASSOC SPECIALIST NON REP "
        TD
          P (block)
            "003313 "
        TD
          P (block)
            "24A "
        TD
          P (block)
            "551 "
        TD
          P (block)
            "SPECIALIST "
      TR
        TH
          P (block)
            ""
            "ASSOC UNIV LIBRARIAN "
        TD
          P (block)
            ""
            "003600 "
        TD
          P (block)
            ""
            "27 "
        TD
          P (block)
            ""
            "627 "
        TD
          P (block)
            ""
            "ASSOC & ASST UNIVERSITY LIBRARIAN "
      TR
        TH
          P (block)
            "ASSOC UNIV LIBRARIAN NEX "
        TD
          P (block)
            "003601 "
        TD
          P (block)
            "27N "
        TD
          P (block)
            "627 "
        TD
          P (block)
            "ASSOC & ASST UNIVERSITY LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "ASSOC VICE CHANC "
        TD
          P (block)
            ""
            "000803 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "ASSOC VICE PROVOST "
        TD
          P (block)
            "001069 "
        TD
          P (block)
            " "
        TD
          P (block)
            "S27 "
        TD
          P (block)
            "PROVOST "
      TR
        TH
          P (block)
            ""
            "ASST ADJ PROF-AY "
        TD
          P (block)
            ""
            "003278 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ASST ADJ PROF-AY-1/10 "
        TD
          P (block)
            "003365 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ASST ADJ PROF-AY-1/10-BEE "
        TD
          P (block)
            ""
            "003368 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ASST ADJ PROF-AY-1/9 "
        TD
          P (block)
            "003361 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ASST ADJ PROF-AY-1/9-B/E/E "
        TD
          P (block)
            ""
            "003373 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ASST ADJ PROF-AY-B/E/E "
        TD
          P (block)
            "003371 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ASST ADJ PROF-FY "
        TD
          P (block)
            ""
            "003279 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ASST ADJ PROF-FY-B/E/E "
        TD
          P (block)
            "003372 "
        TD
          P (block)
            "4 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ASST ADJ PROF-HCOMP "
        TD
          P (block)
            ""
            "001728 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "335 "
        TD
          P (block)
            ""
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            "ASST ADJ PROF-SFT-VM "
        TD
          P (block)
            "001908 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "335 "
        TD
          P (block)
            "ADJUNCT PROFESSOR "
      TR
        TH
          P (block)
            ""
            "ASST AGRON AES "
        TD
          P (block)
            ""
            "003020 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "531 "
        TD
          P (block)
            ""
            "AGRONOMIST-NON-TENURE "
      TR
        TH
          P (block)
            "ASST AGRON AES-AY "
        TD
          P (block)
            "003080 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "531 "
        TD
          P (block)
            "AGRONOMIST-NON-TENURE "
      TR
        TH
          P (block)
            ""
            "ASST AGRON AES-AY-B/E/E "
        TD
          P (block)
            ""
            "003082 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "531 "
        TD
          P (block)
            ""
            "AGRONOMIST-NON-TENURE "
      TR
        TH
          P (block)
            "ASST AGRON AES-B/E/E "
        TD
          P (block)
            "003015 "
        TD
          P (block)
            "4 "
        TD
          P (block)
            "531 "
        TD
          P (block)
            "AGRONOMIST-NON-TENURE "
      TR
        TH
          P (block)
            ""
            "ASST AGRON AES-SFT-VM "
        TD
          P (block)
            ""
            "003021 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "531 "
        TD
          P (block)
            ""
            "AGRONOMIST-NON-TENURE "
      TR
        TH
          P (block)
            "ASST CLIN PROF-VOL "
        TD
          P (block)
            "002057 "
        TD
          P (block)
            " "
        TD
          P (block)
            "346 "
        TD
          P (block)
            "CLINICAL PROFESSOR - VOLUNTEER "
      TR
        TH
          P (block)
            ""
            "ASST COLLEGE PROVOST "
        TD
          P (block)
            ""
            "001051 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "S27 "
        TD
          P (block)
            ""
            "PROVOST "
      TR
        TH
          P (block)
            "ASST COOP EXT ADVISOR "
        TD
          P (block)
            "003461 "
        TD
          P (block)
            "28 "
        TD
          P (block)
            "728 "
        TD
          P (block)
            "COOPERATIVE EXTENSION ADVISOR "
      TR
        TH
          P (block)
            ""
            "ASST COOP EXT ADVISOR NEX "
        TD
          P (block)
            ""
            "003462 "
        TD
          P (block)
            ""
            "28N "
        TD
          P (block)
            ""
            "728 "
        TD
          P (block)
            ""
            "COOPERATIVE EXTENSION ADVISOR "
      TR
        TH
          P (block)
            "ASST COORD PUB PROG NEX NONREP "
        TD
          P (block)
            "003568 "
        TD
          P (block)
            "30A(N) "
        TD
          P (block)
            "927 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            ""
            "ASST COORD PUB PROG NON REP "
        TD
          P (block)
            ""
            "003561 "
        TD
          P (block)
            ""
            "30A "
        TD
          P (block)
            ""
            "927 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            "ASST COORD PUBLIC PROG "
        TD
          P (block)
            "003562 "
        TD
          P (block)
            "30B "
        TD
          P (block)
            "927 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            ""
            "ASST COORD PUBLIC PROG NEX "
        TD
          P (block)
            ""
            "003565 "
        TD
          P (block)
            ""
            "30B(N) "
        TD
          P (block)
            ""
            "927 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            "ASST CURATOR "
        TD
          P (block)
            "003652 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "927 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            ""
            "ASST DEAN "
        TD
          P (block)
            ""
            "001020 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "S21 "
        TD
          P (block)
            ""
            "DEAN "
      TR
        TH
          P (block)
            "ASST DIRECTOR "
        TD
          P (block)
            "000920 "
        TD
          P (block)
            " "
        TD
          P (block)
            "S31 "
        TD
          P (block)
            "DIRECTOR "
      TR
        TH
          P (block)
            ""
            "ASST LAW LIBRARIAN "
        TD
          P (block)
            ""
            "003637 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "627 "
        TD
          P (block)
            ""
            "ASSOC & ASST UNIVERSITY LIBRARIAN "
      TR
        TH
          P (block)
            "ASST LAW LIBRARIAN NEX "
        TD
          P (block)
            "003638 "
        TD
          P (block)
            " "
        TD
          P (block)
            "627 "
        TD
          P (block)
            "ASSOC & ASST UNIVERSITY LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "ASST LIBRARIAN-CAREER NEX "
        TD
          P (block)
            ""
            "003670 "
        TD
          P (block)
            ""
            "26A/B(N) "
        TD
          P (block)
            ""
            "621 "
        TD
          P (block)
            ""
            "LIBRARIAN "
      TR
        TH
          P (block)
            "ASST LIBRARIAN-CAREER NON REP "
        TD
          P (block)
            "003606 "
        TD
          P (block)
            "26A "
        TD
          P (block)
            "621 "
        TD
          P (block)
            "LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "ASST LIBRARIAN-CAREER STATUS "
        TD
          P (block)
            ""
            "003620 "
        TD
          P (block)
            ""
            "26B "
        TD
          P (block)
            ""
            "621 "
        TD
          P (block)
            ""
            "LIBRARIAN "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            "ASST LIBRARIAN-POTLCAR NONREP "
        TD
          P (block)
            "003607 "
        TD
          P (block)
            "26A "
        TD
          P (block)
            "621 "
        TD
          P (block)
            "LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "ASST LIBRARIAN-POTNTL CAR NEX "
        TD
          P (block)
            ""
            "003671 "
        TD
          P (block)
            ""
            "26A/B(N) "
        TD
          P (block)
            ""
            "621 "
        TD
          P (block)
            ""
            "LIBRARIAN "
      TR
        TH
          P (block)
            "ASST LIBRARIAN-POTNTL CAREER "
        TD
          P (block)
            "003621 "
        TD
          P (block)
            "26B "
        TD
          P (block)
            "621 "
        TD
          P (block)
            "LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "ASST LIBRARIAN-TEMP STATUS "
        TD
          P (block)
            ""
            "003622 "
        TD
          P (block)
            ""
            "26B "
        TD
          P (block)
            ""
            "621 "
        TD
          P (block)
            ""
            "LIBRARIAN "
      TR
        TH
          P (block)
            "ASST LIBRARIAN-TEMP STATUS NEX "
        TD
          P (block)
            "003672 "
        TD
          P (block)
            "26A/B(N) "
        TD
          P (block)
            "621 "
        TD
          P (block)
            "LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "ASST PROF IN RES-AY "
        TD
          P (block)
            ""
            "003270 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "ASST PROF IN RES-AY-1/10-B/E/E "
        TD
          P (block)
            "003347 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "ASST PROF IN RES-AY-1/9 "
        TD
          P (block)
            ""
            "003351 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "ASST PROF IN RES-AY-1/9-B/E/E "
        TD
          P (block)
            "003389 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "ASST PROF IN RES-AY-B/E/E "
        TD
          P (block)
            ""
            "003387 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "ASST PROF IN RES-FY "
        TD
          P (block)
            "003271 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "ASST PROF IN RES-FY-B/E/E "
        TD
          P (block)
            ""
            "003388 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "ASST PROF IN RES-HCOMP "
        TD
          P (block)
            "001724 "
        TD
          P (block)
            "5 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "ASST PROF IN RES-SFT-VM "
        TD
          P (block)
            ""
            "001904 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "ASST PROF OF CLIN-FY "
        TD
          P (block)
            "001452 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "317 "
        TD
          P (block)
            "PROFESSOR OF CLINICAL __________ "
      TR
        TH
          P (block)
            ""
            "ASST PROF OF CLIN-HCOMP "
        TD
          P (block)
            ""
            "001455 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "317 "
        TD
          P (block)
            ""
            "PROFESSOR OF CLINICAL __________ "
      TR
        TH
          P (block)
            "ASST PROF OF CLIN-SFT-VM "
        TD
          P (block)
            "001915 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "317 "
        TD
          P (block)
            "PROFESSOR OF CLINICAL __________ "
      TR
        TH
          P (block)
            ""
            "ASST PROF OF TEACH-AY "
        TD
          P (block)
            ""
            "001680 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "211 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - PSOE "
      TR
        TH
          P (block)
            "ASST PROF OF TEACH-AY-1/10 "
        TD
          P (block)
            "001678 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "211 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - PSOE "
      TR
        TH
          P (block)
            ""
            "ASST PROF OF TEACH-AY-1/10-LAW "
        TD
          P (block)
            ""
            "001659 "
        TD
          P (block)
            ""
            "8 "
        TD
          P (block)
            ""
            "211 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - PSOE "
      TR
        TH
          P (block)
            "ASST PROF OF TEACH-AY-1/9 "
        TD
          P (block)
            "001681 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "211 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - PSOE "
      TR
        TH
          P (block)
            ""
            "ASST PROF OF TEACH-AY-1/9-LAW "
        TD
          P (block)
            ""
            "001657 "
        TD
          P (block)
            ""
            "8 "
        TD
          P (block)
            ""
            "211 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - PSOE "
      TR
        TH
          P (block)
            "ASST PROF OF TEACH-AY-B/E/E "
        TD
          P (block)
            "001688 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "211 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - PSOE "
      TR
        TH
          P (block)
            ""
            "ASST PROF OF TEACH-AY-LAW "
        TD
          P (block)
            ""
            "001694 "
        TD
          P (block)
            ""
            "8 "
        TD
          P (block)
            ""
            "211 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - PSOE "
      TR
        TH
          P (block)
            "ASST PROF OF TEACH-FY "
        TD
          P (block)
            "001682 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "211 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - PSOE "
      TR
        TH
          P (block)
            ""
            "ASST PROF OF TEACH-FY-B/E/E "
        TD
          P (block)
            ""
            "001691 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "211 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - PSOE "
      TR
        TH
          P (block)
            "ASST PROF OF TEACH-HCOMP "
        TD
          P (block)
            "001679 "
        TD
          P (block)
            "5 "
        TD
          P (block)
            "211 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - PSOE "
      TR
        TH
          P (block)
            ""
            "ASST PROF OF TEACH-SFT-VM "
        TD
          P (block)
            ""
            "001670 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "211 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - PSOE "
      TR
        TH
          P (block)
            "ASST PROF TEACH-AY-1/10-B/E/E "
        TD
          P (block)
            "001674 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "211 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - PSOE "
      TR
        TH
          P (block)
            ""
            "ASST PROF TEACH-AY-1/9-B/E/E "
        TD
          P (block)
            ""
            "001696 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "211 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - PSOE "
      TR
        TH
          P (block)
            "ASST PROF-AY "
        TD
          P (block)
            "001300 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "011 "
        TD
          P (block)
            "PROFESSORIAL-NON-TENURE "
      TR
        TH
          P (block)
            ""
            "ASST PROF-AY-1/9 "
        TD
          P (block)
            ""
            "001303 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "011 "
        TD
          P (block)
            ""
            "PROFESSORIAL-NON-TENURE "
      TR
        TH
          P (block)
            "ASST PROF-AY-1/9-B/E/E "
        TD
          P (block)
            "001345 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "011 "
        TD
          P (block)
            "PROFESSORIAL-NON-TENURE "
      TR
        TH
          P (block)
            ""
            "ASST PROF-AY-B/E/E "
        TD
          P (block)
            ""
            "001343 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "011 "
        TD
          P (block)
            ""
            "PROFESSORIAL-NON-TENURE "
      TR
        TH
          P (block)
            "ASST PROF-FY "
        TD
          P (block)
            "001310 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "011 "
        TD
          P (block)
            "PROFESSORIAL-NON-TENURE "
      TR
        TH
          P (block)
            ""
            "ASST PROF-FY-B/E/E "
        TD
          P (block)
            ""
            "001344 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "011 "
        TD
          P (block)
            ""
            "PROFESSORIAL-NON-TENURE "
      TR
        TH
          P (block)
            "ASST PROF-HCOMP "
        TD
          P (block)
            "001717 "
        TD
          P (block)
            "5 "
        TD
          P (block)
            "011 "
        TD
          P (block)
            "PROFESSORIAL-NON-TENURE "
      TR
        TH
          P (block)
            ""
            "ASST PROF-SFT-VM "
        TD
          P (block)
            ""
            "001897 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "011 "
        TD
          P (block)
            ""
            "PROFESSORIAL-NON-TENURE "
      TR
        TH
          P (block)
            "ASST PROJ SCIENTIST (WOS) "
        TD
          P (block)
            "003489 "
        TD
          P (block)
            " "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            ""
            "ASST PROJ SCIENTIST-FY "
        TD
          P (block)
            ""
            "003394 "
        TD
          P (block)
            ""
            "37B "
        TD
          P (block)
            ""
            "581 "
        TD
          P (block)
            ""
            "PROJECT SERIES "
      TR
        TH
          P (block)
            "ASST PROJ SCIENTIST-FY NEX "
        TD
          P (block)
            "003494 "
        TD
          P (block)
            "37B(N) "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
      TR
        TH
          P (block)
            ""
            "ASST PROJ SCIENTIST-FY NON REP "
        TD
          P (block)
            ""
            "003407 "
        TD
          P (block)
            ""
            "37A "
        TD
          P (block)
            ""
            "581 "
        TD
          P (block)
            ""
            "PROJECT SERIES "
      TR
        TH
          P (block)
            "ASST PROJ SCIENTIST-FY-B/E/E "
        TD
          P (block)
            "003395 "
        TD
          P (block)
            "38B "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
      TR
        TH
          P (block)
            ""
            "ASST PROJ SCI-FY NEX NON REP "
        TD
          P (block)
            ""
            "003417 "
        TD
          P (block)
            ""
            "37A(N) "
        TD
          P (block)
            ""
            "581 "
        TD
          P (block)
            ""
            "PROJECT SERIES "
      TR
        TH
          P (block)
            "ASST PROJ SCI-FY-B/E/E NON REP "
        TD
          P (block)
            "003408 "
        TD
          P (block)
            "38A "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
      TR
        TH
          P (block)
            ""
            "ASST PROJ SCNTST-FY-B/E/E NEX "
        TD
          P (block)
            ""
            "003495 "
        TD
          P (block)
            ""
            "38B(N) "
        TD
          P (block)
            ""
            "581 "
        TD
          P (block)
            ""
            "PROJECT SERIES "
      TR
        TH
          P (block)
            "ASST PROJSCI-FY-BEE NEX NONREP "
        TD
          P (block)
            "003418 "
        TD
          P (block)
            "38A(N) "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
      TR
        TH
          P (block)
            ""
            "ASST RES (WOS) "
        TD
          P (block)
            ""
            "003222 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASST RES SCRIPPS-AY "
        TD
          P (block)
            "001937 "
        TD
          P (block)
            " "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASST RES-FY "
        TD
          P (block)
            ""
            "003220 "
        TD
          P (block)
            ""
            "13B "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASST RES-FY NEX "
        TD
          P (block)
            "003190 "
        TD
          P (block)
            "13B(N) "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASST RES-FY NEX NON REP "
        TD
          P (block)
            ""
            "003191 "
        TD
          P (block)
            ""
            "13A(N) "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASST RES-FY-B/E/E "
        TD
          P (block)
            "001989 "
        TD
          P (block)
            "14B "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASST RES-FY-B/E/E NEX "
        TD
          P (block)
            ""
            "001999 "
        TD
          P (block)
            ""
            "14B(N) "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASST RES-FY-B/E/E NEX NON REP "
        TD
          P (block)
            "002009 "
        TD
          P (block)
            "14A(N) "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASST RES-FY-B/E/E-NON REP "
        TD
          P (block)
            ""
            "001995 "
        TD
          P (block)
            ""
            "14A "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASST RES-FY-NON REP "
        TD
          P (block)
            "003227 "
        TD
          P (block)
            "13A "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASST RES-LR SCL-AY "
        TD
          P (block)
            ""
            "003223 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASST RES-LR SCL-AY-1/9 "
        TD
          P (block)
            "003225 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASST RES-LR SCL-AY-1/9-B/E/E "
        TD
          P (block)
            ""
            "001986 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASST RES-LR SCL-AY-B/E/E "
        TD
          P (block)
            "001985 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASST RES-LR SCL-FY "
        TD
          P (block)
            ""
            "003221 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASST RES-LR SCL-FY-B/E/E "
        TD
          P (block)
            "001992 "
        TD
          P (block)
            "4 "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASST RES-SFT "
        TD
          P (block)
            ""
            "003226 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "ASST RES-SFT NEX "
        TD
          P (block)
            "003196 "
        TD
          P (block)
            " "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "ASST SPECIALIST "
        TD
          P (block)
            ""
            "003320 "
        TD
          P (block)
            ""
            "24B "
        TD
          P (block)
            ""
            "551 "
        TD
          P (block)
            ""
            "SPECIALIST "
      TR
        TH
          P (block)
            "ASST SPECIALIST (WOS) "
        TD
          P (block)
            "003322 "
        TD
          P (block)
            " "
        TD
          P (block)
            "551 "
        TD
          P (block)
            "SPECIALIST "
      TR
        TH
          P (block)
            ""
            "ASST SPECIALIST AES "
        TD
          P (block)
            ""
            "003024 "
        TD
          P (block)
            ""
            "24A "
        TD
          P (block)
            ""
            "557 "
        TD
          P (block)
            ""
            "SPECIALIST IN A.E.S. "
      TR
        TH
          P (block)
            "ASST SPECIALIST AES NEX "
        TD
          P (block)
            "003124 "
        TD
          P (block)
            "24A(N) "
        TD
          P (block)
            "557 "
        TD
          P (block)
            "SPECIALIST IN A.E.S. "
      TR
        TH
          P (block)
            ""
            "ASST SPECIALIST COOP EXT "
        TD
          P (block)
            ""
            "003475 "
        TD
          P (block)
            ""
            "29 "
        TD
          P (block)
            ""
            "729 "
        TD
          P (block)
            ""
            "SPECIALIST IN COOPERATIVE EXTENSION "
      TR
        TH
          P (block)
            "ASST SPECIALIST COOP EXT NEX "
        TD
          P (block)
            "003476 "
        TD
          P (block)
            "29N "
        TD
          P (block)
            "729 "
        TD
          P (block)
            "SPECIALIST IN COOPERATIVE EXTENSION "
      TR
        TH
          P (block)
            ""
            "ASST SPECIALIST NEX "
        TD
          P (block)
            ""
            "003321 "
        TD
          P (block)
            ""
            "24B(N) "
        TD
          P (block)
            ""
            "551 "
        TD
          P (block)
            ""
            "SPECIALIST "
      TR
        TH
          P (block)
            "ASST SPECIALIST NEX NON REP "
        TD
          P (block)
            "003324 "
        TD
          P (block)
            "24A(N) "
        TD
          P (block)
            "551 "
        TD
          P (block)
            "SPECIALIST "
      TR
        TH
          P (block)
            ""
            "ASST SPECIALIST NON REP "
        TD
          P (block)
            ""
            "003323 "
        TD
          P (block)
            ""
            "24A "
        TD
          P (block)
            ""
            "551 "
        TD
          P (block)
            ""
            "SPECIALIST "
      TR
        TH
          P (block)
            "ASST TEACHER-UNEX "
        TD
          P (block)
            "003572 "
        TD
          P (block)
            " "
        TD
          P (block)
            "828 "
        TD
          P (block)
            "UNIVERSITY EXTENSION-OTHER "
      TR
        TH
          P (block)
            ""
            "ASST UNIV LIBRARIAN "
        TD
          P (block)
            ""
            "003610 "
        TD
          P (block)
            ""
            "27 "
        TD
          P (block)
            ""
            "627 "
        TD
          P (block)
            ""
            "ASSOC & ASST UNIVERSITY LIBRARIAN "
      TR
        TH
          P (block)
            "ASST UNIV LIBRARIAN NEX "
        TD
          P (block)
            "003611 "
        TD
          P (block)
            "27N "
        TD
          P (block)
            "627 "
        TD
          P (block)
            "ASSOC & ASST UNIVERSITY LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "ASST VICE CHANC "
        TD
          P (block)
            ""
            "000802 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            "ASTRONOMER "
        TD
          P (block)
            "003100 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "520 "
        TD
          P (block)
            "ASTRONOMER-TENURE "
      TR
        TH
          P (block)
            ""
            "CHAIR-SEN ASMBLY&ACADEMIC CNCL "
        TD
          P (block)
            ""
            "001059 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "CHI GREEN SCHOLAR-UCSD "
        TD
          P (block)
            "003297 "
        TD
          P (block)
            " "
        TD
          P (block)
            "566 "
        TD
          P (block)
            "OTHER RESEARCH "
      TR
        TH
          P (block)
            ""
            "CHIEF RESID PHYS-NON REP "
        TD
          P (block)
            ""
            "002725 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "CHIEF RESID PHYS-REP "
        TD
          P (block)
            "002738 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "CHIEF RESID PHYS-REP-FNO "
        TD
          P (block)
            ""
            "002762 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "CHIEF RESID PHYS-REP-OV "
        TD
          P (block)
            "002745 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "CHILD DEV DEMO LECT "
        TD
          P (block)
            ""
            "002285 "
        TD
          P (block)
            ""
            "15 "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "CHILD DEV DEMO LECT-CONTINUING "
        TD
          P (block)
            "002284 "
        TD
          P (block)
            "16 "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "CLIN ASSOC/ADMITTING PHYSICIAN "
        TD
          P (block)
            ""
            "CWR007 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "CWR "
        TD
          P (block)
            ""
            "CONTINGENT WORKER "
      TR
        TH
          P (block)
            "CLIN ASSOCIATE-FY "
        TD
          P (block)
            "002081 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "CLIN INSTR-VOL "
        TD
          P (block)
            ""
            "002077 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "346 "
        TD
          P (block)
            ""
            "CLINICAL PROFESSOR - VOLUNTEER "
      TR
        TH
          P (block)
            "CLIN PROF-VOL "
        TD
          P (block)
            "002017 "
        TD
          P (block)
            " "
        TD
          P (block)
            "346 "
        TD
          P (block)
            "CLINICAL PROFESSOR - VOLUNTEER "
      TR
        TH
          P (block)
            ""
            "COLLEGE PROVOST "
        TD
          P (block)
            ""
            "001060 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "S27 "
        TD
          P (block)
            ""
            "PROVOST "
      TR
        TH
          P (block)
            "CONTINUING APPT-TEMP AUG-1/9 "
        TD
          P (block)
            "001653 "
        TD
          P (block)
            "16 "
        TD
          P (block)
            "225 "
        TD
          P (block)
            "LECTURER "
      TR
        TH
          P (block)
            ""
            "CONTINUING APPT-TEMP AUG-AY "
        TD
          P (block)
            ""
            "001652 "
        TD
          P (block)
            ""
            "16 "
        TD
          P (block)
            ""
            "225 "
        TD
          P (block)
            ""
            "LECTURER "
      TR
        TH
          P (block)
            "CONTINUING APPT-TEMP AUG-FY "
        TD
          P (block)
            "001655 "
        TD
          P (block)
            "16 "
        TD
          P (block)
            "225 "
        TD
          P (block)
            "LECTURER "
      TR
        TH
          P (block)
            ""
            "CONTINUING APPT-TEMP-AUG-1/10 "
        TD
          P (block)
            ""
            "001654 "
        TD
          P (block)
            ""
            "16 "
        TD
          P (block)
            ""
            "225 "
        TD
          P (block)
            ""
            "LECTURER "
      TR
        TH
          P (block)
            "CONTINUING EDUCATOR I "
        TD
          P (block)
            "003520 "
        TD
          P (block)
            "31 "
        TD
          P (block)
            "825 "
        TD
          P (block)
            "CONTINUING EDUCATOR -UNEX "
      TR
        TH
          P (block)
            ""
            "CONTINUING EDUCATOR I NEX "
        TD
          P (block)
            ""
            "003530 "
        TD
          P (block)
            ""
            "31N "
        TD
          P (block)
            ""
            "825 "
        TD
          P (block)
            ""
            "CONTINUING EDUCATOR -UNEX "
      TR
        TH
          P (block)
            "CONTINUING EDUCATOR II "
        TD
          P (block)
            "003521 "
        TD
          P (block)
            "31 "
        TD
          P (block)
            "825 "
        TD
          P (block)
            "CONTINUING EDUCATOR -UNEX "
      TR
        TH
          P (block)
            ""
            "CONTINUING EDUCATOR II NEX "
        TD
          P (block)
            ""
            "003531 "
        TD
          P (block)
            ""
            "31N "
        TD
          P (block)
            ""
            "825 "
        TD
          P (block)
            ""
            "CONTINUING EDUCATOR -UNEX "
      TR
        TH
          P (block)
            "CONTINUING EDUCATOR III "
        TD
          P (block)
            "003522 "
        TD
          P (block)
            "31 "
        TD
          P (block)
            "825 "
        TD
          P (block)
            "CONTINUING EDUCATOR -UNEX "
      TR
        TH
          P (block)
            ""
            "CONTINUING EDUCATOR III NEX "
        TD
          P (block)
            ""
            "003532 "
        TD
          P (block)
            ""
            "31N "
        TD
          P (block)
            ""
            "825 "
        TD
          P (block)
            ""
            "CONTINUING EDUCATOR -UNEX "
      TR
        TH
          P (block)
            "COOP EXT ADVISOR "
        TD
          P (block)
            "003441 "
        TD
          P (block)
            "28 "
        TD
          P (block)
            "728 "
        TD
          P (block)
            "COOPERATIVE EXTENSION ADVISOR "
      TR
        TH
          P (block)
            ""
            "COOP EXT ADVISOR NEX "
        TD
          P (block)
            ""
            "003442 "
        TD
          P (block)
            ""
            "28N "
        TD
          P (block)
            ""
            "728 "
        TD
          P (block)
            ""
            "COOPERATIVE EXTENSION ADVISOR "
      TR
        TH
          P (block)
            "COORD FLD WK-AY "
        TD
          P (block)
            "002240 "
        TD
          P (block)
            "15 "
        TD
          P (block)
            "357 "
        TD
          P (block)
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            ""
            "COORD FLD WK-AY-CONTINUING "
        TD
          P (block)
            ""
            "002241 "
        TD
          P (block)
            ""
            "16 "
        TD
          P (block)
            ""
            "357 "
        TD
          P (block)
            ""
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            "COORD FLD WK-FY "
        TD
          P (block)
            "002245 "
        TD
          P (block)
            "15 "
        TD
          P (block)
            "357 "
        TD
          P (block)
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            ""
            "COORD FLD WK-FY-CONTINUING "
        TD
          P (block)
            ""
            "002246 "
        TD
          P (block)
            ""
            "16 "
        TD
          P (block)
            ""
            "357 "
        TD
          P (block)
            ""
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            "COORD PUB PROG NEX NON REP "
        TD
          P (block)
            "003566 "
        TD
          P (block)
            "30A(N) "
        TD
          P (block)
            "927 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            ""
            "COORD PUB PROG NON REP "
        TD
          P (block)
            ""
            "003557 "
        TD
          P (block)
            ""
            "30A "
        TD
          P (block)
            ""
            "927 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            "COORD PUBLIC PROG "
        TD
          P (block)
            "003558 "
        TD
          P (block)
            "30B "
        TD
          P (block)
            "927 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            ""
            "COORD PUBLIC PROG NEX "
        TD
          P (block)
            ""
            "003563 "
        TD
          P (block)
            ""
            "30B(N) "
        TD
          P (block)
            ""
            "927 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            "COURSE AUTHOR-UNEX "
        TD
          P (block)
            "003580 "
        TD
          P (block)
            " "
        TD
          P (block)
            "828 "
        TD
          P (block)
            "UNIVERSITY EXTENSION-OTHER "
      TR
        TH
          P (block)
            ""
            "COURSE AUTHOR-UNEX NEX "
        TD
          P (block)
            ""
            "003581 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "828 "
        TD
          P (block)
            ""
            "UNIVERSITY EXTENSION-OTHER "
      TR
        TH
          P (block)
            "CURATOR "
        TD
          P (block)
            "003650 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "927 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            ""
            "DEAN "
        TD
          P (block)
            ""
            "001000 "
        TD
          P (block)
            ""
            "DEAN "
        TD
          P (block)
            ""
            "S21 "
        TD
          P (block)
            ""
            "DEAN "
      TR
        TH
          P (block)
            "DEAN-EXTENDED LEARNING "
        TD
          P (block)
            "001040 "
        TD
          P (block)
            " "
        TD
          P (block)
            "S21 "
        TD
          P (block)
            "DEAN "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            ""
            "DEMO TEACHER "
        TD
          P (block)
            ""
            "002210 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "DEMO TEACHER-CONTINUING "
        TD
          P (block)
            "002211 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "DEPARTMENT CHAIR "
        TD
          P (block)
            ""
            "001096 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "S61 "
        TD
          P (block)
            ""
            "DEPARTMENT CHAIRPERSON "
      TR
        TH
          P (block)
            "DEPARTMENT VICE CHAIR "
        TD
          P (block)
            "001094 "
        TD
          P (block)
            " "
        TD
          P (block)
            "S61 "
        TD
          P (block)
            "DEPARTMENT CHAIRPERSON "
      TR
        TH
          P (block)
            ""
            "DIRECTOR "
        TD
          P (block)
            ""
            "000900 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "S31 "
        TD
          P (block)
            ""
            "DIRECTOR "
      TR
        TH
          P (block)
            "DIRECTOR-EAP STUDY CENTER "
        TD
          P (block)
            "001070 "
        TD
          P (block)
            " "
        TD
          P (block)
            "927 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            ""
            "DIVISIONAL DEAN "
        TD
          P (block)
            ""
            "001030 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "S26 "
        TD
          P (block)
            ""
            "DIVISIONAL DEAN "
      TR
        TH
          P (block)
            "EAP-TEMP FACULTY HOUSING ALLOW "
        TD
          P (block)
            "003995 "
        TD
          P (block)
            " "
        TD
          P (block)
            "999 "
        TD
          P (block)
            "SUPPLEMENTAL PAY CODES "
      TR
        TH
          P (block)
            ""
            "EDUCATOR (WOS) "
        TD
          P (block)
            ""
            "001675 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "FACULTY ADMIN TRANSITION LV-AY "
        TD
          P (block)
            "003900 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "FACULTY ADMIN TRANSITION LV-FY "
        TD
          P (block)
            ""
            "003910 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "FACULTY ADVISOR "
        TD
          P (block)
            "000812 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "FACULTY ASST TO CHANC "
        TD
          P (block)
            ""
            "001044 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "FACULTY ASST TO PROVOST/DEAN "
        TD
          P (block)
            "001055 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "FACULTY ASST TO VICE CHANC "
        TD
          P (block)
            ""
            "001045 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "FACULTY CONSULTANT "
        TD
          P (block)
            "003700 "
        TD
          P (block)
            " "
        TD
          P (block)
            "927 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            ""
            "FACULTY FELLOW RES-AY "
        TD
          P (block)
            ""
            "003237 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "577 "
        TD
          P (block)
            ""
            "POST-GRADUATE RESEARCH-NON-STUDENT "
      TR
        TH
          P (block)
            "FACULTY FELLOW RES-AY-1/9 "
        TD
          P (block)
            "003238 "
        TD
          P (block)
            " "
        TD
          P (block)
            "577 "
        TD
          P (block)
            "POST-GRADUATE RESEARCH-NON-STUDENT "
      TR
        TH
          P (block)
            ""
            "FACULTY RECRUITMENT ALLOW "
        TD
          P (block)
            ""
            "003993 "
        TD
          P (block)
            ""
            "40 "
        TD
          P (block)
            ""
            "999 "
        TD
          P (block)
            ""
            "SUPPLEMENTAL PAY CODES "
      TR
        TH
          P (block)
            "FLD PROG SUPV "
        TD
          P (block)
            "003230 "
        TD
          P (block)
            " "
        TD
          P (block)
            "927 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SERIES "
      TR
        TH
          P (block)
            ""
            "FLD WK CONSULT-AY "
        TD
          P (block)
            ""
            "002260 "
        TD
          P (block)
            ""
            "15 "
        TD
          P (block)
            ""
            "357 "
        TD
          P (block)
            ""
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            "FLD WK CONSULT-AY-CONTINUING "
        TD
          P (block)
            "002261 "
        TD
          P (block)
            "16 "
        TD
          P (block)
            "357 "
        TD
          P (block)
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            ""
            "FLD WK CONSULT-FY "
        TD
          P (block)
            ""
            "002265 "
        TD
          P (block)
            ""
            "15 "
        TD
          P (block)
            ""
            "357 "
        TD
          P (block)
            ""
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            "FLD WK CONSULT-FY-CONTINUING "
        TD
          P (block)
            "002266 "
        TD
          P (block)
            "16 "
        TD
          P (block)
            "357 "
        TD
          P (block)
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            ""
            "FLD WK SUPV-AY "
        TD
          P (block)
            ""
            "002250 "
        TD
          P (block)
            ""
            "15 "
        TD
          P (block)
            ""
            "357 "
        TD
          P (block)
            ""
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            "FLD WK SUPV-AY-CONTINUING "
        TD
          P (block)
            "002251 "
        TD
          P (block)
            "16 "
        TD
          P (block)
            "357 "
        TD
          P (block)
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            ""
            "FLD WK SUPV-FY "
        TD
          P (block)
            ""
            "002255 "
        TD
          P (block)
            ""
            "15 "
        TD
          P (block)
            ""
            "357 "
        TD
          P (block)
            ""
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            "FLD WK SUPV-FY-CONTINUING "
        TD
          P (block)
            "002256 "
        TD
          P (block)
            "16 "
        TD
          P (block)
            "357 "
        TD
          P (block)
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            ""
            "GEFFEN K-12 INSTR SUMMER PROG "
        TD
          P (block)
            ""
            "002434 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "GEFFEN K-12 INSTR-AY-1/10-CONT "
        TD
          P (block)
            "002433 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "GEFFEN K-12 INSTRUCTOR-AY "
        TD
          P (block)
            ""
            "002430 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "GEFFEN K-12 INSTRUCTOR-AY-1/10 "
        TD
          P (block)
            "002432 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "GEFFEN K-12 INSTRUCTOR-AY-CONT "
        TD
          P (block)
            ""
            "002431 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "GRADUATE ADVISOR "
        TD
          P (block)
            "000810 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "GSR TRAINEE/FELLOW SUPPLEMENT "
        TD
          P (block)
            ""
            "003160 "
        TD
          P (block)
            ""
            "22 "
        TD
          P (block)
            ""
            "436 "
        TD
          P (block)
            ""
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            "GSR-FELLOW-NO REM "
        TD
          P (block)
            "003144 "
        TD
          P (block)
            "22 "
        TD
          P (block)
            "436 "
        TD
          P (block)
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            ""
            "GSR-FELLOW-PAID DIR-NO REM "
        TD
          P (block)
            ""
            "003142 "
        TD
          P (block)
            ""
            "22 "
        TD
          P (block)
            ""
            "436 "
        TD
          P (block)
            ""
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            "GSR-FELLOW-PAID DIR-TUIT REM "
        TD
          P (block)
            "003143 "
        TD
          P (block)
            "22 "
        TD
          P (block)
            "436 "
        TD
          P (block)
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            ""
            "GSR-FELLOW-TUIT REM "
        TD
          P (block)
            ""
            "003145 "
        TD
          P (block)
            ""
            "22 "
        TD
          P (block)
            ""
            "436 "
        TD
          P (block)
            ""
            "GRADUATE STUDENT RESEARCHER "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            "GSR-FULL FEE REM "
        TD
          P (block)
            "003282 "
        TD
          P (block)
            "22 "
        TD
          P (block)
            "436 "
        TD
          P (block)
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            ""
            "GSR-FULL TUIT&PARTIAL FEE REM "
        TD
          P (block)
            ""
            "003283 "
        TD
          P (block)
            ""
            "22 "
        TD
          P (block)
            ""
            "436 "
        TD
          P (block)
            ""
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            "GSR-NO REM "
        TD
          P (block)
            "003266 "
        TD
          P (block)
            "22 "
        TD
          P (block)
            "436 "
        TD
          P (block)
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            ""
            "GSR-PARTIAL FEE REM "
        TD
          P (block)
            ""
            "003276 "
        TD
          P (block)
            ""
            "22 "
        TD
          P (block)
            ""
            "436 "
        TD
          P (block)
            ""
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            "GSR-TRAINEE-NO REM "
        TD
          P (block)
            "003154 "
        TD
          P (block)
            "22 "
        TD
          P (block)
            "436 "
        TD
          P (block)
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            ""
            "GSR-TRAINEE-PAID DIR-NO REM "
        TD
          P (block)
            ""
            "003152 "
        TD
          P (block)
            ""
            "22 "
        TD
          P (block)
            ""
            "436 "
        TD
          P (block)
            ""
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            "GSR-TRAINEE-PAID DIR-TUIT REM "
        TD
          P (block)
            "003153 "
        TD
          P (block)
            "22 "
        TD
          P (block)
            "436 "
        TD
          P (block)
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            ""
            "GSR-TRAINEE-TUIT REM "
        TD
          P (block)
            ""
            "003155 "
        TD
          P (block)
            ""
            "22 "
        TD
          P (block)
            ""
            "436 "
        TD
          P (block)
            ""
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            "GSR-TUIT & FEE REM "
        TD
          P (block)
            "003284 "
        TD
          P (block)
            "22 "
        TD
          P (block)
            "436 "
        TD
          P (block)
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            ""
            "GSR-TUIT & FEE REM-UCSD-GRP B "
        TD
          P (block)
            ""
            "003285 "
        TD
          P (block)
            ""
            "22 "
        TD
          P (block)
            ""
            "436 "
        TD
          P (block)
            ""
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            "GSR-TUIT & FEE REM-UCSD-GRP C "
        TD
          P (block)
            "003286 "
        TD
          P (block)
            "22 "
        TD
          P (block)
            "436 "
        TD
          P (block)
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            ""
            "GSR-TUIT & FEE REM-UCSD-GRP D "
        TD
          P (block)
            ""
            "003287 "
        TD
          P (block)
            ""
            "22 "
        TD
          P (block)
            ""
            "436 "
        TD
          P (block)
            ""
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            "GSR-TUIT & FEE REM-UCSD-GRP E "
        TD
          P (block)
            "003262 "
        TD
          P (block)
            "22 "
        TD
          P (block)
            "436 "
        TD
          P (block)
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            ""
            "GSR-TUIT & FEE REM-UCSD-GRP F "
        TD
          P (block)
            ""
            "003263 "
        TD
          P (block)
            ""
            "22 "
        TD
          P (block)
            ""
            "436 "
        TD
          P (block)
            ""
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            "GSR-TUIT & FEE REM-UCSD-GRP G "
        TD
          P (block)
            "003264 "
        TD
          P (block)
            "22 "
        TD
          P (block)
            "436 "
        TD
          P (block)
            "GRADUATE STUDENT RESEARCHER "
      TR
        TH
          P (block)
            ""
            "HEAL OTH POST-MD 4-6/REP "
        TD
          P (block)
            ""
            "002766 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "HHMI INVESTIGATOR "
        TD
          P (block)
            "001969 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "HS ASSOC CLIN PROF-AY "
        TD
          P (block)
            ""
            "002020 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "341 "
        TD
          P (block)
            ""
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            "HS ASSOC CLIN PROF-FY "
        TD
          P (block)
            "002030 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "341 "
        TD
          P (block)
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            ""
            "HS ASSOC CLIN PROF-HCOMP "
        TD
          P (block)
            ""
            "001733 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "341 "
        TD
          P (block)
            ""
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            "HS ASSOC CLIN PROF-SFT-VM "
        TD
          P (block)
            "001913 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "341 "
        TD
          P (block)
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            ""
            "HS ASST CLIN PROF-AY "
        TD
          P (block)
            ""
            "002040 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "341 "
        TD
          P (block)
            ""
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            "HS ASST CLIN PROF-FY "
        TD
          P (block)
            "002050 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "341 "
        TD
          P (block)
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            ""
            "HS ASST CLIN PROF-HCOMP "
        TD
          P (block)
            ""
            "001732 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "341 "
        TD
          P (block)
            ""
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            "HS ASST CLIN PROF-SFT-VM "
        TD
          P (block)
            "001912 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "341 "
        TD
          P (block)
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            ""
            "HS CLIN INSTR-AY "
        TD
          P (block)
            ""
            "002060 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "341 "
        TD
          P (block)
            ""
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            "HS CLIN INSTR-FY "
        TD
          P (block)
            "002070 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "341 "
        TD
          P (block)
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            ""
            "HS CLIN INSTR-HCOMP "
        TD
          P (block)
            ""
            "001731 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "341 "
        TD
          P (block)
            ""
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            "HS CLIN INSTR-SFT-VM "
        TD
          P (block)
            "001911 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "341 "
        TD
          P (block)
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            ""
            "HS CLIN PROF-AY "
        TD
          P (block)
            ""
            "002000 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "341 "
        TD
          P (block)
            ""
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            "HS CLIN PROF-FY "
        TD
          P (block)
            "002010 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "341 "
        TD
          P (block)
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            ""
            "HS CLIN PROF-HCOMP "
        TD
          P (block)
            ""
            "001734 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "341 "
        TD
          P (block)
            ""
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            "HS CLIN PROF-SFT-VM "
        TD
          P (block)
            "001914 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "341 "
        TD
          P (block)
            "HEALTH SCIENCES CLINICAL PROFESSOR "
      TR
        TH
          P (block)
            ""
            "INSTR IN RES-HCOMP "
        TD
          P (block)
            ""
            "001723 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "INSTR-AY-1/9 "
        TD
          P (block)
            "001403 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "011 "
        TD
          P (block)
            "PROFESSORIAL-NON-TENURE "
      TR
        TH
          P (block)
            ""
            "INSTR-HCOMP "
        TD
          P (block)
            ""
            "001715 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "011 "
        TD
          P (block)
            ""
            "PROFESSORIAL-NON-TENURE "
      TR
        TH
          P (block)
            "INSTR-SFT-VM "
        TD
          P (block)
            "001895 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "011 "
        TD
          P (block)
            "PROFESSORIAL-NON-TENURE "
      TR
        TH
          P (block)
            ""
            "INTERN-CLIN PSYCH-GEN CAMP NEX "
        TD
          P (block)
            ""
            "002718 "
        TD
          P (block)
            ""
            "21 "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "INTERN-CLIN PSYCH-GENL CAMP "
        TD
          P (block)
            "002716 "
        TD
          P (block)
            "21 "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            ""
            "INTERN-CLINICAL PSYCHOLOGY "
        TD
          P (block)
            ""
            "002715 "
        TD
          P (block)
            ""
            "21 "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "INTERN-CLINICAL PSYCHOLOGY NEX "
        TD
          P (block)
            "002717 "
        TD
          P (block)
            "21 "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "INTERN-VET MED/NON REP "
        TD
          P (block)
            ""
            "002714 "
        TD
          P (block)
            ""
            "21 "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "INTRM POSTDOC SCHOLAR-EMPLOYEE "
        TD
          P (block)
            "003256 "
        TD
          P (block)
            "23 "
        TD
          P (block)
            "575 "
        TD
          P (block)
            "POSTDOCTORAL SCHOLAR "
      TR
        TH
          P (block)
            ""
            "JR SPECIALIST "
        TD
          P (block)
            ""
            "003330 "
        TD
          P (block)
            ""
            "24B "
        TD
          P (block)
            ""
            "551 "
        TD
          P (block)
            ""
            "SPECIALIST "
      TR
        TH
          P (block)
            "JR SPECIALIST (WOS) "
        TD
          P (block)
            "003328 "
        TD
          P (block)
            " "
        TD
          P (block)
            "551 "
        TD
          P (block)
            "SPECIALIST "
      TR
        TH
          P (block)
            ""
            "JR SPECIALIST NEX "
        TD
          P (block)
            ""
            "003329 "
        TD
          P (block)
            ""
            "24B(N) "
        TD
          P (block)
            ""
            "551 "
        TD
          P (block)
            ""
            "SPECIALIST "
      TR
        TH
          P (block)
            "JR SPECIALIST NEX NON REP "
        TD
          P (block)
            "003334 "
        TD
          P (block)
            "24A(N) "
        TD
          P (block)
            "551 "
        TD
          P (block)
            "SPECIALIST "
      TR
        TH
          P (block)
            ""
            "JR SPECIALIST NON REP "
        TD
          P (block)
            ""
            "003333 "
        TD
          P (block)
            ""
            "24A "
        TD
          P (block)
            ""
            "551 "
        TD
          P (block)
            ""
            "SPECIALIST "
      TR
        TH
          P (block)
            "K-12 ASST-NON GSHIP/NONREP "
        TD
          P (block)
            "002382 "
        TD
          P (block)
            " "
        TD
          P (block)
            "456 "
        TD
          P (block)
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            ""
            "K-12 DAILY SUBSTITUTE/NONREP "
        TD
          P (block)
            ""
            "002442 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "K-12 INSTRUCTOR-AY "
        TD
          P (block)
            "002440 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "K-12 INSTRUCTOR-AY-1/10 "
        TD
          P (block)
            ""
            "002441 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "LAW LIBRARIAN "
        TD
          P (block)
            "003635 "
        TD
          P (block)
            " "
        TD
          P (block)
            "627 "
        TD
          P (block)
            "ASSOC & ASST UNIVERSITY LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "LAW LIBRARIAN NEX "
        TD
          P (block)
            ""
            "003636 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "627 "
        TD
          P (block)
            ""
            "ASSOC & ASST UNIVERSITY LIBRARIAN "
      TR
        TH
          P (block)
            "LECT IN SUMMER SESSION "
        TD
          P (block)
            "001550 "
        TD
          P (block)
            " "
        TD
          P (block)
            "357 "
        TD
          P (block)
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            ""
            "LECT-AY "
        TD
          P (block)
            ""
            "001630 "
        TD
          P (block)
            ""
            "15 "
        TD
          P (block)
            ""
            "225 "
        TD
          P (block)
            ""
            "LECTURER "
      TR
        TH
          P (block)
            "LECT-AY-1/10 "
        TD
          P (block)
            "001636 "
        TD
          P (block)
            "15 "
        TD
          P (block)
            "225 "
        TD
          P (block)
            "LECTURER "
      TR
        TH
          P (block)
            ""
            "LECT-AY-1/10-CONTINUING "
        TD
          P (block)
            ""
            "001637 "
        TD
          P (block)
            ""
            "16 "
        TD
          P (block)
            ""
            "225 "
        TD
          P (block)
            ""
            "LECTURER "
      TR
        TH
          P (block)
            "LECT-AY-1/9 "
        TD
          P (block)
            "001632 "
        TD
          P (block)
            "15 "
        TD
          P (block)
            "225 "
        TD
          P (block)
            "LECTURER "
      TR
        TH
          P (block)
            ""
            "LECT-AY-1/9-CONTINUING "
        TD
          P (block)
            ""
            "001633 "
        TD
          P (block)
            ""
            "16 "
        TD
          P (block)
            ""
            "225 "
        TD
          P (block)
            ""
            "LECTURER "
      TR
        TH
          P (block)
            "LECT-AY-CONTINUING "
        TD
          P (block)
            "001631 "
        TD
          P (block)
            "16 "
        TD
          P (block)
            "225 "
        TD
          P (block)
            "LECTURER "
      TR
        TH
          P (block)
            ""
            "LECT-FY "
        TD
          P (block)
            ""
            "001634 "
        TD
          P (block)
            ""
            "15 "
        TD
          P (block)
            ""
            "225 "
        TD
          P (block)
            ""
            "LECTURER "
      TR
        TH
          P (block)
            "LECT-FY-CONTINUING "
        TD
          P (block)
            "001635 "
        TD
          P (block)
            "16 "
        TD
          P (block)
            "225 "
        TD
          P (block)
            "LECTURER "
      TR
        TH
          P (block)
            ""
            "LECT-MISCELLANEOUS/PART TIME "
        TD
          P (block)
            ""
            "001650 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "LIBRARIAN-CAREER NON REP "
        TD
          P (block)
            "003602 "
        TD
          P (block)
            "26A "
        TD
          P (block)
            "621 "
        TD
          P (block)
            "LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "LIBRARIAN-CAREER STATUS "
        TD
          P (block)
            ""
            "003612 "
        TD
          P (block)
            ""
            "26B "
        TD
          P (block)
            ""
            "621 "
        TD
          P (block)
            ""
            "LIBRARIAN "
      TR
        TH
          P (block)
            "LIBRARIAN-CAREER STATUS NEX "
        TD
          P (block)
            "003662 "
        TD
          P (block)
            "26A/B(N) "
        TD
          P (block)
            "621 "
        TD
          P (block)
            "LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "LIBRARIAN-POTNTL CAREER NEX "
        TD
          P (block)
            ""
            "003663 "
        TD
          P (block)
            ""
            "26A/B(N) "
        TD
          P (block)
            ""
            "621 "
        TD
          P (block)
            ""
            "LIBRARIAN "
      TR
        TH
          P (block)
            "LIBRARIAN-POTNTL CAREER STATUS "
        TD
          P (block)
            "003613 "
        TD
          P (block)
            "26B "
        TD
          P (block)
            "621 "
        TD
          P (block)
            "LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "LIBRARIAN-POTNTLCAREER NON REP "
        TD
          P (block)
            ""
            "003603 "
        TD
          P (block)
            ""
            "26A "
        TD
          P (block)
            ""
            "621 "
        TD
          P (block)
            ""
            "LIBRARIAN "
      TR
        TH
          P (block)
            "LIBRARIAN-TEMP STATUS "
        TD
          P (block)
            "003614 "
        TD
          P (block)
            "26B "
        TD
          P (block)
            "621 "
        TD
          P (block)
            "LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "LIBRARIAN-TEMP STATUS NEX "
        TD
          P (block)
            ""
            "003664 "
        TD
          P (block)
            ""
            "26A/B(N) "
        TD
          P (block)
            ""
            "621 "
        TD
          P (block)
            ""
            "LIBRARIAN "
      TR
        TH
          P (block)
            "LUDWIG INVESTIGATOR "
        TD
          P (block)
            "001970 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "MILITARY/AIR SCI&TACTICS ASST "
        TD
          P (block)
            ""
            "002600 "
        TD
          P (block)
            ""
            "25 "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "MISCELLANEOUS "
        TD
          P (block)
            "003999 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "NON-PHYS CLIN TRAIN "
        TD
          P (block)
            ""
            "002740 "
        TD
          P (block)
            ""
            "21 "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "NON-PHYS CLIN TRAIN NEX "
        TD
          P (block)
            "002739 "
        TD
          P (block)
            "21 "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "NON-PHYS CLIN TRAIN-GENCMP NEX "
        TD
          P (block)
            ""
            "002742 "
        TD
          P (block)
            ""
            "21 "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            "NON-PHYS CLIN TRAIN-GENL CAMP "
        TD
          P (block)
            "002741 "
        TD
          P (block)
            "21 "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "NON-SENATE ACAD EMERITUS(WOS) "
        TD
          P (block)
            ""
            "003800 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "OMBUDSMAN-ACAD "
        TD
          P (block)
            "000880 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "OTH POST DDS/NON REP "
        TD
          P (block)
            ""
            "002737 "
        TD
          P (block)
            ""
            "21 "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "OTH POST DDS/REP "
        TD
          P (block)
            "002758 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "OTH POST-MD TRAIN 2-8/NON REP "
        TD
          P (block)
            ""
            "002732 "
        TD
          P (block)
            ""
            "21 "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "OTH POST-MD TRAIN 2-8/REP "
        TD
          P (block)
            "002733 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "OTH POST-MD TRAIN 2-8/REP-FNO "
        TD
          P (block)
            ""
            "002764 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "OTH POST-MD TRAIN 2-8/REP-OV "
        TD
          P (block)
            "002747 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "POST DDS I-VI/NON REP "
        TD
          P (block)
            ""
            "002727 "
        TD
          P (block)
            ""
            "21 "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "POST DDS I-VI/REP "
        TD
          P (block)
            "002757 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "POSTDOC-EMPLOYEE "
        TD
          P (block)
            ""
            "003252 "
        TD
          P (block)
            ""
            "23 "
        TD
          P (block)
            ""
            "575 "
        TD
          P (block)
            ""
            "POSTDOCTORAL SCHOLAR "
      TR
        TH
          P (block)
            "POSTDOC-EMPLOYEE NEX "
        TD
          P (block)
            "003255 "
        TD
          P (block)
            "23N "
        TD
          P (block)
            "575 "
        TD
          P (block)
            "POSTDOCTORAL SCHOLAR "
      TR
        TH
          P (block)
            ""
            "POSTDOC-FELLOW "
        TD
          P (block)
            ""
            "003253 "
        TD
          P (block)
            ""
            "23 "
        TD
          P (block)
            ""
            "575 "
        TD
          P (block)
            ""
            "POSTDOCTORAL SCHOLAR "
      TR
        TH
          P (block)
            "POSTDOC-PAID DIRECT "
        TD
          P (block)
            "003254 "
        TD
          P (block)
            "23 "
        TD
          P (block)
            "575 "
        TD
          P (block)
            "POSTDOCTORAL SCHOLAR "
      TR
        TH
          P (block)
            ""
            "PRE-SIX YR APPT-TEMP SUPP-1/10 "
        TD
          P (block)
            ""
            "001651 "
        TD
          P (block)
            ""
            "15 "
        TD
          P (block)
            ""
            "225 "
        TD
          P (block)
            ""
            "LECTURER "
      TR
        TH
          P (block)
            "PRE-SIX YR APPT-TEMP SUPP-1/9 "
        TD
          P (block)
            "001649 "
        TD
          P (block)
            "15 "
        TD
          P (block)
            "225 "
        TD
          P (block)
            "LECTURER "
      TR
        TH
          P (block)
            ""
            "PRE-SIX YR APPT-TEMP SUPP-AY "
        TD
          P (block)
            ""
            "001648 "
        TD
          P (block)
            ""
            "15 "
        TD
          P (block)
            ""
            "225 "
        TD
          P (block)
            ""
            "LECTURER "
      TR
        TH
          P (block)
            "PRE-SIX YR APPT-TEMP SUPP-FY "
        TD
          P (block)
            "001638 "
        TD
          P (block)
            "15 "
        TD
          P (block)
            "225 "
        TD
          P (block)
            "LECTURER "
      TR
        TH
          P (block)
            ""
            "PREUSS K-12 COUNSELOR-AY "
        TD
          P (block)
            ""
            "002447 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "PREUSS K-12 COUNSELOR-AY-1/10 "
        TD
          P (block)
            "002448 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "PROF EMERITUS(WOS) "
        TD
          P (block)
            ""
            "001132 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "016 "
        TD
          P (block)
            ""
            "PROFESSORIAL-EMERITUS "
      TR
        TH
          P (block)
            "PROF IN RES-AY "
        TD
          P (block)
            "003250 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "PROF IN RES-AY-1/10-B/E/E "
        TD
          P (block)
            ""
            "003345 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "PROF IN RES-AY-1/9 "
        TD
          P (block)
            "003353 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "PROF IN RES-AY-1/9-B/E/E "
        TD
          P (block)
            ""
            "003383 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "PROF IN RES-AY-B/E/E "
        TD
          P (block)
            "003381 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "PROF IN RES-FY "
        TD
          P (block)
            ""
            "003251 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "PROF IN RES-FY-B/E/E "
        TD
          P (block)
            "003382 "
        TD
          P (block)
            "4 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "PROF IN RES-HCOMP "
        TD
          P (block)
            ""
            "001726 "
        TD
          P (block)
            ""
            "5 "
        TD
          P (block)
            ""
            "311 "
        TD
          P (block)
            ""
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            "PROF IN RES-SFT-VM "
        TD
          P (block)
            "001906 "
        TD
          P (block)
            "7 "
        TD
          P (block)
            "311 "
        TD
          P (block)
            "PROFESSOR IN RESIDENCE "
      TR
        TH
          P (block)
            ""
            "PROF OF CLIN-FY "
        TD
          P (block)
            ""
            "001450 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "317 "
        TD
          P (block)
            ""
            "PROFESSOR OF CLINICAL __________ "
      TR
        TH
          P (block)
            "PROF OF CLIN-HCOMP "
        TD
          P (block)
            "001453 "
        TD
          P (block)
            "5 "
        TD
          P (block)
            "317 "
        TD
          P (block)
            "PROFESSOR OF CLINICAL __________ "
      TR
        TH
          P (block)
            ""
            "PROF OF CLIN-SFT-VM "
        TD
          P (block)
            ""
            "001917 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "317 "
        TD
          P (block)
            ""
            "PROFESSOR OF CLINICAL __________ "
      TR
        TH
          P (block)
            "PROF OF TEACH-AY "
        TD
          P (block)
            "001603 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "210 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "PROF OF TEACH-AY-1/10 "
        TD
          P (block)
            ""
            "001612 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "210 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            "PROF OF TEACH-AY-1/10-B/E/E "
        TD
          P (block)
            "001672 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "210 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "PROF OF TEACH-AY-1/10-LAW "
        TD
          P (block)
            ""
            "001658 "
        TD
          P (block)
            ""
            "8 "
        TD
          P (block)
            ""
            "210 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            "PROF OF TEACH-AY-1/9 "
        TD
          P (block)
            "001604 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "210 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - SOE "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            ""
            "PROF OF TEACH-AY-1/9-B/E/E "
        TD
          P (block)
            ""
            "001692 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "210 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            "PROF OF TEACH-AY-1/9-LAW "
        TD
          P (block)
            "001656 "
        TD
          P (block)
            "8 "
        TD
          P (block)
            "210 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "PROF OF TEACH-AY-B/E/E "
        TD
          P (block)
            ""
            "001686 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "210 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            "PROF OF TEACH-AY-LAW "
        TD
          P (block)
            "001693 "
        TD
          P (block)
            "8 "
        TD
          P (block)
            "210 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "PROF OF TEACH-EMERITUS(WOS) "
        TD
          P (block)
            ""
            "001621 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "216 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING-EMERITUS "
      TR
        TH
          P (block)
            "PROF OF TEACH-FY "
        TD
          P (block)
            "001613 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "210 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "PROF OF TEACH-FY-B/E/E "
        TD
          P (block)
            ""
            "001689 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "210 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            "PROF OF TEACH-HCOMP "
        TD
          P (block)
            "001619 "
        TD
          P (block)
            "5 "
        TD
          P (block)
            "210 "
        TD
          P (block)
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            ""
            "PROF OF TEACH-SFT-VM "
        TD
          P (block)
            ""
            "001668 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "210 "
        TD
          P (block)
            ""
            "PROFESSOR OF TEACHING - SOE "
      TR
        TH
          P (block)
            "PROF-AY "
        TD
          P (block)
            "001100 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "010 "
        TD
          P (block)
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            ""
            "PROF-AY-1/9 "
        TD
          P (block)
            ""
            "001103 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "010 "
        TD
          P (block)
            ""
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            "PROF-AY-1/9-B/E/E "
        TD
          P (block)
            "001145 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "010 "
        TD
          P (block)
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            ""
            "PROF-AY-1/9-LAW "
        TD
          P (block)
            ""
            "001181 "
        TD
          P (block)
            ""
            "8 "
        TD
          P (block)
            ""
            "010 "
        TD
          P (block)
            ""
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            "PROF-AY-B/E/E "
        TD
          P (block)
            "001143 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "010 "
        TD
          P (block)
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            ""
            "PROF-AY-LAW "
        TD
          P (block)
            ""
            "001180 "
        TD
          P (block)
            ""
            "8 "
        TD
          P (block)
            ""
            "010 "
        TD
          P (block)
            ""
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            "PROF-FY "
        TD
          P (block)
            "001110 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "010 "
        TD
          P (block)
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            ""
            "PROF-FY-B/E/E "
        TD
          P (block)
            ""
            "001144 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "010 "
        TD
          P (block)
            ""
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            "PROF-HCOMP "
        TD
          P (block)
            "001721 "
        TD
          P (block)
            "5 "
        TD
          P (block)
            "010 "
        TD
          P (block)
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            ""
            "PROF-SFT-VM "
        TD
          P (block)
            ""
            "001901 "
        TD
          P (block)
            ""
            "7 "
        TD
          P (block)
            ""
            "010 "
        TD
          P (block)
            ""
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            "PROG COORD "
        TD
          P (block)
            "003540 "
        TD
          P (block)
            " "
        TD
          P (block)
            "828 "
        TD
          P (block)
            "UNIVERSITY EXTENSION-OTHER "
      TR
        TH
          P (block)
            ""
            "PROGRAM COORDINATOR NEX "
        TD
          P (block)
            ""
            "003539 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "828 "
        TD
          P (block)
            ""
            "UNIVERSITY EXTENSION-OTHER "
      TR
        TH
          P (block)
            "PROJ SCIENTIST (WOS) "
        TD
          P (block)
            "003487 "
        TD
          P (block)
            " "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
      TR
        TH
          P (block)
            ""
            "PROJ SCIENTIST-FY "
        TD
          P (block)
            ""
            "003390 "
        TD
          P (block)
            ""
            "37B "
        TD
          P (block)
            ""
            "581 "
        TD
          P (block)
            ""
            "PROJECT SERIES "
      TR
        TH
          P (block)
            "PROJ SCIENTIST-FY NEX "
        TD
          P (block)
            "003490 "
        TD
          P (block)
            "37B(N) "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
      TR
        TH
          P (block)
            ""
            "PROJ SCIENTIST-FY NON REP "
        TD
          P (block)
            ""
            "003403 "
        TD
          P (block)
            ""
            "37A "
        TD
          P (block)
            ""
            "581 "
        TD
          P (block)
            ""
            "PROJECT SERIES "
      TR
        TH
          P (block)
            "PROJ SCIENTIST-FY-B/E/E "
        TD
          P (block)
            "003391 "
        TD
          P (block)
            "38B "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
      TR
        TH
          P (block)
            ""
            "PROJ SCIENTIST-FY-B/E/E NEX "
        TD
          P (block)
            ""
            "003491 "
        TD
          P (block)
            ""
            "38B(N) "
        TD
          P (block)
            ""
            "581 "
        TD
          P (block)
            ""
            "PROJECT SERIES "
      TR
        TH
          P (block)
            "PROJ SCIENTIST-FY-B/E/E NONREP "
        TD
          P (block)
            "003404 "
        TD
          P (block)
            "38A "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
      TR
        TH
          P (block)
            ""
            "PROJ SCI-FY NEX NON REP "
        TD
          P (block)
            ""
            "003413 "
        TD
          P (block)
            ""
            "37A(N) "
        TD
          P (block)
            ""
            "581 "
        TD
          P (block)
            ""
            "PROJECT SERIES "
      TR
        TH
          P (block)
            "PROJ SCI-FY-B/E/E NEX NON REP "
        TD
          P (block)
            "003414 "
        TD
          P (block)
            "38A(N) "
        TD
          P (block)
            "581 "
        TD
          P (block)
            "PROJECT SERIES "
      TR
        TH
          P (block)
            ""
            "READER-GSHIP "
        TD
          P (block)
            ""
            "002850 "
        TD
          P (block)
            ""
            "18 "
        TD
          P (block)
            ""
            "456 "
        TD
          P (block)
            ""
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            "READER-GSHIP/NON REP "
        TD
          P (block)
            "002854 "
        TD
          P (block)
            "18 "
        TD
          P (block)
            "456 "
        TD
          P (block)
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            ""
            "READER-NON GSHIP "
        TD
          P (block)
            ""
            "002851 "
        TD
          P (block)
            ""
            "18 "
        TD
          P (block)
            ""
            "456 "
        TD
          P (block)
            ""
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            "READER-NON GSHIP/NON REP "
        TD
          P (block)
            "002855 "
        TD
          P (block)
            "18 "
        TD
          P (block)
            "456 "
        TD
          P (block)
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            ""
            "READER-NON STDNT "
        TD
          P (block)
            ""
            "002500 "
        TD
          P (block)
            ""
            "18 "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "READER-NON STDNT/NON REP "
        TD
          P (block)
            "002520 "
        TD
          P (block)
            "18 "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "RECALL FACULTY "
        TD
          P (block)
            ""
            "001702 "
        TD
          P (block)
            ""
            "1* "
        TD
          P (block)
            ""
            "012 "
        TD
          P (block)
            ""
            "PROFESSORIAL-RECALL "
      TR
        TH
          P (block)
            "RECALL HCOMP "
        TD
          P (block)
            "001701 "
        TD
          P (block)
            "5* "
        TD
          P (block)
            "012 "
        TD
          P (block)
            "PROFESSORIAL-RECALL "
      TR
        TH
          P (block)
            ""
            "RECALL NON-FACULTY ACAD "
        TD
          P (block)
            ""
            "003802 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            "RECALL NON-FACULTY ACAD NEX "
        TD
          P (block)
            "003812 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "RECALL TEACHING "
        TD
          P (block)
            ""
            "001700 "
        TD
          P (block)
            ""
            "1* "
        TD
          P (block)
            ""
            "012 "
        TD
          P (block)
            ""
            "PROFESSORIAL-RECALL "
      TR
        TH
          P (block)
            "RECALL TEACHING NON-SENATE "
        TD
          P (block)
            "001699 "
        TD
          P (block)
            "1* "
        TD
          P (block)
            "012 "
        TD
          P (block)
            "PROFESSORIAL-RECALL "
      TR
        TH
          P (block)
            ""
            "REGENTS' LECT "
        TD
          P (block)
            ""
            "001968 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "REGENTS' PROF "
        TD
          P (block)
            "001958 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "REMD TUT I-GSHIP "
        TD
          P (block)
            ""
            "002288 "
        TD
          P (block)
            ""
            "20 "
        TD
          P (block)
            ""
            "456 "
        TD
          P (block)
            ""
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            "REMD TUT I-GSHIP/NON REP "
        TD
          P (block)
            "002271 "
        TD
          P (block)
            "20 "
        TD
          P (block)
            "456 "
        TD
          P (block)
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            ""
            "REMD TUT II NON-GSHIP/NON REP "
        TD
          P (block)
            ""
            "002272 "
        TD
          P (block)
            ""
            "20 "
        TD
          P (block)
            ""
            "456 "
        TD
          P (block)
            ""
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            "REMD TUT II-GSHIP "
        TD
          P (block)
            "002289 "
        TD
          P (block)
            "20 "
        TD
          P (block)
            "456 "
        TD
          P (block)
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            ""
            "REMD TUT II-GSHIP/NON REP "
        TD
          P (block)
            ""
            "002273 "
        TD
          P (block)
            ""
            "20 "
        TD
          P (block)
            ""
            "456 "
        TD
          P (block)
            ""
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            "REMD TUT II-NON GSHIP "
        TD
          P (block)
            "002290 "
        TD
          P (block)
            "20 "
        TD
          P (block)
            "456 "
        TD
          P (block)
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            ""
            "REMD TUT I-NON GSHIP "
        TD
          P (block)
            ""
            "002280 "
        TD
          P (block)
            ""
            "20 "
        TD
          P (block)
            ""
            "456 "
        TD
          P (block)
            ""
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            "REMD TUT I-NON GSHIP/NON REP "
        TD
          P (block)
            "002270 "
        TD
          P (block)
            "20 "
        TD
          P (block)
            "456 "
        TD
          P (block)
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            ""
            "RES (WOS) "
        TD
          P (block)
            ""
            "003202 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "RES PROF-MILLER INST-AY "
        TD
          P (block)
            "003290 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "566 "
        TD
          P (block)
            "OTHER RESEARCH "
      TR
        TH
          P (block)
            ""
            "RES PROF-MILLER INST-FY "
        TD
          P (block)
            ""
            "003291 "
        TD
          P (block)
            ""
            "2 "
        TD
          P (block)
            ""
            "566 "
        TD
          P (block)
            ""
            "OTHER RESEARCH "
      TR
        TH
          P (block)
            "RES SCRIPPS-AY "
        TD
          P (block)
            "001935 "
        TD
          P (block)
            " "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "RESEARCH ASSOCIATE "
        TD
          P (block)
            ""
            "CWR022 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "CWR "
        TD
          P (block)
            ""
            "CONTINGENT WORKER "
      TR
        TH
          P (block)
            "RESEARCH FELLOW "
        TD
          P (block)
            "CWR021 "
        TD
          P (block)
            " "
        TD
          P (block)
            "CWR "
        TD
          P (block)
            "CONTINGENT WORKER "
      TR
        TH
          P (block)
            ""
            "RES-FY "
        TD
          P (block)
            ""
            "003200 "
        TD
          P (block)
            ""
            "13B "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "RES-FY NEX "
        TD
          P (block)
            "003170 "
        TD
          P (block)
            "13B(N) "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "RES-FY NEX NON REP "
        TD
          P (block)
            ""
            "003171 "
        TD
          P (block)
            ""
            "13A(N) "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "RES-FY-B/E/E "
        TD
          P (block)
            "001987 "
        TD
          P (block)
            "14B "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "RES-FY-B/E/E NEX "
        TD
          P (block)
            ""
            "001997 "
        TD
          P (block)
            ""
            "14B(N) "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "RES-FY-B/E/E NEX NON REP "
        TD
          P (block)
            "002007 "
        TD
          P (block)
            "14A(N) "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "RES-FY-B/E/E-NON REP "
        TD
          P (block)
            ""
            "001993 "
        TD
          P (block)
            ""
            "14A "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "RES-FY-NON REP "
        TD
          P (block)
            "003207 "
        TD
          P (block)
            "13A "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "RESID PHYS I/NON REP "
        TD
          P (block)
            ""
            "002708 "
        TD
          P (block)
            ""
            "21 "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "RESID PHYS I/REP "
        TD
          P (block)
            "002709 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "RESID PHYS I/REP-FNO "
        TD
          P (block)
            ""
            "002760 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "RESID PHYS I/REP-OV "
        TD
          P (block)
            "002743 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "RESID PHYS II-VIII/NON REP "
        TD
          P (block)
            ""
            "002724 "
        TD
          P (block)
            ""
            "21 "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "RESID PHYS II-VIII/REP "
        TD
          P (block)
            "002723 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "RESID PHYS II-VIII/REP-FNO "
        TD
          P (block)
            ""
            "002761 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "RESID PHYS II-VIII/REP-OV "
        TD
          P (block)
            "002744 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "RESID PHYS MOONLTNG NON REP "
        TD
          P (block)
            ""
            "002753 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "RESID PHYS MOONLTNG REP "
        TD
          P (block)
            "002754 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "RESID PHYS/SUBSPEC 4-8/NON REP "
        TD
          P (block)
            ""
            "002726 "
        TD
          P (block)
            ""
            "21 "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "RESID PHYS/SUBSPEC 4-8/REP "
        TD
          P (block)
            "002736 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            ""
            "RESID PHYS/SUBSPEC 4-8/REP-FNO "
        TD
          P (block)
            ""
            "002763 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "RESID PHYS/SUBSPEC 4-8/REP-OV "
        TD
          P (block)
            "002746 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "RESID PHYS/SUBSPEC/T32/NON REP "
        TD
          P (block)
            ""
            "002749 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "RESID PHYS/SUBSPEC/T32/REP "
        TD
          P (block)
            "002750 "
        TD
          P (block)
            " "
        TD
          P (block)
            "446 "
        TD
          P (block)
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            ""
            "RESID-VET MED/NON REP "
        TD
          P (block)
            ""
            "002730 "
        TD
          P (block)
            ""
            "21 "
        TD
          P (block)
            ""
            "446 "
        TD
          P (block)
            ""
            "INTERN OR RESIDENT "
      TR
        TH
          P (block)
            "RES-LR SCL-AY "
        TD
          P (block)
            "003203 "
        TD
          P (block)
            "1 "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "RES-LR SCL-AY-1/9 "
        TD
          P (block)
            ""
            "003205 "
        TD
          P (block)
            ""
            "1 "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "RES-LR SCL-AY-1/9-B/E/E "
        TD
          P (block)
            "001982 "
        TD
          P (block)
            "3 "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "RES-LR SCL-AY-B/E/E "
        TD
          P (block)
            ""
            "001981 "
        TD
          P (block)
            ""
            "3 "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "RES-LR SCL-FY "
        TD
          P (block)
            "003201 "
        TD
          P (block)
            "2 "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "RES-LR SCL-FY-B/E/E "
        TD
          P (block)
            ""
            "001990 "
        TD
          P (block)
            ""
            "4 "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "RES-SFT "
        TD
          P (block)
            "003206 "
        TD
          P (block)
            " "
        TD
          P (block)
            "541 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            ""
            "RES-SFT NEX "
        TD
          P (block)
            ""
            "003176 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "541 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-REGULAR "
      TR
        TH
          P (block)
            "SALARY SUPPLEMENTATION "
        TD
          P (block)
            "003998 "
        TD
          P (block)
            " "
        TD
          P (block)
            "999 "
        TD
          P (block)
            "SUPPLEMENTAL PAY CODES "
      TR
        TH
          P (block)
            ""
            "SENATE EMERITUS (WOS) "
        TD
          P (block)
            ""
            "003249 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "316 "
        TD
          P (block)
            ""
            "________-SENATE-EMERITUS "
      TR
        TH
          P (block)
            "SPEAKER-UNEX "
        TD
          P (block)
            "003575 "
        TD
          P (block)
            " "
        TD
          P (block)
            "828 "
        TD
          P (block)
            "UNIVERSITY EXTENSION-OTHER "
      TR
        TH
          P (block)
            ""
            "SPECIAL READER-UCLA-GSHIP "
        TD
          P (block)
            ""
            "002852 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "456 "
        TD
          P (block)
            ""
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            "SPECIAL READER-UCLA-NON GSHIP "
        TD
          P (block)
            "002853 "
        TD
          P (block)
            " "
        TD
          P (block)
            "456 "
        TD
          P (block)
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            ""
            "SPECIALIST "
        TD
          P (block)
            ""
            "003300 "
        TD
          P (block)
            ""
            "24B "
        TD
          P (block)
            ""
            "551 "
        TD
          P (block)
            ""
            "SPECIALIST "
      TR
        TH
          P (block)
            "SPECIALIST (WOS) "
        TD
          P (block)
            "003302 "
        TD
          P (block)
            " "
        TD
          P (block)
            "551 "
        TD
          P (block)
            "SPECIALIST "
      TR
        TH
          P (block)
            ""
            "SPECIALIST AES "
        TD
          P (block)
            ""
            "003004 "
        TD
          P (block)
            ""
            "24A "
        TD
          P (block)
            ""
            "557 "
        TD
          P (block)
            ""
            "SPECIALIST IN A.E.S. "
      TR
        TH
          P (block)
            "SPECIALIST AES NEX "
        TD
          P (block)
            "003104 "
        TD
          P (block)
            "24A(N) "
        TD
          P (block)
            "557 "
        TD
          P (block)
            "SPECIALIST IN A.E.S. "
      TR
        TH
          P (block)
            ""
            "SPECIALIST COOP EXT "
        TD
          P (block)
            ""
            "003479 "
        TD
          P (block)
            ""
            "29 "
        TD
          P (block)
            ""
            "729 "
        TD
          P (block)
            ""
            "SPECIALIST IN COOPERATIVE EXTENSION "
      TR
        TH
          P (block)
            "SPECIALIST COOP EXT NEX "
        TD
          P (block)
            "003480 "
        TD
          P (block)
            "29N "
        TD
          P (block)
            "729 "
        TD
          P (block)
            "SPECIALIST IN COOPERATIVE EXTENSION "
      TR
        TH
          P (block)
            ""
            "SPECIALIST NEX "
        TD
          P (block)
            ""
            "003301 "
        TD
          P (block)
            ""
            "24B(N) "
        TD
          P (block)
            ""
            "551 "
        TD
          P (block)
            ""
            "SPECIALIST "
      TR
        TH
          P (block)
            "SPECIALIST NEX NON REP "
        TD
          P (block)
            "003304 "
        TD
          P (block)
            "24A(N) "
        TD
          P (block)
            "551 "
        TD
          P (block)
            "SPECIALIST "
      TR
        TH
          P (block)
            ""
            "SPECIALIST NON REP "
        TD
          P (block)
            ""
            "003303 "
        TD
          P (block)
            ""
            "24A "
        TD
          P (block)
            ""
            "551 "
        TD
          P (block)
            ""
            "SPECIALIST "
      TR
        TH
          P (block)
            "SR LECT-AY-1/10-CONTINUING "
        TD
          P (block)
            "001647 "
        TD
          P (block)
            "16 "
        TD
          P (block)
            "225 "
        TD
          P (block)
            "LECTURER "
      TR
        TH
          P (block)
            ""
            "SR LECT-AY-1/9-CONTINUING "
        TD
          P (block)
            ""
            "001643 "
        TD
          P (block)
            ""
            "16 "
        TD
          P (block)
            ""
            "225 "
        TD
          P (block)
            ""
            "LECTURER "
      TR
        TH
          P (block)
            "SR LECT-AY-CONTINUING "
        TD
          P (block)
            "001641 "
        TD
          P (block)
            "16 "
        TD
          P (block)
            "225 "
        TD
          P (block)
            "LECTURER "
      TR
        TH
          P (block)
            ""
            "SR LECT-FY-CONTINUING "
        TD
          P (block)
            ""
            "001645 "
        TD
          P (block)
            ""
            "16 "
        TD
          P (block)
            ""
            "225 "
        TD
          P (block)
            ""
            "LECTURER "
      TR
        TH
          P (block)
            "STIPEND-OTH POST-MD TRAIN "
        TD
          P (block)
            "002735 "
        TD
          P (block)
            " "
        TD
          P (block)
            "999 "
        TD
          P (block)
            "SUPPLEMENTAL PAY CODES "
      TR
        TH
          P (block)
            ""
            "STIPEND-RESID "
        TD
          P (block)
            ""
            "001092 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "999 "
        TD
          P (block)
            ""
            "SUPPLEMENTAL PAY CODES "
      TR
        TH
          P (block)
            "SUBSTITUTE TEACHER "
        TD
          P (block)
            "002427 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "SUBSTITUTE TEACHER-CONTINUING "
        TD
          P (block)
            ""
            "002428 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "SUMMER DIFFERENTIAL "
        TD
          P (block)
            "001098 "
        TD
          P (block)
            " "
        TD
          P (block)
            "999 "
        TD
          P (block)
            "SUPPLEMENTAL PAY CODES "
      TR
        TH
          P (block)
            ""
            "SUPV TEACHER ED-AY "
        TD
          P (block)
            ""
            "002220 "
        TD
          P (block)
            ""
            "32 "
        TD
          P (block)
            ""
            "357 "
        TD
          P (block)
            ""
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            "SUPV TEACHER ED-AY-CONTINUING "
        TD
          P (block)
            "002221 "
        TD
          P (block)
            "32 "
        TD
          P (block)
            "357 "
        TD
          P (block)
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            ""
            "SUPV TEACHER ED-FY "
        TD
          P (block)
            ""
            "002222 "
        TD
          P (block)
            ""
            "33 "
        TD
          P (block)
            ""
            "357 "
        TD
          P (block)
            ""
            "INSTRUCTIONAL ASSISTANT "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            "SUPV TEACHER ED-FY-CONTINUING "
        TD
          P (block)
            "002223 "
        TD
          P (block)
            "33 "
        TD
          P (block)
            "357 "
        TD
          P (block)
            "INSTRUCTIONAL ASSISTANT "
      TR
        TH
          P (block)
            ""
            "TEACHER-LHS "
        TD
          P (block)
            ""
            "002650 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "TEACHER-LHS-CONTINUING "
        TD
          P (block)
            "002651 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "TEACHER-SPEC PROG "
        TD
          P (block)
            ""
            "002460 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "TEACHER-SPEC PROG-CONTINUING "
        TD
          P (block)
            "002461 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "TEACHER-UNEX "
        TD
          P (block)
            ""
            "003574 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "828 "
        TD
          P (block)
            ""
            "UNIVERSITY EXTENSION-OTHER "
      TR
        TH
          P (block)
            "TEACHER-UNEX-CONTRACT YR "
        TD
          P (block)
            "003570 "
        TD
          P (block)
            " "
        TD
          P (block)
            "828 "
        TD
          P (block)
            "UNIVERSITY EXTENSION-OTHER "
      TR
        TH
          P (block)
            ""
            "TEACHG ASST-1/10-GSHIP "
        TD
          P (block)
            ""
            "002320 "
        TD
          P (block)
            ""
            "18 "
        TD
          P (block)
            ""
            "426 "
        TD
          P (block)
            ""
            "TEACHING ASSISTANT & EQUIVALENT "
      TR
        TH
          P (block)
            "TEACHG ASST-1/10-NON GSHIP "
        TD
          P (block)
            "002321 "
        TD
          P (block)
            "18 "
        TD
          P (block)
            "426 "
        TD
          P (block)
            "TEACHING ASSISTANT & EQUIVALENT "
      TR
        TH
          P (block)
            ""
            "TEACHG ASST-GSHIP "
        TD
          P (block)
            ""
            "002310 "
        TD
          P (block)
            ""
            "18 "
        TD
          P (block)
            ""
            "426 "
        TD
          P (block)
            ""
            "TEACHING ASSISTANT & EQUIVALENT "
      TR
        TH
          P (block)
            "TEACHG ASST-GSHIP/NON REP "
        TD
          P (block)
            "002312 "
        TD
          P (block)
            "18 "
        TD
          P (block)
            "426 "
        TD
          P (block)
            "TEACHING ASSISTANT & EQUIVALENT "
      TR
        TH
          P (block)
            ""
            "TEACHG ASST-NON GSHIP "
        TD
          P (block)
            ""
            "002311 "
        TD
          P (block)
            ""
            "18 "
        TD
          P (block)
            ""
            "426 "
        TD
          P (block)
            ""
            "TEACHING ASSISTANT & EQUIVALENT "
      TR
        TH
          P (block)
            "TEACHG ASST-NON GSHIP/NON REP "
        TD
          P (block)
            "002313 "
        TD
          P (block)
            "18 "
        TD
          P (block)
            "426 "
        TD
          P (block)
            "TEACHING ASSISTANT & EQUIVALENT "
      TR
        TH
          P (block)
            ""
            "TEACHG FELLOW-GSHIP "
        TD
          P (block)
            ""
            "002300 "
        TD
          P (block)
            ""
            "18 "
        TD
          P (block)
            ""
            "426 "
        TD
          P (block)
            ""
            "TEACHING ASSISTANT & EQUIVALENT "
      TR
        TH
          P (block)
            "TEACHG FELLOW-GSHIP/NON REP "
        TD
          P (block)
            "002302 "
        TD
          P (block)
            "18 "
        TD
          P (block)
            "426 "
        TD
          P (block)
            "TEACHING ASSISTANT & EQUIVALENT "
      TR
        TH
          P (block)
            ""
            "TEACHG FELLOW-NON GSHIP "
        TD
          P (block)
            ""
            "002301 "
        TD
          P (block)
            ""
            "18 "
        TD
          P (block)
            ""
            "426 "
        TD
          P (block)
            ""
            "TEACHING ASSISTANT & EQUIVALENT "
      TR
        TH
          P (block)
            "TEACHG FELLOW-NON GSHIP/NONREP "
        TD
          P (block)
            "002303 "
        TD
          P (block)
            "18 "
        TD
          P (block)
            "426 "
        TD
          P (block)
            "TEACHING ASSISTANT & EQUIVALENT "
      TR
        TH
          P (block)
            ""
            "TUT-GSHIP "
        TD
          P (block)
            ""
            "002860 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "456 "
        TD
          P (block)
            ""
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            "TUT-GSHIP/NON REP "
        TD
          P (block)
            "002862 "
        TD
          P (block)
            " "
        TD
          P (block)
            "456 "
        TD
          P (block)
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            ""
            "TUT-NON GSHIP "
        TD
          P (block)
            ""
            "002861 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "456 "
        TD
          P (block)
            ""
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            "TUT-NON GSHIP/NON REP "
        TD
          P (block)
            "002863 "
        TD
          P (block)
            " "
        TD
          P (block)
            "456 "
        TD
          P (block)
            "OTHER STUDENT TITLES "
      TR
        TH
          P (block)
            ""
            "TUT-NON STDNT "
        TD
          P (block)
            ""
            "002510 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "928 "
        TD
          P (block)
            ""
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            "TUT-NON STDNT/NON REP "
        TD
          P (block)
            "002521 "
        TD
          P (block)
            " "
        TD
          P (block)
            "928 "
        TD
          P (block)
            "MISCELLANEOUS TITLES-SINGLE TITLES "
      TR
        TH
          P (block)
            ""
            "UNIV PROF "
        TD
          P (block)
            ""
            "001104 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "010 "
        TD
          P (block)
            ""
            "PROFESSORIAL-TENURE "
      TR
        TH
          P (block)
            "VICE PROVOST "
        TD
          P (block)
            "001068 "
        TD
          P (block)
            " "
        TD
          P (block)
            "S27 "
        TD
          P (block)
            "PROVOST "
      TR
        TH
          P (block)
            ""
            "VIS ASSOC PROF "
        TD
          P (block)
            ""
            "001208 "
        TD
          P (block)
            ""
            "1* "
        TD
          P (block)
            ""
            "323 "
        TD
          P (block)
            ""
            "VISITING PROFESSOR "
      TR
        TH
          P (block)
            "VIS ASSOC PROF-HCOMP "
        TD
          P (block)
            "001713 "
        TD
          P (block)
            "5* "
        TD
          P (block)
            "323 "
        TD
          P (block)
            "VISITING PROFESSOR "
      TR
        TH
          P (block)
            ""
            "VIS ASSOC PROJ SCIENTIST "
        TD
          P (block)
            ""
            "003397 "
        TD
          P (block)
            ""
            "37A* "
        TD
          P (block)
            ""
            "583 "
        TD
          P (block)
            ""
            "PROJECT SERIES-VISITING "
      TR
        TH
          P (block)
            "VIS ASSOC PROJ SCIENTIST NEX "
        TD
          P (block)
            "003497 "
        TD
          P (block)
            "37A(N)* "
        TD
          P (block)
            "583 "
        TD
          P (block)
            "PROJECT SERIES-VISITING "
      TR
        TH
          P (block)
            ""
            "VIS ASSOC RES "
        TD
          P (block)
            ""
            "003218 "
        TD
          P (block)
            ""
            "13A* "
        TD
          P (block)
            ""
            "543 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-VISITING "
      TR
        TH
          P (block)
            "VIS ASSOC RES NEX "
        TD
          P (block)
            "003188 "
        TD
          P (block)
            "13A(N)* "
        TD
          P (block)
            "543 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-VISITING "
      TR
        TH
          P (block)
            ""
            "VIS ASSOC SPECIALIST "
        TD
          P (block)
            ""
            "003315 "
        TD
          P (block)
            ""
            "24A* "
        TD
          P (block)
            ""
            "553 "
        TD
          P (block)
            ""
            "SPECIALIST-VISITING "
      TR
        TH
          P (block)
            "VIS ASSOC SPECIALIST NEX "
        TD
          P (block)
            "003316 "
        TD
          P (block)
            "24A(N)* "
        TD
          P (block)
            "553 "
        TD
          P (block)
            "SPECIALIST-VISITING "
      TR
        TH
          P (block)
            ""
            "VIS ASST PROF "
        TD
          P (block)
            ""
            "001308 "
        TD
          P (block)
            ""
            "1* "
        TD
          P (block)
            ""
            "323 "
        TD
          P (block)
            ""
            "VISITING PROFESSOR "
      TR
        TH
          P (block)
            "VIS ASST PROF-HCOMP "
        TD
          P (block)
            "001712 "
        TD
          P (block)
            "5* "
        TD
          P (block)
            "323 "
        TD
          P (block)
            "VISITING PROFESSOR "
      TR
        TH
          P (block)
            ""
            "VIS ASST PROJ SCIENTIST "
        TD
          P (block)
            ""
            "003398 "
        TD
          P (block)
            ""
            "37A* "
        TD
          P (block)
            ""
            "583 "
        TD
          P (block)
            ""
            "PROJECT SERIES-VISITING "
      TR
        TH
          P (block)
            "VIS ASST PROJ SCIENTIST NEX "
        TD
          P (block)
            "003498 "
        TD
          P (block)
            "37A(N)* "
        TD
          P (block)
            "583 "
        TD
          P (block)
            "PROJECT SERIES-VISITING "
      TR
        TH
          P (block)
            ""
            "VIS ASST RES "
        TD
          P (block)
            ""
            "003228 "
        TD
          P (block)
            ""
            "13A* "
        TD
          P (block)
            ""
            "543 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-VISITING "
      TR
        TH
          P (block)
            "VIS ASST RES NEX "
        TD
          P (block)
            "003198 "
        TD
          P (block)
            "13A(N)* "
        TD
          P (block)
            "543 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-VISITING "
  Table (block)
    THead
      TR
        TH
          P (block)
            "Title/Job Descr "
        TH
          P (block)
            "Title/Job Code "
        TH
          P (block)
            "Salary Scale Table "
        TH
          P (block)
            "CTO "
        TH
          P (block)
            "CTO Name "
    TBody
      TR
        TH
          P (block)
            ""
            "VIS ASST SPECIALIST "
        TD
          P (block)
            ""
            "003325 "
        TD
          P (block)
            ""
            "24A* "
        TD
          P (block)
            ""
            "553 "
        TD
          P (block)
            ""
            "SPECIALIST-VISITING "
      TR
        TH
          P (block)
            "VIS ASST SPECIALIST NEX "
        TD
          P (block)
            "003326 "
        TD
          P (block)
            "24A(N)* "
        TD
          P (block)
            "553 "
        TD
          P (block)
            "SPECIALIST-VISITING "
      TR
        TH
          P (block)
            ""
            "VIS JR SPECIALIST "
        TD
          P (block)
            ""
            "003335 "
        TD
          P (block)
            ""
            "24A* "
        TD
          P (block)
            ""
            "553 "
        TD
          P (block)
            ""
            "SPECIALIST-VISITING "
      TR
        TH
          P (block)
            "VIS JR SPECIALIST NEX "
        TD
          P (block)
            "003336 "
        TD
          P (block)
            "24A(N)* "
        TD
          P (block)
            "553 "
        TD
          P (block)
            "SPECIALIST-VISITING "
      TR
        TH
          P (block)
            ""
            "VIS LIBRARIAN "
        TD
          P (block)
            ""
            "003615 "
        TD
          P (block)
            ""
            "26A* "
        TD
          P (block)
            ""
            "623 "
        TD
          P (block)
            ""
            "VISITING LIBRARIAN "
      TR
        TH
          P (block)
            "VIS LIBRARIAN NEX "
        TD
          P (block)
            "003665 "
        TD
          P (block)
            "26A(N)* "
        TD
          P (block)
            "623 "
        TD
          P (block)
            "VISITING LIBRARIAN "
      TR
        TH
          P (block)
            ""
            "VIS PROF "
        TD
          P (block)
            ""
            "001108 "
        TD
          P (block)
            ""
            "1* "
        TD
          P (block)
            ""
            "323 "
        TD
          P (block)
            ""
            "VISITING PROFESSOR "
      TR
        TH
          P (block)
            "VIS PROF-HCOMP "
        TD
          P (block)
            "001714 "
        TD
          P (block)
            "5* "
        TD
          P (block)
            "323 "
        TD
          P (block)
            "VISITING PROFESSOR "
      TR
        TH
          P (block)
            ""
            "VIS PROJ SCIENTIST "
        TD
          P (block)
            ""
            "003396 "
        TD
          P (block)
            ""
            "37A* "
        TD
          P (block)
            ""
            "583 "
        TD
          P (block)
            ""
            "PROJECT SERIES-VISITING "
      TR
        TH
          P (block)
            "VIS PROJ SCIENTIST NEX "
        TD
          P (block)
            "003496 "
        TD
          P (block)
            "37A(N)* "
        TD
          P (block)
            "583 "
        TD
          P (block)
            "PROJECT SERIES-VISITING "
      TR
        TH
          P (block)
            ""
            "VIS RES "
        TD
          P (block)
            ""
            "003208 "
        TD
          P (block)
            ""
            "13A* "
        TD
          P (block)
            ""
            "543 "
        TD
          P (block)
            ""
            "PROFESSIONAL RESEARCH-VISITING "
      TR
        TH
          P (block)
            "VIS RES NEX "
        TD
          P (block)
            "003178 "
        TD
          P (block)
            "13A(N)* "
        TD
          P (block)
            "543 "
        TD
          P (block)
            "PROFESSIONAL RESEARCH-VISITING "
      TR
        TH
          P (block)
            ""
            "VIS SPECIALIST "
        TD
          P (block)
            ""
            "003305 "
        TD
          P (block)
            ""
            "24A* "
        TD
          P (block)
            ""
            "553 "
        TD
          P (block)
            ""
            "SPECIALIST-VISITING "
      TR
        TH
          P (block)
            "VIS SPECIALIST NEX "
        TD
          P (block)
            "003306 "
        TD
          P (block)
            "24A(N)* "
        TD
          P (block)
            "553 "
        TD
          P (block)
            "SPECIALIST-VISITING "
      TR
        TH
          P (block)
            ""
            "VISITING SCHOLAR "
        TD
          P (block)
            ""
            "CWR015 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "CWR "
        TDa
          P (block)
            ""
            "CONTINGENT WORKER "
      TR
        TH
          P (block)
            "VISITING STUDENT RES-GRADUATE "
        TD
          P (block)
            "CWR003 "
        TD
          P (block)
            " "
        TD
          P (block)
            "CWR "
        TD
          P (block)
            "CONTINGENT WORKER "
      TR
        TH
          P (block)
            ""
            "VISITING STUDENT RES-UNDERGRAD "
        TD
          P (block)
            ""
            "CWR016 "
        TD
          P (block)
            " "
        TD
          P (block)
            ""
            "CWR "
        TD
          P (block)
            ""
            "CONTINGENT WORKER "
      TR
"""

# Define the path for the output CSV
output_csv = 'titles.csv'

# Call the function to parse input and save to CSV
parse_input_to_csv(input_str, output_csv)