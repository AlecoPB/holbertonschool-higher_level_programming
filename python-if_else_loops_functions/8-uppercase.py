#!/usr/bin/python3
def uppercase(c):
    for i in c:
      if 97 <= ord(c[i]) <= 123:
        booly = True
      else:
        booly = False
      print("{}".format(chr(ord(c[i])-32)) if booly else "{}".format(c[i]), end='')
    print()
