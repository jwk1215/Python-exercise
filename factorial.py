#! /usr/bin/env python

#1!+2!+3!+4!+5!+6!+7!+8!+9!+10!의 합을 구하는 코드를 작성하시오.

in_no =10
tot_sum=0
num_sum = 1

for i in range(1,n+1):      
    num_sum *=i              
                          
for k in range(1,in_no+1): 
    tot_sum += calcu(k)    
                                                     
print(tot_sum)
