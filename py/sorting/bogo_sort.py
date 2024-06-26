def is_sorted(arr:list):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]: return False
    return True

def bogo(array:list):
    from random import shuffle
    itteration_count=0
    while not is_sorted(array):
        shuffle(array)
        itteration_count+=1
    return itteration_count, array 