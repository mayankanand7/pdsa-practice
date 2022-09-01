''' Topological sorting using Matrix '''

def toposort(AMat):
    (rows, cols) = AMat.shape
    (indegree, toposortList) = ({}, [])

    for c in range(cols):
        indegree[c] = 0
        for r in range(rows):
            if AMat[r,c] == 1:
                indegree[c] = indegree[c] + 1
    
    for i in range(rows):
        j = min([k for k in range(cols) if indegree[k] == 0])

        toposortList.append(j)
        indegree[j] = indegree[j] - 1

        for k in range(cols):
            if AMat[j,k] == 1:
                indegree[k] = indegree[k] - 1
        
    return(toposortList)

edges=[(0,2),(0,3),(0,4),(1,2),(1,7),(2,5),(3,5),(3,7),(4,7),(5,6),(6,7)]
size = 8
import numpy as np
AMat = np.zeros(shape=(size,size))
for (i,j) in edges:
    AMat[i,j] = 1
print(toposort(AMat))



''' Topological sort using List '''

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


def toposortlist(AList):
    (indegree, toposortList) = ({}, [])
    zerodegree = Queue()

    for i in AList.keys():
        indegree[i] = 0
    
    for i in AList.keys():
        for j in AList[i]:
            indegree[j] = indegree[j] + 1
    
    for i in AList.keys():
        if indegree[i] == 0:
            zerodegree.addq(i)
    
    while(not zerodegree.isempty()):
        j = zerodegree.delq()
        toposortList.append(j)
        indegree[j] = indegree[j] - 1

        for k in AList[j]:
            indegree[k] = indegree[k] - 1
            if (indegree[k] == 0):
                zerodegree.addq(k)
    return(toposortList)

AList={0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
print(toposortlist(AList))