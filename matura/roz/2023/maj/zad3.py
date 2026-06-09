file = 'Dane_2305\\pi.txt'
# file = 'Dane_2305\\pi_przyklad.txt'

with open(file, 'r') as f:
    pi = ''
    for line in f:
        pi += line.strip()

# print(pi)

def if_rosmal_6(smallset:str):
    if len(smallset) != 6:
        raise ValueError('Cwel')
    
    if smallset[0] >= smallset[1] or smallset[4] <= smallset[5]: return False
    
    for i in range(1,4): 
        if smallset[i] >= smallset[i+1]: break
        
    for j in range(i+1, 4):  #I DONT FUCKING CARE ITS OKAY
        if smallset[j] <= smallset[j+1]: return False
        
    return True

"""
print(if_rosmal('257983')) # True
print(if_rosmal('579831')) # True
print(if_rosmal('028841')) # True
print(if_rosmal('089986')) # True
print(if_rosmal('899862')) # True
print(if_rosmal('258434')) # False
"""

# counter = 0
# for i in range(len(pi)-5):
#     if if_rosmal_6(pi[i:i+6]):
#         counter += 1
#         print(pi[i:i+6])
# print(counter)

def if_rosmal(smallset:str):
    
    if smallset[0] >= smallset[1] or smallset[-2] <= smallset[-1]: return False
    
    for k in range(1,len(smallset)-1): 
        if smallset[k] >= smallset[k+1]: break
        
    for n in range(k+1, len(smallset)-2):  #I DONT FUCKING CARE ITS OKAY
        if smallset[n] <= smallset[n+1]: return False
        
    return True

def ifnurincreasing(small:str):
    for k in range(len(small)-1):
        if small[k] >= small[k+1]: return False
    return True
        

max_index = 0
max_length = 0
for i in range(len(pi)-4):
    for j in range(i+4, len(pi)-4):
        # print(i, pi[i:j])
        if pi[j-1] == pi[j-2] and pi[j-2] != pi[j-3]: continue
        if ifnurincreasing(pi[i:j]): continue
        
        if not if_rosmal(pi[i:j]):
            if max_length < j-i -1:
                max_length = j-i -1
                max_index = i
            break
    # if i == 3000: break
print(max_index+1, max_length, pi[max_index:max_index+max_length])

