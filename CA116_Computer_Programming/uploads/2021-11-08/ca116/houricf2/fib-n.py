#!/usr/bin/env python3

n = int(input())
prev = 1
curr = 0
print(curr)
print(prev)

if n == 0:
   print(curr)

i = 0
while i < n - 2:
   nth = curr + prev
   curr = prev
   prev = nth
   print(nth)
   i = i + 1
