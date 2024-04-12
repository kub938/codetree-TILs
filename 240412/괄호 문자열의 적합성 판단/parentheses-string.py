s = input()
stack = []
check = True

def top(stack):
    return stack[-1]

for i in s:
    if len(stack)==0 and i==')':
        check = False
        break
    elif i=='(':
        stack.append('(')
    elif i==')' and top(stack)=='(':
        stack.pop()
    elif i==')' and top(stack)==')':
        stack.append(')')
if len(stack)>0:
    check=False

if check:
    print('Yes')
else:
    print('No')