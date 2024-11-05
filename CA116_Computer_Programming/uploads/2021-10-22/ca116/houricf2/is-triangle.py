#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

if (a * a) == (c * c) - (b * b):
   print("yes")
elif (b * b) == (c * c) - (a * a):
   print("yes")
elif (c * c) == (a * a) + (b * b):
   print("yes")
elif -(a * a) == (c * c) - (b * b):
   print("yes")
elif -(b * b) == (c * c) - (a * a):
   print("yes")
else:
   print("no")
