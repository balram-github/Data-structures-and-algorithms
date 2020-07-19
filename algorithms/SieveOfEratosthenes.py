#!/usr/bin/python3
def SieveOfEratosthenes(n):
    primes = [True for i in range(n+1)]
    
    p=2
    while(p*p <=n):
        
        if primes[p] == True:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p+=1
    # print(primes)    
    # print(primes[2:])

    return  [i for i in range(2, n+1) if primes[i]]       


def exactly3Divisors(N):
    print(SieveOfEratosthenes(N))
    return sum(1 for _ in  filter(lambda x: x*x <=N,  SieveOfEratosthenes(N)))


print('\n[count] => {0}'.format(exactly3Divisors()))