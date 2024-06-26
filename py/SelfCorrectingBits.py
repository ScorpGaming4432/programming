#generate a twodimentional array
from random import randint
from defs import printarray

#generate a random number
n = 2
data = []
for i in range(2**n):
    tmp = []
    for j in range(4):
        tmp.append(randint(0, 1))
    data.append(tmp)
data = '1000'+'0011'+'1011'+'0110'
#check for errors
def correct(data):
    futuredata = data
    futuredata[0][0] = (data[0][:2] + data[1][:2] + data[2][:2] + data[3][:2])%2
    futuredata[0][2] = (data[0][2:] + data[1][2:] + data[2][2:] + data[3][2:])%2
    futuredata[]