#!/usr/bin/env python3

s = input()

i = 0
while not (s[i] >= "a" and "g" >= s[i]):
   i = i + 1

print(s[i])
