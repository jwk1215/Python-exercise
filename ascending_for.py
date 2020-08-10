#! /usr/bin/env python

#a = [2, 7, 22, 1, 5, 65, 12, 34, 75] 
#리스트a 를 오름차순으로 정렬하여 b 라는 리스트로 만드시오

a = [2, 7, 22, 1, 5, 65, 12, 34, 75]

b = []

for i in a:
    mini = i

    for j in a:
        if mini > j:
            mini = j
    b.append(mini)
    a[a.index(mini)] = 999

print(a)
print(b)
