from collections import deque


def isCorrect(s):
    stack = []
    isCorrect = True

    for i in s:
        if not i in [")", "}", "]"]:
            stack.append(i)
        else:
            if stack:
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    isCorrect = False
                    break
            else:
                isCorrect = False
                break
    if stack:
        return False
    return isCorrect

def solution(s):
    answer = 0

    s = deque(s)
    for i in range(len(s)):
        if isCorrect("".join(s)):
            answer += 1
        s.append(s.popleft())

    return answer
