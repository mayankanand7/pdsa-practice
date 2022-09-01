''' Directly check any faction between 2 and n-1 '''
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


''' Directly check if n has a factor between 2 and n//2 '''
def isPrime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


''' It is sufficent to check till sqrt(n) '''
import math
def isPrime_method3(n):
    (result, i) = (True, 2)
    while (result and (i <= math.sqrt(n))):
        if n%i == 0:
            result = False
        i += 1
    return(result)


print(isPrime_method3(4))