''' BFS for Adjacency List '''

class Queue:
    def __init__(self):
        self.queue = []
    
    def addq(self, v):
        self.queue.append(v)
    
    def isempty(self):
        return(self.queue == [])
    
    def delq(self):
        v = self.queue[0]
        self.queue = self.queue[1:]
        return(v)
    
    def __str__(self):
        return(str(self.queue))



''' Reachability '''
''' BFS - Explore the graph level by level using Adjacency List'''
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

AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
print(BFSList(AList,0))




''' BFS - Explore the graph level by level using Adjacency List'''
def BFS(AMat, v):
    (rows, cols) = AMat.shape
    visited = {}
    for i in range(rows):
        visited[i] = False
    
    q = Queue()
    
    visited[v] = True
    q.addq(v)

    while(not q.isempty()):
        j = q.delq()
        
        nbrs = neighbours(AMat, j)
        for i in nbrs:
            if (not visited[i]):
                visited[i] = True
                q.addq(i)
    
    return(visited)


def neighbours(AMat, i):
    nbrs = []
    (rows, cols) = AMat.shape
    for j in range(cols):
        if AMat[i,j] == 1:
            nbrs.append(j)
    
    return(nbrs)

V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)] 
size = len(V)
import numpy as np
AMat = np.zeros(shape=(size,size))
for (i,j) in E:
    AMat[i,j] = 1
print(BFS(AMat,0))