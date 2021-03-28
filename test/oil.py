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

#      print(f"{oilAmount['oil_amount']}")
if oil_amoun > 0:
    oil_amoun1 = oil_amoun - 5*bottle5
if oil_amoun1 > 0:
    oil_amoun2 = oil_amoun1 - 3*bottle3
if oil_amoun2 > 0:
    oil_amoun3 = oil_amoun2 - 1*bottle1
f = open("U1rez.txt", "a")
print(bottle1, bottle3, bottle5, oil_amoun3, file=f)

# how many bottles left unused
left_oil = oil_amoun3

usedbottle5 = 0
usedbottle3 = 0
usedbottle1 = 0

while left_oil >= 5 and bottle5 > 0:
    bottle5 -= 1
    usedbottle5 += 1
    left_oil -= 5

while left_oil >= 3 and bottle3 > 0:
    bottle3 -= 1
    usedbottle3 += 1
    left_oil -= 3

while left_oil >= 1 and bottle1 > 0:
    bottle1 -= 1
    usedbottle1 += 1
    left_oil -= 1

print(bottle1, bottle3, bottle5, file=f)


needed5 = oil_amoun3//5
oil_amoun3 = oil_amoun3 % 5
needed1 = oil_amoun3//1
oil_amoun3 = oil_amoun3 % 1
needed3 = oil_amoun3//3
oil_amoun3 = oil_amoun3 % 3
print(needed1, needed3, needed5, file=f)

# profit sum of bottles' amount minus expenses
prices =  db.execute("SELECT price1, price3, price5, expense, bottle1, bottle3, bottle5 FROM data")

for price in prices:
    price1 = price['price1']
    price3 = price['price3']
    price5 = price['price5']
    expense = price['expense']
    bottle1 = price['bottle1']
    bottle3 = price['bottle3']
    bottle5 = price['bottle5']


profit = (((needed1 + bottle1) * price1) + ((needed3 + bottle3) * price3) + ((needed5 + bottle5) * price5)) - expense
print(profit, file=f)
f.close()



# bandau ANTRA uzduoti
# from cs50 import SQL

# db = SQL("sqlite:///oil.db")
# amount = db.execute("SELECT oil_amount FROM data")
# rows = db.execute("SELECT bottle1, bottle3, bottle5 FROM data")

# for bottle in rows:
#     bottle1 = bottle['bottle1']
#     bottle3 = bottle['bottle3']
#     bottle5 = bottle['bottle5']
#  # print(f"{bottle['bottle1']} {bottle['bottle3']} {bottle['bottle5']}")
# for oilAmount in amount:
#     oil_amoun = oilAmount['oil_amount']

##  print(f"{oilAmount['oil_amount']}")


# if oil_amoun > 0:
#     oil_amoun1 = oil_amoun - 5*bottle5
# if oil_amoun1 > 0:
#     oil_amoun2 = oil_amoun1 - 3*bottle3
# if oil_amoun2 > 0:
#     oil_amoun3 = oil_amoun2 - 1*bottle1
# # f = open("U1rez.txt", "a")
# print(bottle1, bottle3, bottle5, oil_amoun3)

# # # ANTRA UZDUOTIS: how many bottles left unused
# # if bottle was unused print amount of unused bottle
# # kazkaip virsuj sutvarkyti
# # if bottle['bottle1'] - 1*bottle1

# unusedbottle5 = bottle['bottle5']
# unusedbottle3 = bottle['bottle3']
# unusedbottle1 = bottle['bottle1']

# while oil_amoun3 >= 5 and bottle5 <= bottle['bottle5']:
#     oil_amoun3 -= 5 * bottle5
#     unusedbottle5 -=1

# while oil_amoun3 >= 3 and bottle3 <= bottle['bottle3']:
#     oil_amoun3 -= 3 * bottle3
#     unusedbottle3 -=1

# while oil_amoun3 >= 1 and bottle1 <= bottle['bottle1']:
#     oil_amoun3 -= 1 * bottle1
#     unusedbottle1 -=1

# print(unusedbottle1, unusedbottle3, unusedbottle5)

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