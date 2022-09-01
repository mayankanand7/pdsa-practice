''' GCD computation '''
def gcd(m,n):
    cf = [] # List of common factors
    for i in range(1,min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            cf.append(i)
    return(cf[-1])

''' GCD computation by Elimination '''
def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            mrcf = i
    return(mrcf)

''' Better Way '''
def gcd(m,n):
    (a,b) = (max(m,n), min(m,n))
    if a%b == 0:
        return(b)
    else:
        return(gcd(b,a-b))

''' Euclid's Algorithm '''
def gcd(m,n):
    (a,b) = (max(m,n), min(m,n))
    if a%b == 0:
        return(b)
    else
        return(gcd(b,a%b))