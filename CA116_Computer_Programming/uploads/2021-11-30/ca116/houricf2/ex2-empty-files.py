#!/usr/bin/env python3

import sys

i = 0
while i < len(sys.argv):
   with open(sys.argv[i], "r") as f:
      g = f.read().split()
   if len(g) == 0:
      print(sys.argv[i])
   i = i + 1
