class Queue:
    
    def __init__(self):
        self.A = []
    
    def addq(self, v):
        self.A.append(v)
    
    def delq(self):
        if (self.A==[]):
            return(None)

        item = self.A[0]
        self.A = self.A[1:]
        return(item)
    
    def isempty(self):
        return(self.A == [])


class Stack:
    def __init__(self):
        self.A = []
    
    def isempty(self):
        return(self.A == [])
    
    def push(self, v):
        self.A.append(v)
    
    def pop(self):
        if self.A == []:
            return(None)
        
        item = self.A[-1]
        self.A = self.A[:-1]
        return(item)


def bfsTest(AList, v):
    visited = {}

    for i in AList.keys():
        visited[i] = False
    
    q = Queue()
    # visited[q] = True
    q.addq(v)

    while(not q.isempty()):
        j = q.delq()

        if not visited[j]:
            visited[j] = True
            print("visited : ", j)

            for k in AList[j]:
                q.addq(k)
    return(visited)


def dfsTest(AList, v):
    visited = {}

    for i in AList.keys():
        visited[i] = False
    
    s = Stack()
    s.push(v)

    while(not s.isempty()):
        j = s.pop()

        if not visited[j]:
            visited[j] = True
            print("visited : ", j)

            for k in AList[j]:
                s.push(k)
    
    return(visited)




AList = {1:[3,4], 2:[3], 3:[6], 4:[6,7], 5:[4,6], 6:[2], 7:[5]}
print(dfsTest(AList, 1))
# print(bfsTest(AList, 1))