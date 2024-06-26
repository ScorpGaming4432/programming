#from read_data_def import read_data as read

def is_sorted(arr:list):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]: return False
    return True


def counting(arr, exp1): 
   
    n = len(arr) 
   
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
   
    # initialize count array as 0 
    count = [0] * (10) 
   
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
   
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
   
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        i -= 1
   
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
 
# Method to do Radix Sort
def radix(arr):
 
    # Find the maximum number to know number of digits
    max1 = max(arr)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        counting(arr,exp)
        exp *= 10

def cocktail(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
 
        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False
 
        # loop from left to right same as the bubble
        # sort
        for i in range (start, end):
            if (a[i] > a[i+1]) :
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True
 
        # if nothing moved, then array is sorted.
        if (swapped==False):
            return a
 
        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False
 
        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end-1
 
        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
 
        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start+1







