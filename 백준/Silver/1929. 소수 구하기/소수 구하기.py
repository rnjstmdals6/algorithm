import sys
import time

def sieve(n, m):
    flags = [0, 0] + [1] * (m - 1)
    for i in range(m+1):
        if flags[i] == 1:
            for j in range(i*2,m+1,i):
                flags[j] = 0
    prime = []
    for i in range(n,len(flags)):
        if flags[i] == 1:
            prime.append(i)
    return prime

n, m = map(int, sys.stdin.readline().split())
list = sieve(n, m)

for i in list:
    print(i)
