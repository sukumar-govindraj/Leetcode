st=''
def valid_parenthesis(st):
    maps ={ '(':')', '[':']', '}':'{'}
    stack=[]
    for s in st:
        if s in maps:
            top = stack.pop() if stack else '#'
            if maps[s] != top:
                return False
        else:
            stack.append(s)
    return not stack