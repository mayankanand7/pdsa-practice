def binarySearch(v,l):
    if l == []:
        return (False)
    
    # Mid point of the list
    m = len(l)//2

    if v == l[m]:
        return(True)
    
    if v < l[m]:
        return binarySearch(v, l[:m])
    else:
        return binarySearch(v, l[m+1:])

L = list(range(100000000))
print(binarySearch(1000000,L))