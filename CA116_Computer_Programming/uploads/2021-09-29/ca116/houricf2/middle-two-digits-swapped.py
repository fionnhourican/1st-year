#!/usr/bin/env python3

n = int(input())

x = (n % 10000) // 100

y = x // 10
z = x % 10

print(z * 10 + y)
