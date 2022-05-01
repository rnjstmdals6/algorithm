import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
answer = 0

A.sort()

for i in range(len(A)):
    left, right = 0, len(A)-1

    while left < right:
        if left == i:
            left += 1
            continue
        elif right == i:
            right -= 1
            continue

        if A[left] + A[right] == A[i]:
            answer += 1
            break
        if A[left] + A[right] < A[i]:
            left += 1
        else:
            right -= 1

print(answer)