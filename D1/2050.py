import sys

sys.stdin = open("2050.txt")

words = input()

for word in words:
    print(ord(word) - 64, end=" ")
