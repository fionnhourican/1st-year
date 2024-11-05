#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

x = ((c % 2) + 1) % 2 * a
y = (c % 2) * b

print(x + y)
