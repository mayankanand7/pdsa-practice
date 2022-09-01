def print_list_elements(L):
    n = len(L)
    if n == 0:
        return
    print(L[0])
    print_list_elements(L[1:])

L = [1,2,3,4,5]
print_list_elements(L)