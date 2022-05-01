import sys
import copy

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = int(input())

for i in range(N-1):
    j = N
    while True:
        if i == A.index(max(A[i:j])) or S <= 0:
            break
        else:
            if A.index(max(A[i:j]))-i <= S:
                S -= A.index(max(A[i:j])) - i
                for k in range(A.index(max(A[i:j]))-1, i-1, -1):
                    A[k], A[k+1] = A[k+1], A[k]
            else:
                j -= 1
print(*A)