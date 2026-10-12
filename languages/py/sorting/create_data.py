from random import shuffle

file = open('data.txt', 'w')

out = [x for x in range(100000)]
shuffle(out)

file.write(str(out)[1:-1])
print(out)