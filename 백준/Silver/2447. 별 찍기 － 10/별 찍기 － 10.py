N = int(input())

pattern = ["***", "* *", "***"]

def conquer(K, x):
    out = []
    if K == 3:
        return x
    else:
        for i in x:
            out.append(i*3)
        for i in x:
            out.append(i + ' ' * len(x) + i)
        for i in x:
            out.append(i*3)
        return conquer(K//3, out)

answer = conquer(N, pattern)
for i in answer:
    print(i)