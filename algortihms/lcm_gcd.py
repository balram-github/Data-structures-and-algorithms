#!/usr/bin/python3

# Given two numbers A and B. The task is to find out their LCM and GCD.

# Input:
# The first line of input contains an integer T denoting the number of testcases. T testcases follow. In each test cases, there are two numbers A and B separated by space.

# Output:
# For each testcase in a new line, print LCM and GCD separated by space.

# Constraints:
# 1 <= T <= 104
# 1 <= A <= 108
# 1 <= B <= 108

# Example:
# Input:
# 2
# 5 10
# 14 8

# Output:
# 10 5
# 56 2


def f_gcd(a,b):
    if(a == 0):
        return b

    return f_gcd(b%a, a)
    
#lcm = smallest multiple of larger no divisble by the smaller no    
def f_lcm(a,b):
    
    small = min(a,b)
    big   = max(a,b)
    
    i = big
    
    while(1):
        if (i % small ==0):
            return i
        else:
            i += big
 
 
#Runner 
tcs = int(input())            

for _ in range(tcs):
    a,b = map(int, input().split(' '))
    hcf = f_gcd(a, b)
    
    #lcm = (a*b)//(hcf)
    lcm  = f_lcm(a,b)
    
    print('[output] for {0}, {1} =>'.format(a,b), lcm, hcf, sep=' ')

# output =>
# 2
# 10 5
# [output] for 10, 5 => 10 5
# 14 8
# [output] for 14, 8 => 56 2


