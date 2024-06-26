'''
Things we know from pythagorean
a*a + b*b = c*c


'''
from time import time
from defs import isprime
lim = int(input("Do jakiej liczby podać trójki pitagorejskie?\n"))
t = time()
#lim = 100
pitagorejskie = []
najw = (0, 0, 0)
for a in range(3, lim):
    for b in range(a, a*a):
        c = (a**2 + b**2)**0.5
        if (isprime(a) or isprime(b) or isprime(c)) and round(c) == c: 
            pitagorejskie.append({a, b, int(c)})
            if max(najw) < max((a, b, c)): najw = (a, b, c)
            print(a, b, int(c))
#print(pitagorejskie)
        