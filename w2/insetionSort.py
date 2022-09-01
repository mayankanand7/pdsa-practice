''' Iterative '''
def insertionSort(L):
    n = len(L)
    if n < 1:
        return(L)
    
    for i in range(n):
        j = i
        while(j > 0 and L[j] < L[j-1]):
            (L[j],L[j-1]) = (L[j-1], L[j])
            j = j-1
    return(L)


''' Recursive '''
def insert(L, v):
    n = len(L)
    if n == 0:
        return([v])
    if v >= L[-1]:
        return(L+[v])
    else:
        return(insert(L[:-1], v)+L[-1:])


def Isort(L):
    n = len(L)
    if n < 1:
        return(L)
    L = insert(Isort(L[:-1]), L[-1])
    return(L)

L = [1,4,5,6,7,8,8,9,10,-1,29,2]
print(Isort(L))