# Queue 대기 줄과 같은 선입선출 First In First Out

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # print from the first input
queue.reverse()
print(queue) # print from the last input