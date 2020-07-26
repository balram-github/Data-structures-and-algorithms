#!/usr/bin/python3

def isPrime(N):
#Your code here
p=2
while (p*p <= N):
    if N%p == 0:
        return False
    p +=1    
return True