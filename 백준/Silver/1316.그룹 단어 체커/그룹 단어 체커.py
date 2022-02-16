if __name__ == "__main__":
    n = int(input())
    result = n

    for _ in range(n):
        s = list(input())
        t = set(s)

        for i in range(len(s)):
            if i < len(s) - 1 and s[i] == s[i + 1]:
                continue
            if s[i] in t:
                t.remove(s[i])
            else:
                result -= 1
                break

    print(result)