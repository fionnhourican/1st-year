#!/usr/bin/env python3

prev = int(input())
curr = prev
while curr != 0:
   curr = int(input())
   if curr < prev and curr != 0:
      print("lower")
   elif prev < curr:
      print("higher")
   elif prev == curr:
      print("equal")
   prev = curr
