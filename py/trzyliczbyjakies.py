a = int(input())
b = int(input())
c = int(input())

sorted = [a, b, c].sort()
print((sorted+'\n')*max(sorted[-1]))