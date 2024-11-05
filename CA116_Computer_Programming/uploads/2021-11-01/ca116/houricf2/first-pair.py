#!/usr/bin/env python3

s = input()

i = 1
while i < len(s) and (s[i - 1] != s[i]):
   i = i + 1

if i < len(s):
   if i != 0:
      print(s[i - 1:i + 1])
