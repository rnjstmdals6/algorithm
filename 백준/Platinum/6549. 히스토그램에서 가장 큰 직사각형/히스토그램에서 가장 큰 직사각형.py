import sys
input = sys.stdin.readline


def MaxSize(s):
    max_size = 0
    stack = []

    for i in range(len(s)):
        min_point = i
        while stack and stack[-1][0] >= s[i]:
            h, min_point = stack.pop()
            temp = h * (i - min_point)
            max_size = max(max_size, temp)
        stack.append([s[i], min_point])
    for h, point in stack:
        max_size = max(max_size, (len(s) - point) * h)

    return max_size


while True:
    height = list(map(int, input().split()))
    if height[0] == 0:
        break
    height = height[1:]
    print(MaxSize(height))