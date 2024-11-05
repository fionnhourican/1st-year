#!/usr/bin/env python3

n = int(input())
m = int(input())

print(m)
x = n - 1
i = 0
while i < x:
   if m % 2 == 0:
      m = m // 2
      print(m)
   else:
      m = (3 * m + 1)
      print(m)
   i = i + 1
