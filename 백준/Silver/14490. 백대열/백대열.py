from sys import stdin
import math

N, M = map(int, input().split(":"))
g = math.gcd(N, M)
print(N//g, end=":")
print(M//g)