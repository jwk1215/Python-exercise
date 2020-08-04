#! /usr/bin/env python

#자연수 753 의 약수를 구하는 코드를 작성하시오

num = int(input("자연수를 입력하세요: "))

for i in range(1, num+1):
    if num % i == 0:
        print(i)
    







