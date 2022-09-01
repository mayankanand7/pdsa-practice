from requests import ReadTimeout


def binarySearch(L, s, e, v):
    if s > e:
        return(False)
    
    mid = (s + e) // 2

    if v < L[mid]:
        s = s
        e = mid - 1
        return(binarySearch(L, s, e, v))
    elif v > L[mid]:
        s = mid + 1
        e = e
        return(binarySearch(L, s, e, v))
    else:
        return(v == L[mid])

L = [1,2,3,4,5,6,7,8,9,10,11]
print(binarySearch(L, 0, (len(L)-1), 91 ))