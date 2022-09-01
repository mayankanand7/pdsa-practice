from pyrsistent import m


def selectionSort(L):
    n = len(L)
    if n < 1:
        return(L)
    
    for i in range(n):
        min_pos = i
        for j in range(i+1, n):
            if L[j] < L[min_pos]:
                min_pos = j
        (L[i],L[min_pos]) = (L[min_pos], L[i])
    
    return(L)