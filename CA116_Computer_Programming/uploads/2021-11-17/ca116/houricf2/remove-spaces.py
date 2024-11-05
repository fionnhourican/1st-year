#!/usr/bin/env python3

s = input()
space = " "
word = ""

i = 0
while i < len(s):
   if s[i] != space:
      word = word + s[i]
   i = i + 1
print(word)
