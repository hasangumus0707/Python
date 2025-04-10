# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 14:07:04 2025

@author: gumus
"""

var1 = 10
var2 = 20

if (var1 > var2):
    print("var1 > var2")
elif (var1 == var2):
    print("var1 == var2")
else:
    print("var1 < var2")

list = [5, 8, 9, 2, 3]

if 9 in list:
    print("yes")
else:
    print("no")

value = 5
if value in list:
    print("evet {} degeri listenin icinde".format(value))
else:
    print("hayır")


dictionary = {"ali": 32, "veli": 45, "ayse": 13}
keys = dictionary.keys()

if "ali" in keys:
    print("yes")
else:
    print("no")


def find_century(year):
    #from year to century
    str_year = str(year)

    if (len(str_year) < 3):
        return 1
    elif (len(str_year) == 3):
        if (str_year[1] == "0" and str_year[2] == "0"):
            return str_year[0]
        else:
            return int(str_year[0]) + 1
    elif (len(str_year) == 4):
        if(str_year[2] == "0" and str_year[3] == "0"):
            return str_year[0:2]
        else:
            return int(str_year[0:2]) + 1
    else:
        return "Wrong Entry"
        

print(find_century(2999))




