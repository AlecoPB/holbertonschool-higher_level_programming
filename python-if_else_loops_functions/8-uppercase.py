#!/usr/bin/python3
def uppercase(c):
    for i in range(len(c)):
        if i != len(c):
            print("{}".format(chr(ord(c[i])-32)) if 97 <= ord(c([i])) <= 123 else "{}".format(c[i]), end='')
        else:
            print("{}".format(chr(ord(c[i])-32)) if 97 <= ord(c([i])) <= 123 else "{}".format(c[i]))
