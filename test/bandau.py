# bandau antra uzduoti
from cs50 import SQL

db = SQL("sqlite:///oil.db")
amount = db.execute("SELECT oil_amount FROM data")
rows = db.execute("SELECT bottle1, bottle3, bottle5 FROM data")

for bottle in rows:
    bottle1 = bottle['bottle1']
    bottle3 = bottle['bottle3']
    bottle5 = bottle['bottle5']
        # print(f"{bottle['bottle1']} {bottle['bottle3']} {bottle['bottle5']}")
for oilAmount in amount:
    oil_amoun = oilAmount['oil_amount']

    #  print(f"{oilAmount['oil_amount']}")
if oil_amoun > 0:
    oil_amoun1 = oil_amoun - 5*bottle5
if oil_amoun1 > 0:
    oil_amoun2 = oil_amoun1 - 3*bottle3
if oil_amoun2 > 0:
    oil_amoun3 = oil_amoun2 - 1*bottle1
# f = open("U1rez.txt", "a")
print(bottle1, bottle3, bottle5, oil_amoun3)


# # # ANTRA UZDUOTIS: how many bottles left unused
# # if bottle was unused print amount of unused bottle
# # kazkaip virsuj sutvarkyti
# # if bottle['bottle1'] - 1*bottle1

# unusedbottle5 = bottle['bottle5']
# unusedbottle3 = bottle['bottle3']
# unusedbottle1 = bottle['bottle1']
usedbottle5 = 0
usedbottle3 = 0
usedbottle1 = 0

while oil_amoun3 >= 5 and bottle5 > 0:
    bottle5 -= 1
    usedbottle5 += 1
    oil_amoun3 -= 5

while oil_amoun3 >= 3 and bottle3 > 0:
    bottle3 -= 1
    usedbottle3 += 1
    oil_amoun3 -= 3

while oil_amoun3 >= 1 and bottle1 > 0:
    bottle1 -= 1
    usedbottle1 += 1
    oil_amoun -= 1

print(bottle1, bottle3, bottle5)

# # unused1 = bottle['bottle1'] - (1*bottle1)
# # unused3 = bottle['bottle3'] - (3*bottle3)
# # unused5 = bottle['bottle5'] - (5*bottle5)
# # print("", unused1, unused3, unused5)
# # while oil_amoun3 > 5:
# #     needed5 = oil_amoun3 // 5
# # while oil_amoun3 > 1:
# #     needed1 = oil_amoun3 // 1
# # while oil_amoun3 > 3:
# #     needed3 = oil_amoun3 // 3