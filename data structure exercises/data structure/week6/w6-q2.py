class RacingQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.buffer = []
        self.start = 0
        self.count = 0

    def check_overflow(self):
        return self.count >= self.max_size

    def check_underflow(self):
        return self.count == 0

    def add(self, val):
        if self.check_overflow():
            print("Queue is full")
            return

        while self.buffer and self.buffer[-1] > val:
            self.buffer.pop()
            self.count -= 1

        self.buffer.append(val)
        self.count += 1

        print(f"QUEUE: {self.buffer}")

    def remove(self):
        if self.check_underflow():
            print("Queue is empty")
            return

        item = self.buffer.pop(0)
        self.count -= 1

        print(f"Car sent to starting line: [{item}]")
        print(f"QUEUE: {self.buffer}")

    def show(self):
        if self.check_underflow():
            print("QUEUE: []")
        else:
            print(f"QUEUE: {self.buffer}")


import sys

size = int(input())
rq = RacingQueue(size)

for req in sys.stdin:
    cmd = req.strip().split()

    if not cmd:
        continue

    if cmd[0] == "INSERT":
        try:
            val = float(cmd[1])
            rq.add(val)
        except:
            print("Invalid input")

    elif cmd[0] == "DELETE":
        rq.remove()

    elif cmd[0] == "DISPLAY":
        rq.show()

    elif cmd[0] == "EXIT":
        break

    else:
        print("Invalid input")
