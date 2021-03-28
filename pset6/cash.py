# from cs50 import get_float, get_int

# while True:
#     dollars = get_float("Change: ")
#     if dollars >= 0:
#         break

# cents = round(dollars * 100)
# coins = 0

# while cents >= 25 and cents//25:
#     cents -= 25
#     coins += 1


# while cents >= 10:
#     cents -= 10
#     coins +=1


# while cents >= 5:
#     cents -= 5
#     coins +=1

# while cents >= 1:
#     cents -= 1
#     coins +=1

# print("Coins: ", coins)


# jei noriu kad ir isprintintu kiek ir kokiu monetu, ne tik kieki.
from cs50 import get_float, get_int



while True:
    dollars = get_float("Change: ")
    if dollars >= 0:
        break

cents = round(dollars * 100)
coins = 0
f = open("output.txt", "a")
print(cents//25, "25c", file=f)
cents = cents%25
print(cents//10, "10c", file=f)
cents = cents%10
print(cents//5, "5c", file=f)
cents = cents%5
print(cents//1, "1c", file=f)
f.close()