#! /usr/bin/env python

#a = [60, 20, 10, 45, 90, 100, 15]
#위 리스트 a 는 시험 점수를 담고 있다
#위 점수를 참고하여 석차 담은 grade 라는 리스트를 출력하는 코드를 작
#print(grade) --> [3, 5, 7, 4, 2, 1, 6]

score = [60, 20, 10, 45, 90, 100, 15]
l_max = []
ln = len(score)
grade = []

n = 1
for i in range(0,ln):
    max_score = score[i] 
    for j in range(0,ln):
        if max_score > score[j]: 
            pass 
        elif max_score == score[j]:
            pass
        else:
            pass
            n +=1
            continue
    grade.append(n)
    n=1

print(grade)






