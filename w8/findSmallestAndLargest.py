from traceback import print_tb


def findSmallestAndLargest_v1(L):
    smallest = L[0]
    largest = L[0]
    for i in range(1, len(L)):
        if L[i] < smallest:
            smallest = L[i]
        if L[i] > largest:
            largest = L[i]
    print("smallest : ", smallest, " and largest : ", largest)

def findSmallestAndLargest_v2(L):
    _min = L[0]
    _max = L[0]
    for i in range(1,len(L)-1,2):
        if L[i] < L[i+1]:
            if L[i] < _min:
                _min = L[i]
            if L[i+1] > _max:
                _max = L[i+1]
        if L[i] > L[i+1]:
            if L[i+1] < _min:
                _min = L[i+1]
            if L[i] > _max:
                _max = L[i]
    print("min : ", _min, " and max : ", _max)

L = [1,4,5,6,7,8,8,9,10,-1,29,2]

findSmallestAndLargest_v2(L)

findSmallestAndLargest_v1(L)