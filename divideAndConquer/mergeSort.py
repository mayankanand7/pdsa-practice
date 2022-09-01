def mergerSort(L, s, e):
    if s - e == 0:
        return([L[s]])
    
    mid = (s + e)//2
    return(merge(mergerSort(L, s, mid), mergerSort(L, mid+1, e)))


def merge(A, B):
    (m,n) = (len(A), len(B))
    (C, i, j) = ([], 0, 0)
    while i < m and j < n:
        if A[i] <= B[j]:
            C.append(A[i])
            i = i + 1
        else:
            C.append(B[j])
            j = j + 1
    while i < m:
        C.append(A[i])
        i = i + 1
    while j < n:
        C.append(B[j])
        j = j + 1

    return(C)

L =[9,4,-1,0,5,-1,10,12,100,-110]
print(mergerSort(L, 0, (len(L) - 1)))