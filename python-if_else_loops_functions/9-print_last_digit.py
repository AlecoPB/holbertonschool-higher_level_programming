#!/usr/bin/python3
def print_last_digit(number):
    print(str(int(number))[len(str(number))-1], end='')
    return int(str(number)[len(str(number))-1])
