def digitsum(num:str):
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum

import math
def isprime(n:int):
    """Check if n is a prime number
    
    A prime number is a positive natural number that can only be divided by itself and 1 without remainders

    Args:
        n (int): positive integer valuse

    Returns:
        bool: True (if n is prime), False (if n is not prime)
    """    ''''''
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

output = [[], [], [], [0, 0]] # [zad1[], zad2[], zad3[], zad4[ile, największa]]
for i in range(len(data)):
# 66.1
    if digitsum(str(data[i][0])) + digitsum(str(data[i][1])) == data[i][2]:
        output[0].append(data[i])
# 66.2
    if isprime(data[i][0]) and isprime(data[i][1]) and data[i][2] == data[i][0] * data[i][1]:
        output[1].append(data[i])
# 66.3
    tmp = (data[i][0]**2, data[i][1]**2, data[i][2]**2)
    if sum(tmp) - max(tmp) == max(tmp):
        output[2].append(data[i])
# 66.4
    if max(data[i]) < sum(data[i]) - max(data[i]):
        if output[3][1] < max(data[i]):
            output[3][1] = max(data[i])
        output[3][0] += 1

print(output[0])
print(output[1])
print(output[2])
print(output[3])
i = 71824957
ile = 0
while True:
    if isprime(i):
        if not(ile % 100):
            print(i, len(str(i)))
        ile += 1
    i+=1