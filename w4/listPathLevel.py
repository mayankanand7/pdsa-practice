class Queue:
    def __init__(self):
        self.queue = []
    def addq(self,v):
        self.queue.append(v)
    def isempty(self):
        return(self.queue == [])
    def delq(self):
        v = None
        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]
        return(v)    
    def __str__(self):
        return(str(self.queue))


def BFSListPathLevel(AList, v):
    (level, parent) = ({}, {})

    for i in AList.keys():
        level[i] = -1
        parent[i] = -1
    
    q = Queue()

    level[v] = 0
    q.addq(v)

    while(not q.isempty()):
        j = q.delq()

        for k in AList[j]:
            if (level[k] == -1):
                level[k] = level[j] + 1
                parent[k] = j
                q.addq(k)

    return(level, parent)

AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
print(BFSListPathLevel(AList,0))