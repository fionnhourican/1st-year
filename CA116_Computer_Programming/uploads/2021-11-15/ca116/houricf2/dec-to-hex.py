#!/usr/bin/env python3

base = 16
s = ""
n = int(input())

while 0 < n:
   d = n % base
   if d == 10:
      d = "a"
   elif d == 11:
      d = "b"
   elif d == 12:
      d = "c"
   elif d == 13:
      d = "d"
   elif d == 14:
      d = "e"
   elif d == 15:
      d = "f"
   s = str(d) + s
   n = n // base
print(s)
