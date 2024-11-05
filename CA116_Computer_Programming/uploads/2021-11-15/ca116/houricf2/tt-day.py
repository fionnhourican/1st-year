#!/usr/bin/env python3

a = []

s = input()
while s != "end":
   a.append(s)
   s = input()

n = input()
i = 0
while i < len(a):
   module = a[i]
   module.split()
   if module[0] == n:
      print(module)
   i = i + 1
