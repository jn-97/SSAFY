import sys
import math

sys.stdin = open("2063.txt")

n = int(input())

list_ = list(map(int, input().split()))
list_ = sorted(list_)

print(list_[math.trunc(n / 2)])
