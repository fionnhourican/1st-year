#!/usr/bin/env python3

s = input()

total = 0

i = 0
while i < len(s):
   n = s[i]
   x = int(n)
   total = total + x
   i = i + 1

print(total)
