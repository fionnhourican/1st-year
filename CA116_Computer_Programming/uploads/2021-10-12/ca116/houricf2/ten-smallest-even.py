#!/usr/bin/env python3

n = 10
smallest = int(input())

i = 0
while i < n - 1:
   x = int(input())
   even = ((x % 2) - 1) * -x
   if even < smallest and even != 0:
      smallest = x
   i = i + 1

print(smallest)
