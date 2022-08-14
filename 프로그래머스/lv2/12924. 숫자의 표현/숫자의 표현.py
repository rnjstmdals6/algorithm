def solution(n):
    answer = 0

    arr = [i for i in range(1, n + 1)]
    end = 0
    _sum = 0

    for start in range(n):
        while _sum < n and end < n:
            _sum += arr[end]
            end += 1
        
        if _sum == n:
            answer += 1
        _sum -= arr[start]
    return answer