# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 10:35:48 2025

@author: gumus
"""

list1 = [1, 2, 3, 4]
print(type(list1))

list_str = ["monday", "tuesday","wednesday"]
print(type(list_str))

value = list1[1]
print(value)

print(list1[-1]) 
print(list1[-2])
print(list1[0:3])

list1.append(8)
list1.reverse()
print(list1)
list1.sort()
print(list1)

string_int_liste = [1,2,3,"aa","bb"]
print(string_int_liste)
print(string_int_liste[1:5])

if "aa" in string_int_liste:
    print("Yes")
    
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant" , "watermelon"]
print(thislist)