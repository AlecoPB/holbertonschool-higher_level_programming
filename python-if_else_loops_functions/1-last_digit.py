#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
dgt = str(number)[len(str(number))-1]
# dgt = int(dgt)
if number < 0:
    dgt = -1*int(dgt)
if int(dgt) > 5:
    indic = "and is greater than 5"
elif int(dgt) == 0:
    indic = "and is 0"
else:
    indic = "and is less than 6 and not 0"
print("Last digit of", number, "is", dgt, indic)
