''' Quick sort iterative '''
from numpy import partition
from pandas import pivot


def quickSort(L, s, e):
    if e - s <= 1:
        return(L)
    
    (pivot, lower, upper) = (L[s], s+1, s+1)

    for i in range(s+1, e):
        if pivot < L[i]:
            upper = upper + 1 # Extend upper segment
        else:
            (L[i], L[lower]) = (L[lower], L[i]) # Swap L[i] with L[lower]
            (lower, upper) = (lower + 1, upper + 1) # Extend both lower and upper segment
    
    # Move pivot between lower and upper segment
    (L[s], L[lower-1]) = (L[lower-1], L[s])
    lower = lower - 1
    
    # Recursive calls
    quickSort(L, s, lower)
    quickSort(L, lower+2, e)

    return(L)


''' Quick sort recursive '''
def quickSortRecursive(L, s, e):
    if e - s <= 1:
        return(L)
    pivot_pos = partition(L, s ,e)

    quickSortRecursive(L, s, pivot_pos-1)
    quickSortRecursive(L, pivot_pos+1, e)

    return(L)

def partition(L, lower, upper):
    # Selecting first element as pivot
    pivot = L[lower]
    
    i = lower
    for j in range(lower+1, upper+1):
        if L[j] <= pivot:
            i = i + 1
            (L[i], L[j]) = (L[j], L[i])
    (L[lower], L[i]) = (L[i], L[lower])

    return(i)
    


L =[9,4,-1,0,5,-1,10,12,100,-110]
print(quickSortRecursive(L, 0, (len(L)-1)))