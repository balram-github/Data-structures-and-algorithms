#!/usr/bin/python3
a = [1,2,3,4,5,6,7]
b = [i for i in range(len(a))]

print('a => {0}'.format(a))
print('b => {0}'.format(b))


i = 0
while len(b) !=1:
    print('Starting iteration')
    print('b => {0}, length => [{1}], i => [{2}]'.format(b, len(b), i))
    j = (i+2)%len(a)
    print('j => [{0}]'.format(j))
    print('deleting index => [{0}], value => [{1}]'.format(j, a[j]))
    del b[j]
    i = (j+1)%len(a)
    print('i => [{0}], b => {1}'.format(i, b))
    print('-----------------Finished iteration---------------')
    