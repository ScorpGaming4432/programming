with open("liczby.txt") as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].rstrip()

def binToDec(num:str):
    out = 0
    for i in range(len(num)):
        out += int(num[-i-1]) * (2**i)
    return out

def decToBin(num:int):
    n = 0
    ws = ''
    while num >= 2**n:
        ws += '0'
        n += 1
    out = ''
    for i in range(len(ws)):
        if num >= 2**(len(ws) - i - 1):
            out += '1'
            num -= 2**(len(ws) - i - 1)
        else:
            out += '0'
    return(out)


# 6.a
hm = 0
for num in data:
    if num[-1] == '0':
        hm += 1
print(hm)

# 6.b
largest = [0, 0]
for num in data:
    if binToDec(num) > largest[1]:
        largest = [num, binToDec(num)]
print(largest)

# 6.c
tmp = []
for num in data:
    if len(num) == 9:
        tmp.append(binToDec(num))
print(len(tmp), decToBin(sum(tmp)))
