def sumOfNaturalNumbers(n):
    if n < 1:
        return n
    return(n + sumOfNaturalNumbers(n-1))


print(sumOfNaturalNumbers(10))