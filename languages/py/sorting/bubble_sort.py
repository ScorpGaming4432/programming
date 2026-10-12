def bubble(arr):
	swapped=True
	while swapped:
		swapped=False
		for i in range(1,len(arr)):
			if arr[i-1]>arr[i]:
				arr[i],arr[i-1] = arr[i-1],arr[i]
				swapped=True
	return arr