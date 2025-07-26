F_Counter = 0

def F(x:int, p:int):

  global F_Counter
  F_Counter += 1

  if x < 0 or not (1 <= p <= 10): raise ValueError("jestes pojebem kurwa")

  if x==0:
    return 0
  else:
    c = x % p
    if c % 2 == 1:
      return F(x//p, p) + c
    else:
      return F(x//p, p) - c
    
# 2.1
print(F(130, 3), F_Counter);F_Counter=0
print(F(220, 4), F_Counter);F_Counter=0

# 2.2 (bruteforce)
x = 99
while F(x, 3) != 0:
  x-=1
print(x)

x = 99
while F(x, 4) != 0:
  x-=1
print(x)