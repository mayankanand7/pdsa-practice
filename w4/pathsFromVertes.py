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


def BFSListPath(AList, v):
    (visited, parents) = ({}, {})
    
    for i in AList.keys():
        visited[i] = False
        parents[i] = -1
    
    q = Queue()
    visited[j] = True
    q.addq(v)

    while(not q.isempty()):
        j = q.delq()

        for k in AList[j]:
            if (not visited[k]):
                visited[k] = True
                q.addq(k)
                parents[k] = j
    
    return(visited, parents)

AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
print(BFSListPath(AList,0))