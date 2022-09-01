def quicksort(L, l, r):
    if (r-l <= 1):
        return(L)
    
    (pivot, lower, upper) = (L[l], l+1, l+1)
    for i in range(l+1, r):
        if L[i] > pivot:
            upper += 1
        else:
            (L[i], L[lower]) = (L[lower], L[i])
            # Shift both segments
            (lower, upper) = (lower+1, upper+1)
    
    # Move pivot between lower and upper segment
    (L[l], L[lower-1]) = (L[lower-1], L[l])
    lower = lower-1

    # Recursive sort
    quicksort(L, l, lower)
    quicksort(L, lower+1, upper)

    return(L)


L = [1,4,12,6,7,8,8,9,10,-1,29,2]
print(quicksort(L, 0, 12))