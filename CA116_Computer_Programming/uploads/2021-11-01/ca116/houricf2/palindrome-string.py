#!/usr/bin/env python3

s = input()

rev = ""
i = 0
while i < len(s) and not (s[(len(s) - 1) - i] == s[i]):
   i = i + 1

   # even
if i < len(s) and len(s) % 2 != 0:
   print("palindrome")

   # odd
if i < len(s) and s[(len(s) // 2) - 1] == s[len(s) // 2]:
   print("palindrome")
