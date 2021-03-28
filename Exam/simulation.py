
import csv
from sys import argv, exit
from cs50 import SQL
from cs50 import get_float, get_int

db = SQL("sqlite:///information.db")

#  taip isprintina kiekvieno int value
information = db.execute("SELECT money_you_own, price_for_kiwi, price_for_pomegranate, price_for_avocado FROM data")

# information = db.execute("SELECT (money_you_own) - (price_for_kiwi) - (price_for_pomegranate) - (price_for_avocado) FROM data") galima taip daryti ir isprintins list'a su atsakymu teising atimties
print("information: ", information)
# print(" ",(money_you_own) - (price_for_kiwi) - (price_for_pomegranate) - (price_for_avocado))
money_you_own = 11
price_for_kiwi = 2
price_for_pomegranate = 3
price_for_avocado = 1

# money = lookup(request.form.get("money_you_own"))
# print("aa", money)

price = 11 - 2 - 3 - 1
f = open("output.txt", "a")
print("Money you own after buying 1 kiwi, 1 pomegranate and 1 avocado: ", price, file=f)
print("How many avocados you can buy:", price, file=f)
f.close()