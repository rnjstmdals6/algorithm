import sys
import copy

input = sys.stdin.readline


def dfs(depth):
    if depth == N - 1:
        operator.append(copy.deepcopy(sign))
        return

    sign.append(' ')
    dfs(depth + 1)
    sign.pop()

    sign.append('+')
    dfs(depth + 1)
    sign.pop()

    sign.append('-')
    dfs(depth + 1)
    sign.pop()


t = int(input())
for _ in range(t):
    N = int(input())
    s = list(range(1, N+1))
    sign = []
    operator = []
    dfs(0)

    for op in operator:
        result = ''
        for i in range(N - 1):
            result += str(s[i]) + op[i]
        result += str(s[N-1])
        if eval(result.replace(' ', '')) == 0:
            print(result)
    print()