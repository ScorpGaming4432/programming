file = open('szachy.txt').readlines()
data = []
pod = []
for i in range(len(file)):
    if file[i] == '\n': 
        data.append(pod)
        pod = []
    else: pod.append(file[i].rstrip())
print(len(data))
# 1.1
['........', 
 '.......H', 
 'K.......', 
 'P....hp.', 
 '....W.k.', 
 '.......p', 
 '........', 
 '........']
ile = [0, []]
for plansza in data:
    flag = True
    tmpile = 0
    for j in range(len(plansza[0])):
        for i in range(len(plansza)):
            if plansza[i][j] != '.': break
            flag = True
            tmpile += 1
    ile[1].append(tmpile)
    if flag: ile[0] += 1

print(ile)


def piececounter(board):
    small, large = 0, 0
    for pod in board:
        for piece in pod:
            small += int(piece.islower())
            large += int(piece.isupper())
    return small, large

ile = 0
for plansza in data:
    print(plansza)
    lower, upper = piececounter(plansza)
    print(lower, upper)
    ile += int(lower == upper)
    print(ile)
print(ile)
