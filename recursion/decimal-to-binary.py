def decToBinary(n, result):
    if n == 0:
        return result
    
    result = str(n % 2) + result
    return(decToBinary(n//2, result))

print(decToBinary(7, ""))