#!/usr/bin/env python3

import sys

with open("input.txt") as f:
   s = f.read()
#
a = ""
i = 0
while i < len(s):
   if ("a" <= s[i] and s[i] <= "z") or ("A" <= s[i] and s[i] <= "Z"):
      a = a + "*"
   else:
      a = a + s[i]
   i = i + 1

with open("output.txt", "w") as f:
   f.write(a)
