#!/usr/bin/env python3

m = int(input())

x = (m >= 70)
y = (m < 70 and m >= 50)
z = (m < 50 and m >= 40)
p = (m < 40)

print("first:", x)
print("second:", y)
print("third:", z)
print("fail:", p)
