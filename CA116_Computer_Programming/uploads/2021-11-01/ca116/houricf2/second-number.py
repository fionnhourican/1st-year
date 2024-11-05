#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and not ("0" <= s[i] and s[i] <= "9"):
   i = i + 1
j = 0
if i < len(s):
   j = i
   while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
      j = j + 1

k = 0
if j < len(s):
   k = j
   while k < len(s) and not ("0" <= s[k] and s[k] <= "9"):
      k = k + 1

x = 0
if k < len(s):
   x = k
   while x < len(s) and ("0" <= s[x] and s[x] <= "9"):
      x = x + 1
   print(s[k:x], k)
