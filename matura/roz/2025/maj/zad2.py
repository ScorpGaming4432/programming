with open('dane maj 23\\symbole.txt', 'r') as f1:
    dane = f1.readlines()
for i in range(len(dane)):
    dane[i] = dane[i].rstrip()


def is_palindrome(s:str):
    for i in range(len(s)//2):
        if wiersz[i] != wiersz[-1-i]:
            return False
        
    return True

# 2.1
# for wiersz in dane:
#     if is_palindrome(wiersz): print(wiersz)
    
# 2.2
# sym_set = {'+', '*', 'o'}

# for i in range(1, len(dane)-1):
#     for j in range(1, len(dane[i])-1):
#         kwad = [wiersz[j-1:j+2] for wiersz in dane[i-1:i+2]]
#         if (kwad[0] == kwad[1] == kwad[2]) and (set(kwad[0]).__len__() == 1):
#             print(i+1, j+1, kwad)




# 2.3
maks = 0
w_maks = ''
mapping = {'+':'1', '*':'2', 'o':'0'}
rev_mapping = {'0':'o', '1':'+', '2':'*'}
for wiersz in dane:
    base3 = ''
    for i in range(len(wiersz)):
        base3 += mapping[wiersz[i]]
    base3 = int(base3, 3)
    if maks < base3: 
        maks = base3
        w_maks = wiersz

print(maks, w_maks)

# 2.4
out = ''
to_sum = []
for wiersz in dane:
    tmp = ''
    for i in range(len(wiersz)):
        tmp += mapping[wiersz[i]]
    to_sum.append(int(tmp, 3))
summed = sum(to_sum)
print(summed, end=' ')

while summed > 0:
    out = rev_mapping[str(summed%3)] + out
    summed //= 3
print(out)

import math
math.gcd