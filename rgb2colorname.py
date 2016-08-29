#!/usr/bin/env python
# rb2colorname.py
# by wilsonmar@gmail.com, ayush.original@gmail.com, 
# https://github.com/paarthneekhara
# Usage: 
# Based on http://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
# This will be upgraded to 3 dimensional arrays

import numpy as np

def find_nearest_vector(array, value):
  idx = np.array([np.linalg.norm(x+y) for (x,y) in array-value]).argmin()
  return array[idx]

A = np.random.random((10,2))*100
""" A = array([[ 34.19762933,  43.14534123],
   [ 48.79558706,  47.79243283],
   [ 38.42774411,  84.87155478],
   [ 63.64371943,  50.7722317 ],
   [ 73.56362857,  27.87895698],
   [ 96.67790593,  77.76150486],
   [ 68.86202147,  21.38735169],
   [  5.21796467,  59.17051276],
   [ 82.92389467,  99.90387851],
   [  6.76626539,  30.50661753]])"""

pt = [6, 30]
print find_nearest_vector(A,pt)
# array([  6.76626539,  30.50661753])  
