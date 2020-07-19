def termOfGP(A,B,N):
    #Your code here

    r = B/A
    # print(r)
    # print(math.pow(r, (N-1)))
    #return (A*math.pow(r, (N-1)))
    return (A*(r**(N-1)))
    