#!/usr/bin/env python3

f = open("input.txt")

a = f.readlines()

i = 0
while i < len(a):
   print(a[i].rstrip("\n"))
   i = i + 1

f.close()
