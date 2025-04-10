# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 14:54:12 2025

@author: gumus
"""

for each in range(1,11):
    print(each)
    
for each in "ankara ist":
    print(each)
    
for each in "ankara ist".split():
    print(each)

list1 = [1,2,3,4,5,6,100]

summation = sum(list1)

count = 0
for each in list1:
    count = count + each
    print(count)
    
i = 0
while(i < 4):
    print(i)
    i = i + 1
    
length = len(list1)
each = 0
count = 0
while(each < length):
    count = count + list1[each]
    each = each + 1