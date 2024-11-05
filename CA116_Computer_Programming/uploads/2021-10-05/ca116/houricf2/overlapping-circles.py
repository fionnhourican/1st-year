#!/usr/bin/env python3

x1 = int(input())  # first circle
y1 = int(input())
r1 = int(input())

x2 = int(input())  # second circle
y2 = int(input())
r2 = int(input())

distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)
radii = r1 + r2

if distance < radii:
   print("yes")
else:
   print("no")
