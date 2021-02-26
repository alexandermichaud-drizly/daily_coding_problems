def is_balanced(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(')')
        elif char == '{':
            stack.append('}')
        elif char == '[':
            stack.append(']')
        else:
            if char == stack[-1]:
                stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False

assert is_balanced("([])[]({})") == True
assert is_balanced("([)]") == False
assert is_balanced("((()") == False
