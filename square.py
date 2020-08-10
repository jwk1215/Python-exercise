#! /usr/bin/env python

#a^n을 계산하는 코드를 작성해보자 (a와 n은 자연수)
#입력
#a = 16
#n = 8

num0 = int(input('write a: '))
num1 = int(input('write b: '))

def square(num0, num1):
    result = num0 ** num1
    return result

print(square(num0,num1))




