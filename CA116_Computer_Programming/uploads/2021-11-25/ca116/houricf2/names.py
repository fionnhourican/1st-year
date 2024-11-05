#!/usr/bin/env python3

import sys

name = sys.stdin.read().split()

with open("boys.txt") as f:
   b = f.read().split()

with open("girls.txt") as f:
   g = f.read().split()

sex = {}

i = 0
while i < len(b):
   sex[b[i]] = "boy"
   i = i + 1

j = 0
while j < len(g):
   sex[g[j]] = "girl"
   j = j + 1

r = 0
while r < len(name):
   if name[r] in g and name[r] in b:
      sex[name[r]] = "either"
   r = r + 1

k = 0
while k < len(name):
   print(name[k], sex[name[k]])
   k = k + 1
