#!/usr/bin/env python3

n = int(input())

a = ["|"]

i = 0
while i < n:
   a.append(" ")
   i = i + 1

m = int(input())
a[m + 1] = "*"
while m != (n - 1):
   m = int(input())
   a[m + 1] = "*"

a.append("|")

s = ""
j = 0
while j < len(a):
   s = s + a[j]
   j = j + 1
print(s)
