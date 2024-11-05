#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

if a + c > b and a + b > c and b + c > a:
   print("yes")
else:
   print("no")
