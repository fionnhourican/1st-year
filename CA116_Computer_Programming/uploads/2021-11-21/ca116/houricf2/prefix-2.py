#!/usr/bin/env python3

if __name__ == "__main__":
   a = ["mountain", "montagne", "mont", "mo", "montages", "zebra", "monthly"]
   s = "mont"

i = 0
x = len(a)
b = a[i]
while i < len(a) and s != b[:x]:
   i = i + 1
   b = a[i]

if i < len(a):
   print(a[i])
