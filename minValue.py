#! /usr/bin/env python

data = [40, 88, 62, 15, 24, 75, 35]


minimum = data[0]

for num in data[1:]:
    if num < minimum:
        minimum = num

print(minimum)
print(min(data))

