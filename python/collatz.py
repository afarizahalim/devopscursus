#!/usr/bin/env python3

def collatz(number):
    nb = int(input("Enter a positive interger: "))
    
    if nb % 2 == 0:
        return nb // 2
    else:
        return 3 * nb + 1