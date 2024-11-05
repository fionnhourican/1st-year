#!/usr/bin/env python3

s = input()
while s != "end":
   a = s.split()
   print(" ".join(a[5:]))
   s = input()
