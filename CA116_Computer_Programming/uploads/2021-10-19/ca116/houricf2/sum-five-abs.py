#!/usr/bin/env python3

n = 5
total = 0

i = 0
while i < n:
   m = int(input())
   if m > 0:
      x = m
   else:
      x = m * -1
   total = total + x
   i = i + 1

print(total)
