def valid_braces(string) -> bool:
    stack = []
    
    for c in string:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if stack.count == 0:
                return False
            elif c == ')':
                if stack[-1] != '(':
                    return False
                else:
                    stack.pop()
            elif c == '}':
                if stack[-1] != '{':
                    return False
                else:
                    stack.pop()
            elif c == ']':
                if stack[-1] != '[':
                    return False
                else:
                    stack.pop()
    if not stack:
        return True
    else:
        return False

if valid_braces("()("):
    print(1)
else:
    print(0)