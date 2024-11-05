#!/usr/bin/env python3

t0 = 0
t1 = 0
t2 = 0
t4 = 0
t3 = 0
t5 = 0
t6 = 0
t7 = 0
t8 = 0
t9 = 0

s = input()
while s != "end":
   if s == "0":
      t0 = t0 + 1
   elif s == "1":
      t1 = t1 + 1
   elif s == "2":
      t2 = t2 + 1
   elif s == "3":
      t3 = t3 + 1
   elif s == "4":
      t4 = t4 + 1
   elif s == "5":
      t5 = t5 + 1
   elif s == "6":
      t6 = t6 + 1
   elif s == "7":
      t7 = t7 + 1
   elif s == "8":
      t8 = t8 + 1
   else:
      t9 = t9 + 1
   s = input()

print("0" + " " + "*" * t0)
print("1" + " " + "*" * t1)
print("2" + " " + "*" * t2)
print("3" + " " + "*" * t3)
print("4" + " " + "*" * t4)
print("5" + " " + "*" * t5)
print("6" + " " + "*" * t6)
print("7" + " " + "*" * t7)
print("8" + " " + "*" * t8)
print("9" + " " + "*" * t9)
