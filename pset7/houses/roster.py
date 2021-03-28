# TODO


import csv
from sys import argv, exit
from cs50 import SQL

db = SQL("sqlite:///students.db")

if len(argv) != 2:
    exit(1)("Usage: python roster.py house name")
    
house = argv[1] 
people = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", house)

for student in people:
    if student['middle'] == None:
        print(f"{student['first']} {student['last']}, born {student['birth']}")
    else:
        print(f"{student['first']} {student['middle']} {student['last']}, born {student['birth']}")
        