def zliczacz(word: str):
    out = {}
    for litera in word:
        if litera in ['A', 'I', 'U', 'E', 'O', 'Y']:
            if litera not in out: 
                out[litera] = 1
            else:
                out[litera] += 1
    return out
            
print(zliczacz('MATKA'))

with open('sygnaly.txt', 'r') as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].rstrip()

print(set([0,1,2,3,2,1,0,-1]))

zapisane_i = 0
naj = 0
for i in range(len(data)):
    if sum(zliczacz(data[i]).values()) > naj:
        naj, zapisane_i = sum(zliczacz(data[i]).values()), i

print(sum(zliczacz(data[zapisane_i]).values()))
print(zapisane_i)
print(data[zapisane_i], zliczacz(data[zapisane_i]))

ile = 0
for i in range(len(data)):
    if len(data[i]) % 2 and data[i][-1] in ['B','C','D','F','G','H','K','L','M','N','P','Q','R','S','T','V','W','X','Z']: ile+=1
    
print(ile)