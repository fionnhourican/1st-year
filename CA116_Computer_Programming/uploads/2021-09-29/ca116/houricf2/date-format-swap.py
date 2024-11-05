#!/usr/bin/env python3

n = int(input())
x = n % 10000 // 100
y = n // 10000
z = n % 100

print((x * 10000) + (y * 100) + z)
