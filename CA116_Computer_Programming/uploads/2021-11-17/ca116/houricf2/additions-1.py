#!/usr/bin/env python3

n = 10

counter = 0
while counter != n:
   s = input()
   i = 0
   while i < len(s) and s[i] !+ "+":
      i = i + 1

   no1 = s[0:i]
   no2 = s[i + 1:len(s)]
   print(int(no1) + int(no2))
   counter = counter + 1
