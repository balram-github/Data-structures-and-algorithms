# Input:
# 3
# 1 -2 1
# 1 -7 12
# 1 4 8

# Output:
# 1 1
# 4 3
# Imaginary

def quadraticRoots(a,b,c):
    #Your code here

    d = (b*b)-(4*a*c)
    if d < 0:
        print('Imaginary')
        return
        
    rt1 = (-b+math.sqrt(d))/(2*a)    
    rt2 = (-b-math.sqrt(d))/(2*a)
    
    print(math.floor(rt1), math.floor(rt2), sep=' ') 