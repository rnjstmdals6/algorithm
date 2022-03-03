import sys
from itertools import permutations

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
A.sort()
result = -(10**5)
B = list(permutations(A, N))
for i in B:
    _sum = 0
    for j in range(N-1):
        _sum += abs(i[j] - i[j+1])
    result = max(_sum, result)

print(result)