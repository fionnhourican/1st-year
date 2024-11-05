#!/usr/bin/env python3

s = input()
total = 0

i = 0
counter = 0
while counter != 5:
   a = ""
   while i < len(s) and s[i] != "+":
      a = a + s[i]
      i = i + 1
   total = total + int(a)
   counter = counter + 1
   i = i + 1

print(total)
