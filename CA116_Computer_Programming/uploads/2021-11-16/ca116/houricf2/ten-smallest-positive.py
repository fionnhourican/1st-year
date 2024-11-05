#!/usr/bin/env python3

n = 10
smallest = int(input())

i = 0
while i < n - 1:
   x = int(input())
   if x < smallest and x > 0:
      smallest = x
   i = 1 + i

print(smallest)
