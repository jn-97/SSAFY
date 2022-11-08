import sys
import math

sys.stdin = open("1938.txt")

a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(math.trunc(a / b))
