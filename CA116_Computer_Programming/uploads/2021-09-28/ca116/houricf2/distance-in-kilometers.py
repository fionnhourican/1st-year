#!/usr/bin/env python3

m = int(input())

k = (m % 1000) // 500 + (m // 1000)

print(k)
