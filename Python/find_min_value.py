# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 15:13:28 2025

@author: gumus
"""

#find min value in a list

list1 = [5,9,8,3,6,10,11,99,50]

min_value = list1[0]

for each in list1:
    if(each < min_value):
        min_value = each
        
print(min_value) 