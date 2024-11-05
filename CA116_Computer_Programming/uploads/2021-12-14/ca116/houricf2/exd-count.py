#!/usr/bin/env python3

import sys

n = sys.argv[1]
n = int(n)

if n != 0:
   print("0")
i = 1
while i < n and (i * i) < n:
   print(i)
   i = i + 1
