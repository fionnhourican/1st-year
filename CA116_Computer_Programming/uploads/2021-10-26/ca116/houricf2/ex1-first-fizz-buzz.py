#!/usr/bin/env python3

n = int(input())

total = 0
while n % 3 != 0 or n % 5 != 0:
   n = int(input())
   total = 0

if n % 3 == 0 and n % 5 == 0:
   print(n)
