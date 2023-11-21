#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
dgt = str(number)[len(str(number))-1]
dgt = int(dgt)
if dgt > 5 and number > 0:
    indic = "and is greater than 5"
elif (dgt < 6 or number < 0) and dgt != 0:
    indic = "and is less than 6 and not 0"
else:
    indic = "and is 0"
if number < 0:
    print("Last digit of", number, "is", -1*dgt, indic)
else:
    print("Last digit of", number, "is", dgt, indic)
