class NumSet:
    def __init__(self):
        self.s = set()  

    def add(self, x):
        self.s.add(x)

    def remove(self, x):
        self.s.discard(x)  

    def check(self, x):
        return 1 if x in self.s else 0

    def toggle(self, x):
        if x in self.s:
            self.s.remove(x)
        else:
            self.s.add(x)

    def all(self):
        self.s = set(range(1, 21))

    def empty(self):
        self.s.clear()

    def process_command(self, command):
        if len(command) == 2:
            operation, x = command[0], int(command[1])
        else:
            operation = command[0]
        
        if operation == "add":
            self.add(x)
        elif operation == "remove":
            self.remove(x)
        elif operation == "check":
            print(self.check(x))
        elif operation == "toggle":
            self.toggle(x)
        elif operation == "all":
            self.all()
        elif operation == "empty":
            self.empty()

# 예제 실행
import sys
input = sys.stdin.readline

num_set = NumSet()

while True:
    command = input().strip().split()
    if not command:
        break
    num_set.process_command(command)
