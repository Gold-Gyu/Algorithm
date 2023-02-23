size = 10
q = [0] * size
front = rear = -1

def isFUll():
    print

def enqueue(item):
    global rear
    if isFull():
        print("full")
    rear += 1
    q[rear] = item


def isEmpty():
    return front == rear

def dequeue():
    global front
    if isEmpty():
        print("empty")
        return
    front += 1
    return q[front]

for i in range(10):
    enqueue(i)

print(q)
print(isEmpty())
print(isFull())

for i in range(10):
    print(dequeue(), end= " ")
print()

print(isEmpty())
print(isFUll())