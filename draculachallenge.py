#!/usr/bin/env python3


wget https://www.gutenberg.org/files/345/345-0.txt -qO dracula.txt

with open ("dracula.txt", "r") as foo:

    count = 0
    for line in foo:
        if "vampire" in line.lower():
            count += 1

    for line in foo:
        if "vampire" in line.lower():
            print(line)
