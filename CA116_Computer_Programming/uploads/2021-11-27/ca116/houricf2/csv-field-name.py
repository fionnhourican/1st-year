#!/usr/bin/env python3

import sys

position = int(sys.argv[1])

s = input()
a = []

p = 0
i = 0
while i < len(s):
   if s[i] == ",":
      a.append(s[p:i])
      p = i + 1
   i = i + 1
a.append(s[i - 1:])
print(a[position])
