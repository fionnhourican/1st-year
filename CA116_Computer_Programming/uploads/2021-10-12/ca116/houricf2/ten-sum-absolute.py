#!/usr/bin/env python3

n = 10
total = 0

i = 0
while i < n:
   x = int(input())
   if x < 0:
      z = x * -1
   else:
      z = x
   total = total + z
   i = i + 1


print(total)
