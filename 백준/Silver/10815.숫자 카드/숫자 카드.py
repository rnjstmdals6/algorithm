import sys

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
M = int(input())
check = list(map(int, sys.stdin.readline().split()))
cards.sort()

for i in check:
    l = 0
    r = len(cards) - 1
    flag = False
    while l <= r:
        mid = (l + r) // 2
        if i == cards[mid]:
            print(1, end=" ")
            flag = True
            break
        elif i > cards[mid]:
            l = mid + 1
        else:
            r = mid - 1

    if not flag:
        print(0, end=" ")
