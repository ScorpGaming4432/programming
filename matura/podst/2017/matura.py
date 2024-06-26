with open("liczby.txt") as plik:
    dane = plik.readlines()
    for i in range(len(dane)):
        dane[i] = dane[i].rstrip().split(' ')

def nwd(a, b): return nwd(b, a%b) if b else a

# 4.1
ile = 0
for i in range(len(dane)):
    if dane[i][0] < dane[i][1] < dane[i][2]:
        ile += 1
print(ile)

# 4.2
lista = []
for i in range(len(dane)):
    lista.append(nwd(nwd(int(dane[i][0]), int(dane[i][1])), int(dane[i][2])))
print(sum(lista))

# 4.3
lista = []
for i in range(len(dane)):
    temp = 0
    for j in range(len(dane[i])):
        for cyfra in dane[i][j]:
            temp += int(cyfra)
    lista.append(temp)
temp = [0] * 3
for suma in lista:
    if suma == 35:
        temp[0] += 1
    if suma > temp[1]:
        temp[1] = suma
    elif suma == temp[1]:
        temp[2] += 1
print(temp[0], temp[2])

