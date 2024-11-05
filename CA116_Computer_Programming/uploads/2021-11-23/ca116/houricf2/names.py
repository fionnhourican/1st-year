#!/usr/bin/env python2

import sys

name = sys.stdin.read().split()

with open ("boys.tex") as f:
   b = f.read().split()

with open ("girls.tex") as f:
   g = f.read().split()

sex = {}

i = 0
while i < len(b):
   sex[b[i]] = "boy"
   i = i + 1

j = 0
while j < len(g):
   sex[g[i]] = "girl"
   j = j + 1

k = 0
while k < len(name):
   print(name[k], sex[name[k]])
