import sys

a = list(map(int, input().split()))
cnt1 = 0
cnt2 = 0
for i in a:
    if i == 1:
        cnt1 +=1
    else:
        cnt2 +=1

if cnt1 > cnt2:
    print(1)
else:
    print(2)