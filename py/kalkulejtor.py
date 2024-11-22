def add(n1, n2): return n1 + n2
def sub(n1, n2): return n1 - n2
def mul(n1, n2): return n1 * n2
def div(n1, n2): return n1 / n2
a = int(input("Podaj pierwszą liczbę"))
b = int(input("Podaj drugą liczbę"))
o = input("Podaj jaką operację wykonać")
print(o(a, b))