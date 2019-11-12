#!/usr/bin/env python3

import random

with open("words.txt","r") as f:
    words = f.readlines()

maximum = len(words)
n = int(random.random()*maximum)

word = words[n].rstrip()

spaces = len(word)

answer = "X" * spaces

print(word+answer)
