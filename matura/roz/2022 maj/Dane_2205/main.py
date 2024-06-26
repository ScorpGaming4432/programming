def rozklad(val:int):
    i = 2
    out = []
    while i < val:
        if not val % i:
            out.append(i)
            val = val / i
        else:
            i += 1
    return out + [i]

file = 'liczby.txt'
#file = 'przyklad.txt'
liczby = open(file).readlines()
for i in range(len(liczby)):
    liczby[i] = liczby[i].rstrip()

odp = [[0, 0], [0, 0, 0, 0], [0, [], 0]]
for i in range(len(liczby)):
    odp[0][0] += liczby[i][0] == liczby[i][-1]
    if not odp[0][1] and liczby[i][0] == liczby[i][-1]:
        odp[0][1] = int(liczby[i])
    
    pierw = rozklad(int(liczby[i]))
    if len(pierw) > odp[1][1]:
        odp[1][0:2] = [int(liczby[i]), len(pierw)]
    if len(set(pierw)) > odp[1][3]:
        odp[1][2::] = [int(liczby[i]), len(set(pierw))]
    liczby[i] = int(liczby[i])

for a in liczby:
    for b in liczby:
        if not(a < b) or b % a: continue
        for c in liczby:
            if b < c and not(c % b):
                odp[2][1].append((a, b, c))
odp[2][0] = len(odp[2][1])
for a in liczby:
    for b in liczby:
        if not(a < b) or b % a: continue
        for c in liczby:
            if not(b < c) or c % b: continue
            for d in liczby:
                if not(c < d) or d % c: continue
                for e in liczby:
                    if d < e and not(e % d):
                        odp[2][2] += 1


w = open('wyniki4.txt', 'w')
w.write('1. {} {}\n'.format(*odp[0]))
w.write('2. {} {} {} {}\n'.format(*odp[1]))
w.write(f'3a. {odp[2][0]}\n')
for i in range(len(odp[2][1])):
    w.write(f'{odp[2][1][i]}\n')
w.write(f'3b. {odp[2][2]}\n')
