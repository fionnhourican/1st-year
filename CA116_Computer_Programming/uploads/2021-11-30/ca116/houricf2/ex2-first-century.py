#!/usr/bin/env python3

import sys

s = sys.stdin.read().split()

i = 0
while i < len(s) and not (int(s[i]) >= 100):
   i = i + 1

if i < len(s):
   print(s[i])
else:
   print("none")
