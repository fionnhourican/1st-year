#!/usr/bin/env python3

n = int(input())
fib = {}

n1 = 0
n2 = 1
fib[n1] = "yes"


nth = 1
while nth <= n:
   fib[nth] = "yes"
   nth = n1 + n2
   n1 = n2
   n2 = nth

if n in fib:
   print("yes")
else:
   print("no")
