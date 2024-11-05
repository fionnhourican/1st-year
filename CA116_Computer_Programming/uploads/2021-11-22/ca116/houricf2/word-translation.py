#!/usr/bin/env python3

import sys

word = sys.stdin.read().split()
#
f = open("translation.txt")
#
rules = f.read().split()
translate_r = {}
#
i = 0
while i < len(rules):
   translate_r[rules[i]] = rules[i + 1]
   i = i + 2
#
i = 0
while i < len(word):
   print(translate_r[word[i]])
   i = i + 1
f.closed
