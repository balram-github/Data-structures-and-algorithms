##Complete this function
def digitsInFactorial(N):
    #Your code here

    fac  =1 
    
    while(N):
        fac *= N
        N-=1
        
    return math.floor(math.log10(fac) +1)    
