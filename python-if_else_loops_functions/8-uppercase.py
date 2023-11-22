#!/usr/bin/python3
def uppercase(c):
    for i in c:
      print("{}".format(chr(ord(c[i])-32)) if 97 <= ord(c[i]) <= 123 else c[i], end='')
    print()
