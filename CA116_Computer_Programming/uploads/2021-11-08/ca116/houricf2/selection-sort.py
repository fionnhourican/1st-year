#!/usr/bin/env python3

a = []
s = input()

while s != "end":
   s = int(s)
   a.append(s)
   s = input()
   p = 0
   i = 1
   while i < len(a):
      if a[i] < a[p]:
         # swap
         temp = a[p]
         a[p] = a[i]
         a[i] = temp
         p = i
      #
   print(a)
   i = i + 1
