#!/usr/bin/python3
def uppercase(c):
    for i in range(len(c)):
      if 97 <= ord(c[i]) <= 123:
        booly = True
      else:
        booly = False
      print("{}".format(chr(ord(c[i])-32)) if booly else c[i], end='')
    print()
