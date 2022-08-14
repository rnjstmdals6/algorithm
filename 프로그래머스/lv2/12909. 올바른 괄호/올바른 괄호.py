def solution(s):
    isCorrect = True
    stack = []
    
    for i in s:
        if not stack and i == ')':
            isCorrect = False
            break
        elif stack and i == ')':
            stack.pop()
        else:
            stack.append('(')
    
    if stack:
        return False
    return isCorrect


