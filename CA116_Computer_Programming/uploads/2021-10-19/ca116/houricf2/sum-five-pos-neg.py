#!/usr/bin/env python3

m = 5

pos = 0
neg = 0
i = 0
while i < m:
   n = int(input())
   if n > 0:
      pos = pos + n
   else:
      neg = neg + n
   i = i + 1
print(neg, pos)
