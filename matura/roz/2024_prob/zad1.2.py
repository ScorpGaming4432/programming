def J(n:int):
  out = []
  temp = 0
  i=0
  while n != 0:
    temp += (n % 2) * (10**i)
    n//=2
    i+=1
  
  for i in range(len(str(temp))): # jednak str() jest dozwolony
    if str(temp)[-i-1] == "1": out.append(i+1)
  return out

print(J(19))