#!/usr/bin/env python3

n = int(input())

i = 0
while i < n:
   if i < n // 2:
      j = i
      print((" " * j) + "*" + (" " * (n - j * 2 - 2) + "*"))
   elif i > n // 2:
      j = n - i - 1
      print((" " * j) + "*" + (" " * (n - j * 2 - 2) + "*"))
   else:
      print(" " * i + "*")
   i = i + 1
