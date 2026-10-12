def insertion(a):
	for sort_len in range(1,len(a)):
		cur_item = a[sort_len] # next item to insert
		insert_idx = sort_len # current index of item
		# iterate down until we reach appropriate insertion location
		while insert_idx > 0 and cur_item < a[insert_idx-1]:
			a[insert_idx] = a[insert_idx-1] # shift elements to make room
			insert_idx -= 1 # decrement the insertion index
		a[insert_idx] = cur_item # insert at correct location
	return a