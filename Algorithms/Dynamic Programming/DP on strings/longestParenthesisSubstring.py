def longestValidParentheses(s: str) -> int:
    '''
    - we use a stack to track opening and closing brackets
    - on every opening bracket, we push the index on to the stack
    - on every closing bracket, we pop from the stack --> this means that we have found a valid parenthesis substring
    - we update the max value (curr - stack.top()) --> stack.top() will be the index of the previous ending parenthesis.
    - In case our stack becomes empty, we push the index of the current ending parenthesis substring
    - Also when the stack becomes empty, it means that we cannot extend the previous long parenthesis any more. We have to start a new one.
    '''
    stack = [-1]

    best = 0
    for i in range(len(s)):
        if s[i] == '(': stack.append(i)
        else:
            stack.pop()
            if not stack: stack.append(i)
            best = max(best, i - stack[-1])
    return best