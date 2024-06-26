def selection(arr):
	sort_idx = 0 # end of sorted portion of array
	while sort_idx < len(arr):
		min_idx = arr[sort_idx:].index(min(arr[sort_idx:])) + sort_idx
		arr[sort_idx], arr[min_idx] = arr[min_idx], arr[sort_idx]
		sort_idx += 1
	return arr