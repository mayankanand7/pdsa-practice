def mergeSort(L):
    n = len(L)
    if n < 2:
        return(L)
    
    A = mergeSort(L[:n//2])
    B = mergeSort(L[n//2:])

    C = merge(A, B)

    return(C)

def merge(A, B):
    (m, n) = (len(A), len(B))
    (C, i, j, k) = ([], 0, 0, 0)

    while k < m+n:
        if i == m:
            C.extend(B[j:])
            k = k + n-j
        elif j == n:
            C.extend(A[i:])
            k = k + m-i
        elif A[i] < B[j]:
            C.append(A[i])
            (i, k) = (i+1, k+1)
        else:
            C.append(B[j])
            (j, k) = (j+1, k+1)
    
    return C

L = [1,4,5,6,7,8,8,9,10,-1,29,2]
print(mergeSort(L))