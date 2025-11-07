class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.first = 0
        self.num = 0

    def is_full(self):
        return self.num >= self.capacity

    def is_empty(self):
        return self.num == 0

    def insert(self, x):
        if self.is_full():
            print("Queue is full")
            return

        while len(self.queue) > 0 and self.queue[-1] > x:
            self.queue.pop()
            self.num -= 1

        self.queue.append(x)
        self.num += 1

        print(f"QUEUE: {self.queue}")

    def delete(self):
        if self.is_empty():
            print("Queue is empty")
            return

        deleted = self.queue.pop(0)
        self.num -= 1

        print(f"Car sent to starting line: [{deleted}]")
        print(f"QUEUE: {self.queue}")

    def display(self):
        if self.is_empty():
            print("QUEUE: []")
        else:
            print(f"QUEUE: {self.queue}")


capacity = int(input())
cq = CircularQueue(capacity)

import sys

for line in sys.stdin:
    command = line.strip().split()

    if not command:
        continue

    if command[0] == "INSERT":
        try:
            x = float(command[1])
            cq.insert(x)
        except:
            print("Invalid input")

    elif command[0] == "DELETE":
        cq.delete()

    elif command[0] == "DISPLAY":
        cq.display()

    elif command[0] == "EXIT":
        break

    else:
        print("Invalid input")
