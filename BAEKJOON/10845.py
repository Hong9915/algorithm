class QUEUE:
    def __init__(self):
        self.result = []
    
    def push(self, X):
        self.result.append(X)
        
    def pop(self): #고쳐야됌
        if self.result:
            result=self.result[0]
            del self.result[0]
            return result
        else:
            return -1
    
    def size(self):
        return len(self.result)
    
    def empty(self):
        return 0 if self.result else 1
    
    def front(self):
        return self.result[0] if self.result else -1
    
    def back(self):
        return self.result[-1] if self.result else -1
    

N = int(input())
temp_queue=QUEUE()
output=[]
for _ in range(N):
    command = input().strip()
    if command.startswith("push"):
        _, num = command.split()
        temp_queue.push(int(num))
    elif command == "pop":
        output.append(temp_queue.pop())
    elif command == "size":
        output.append(temp_queue.size())
    elif command == "empty":
        output.append(temp_queue.empty())
    elif command == "front":
        output.append(temp_queue.front())
    elif command == "back":
        output.append(temp_queue.back())
        
print("\n".join(map(str,output)))