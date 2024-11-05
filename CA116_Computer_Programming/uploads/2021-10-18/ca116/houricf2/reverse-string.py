#!/usr/bin/env python3

s = input()

reverse = ""
i = 0
while i < len(s):
   r = s[len(s) - 1 - i]
   reverse = reverse + r
   i = i + 1

print(reverse)
