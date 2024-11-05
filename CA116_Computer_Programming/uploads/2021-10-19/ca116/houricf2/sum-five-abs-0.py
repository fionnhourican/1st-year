#!/usr/bin/env python3

total = 0

n = int(input())
while n != 0:
   if n > 0:
      x = n
   else:
      x = n * -1
   total = total + x
   n = int(input())

print(total)
