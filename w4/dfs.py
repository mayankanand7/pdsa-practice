class Stack:
    def __init__(self):
        self.stack = []

    def push(self, v):
        self.stack.append(v)    

    def pop(self):
        if (self.isempty()):
            return None

        v = self.stack[-1]
        self.stack = self.stack[:-1]
        return(v)

    def isempty(self):
        return(self.stack == [])
    

    def __str__(self):
        return(str(self.stack))


def DFSList(AList, v):
    visited = {}

    for i in AList.keys():
        visited[i] = False
    
    st = Stack()
    st.push(v)

    while(not st.isempty()):
        j = st.pop()
        if (not visited[j]):
            visited[j] = True
            for k in AList[j]:
                if (not visited[k]):
                    st.push(k)
    
    return(visited)

AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
print(DFSList(AList,0))



''' DFS Recursive without using Stack '''
def DFSInitList(AList):
    (visited, parent) = ({}, {})

    for i in AList.keys():
        visited[i] = False
        parent[i] = -1

    return(visited, parent)

def DFSListI(AList, visited, parent, v):
    visited[v] = True

    for k in AList[v]:
        if (not visited[k]):
            parent[k] = v
            (visited, parent) = DFSListI(AList, visited, parent, k)

    return(visited, parent)

AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
v,p = DFSInitList(AList)
print(DFSListI(AList,v,p,0))



''' DFS Global for Adjacency List  of graph '''

(visited, parent) = ({}, {})

def DFSInitListGlobal(AList):
    for i in AList.keys():
        visited[i] = False
        parent[i] = -1


def DFSListIGlobal(AList, v):
    visited[v] = True

    for k in AList[v]:
        if (not visited[k]):
            parent[k] = v
            DFSListIGlobal(AList, k)

AList ={0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
DFSInitListGlobal(AList)
DFSListIGlobal(AList,0)
print(visited,parent)



''' DFS for Adjacency Matrix '''

def neighbours(AMat, i):
    nbrs = []
    (rows, cols) = AMat.shape

    for j in range(cols):
        if (AMat[i,j] == 1):
            nbrs.append(j)

    return(nbrs)


def DFSInitM(AMat):
    (visited, parent) = ({}, {})

    (rows, cols) = AMat.shape
    for i in range(rows):
        visited[i] = False
        parent[i] = -1
    
    return(visited, parent)


def DFSM(AMat, visited, parent, v):
    visited[v] = True

    for k in neighbours(AMat, v):
        if (not visited[k]):
            parent[k] = v
            DFSM(AMat, visited, parent, k)
    
    return(visited, parent)

V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)] 
size = len(V)
import numpy as np
AMat = np.zeros(shape=(size,size))
for (i,j) in E:
    AMat[i,j] = 1
v,p=DFSInitM(AMat)
print(DFSM(AMat,v,p,0))



''' DFS Global using adjacency matrix '''
(visitedM,parentM) = ({},{})
def DFSInitGlobalM(AMat):
    (rows, cols) = AMat.shape
    for i in range(rows):
        visitedM[i] = False
        parentM[i] = -1
    
    return(visitedM, parentM)

def DFSGlobalM(AMat,v):
    visitedM[v] = True

    for k in neighbours(AMat, v):
        if (not visitedM[k]):
            parentM[k] = v
            DFSGlobalM(AMat, k)

DFSInitGlobalM(AMat)
DFSGlobalM(AMat,0)
print(visitedM,parentM)