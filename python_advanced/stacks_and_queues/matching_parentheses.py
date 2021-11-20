expression = input()

brackets_stack = []

for i in range(len(expression)):

    if expression[i] == '(':
        brackets_stack.append(i)
    elif expression[i] == ')':
        print(expression[brackets_stack[-1]:i + 1])
        brackets_stack.pop()
