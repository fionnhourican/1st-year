#!/usr/bin/env python3

if __name__ == "__main__":
   a = ["", "", "dog", "goat", ""]

i = 0
while i < len(a) and a[i] == "":
   i = i + 1

if i < len(a):
   print(a[i])
