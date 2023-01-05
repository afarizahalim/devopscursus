#!/usr/bin/env python3

def division(divideBy):
    try:
        print(f"Division of 42 / {divideBy} is: ")
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument")

print(division(2))
print(division(12))
print(division(0))
print(division(1))