#JFORMUŁA-3.pdf zrobione na lekcji
#JTEMP-3.pdf
temp = int(input())
while not(-100 <= temp <= 100): temp = int(input())
print(f'C\tK\tF\tR\n{temp}\t{round(temp+273.15,2)}\t{round((temp*9/5)+32,2)}\t{round((temp+273.15)*9/5,2)}')
#JWALUTY-2.pdf zrobione na lekcji
#LEKO01AJD-2.pdf
nums = input().split(' ')
while not(-2**15 <= int(nums[0]) <= 2**15-1 and -2**15 <= int(nums[1]) <= 2**15-1): nums = [input(), input()]
print(int(nums[0]) + int(nums[1]))
#LEK01BJD-2.pdf
nums = input().split(' ')
while not(-1000000 <= float(nums[0]) <= 1000000 and -1000000 <= float(nums[1]) <= 1000000): nums = [input(), input()]
print(round(float(nums[0])-float(nums[1]),2))
#LEK01CJD-2.pdf
s, t = int(input()), int(input())
while not(0<=s<=1000 and 0<=100<=100): s, t = int(input()), int(input())
print(round(s/t,2))