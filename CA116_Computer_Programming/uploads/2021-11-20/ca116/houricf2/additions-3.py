#!/usr/bin/env python3

total = 0
while total != 1000:
   a = ""
   s = input()
   i = 0
   while s[i] != "+":
      a = a + s[i]
      i = i + 1
   b = s[i + 1:len(s)]
   total = int(a) + int(b)
   print(total)
