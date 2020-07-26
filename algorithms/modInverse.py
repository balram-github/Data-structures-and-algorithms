#!/usr/bin/python3

def modInverse(a,m):
    ##Your code here
    
    for i in range(1, m+1):
        mi = -1
        if (i*a)%m ==1:
            return i%m
     
    return mi