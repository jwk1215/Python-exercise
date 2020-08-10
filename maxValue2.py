#! /usr/bin/env python


def max_search(num):
    n = len(num)
    maxValue = num[0]
    for i in range(1,n):
        if num[i] > maxValue:
            maxValue = num[i]
    return maxValue

num = [4, 7, 12, 25, 2, 47, 28, 24]
print(max_search(num))
    
