# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 18:20:13 2025

@author: gumus
"""
import numpy as np

array = np.array([1,2,3,4,5,6,7])
print("\n", array[0])
print("\n", array[0:4])

reverse_array = array[::-1]
print("\n",reverse_array)

array1 = np.array([[1,2,3,4,5,],[6,7,8,9,10]])
print("\n",array1)
print("\n",array1[1,1])
print("\n",array1[:,1])
print("\n",array1[1,1:4])
print("\n",array1[-1,-1])
print("\n",array1[-1,:])

#shape manipulation
array2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("\n", array2)
# flatten
a = array2.ravel()
print("\n",a)
array3 = a.reshape(3,3)
print("\n",array3)
arrayT = array3.T
print("\n",arrayT)
print(arrayT.shape)

#stacking arrays

array4 = np.array([[1,2],[3,4]])
array5 = np.array([[-1,-2],[-3,-4]])

print("\n",array4)
print("\n",array5)

array6 = np.vstack((array4,array5))
array7 = np.hstack((array4,array5))

print("\n",array6)
print("\n",array7)

#convert and copy array

list1 = [1,2,3,4]
array7 = np.array(list1)
print("\n",type(array7))

list2 = list(array7)
print("\n",type(list2))

a= np.array([1,2,3])
b = a
b[0] = 5
c = a

d = np.array([1,2,3])
e = d.copy()
f = d.copy()




















