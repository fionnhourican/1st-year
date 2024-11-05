#!/usr/bin/env python3

a = []
s = input()

while s != "end":
   s = int(s)
   a.append(s)
   #
   p = 0
   i = 0
   while i < len(a):
      if a[i] < a[p]:
         p = i
      i = i + 1
   #
   s = input()

print(p)
