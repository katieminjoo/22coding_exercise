# 스택예제 Stack
# 선입후출First In Last Out, 후입선출 Last In First Out
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])