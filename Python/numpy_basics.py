# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 16:39:18 2025

@author: gumus
"""

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

print(array.shape)
a = array.reshape(3, 5)
print(a)
print(a.shape)
print("dimension: ", a.ndim)
print("data type: ", a.dtype.name)
print("size: ", a.size)
print("type", type(a))

array1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 5, 1]])
print(array1)

zero = np.zeros((3, 4))
print(zero)

zero[0, 0] = 5
print(zero)

np.ones((3, 4))

np.empty((2, 3))

array2 = np.arange(10, 50, 5)
print(array2)

array3 = np.linspace(10, 50, 8)
print("\n", array3)

d = np.array([1, 3, 5])
e = np.array([7, 8, 9])

print("\n", d+e)
print("\n", d-e)
print("\n", d**2)

print("\n", np.sin(d))
print("\n", d < 2)

f = np.array([[1,2,3],[4,5,6]])
g = np.array([[9,8,3],[4,5,6]])

print(f)
print(g)

# element wise product
print("\n",f*g)

# matrix product
print("\n",f.dot(g.T))


p = np.random.random((5,5))
print("\n",p)
print("\n",f.sum())
print("\n",f.max())
print("\n",f.min())
print("\n",f.sum(axis = 0))
print("\n",f.sum(axis = 1))

print("\n",np.sqrt(f))
print("\n",np.square(f)) # a**2

print("\n",np.add(f,f))





