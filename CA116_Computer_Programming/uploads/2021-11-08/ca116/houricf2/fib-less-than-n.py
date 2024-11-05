#!/usr/bin/env python3

n = int(input())
n1 = 0
n2 = 1
print(n1)

if n == 0:
   print(n1)

nth = 1
i = 0
while i < n - 2 and nth < n:
   print(nth)
   nth = n1 + n2
   n1 = n2
   n2 = nth
