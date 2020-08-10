#! /usr/bin/env python

a = [2, 7, 22, 1, 5, 65, 12, 34, 75]

def max_search(a):
    ln = len(a)
    maxValue = a[0] 
    for i in range(1,ln):
        if maxValue < a[i]: 
            maxValue = a[i]
    return maxValue

print(max_search(a))




