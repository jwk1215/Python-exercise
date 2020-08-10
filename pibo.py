#! /usr/bin/env python

#피보나치 수열 (1+1+2+3+5+8....)의 20번째 항까지의 합을 구하는 코드를 작성하시오.
#출력 17710

pibo = [1,1]

def pibonacci(pibo):
    pibo_sum = 0
    for i in range(2,20):
        num = pibo[-1]+pibo[-2]
        pibo.append(num)

    for i in range(0,len(pibo)):
        pibo_sum += pibo[i]

    return pibo_sum

print(pibonacci(pibo))

#print(sum(pibo))


