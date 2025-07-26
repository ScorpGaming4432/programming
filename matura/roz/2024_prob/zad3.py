workingfile = 'Dane-2412\\liczby.txt'
# workingfile = 'Dane-2412\\liczby_przyklad.txt'

with open(workingfile) as file:
  dane = file.readlines()
  for i in range(len(dane)):
    dane[i]:int = int(dane[i].rstrip()) # type: ignore



from math import sqrt

out = [[], [], {
  "<":0,
  ">":0,
  "==":[]
}]

'''for num in dane:
  num = int(num)

  # 3.1
  if sqrt(num) % 1 == 0:
    out[0].append(num)

  # 3.2 (the worst method by far)
  i = 2
  n = 5
  t_num = num
  while t_num != 1 and i<=t_num:
    if t_num % i == 0: n-=1
    
    while t_num % i == 0:
      t_num //= i
    i+=1
  if n <=0:
    out[1].append(num)

  # 3.3
  max_possible = ""
  min_possible = ""
  l = [0,0,0,0,0,0,0,0,0,0]
  for n in str(num):
    l[int(n)] += 1
  for i in range(len(l)):
    if l[i] != 0:
      min_possible += str(i) * l[i]
  for i in range(len(l)-1, -1, -1):
    if l[i] != 0:
      max_possible += str(i) * l[i]
  
  roz = int(max_possible) - int(min_possible)
  if roz < num:
    out[2]["<"] += 1
  elif roz > num:
    out[2][">"] += 1
  elif roz == num:
    out[2]["=="].append(num)
  else:
    raise ValueError("Cos jest kurwa nie tak")
  

print(out)'''
out = [
  [4489, 6241, 3136, 5476, 3721, 4900, 2304, 7569, 1521, 6724, 3364, 4624, 8281, 3481, 2025, 9025, 2500, 1296, 2601, 9801], 
  [2730, 8190, 2310, 4620, 7770, 8610, 4830, 4290, 6930, 6630], 
  {'<': 947, '>': 1052, '==': [6174]}
]
    
    
