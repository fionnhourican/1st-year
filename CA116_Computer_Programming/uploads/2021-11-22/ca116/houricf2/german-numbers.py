#!/usr/bin/env python3

import sys

word = sys.stdin.read().split()

translate = {
   "one": "eins",
   "two": "zwei",
   "three": "drei",
   "four": "vier",
   "five": "funf",
   "six": "sechs",
   "seven": "sieben",
   "eight": "acht",
   "nine": "neun",
   "ten": "zehn",
}

i = 0
while i < len(word):
   print(translate[word[i]])
   i = i + 1
