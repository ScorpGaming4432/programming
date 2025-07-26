def J(n:int):
  out = []
  temp = bin(n)[:1:-1]
  for i in range(len(temp)):
    if temp[i] == "1": out.append(i+1)
  return out

print(bin(19)[2:], J(19))
print(bin(6)[2:], J(6))
print(bin(42)[2:], J(42))
print(int("1001011", 2), "0b1001011")