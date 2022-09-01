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


def BFSList(AList, v):
    visited = {}

    for i in AList.keys():
        visited[i] = False
    
    q = Queue()
    visited[v] = True
    q.addq(v)

    while(not q.isempty()):
        j = q.delq()

        for k in AList[j]:
            if (not visited[k]):
                visited[k] = True
                q.addq(k)
    return(visited)


def Components(AList):
    component = {}

    for i in AList.keys():
        component[i] = -1
    
    (compid, seen) = (0, 0)

    while seen <= max(AList.keys()):
        startv = min([i for i in AList.keys() if component[i] == -1])
        visited = BFSList(AList, startv)

        for i in visited.keys():
            if (visited[i]):
                seen = seen + 1
                component[i] = compid
        compid = compid + 1
    
    return(component)



AList = {0: [1], 1: [2], 2: [0], 3: [4, 6], 4: [3, 7], 5: [3, 7], 6: [5], 7: [4, 8], 8: [5, 9], 9: [8]}
print(Components(AList))