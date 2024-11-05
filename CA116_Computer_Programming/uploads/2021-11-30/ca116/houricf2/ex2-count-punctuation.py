#!/usr/bin/env python3

import sys

s = sys.stdin.read()

characters = {
   ".": True,
   ",": True,
   "!": True,
   "?": True,
   ";": True,
   ":": True,
}

total = 0
i = 0
while i < len(s):
   if s[i] in characters:
      total = total + 1
   i = i + 1

print(total)
