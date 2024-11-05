#!/usr/bin/env python3

s = input()
total = 0
while s != "end":
   x = s.split()
   total = total + int(x[2])
   s = input()

print(total)
