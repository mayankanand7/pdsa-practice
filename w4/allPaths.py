class Stack:
    def __init__(self):
        self.A = []
    
    def isempty(self):
        return(self.A == [])
    
    def push(self, v):
        self.A.append(v)
    
    def pop(self):
        if self.isempty():
            return None
        
        item = self.A[-1]
        self.A = self.A[:-1]
        return(item)
    

def getAllPaths(AList, src, dst):
    (visited, path, allPaths) = ({}, [], [])

    for i in AList.keys():
        visited[i] = False
    
    st = Stack()
    st.push(src)

    while(not st.isempty()):
        j = st.pop()

        if (not visited[j]):
            visited[j] = True

            path.append(j)

            if j == dst:
                allPaths.append(path.copy())
                path.pop()

            for k in AList[j]:
                if k not in st.A:
                    st.push(k)
                
    return(allPaths)

AList = {1:[3,4], 2:[3], 3:[6], 4:[6,7], 5:[4,6], 6:[2], 7:[5]}
print(getAllPaths(AList, 1, 2))