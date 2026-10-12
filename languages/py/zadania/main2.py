def searchfor(matrix, number):
    ile = []
    for row in matrix:
        for element in row:
            if element == number:
                ile.append(row)
    return ile

def digitsum(num:str):
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum

import math
def isprime(n:int):
    if (n % 2 == 0 and n > 2) or (n in (0, 1)): 
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

with open("trojki.txt") as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].split()
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])

ile = [0, 0, [0, sum(data[0])], 0]
for i in range(len(data)):
    for j in range(len(data[i])):
        if isprime(data[i][j]): ile[0]+=1
    if data[i][0] - data[i][1] < 0: ile[1]+=1
    if sum(data[i]) > ile[2][0]: 
        ile[2][0] = sum(data[i])
    elif sum(data[i]) < ile[2][1]: ile[2][1]= sum(data[i])
    ile[3] += sum(data[i])
if isprime(digitsum(str(ile[3]))):
    tmp = searchfor(data, digitsum(str(ile[3])))
    print(tmp)
    print(len(tmp))
    