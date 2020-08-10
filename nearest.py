#! /usr/bin/python

#a=[11, 5, 2, 22, 10, 9, 8] 7 near 

a = [11, 5, 2, 22, 10, 9, 8]

num = 7
list_sub = [] #-4 2 5 -15 -3 -2 -1 
absol = [] # 4 2 5 15 3 2 1 

def min_search(absol):
    for i in a:
        sub = num - i
        list_sub.append(sub)
        #print(list_sub)

    for j in list_sub:
        tmp = abs(j)
        absol.append(tmp)
        #print(absol)

    n = len(absol)
    minValue = absol[0]
    
    for k in range(1,n):
        if absol[k] < minValue:
            minValue = absol[k]
            min_index = absol.index(minValue)
            a_index = a[min_index]
    return a_index

print(min_search(absol))
#print(min_search(absol))

    


