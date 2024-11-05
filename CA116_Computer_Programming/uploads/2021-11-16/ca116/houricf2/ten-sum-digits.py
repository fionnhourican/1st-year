#!/usr/bin/env python3

n = 10

total = 0
i = 0
while i < n - 1:
   x = int(input())
   lsig = x % 10
   if lsig < 0:
      m = (-1 * lsig)
   else:
      m = lsig
   total = total + m
   i = 1 + i

print(total)
