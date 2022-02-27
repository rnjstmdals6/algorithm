import sys

N = int(input())
S = []
for _ in range(N):
    S.append(int(sys.stdin.readline()))
# 정렬
S.sort(reverse=True)
Stack = []
ans = 0

if N == 1:
    print(0)
else:
    while S:
        Stack.append(S.pop())
        if len(Stack) == 2:
            a = Stack.pop()
            b = Stack.pop()
            c = a + b
            ans += c
            flag = False
            for i in range(len(S)):
                if c >= S[i]:
                    flag = True
                    S.insert(i, c)
                    break
            if not flag:
                S.append(c)
    print(ans)