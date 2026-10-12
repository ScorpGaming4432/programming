def quick(a):
	from random import randint
	if len(a)<=1: return a 

	smaller,equal,larger=[],[],[]
	pivot=a[randint(0,len(a)-1)]

	for x in a:
		if x<pivot:    smaller.append(x)
		elif x==pivot: equal.append(x)
		else:          larger.append(x)

	return quick(smaller)+equal+quick(larger)