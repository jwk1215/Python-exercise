#! /usr/bin/env python

#자릿수 채우기 위한 0이 나오기 이전까지 숫자들의 위치를 반대로 뒤집어
#출력하는 코드를 작성하시오. (모든 수는 10자리)
#예를 들어 3456700000를 7654300000으로 출력해야 한다.

#입력
#3430156000
#6534300000
#출력
#6510343000
#3435600000

enter = input('write num: ')
s = ''
s+= enter
reverse = s[::-1]

zero = ''
num = ''

for i in range(0, len(reverse)):
    if reverse[i]== '0':
        zero += reverse[i]
    else:
        num += reverse[i]

print(num+zero)
