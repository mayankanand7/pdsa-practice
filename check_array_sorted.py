''' The program is to check if the array is sorted in recursive way '''
def isArraySorted(L, index):
    if len(L) == 1:
        return True
    print("Check :: ", L[index-1], L[index-2])
    if (L[index-1] < L[index-2]):
        return False
    else:
        return isArraySorted(L[:index-1], index-1)

L = [1,2,3,8,5,6]
print(isArraySorted(L, 6))