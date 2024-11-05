#!/usr/bin/env python3

s = input()
a = []

count = 0
i = 0
while s != "end":
   a.append(i)
   a.append("tmp")
   a.append(s)
   i = i + 1
   s = input()
   count = count + 1

j = 1
while j < len(a):
   a[j] = count
   j = j + 3

j = 0
while j < len(a):
   print(a[j], a[j + 1], a[j + 2])
   j = j + 3
