# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 19:28:24 2025

@author: gumus
"""
float1 = 10.6
str1 = "1005"
int(str1)
print(type(str1))
print(type(int(str1)))

# user defined functions


def first_function(var1, var2):
    output = var1 + var2
    return output


sonuc = first_function(10, 20)


def perimeter_circle(r, pi=3.14):
    output = 2*pi*r
    return output


print(perimeter_circle(5))


def calculate(weight, height, *args):
    print(args)
    output = weight*height*args[0]
    return output


age = 10
name = "ali"
surname = "veli"


def function_quiz(age, name, surname, *args, shoes_number=35):
    print("Name: ", name, "Age:", age, "Shoe Number: ", shoes_number)
    print(type(name))
    print(float(age))
    output = args[0]*age
    print(output)
    return output


sonuc = function_quiz(5, "ali", "veli", "a")


def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")


def calculate2(x):
    return x*x


result = calculate2(3)


def result2(x): return x*x


print(result2(3))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))
