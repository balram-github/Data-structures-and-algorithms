#!/usr/bin/python3
import functools


def mean_median(l):
    l.sort()


    sum = functools.reduce((lambda x, y: x + y), l)
    mean = sum // len(l)

    median = l[0]
    if (len(l)%2) == 1:
        median = l[len(l)//2]
    else:
        median = ((l[len(l)//2]) + (l[len(l)//2 -1]))//2    

    return mean, median


l = [1, 2, 19, 28, 5]
print('[Mean, Median] of {0} => {1}'.format(l, mean_median(l)))

l = [2, 8, 3, 4]
print('[Mean, Median] of {0} => {1}'.format(l, mean_median(l)))