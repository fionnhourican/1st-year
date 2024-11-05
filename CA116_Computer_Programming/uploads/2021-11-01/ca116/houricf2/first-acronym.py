#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and not ("A" <= s[i] and s[i] <= "Z"):
   i = 1 + i

if i < len(s):
   j = i + 1
   while j < len(s) and ("A" <= s[j] and s[j] <= "Z"):
      j = j + 1
   print(s[i:j], i)