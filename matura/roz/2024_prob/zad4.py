workingfile = 'Dane-2412\\prostokaty.txt'
# workingfile = 'Dane-2412\\prostokaty_przyklad.txt'

with open(workingfile) as file:
  fread = file.readlines()
dane = []
for wiersz in fread:
  dane.append(wiersz.rstrip().split(" "))


# 4.1
pole = []
for w in dane:
  pole.append(int(w[0])*int(w[1]))
print(max(pole), min(pole))

# 4.2
kolejne=[]
tkol=[dane[0]]
for i in range(1, len(dane)):
  if int(dane[i][0])>int(dane[i-1][0]) or int(dane[i][1])>int(dane[i-1][1]):
    kolejne.append(tkol)
    tkol=[dane[i]]
  else:
    tkol.append(dane[i])
kolejne.append(tkol)

kolejne_lengths = [len(w) for w in kolejne]
print(max(kolejne_lengths), kolejne[kolejne_lengths.index(max(kolejne_lengths))][-1])

# 4.3
max_szer_2 = 0
for a in range(len(dane)):
  for b in range(a+1,len(dane)):
    if dane[a][0] != dane[b][0]: continue
    max_szer_2 = max(max_szer_2, int(dane[a][1]) + int(dane[b][1]))

max_szer_3 = 0
for a in range(len(dane)):
  for b in range(a+1,len(dane)):
    if dane[a][0] != dane[b][0]: continue
    for c in range(b+1,len(dane)):
      if dane[b][0] != dane[c][0]: continue
      max_szer_3 = max(max_szer_3, int(dane[a][1]) + int(dane[b][1]) + int(dane[c][1]))

max_szer_5 = 0
for a in range(len(dane)):
  for b in range(a+1,len(dane)):
    if dane[a][0] != dane[b][0]: continue
    for c in range(b+1,len(dane)):
      if dane[b][0] != dane[c][0]: continue
      for d in range(c+1,len(dane)):
        if dane[c][0] != dane[d][0]: continue
        for e in range(d+1,len(dane)):
          if dane[d][0] != dane[e][0]: continue
          max_szer_5 = max(max_szer_5, int(dane[a][1]) + int(dane[b][1]) + int(dane[c][1]) + int(dane[d][1]) + int(dane[e][1]))

print(max_szer_2, max_szer_3, max_szer_5)


'''ODP 
1545605418 10425
10 ['1001', '627']
79506 118786 180895
'''