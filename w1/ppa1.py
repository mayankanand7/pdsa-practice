''' 
Twin primes are pairs of prime numbers that differ by 2. For example (3, 5), (5, 7), and (11,13) are twin primes.
Write a function Twin_Primes(n, m) where n and m are positive integers and n < m , that returns all unique twin primes between m and n (both inclusive). The function returns a list of tuples and each tuple (a,b) represents one unique twin prime where n <= a < b <= m. 
'''
def twin_prime(n, m):
  (result, p1, i) = ([], 2, n)
  while (i <= m):
    if isPrime(i):
      p2 = i
      if ((p2 - p1) == 2):
        result.append((p1,p2))
      p1 = p2
    i += 1

  return(result)


'''
The method checks whether the number is prime or not. If it's prime then it returns True, otherwise False. It uses sqaure root method to check the primeness of the number.
'''
import math

def isPrime(a):
  if a == 1:
    return False
  (result, i) = (True, 2)
  while(result and (i <= math.sqrt(a))):
    if (a % i == 0):
      result = False
    i += 1
  
  return(result)



print(twin_prime(1,15))