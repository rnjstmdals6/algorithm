i = 1
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    ans = 0
    while V > P:
        V -= P
        ans += L

    if V > L:
        ans += L
    else:
        ans += V

    print("Case "+ str(i) +": " + str(ans))
    i += 1