#!/usr/bin/env python3

month = int(input())
day = int(input())

n = (month - 1) * 30 + day

print(n % 7)
