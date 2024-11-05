#!/usr/bin/env python3

s = input()

i = 0
while not (s[i] >= "A" and "Z" >= s[i]):
   i = i + 1

print(i)
