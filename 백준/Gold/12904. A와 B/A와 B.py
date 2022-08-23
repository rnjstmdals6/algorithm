import sys

S = list(input())
T = list(input())
check = 0
while T:
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()
    if T == S:
       check = 1

print(check)