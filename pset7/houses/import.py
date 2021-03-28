# TODO
# import.py, write a program that imports data from a CSV spreadsheet.


import csv
from sys import argv, exit
from cs50 import SQL

db = SQL("sqlite:///students.db")

if len(argv) != 2:
    exit(1)("Usage: python import.py char.csv")


# with open("(argv[1])", "r") as characters:
#   reader =  csv.DictReader as characters


with open (argv[1], "r") as file:
    reader = csv.DictReader(file)
    for student in reader:
        name = student["name"].split()
        # print(name)
        if len(name) == 2:
            first, last = name
            middle = None;
            # db.execute ("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", first, None, last, student["house"], student["birth"])
        elif len(name) == 3:
          first, middle, last = name
         
         db.execute ("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", first, middle, last, student["house"], student["birth"])
