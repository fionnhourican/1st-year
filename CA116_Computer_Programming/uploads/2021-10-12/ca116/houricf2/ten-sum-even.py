#!/usr/bin/env python3

n = 10

total = 0

i = 0
while i < n:
   x = int(input())
   even = ((x % 2) - 1) * -x
   total = total + even
   i = i + 1

print(total)
