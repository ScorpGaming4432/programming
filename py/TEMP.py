def function(x):
    if x == 0:
<<<<<<< HEAD
        return 0, 1  # Funkcja została wywołana 1 raz
    else:
        wynik, wywolania_z_rekurencji = function(x // 2)
        return 2 + wynik, wywolania_z_rekurencji + 1  # Dodajemy 1 wywołanie za bieżące wywołanie

'''import time
i = 2
while True:
    wynik = function(i)
    print(i, wynik)
    i*=2
    if i :
        break'''

out = []
for i in range(20000):
    wynik = function(i)
    if wynik[0] == 18:
        out.append(i)
print(min(out), max(out))
=======
        return x
    else:
        return 2 + function(x // 2)

print(function(3))
print(function(16))
print(function(35))
>>>>>>> 6c0e11f6032e7b9187ab17acf7c46f2587e7caa0
