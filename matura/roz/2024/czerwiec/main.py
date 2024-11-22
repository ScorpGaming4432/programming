import collections
from math import *

# from defs import printarray, occurence
def mprintarray(array:list):
    """Prints a 2d array. right adjusting the objects for the space difference between object sizes.

    Args:
        array (list): array for printing
    """
    maxlength = 0
    for line in array:
        for object in line:
            if maxlength < len(str(object)):
                maxlength = len(str(object))
    for line in array:
        for object in line:
            print(str(object).rjust(maxlength), end=" ")
        print()
def occurance(itt: collections.Iterable, sort:str =None):
    """Count the occurance of each element in an itterable element f.e. letters, numbers in an array or string.

    Args:
        itt (Itterable): Itterable element to count the occurance of.
    (optional)
        sort (str): Ascending ('asc') or Descending ('desc')

    Returns:
        dict {element : count}: Output with all counted occurances of each element.
    (if `sort` used)
        list [element]: Output with sorted elements 

    """
    out = {}
    for occ in itt:
        if occ in out:
            out[occ] += 1
        else:
            out[occ] = 1
    if sort == None:
        return out
    else:
        return sorted(out, key=lambda d: out[d], reverse=sort=='desc')


def mbin(i: int):
    """Converts an integer to binary."""
    out = ''
    
    while i != 0:
        out = str(i % 2) + out
        i = i // 2
    return out

## 1
'''w = int(input())
k = int(input())
n = int(input())
nabis = mbin(n)
ilerazy = ceil(w * k / len(nabis))

nagrid = nabis * ilerazy
nagrid = nagrid[:w*k]
nagrid = [nagrid[i*k:(i+1)*k] for i in range(len(nagrid)//k)]

mprintarray(nagrid)'''

with open('informatyka-2024-czerwiec-matura-rozszerzona-zalaczniki\\slowa.txt') as file:
    slowa = file.readlines()
for i in range(len(slowa)):
    slowa[i] = slowa[i].rstrip()

'''out = []

#1
tmpout = 0
for slowo in slowa:
    for i in range(len(slowo)-2):
        if slowo[i] == 'k' and slowo[i+2] == 't':
            tmpout += 1
print(tmpout)

#2
tmpout=0
def rot13(sl:str):
    out = ''
    for i in range(len(sl)):
        out += 'nopqrstuvwxyzabcdefghijklm'[ord(sl[i])-ord('a')]
    return out

for slowo in slowa:
    if slowo[::-1] == rot13(slowo):
        tmpout += 1
print(tmpout)
'''
#3
for slowo in slowa:
    occ = occurance(slowo)
    if max(occ.values()) >= len(slowo)/2:
        print(slowo) 


# 4
def inttobase(num:int, base:int):
    pass