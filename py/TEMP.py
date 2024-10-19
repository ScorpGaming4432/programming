def function(x):
    if x == 0:
        return x
    else:
        return 2 + function(x // 2)

print(function(3))
print(function(16))
print(function(35))