import sys

sys.stdin = open("2058.txt")

words = input()

result = 0
for word in words:
    result += int(word)

print(result)
