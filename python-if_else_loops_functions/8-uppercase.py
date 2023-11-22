#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if i != len(str):
            print(chr(ord(str[i])-32) if 97 <= ord(str([i])) <= 123 else str[i], end='')
        else:
            print(chr(ord(str[i])-32) if 97 <= ord(str([i])) <= 123 else str[i])
