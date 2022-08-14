def solution(n):
    start = n
    while True:
        n += 1
        if str(bin(start)).count("1") == str(bin(n)).count("1"):
            break
    return n