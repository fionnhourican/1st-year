#!/usr/bin/env python3

import sys

word = sys.stdin.read().split()
seen = {}

i = 0
while i < len(word):
   if word[i] not in seen:
      seen[word[i]] = "True"
   else:
      seen.pop(word[i])
   i = i + 1

i = 0
while i < len(word):
   if word[i] in seen:
      print(word[i])
   i = i + 1
