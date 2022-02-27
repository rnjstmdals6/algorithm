S = list(input())

cnt1 = 0
flag = False
for i in range(len(S)):
    if S[i] != '0':
        if not flag:
            cnt1 += 1
        flag = True
    else:
        flag = False

cnt2 = 0
flag = False
for i in range(len(S)):
    if S[i] != '1':
        if not flag:
            cnt2 += 1
        flag = True
    else:
        flag = False

print(min(cnt1, cnt2))