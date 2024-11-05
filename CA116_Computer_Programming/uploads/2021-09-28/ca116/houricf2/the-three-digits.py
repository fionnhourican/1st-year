#!/usr/bin/env python3

n = int(input())

a = (n % 1000) - (n % 100)
b = (n % 100) - (n % 10)
c = (n % 10)

print(a // 100)
print(b // 10)
print(c)
