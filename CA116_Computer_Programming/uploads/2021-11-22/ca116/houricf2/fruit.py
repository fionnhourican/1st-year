#!/usr/bin/env python3

import sys

word = sys.stdin.read().split()

fruit = {
   "apple": True,
   "pear": True,
   "orange": True,
   "banana": True,
   "cherry": True,
}

i = 0
while i < len(word):
   if word[i] in fruit:
      print(word[i])
   i = i + 1
