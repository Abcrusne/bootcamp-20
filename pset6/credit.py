from cs50 import get_int, get_string

card = input("Number: ")
while not card.isdigit() or int(card) < 0:
    card = input("Again: ")
length = len(card)

luhn1 = sum(int(n) * 2 % 10 + int(n) * 2 // 10 for n in card [-2::-2])


#print(luhn1)


luhn2 = sum(int(n) for n in card [-1::-2])


# print(luhn2)


if (luhn1 + luhn2) % 10:
    print("INVALID")
elif length == 15 and card[0:2] == "34" or card[0:2] == "37":
    print("AMEX")
elif length == 16 and card[0:2] == "51" or card[0:2] == "52" or card[0:2] == "53" or card[0:2] == "54" or card[0:2] == "55":
    print("MASTERCARD")
elif length == 13 or length == 16 and card[0:1] == "4":
    print("VISA")

# count = 0
# sum = 0

# while (card > 0):
#     card = card // 10
#     count +=1

# while (card > 0):
#     a = card % 10
#     sum = sum + a
#     card // 100
# # while not card.isdigit() or int(card) < 0: jei input naudoju
# #     card = get_int("Number: ")
# #     print(card[-2::-2])
# # for i in range (len(card)):
# while (card > 0):
#     a = card % 10
#     b = a * 2
#     sum = sum + (b % 10) + (b/10)
#     card // 100

# if (sum % 10 == 0):
#     if ((card >= 4000000000000 and card < 5000000000000) or (card >= 4000000000000000 and card < 5000000000000000)):
#             print("VISA")