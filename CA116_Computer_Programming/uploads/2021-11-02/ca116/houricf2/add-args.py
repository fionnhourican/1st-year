#!/usr/bin/env python3

import sys

args = sys.argv[1:]

total = 0

i = 0
while i < len(args):
   n = int(args[i])
   total = total + n
   i = i + 1
print(total)
