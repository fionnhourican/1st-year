#!/usr/bin/env python3

n = input()

even = []
odd = []

while n != "end":
   n = int(n)
   if n % 2 == 0:
      even.append(n)
   else:
      odd.append(n)
   n = input()

i = 0
while i < len(even):
   print(even[i])
   i = i + 1

i = 0
while i < len(odd):
   print(odd[i])
   i = i + 1
