#!/usr/bin/env python3

n = 10
total = 0

i = 0
while i < n:
   x = int(input())
   if x > 0:
      p = x
   else:
      p = 0
   total = total + p
   i = i + 1

print(total)
