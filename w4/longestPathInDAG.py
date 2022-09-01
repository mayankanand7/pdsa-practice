from sklearn.linear_model import lars_path


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


def longestPathList(AList):
    (indegree, lpath) = ({}, {})
    zerodegree = Queue()

    for i in AList.keys():
        indegree[i] = 0
        lpath[i] = 0
    
    for i in AList.keys():
        for j in AList[i]:
            indegree[j] = indegree[j] + 1
    
    for i in AList.keys():
        if indegree[i] == 0:
            zerodegree.addq(i)
        
    while(not zerodegree.isempty()):
        j = zerodegree.delq()
        indegree[j] = indegree[j] - 1

        for k in AList[j]:
            indegree[k] = indegree[k] - 1
            lpath[k] = max(lpath[k], lpath[j] + 1)
            if indegree[k] == 0:
                zerodegree.addq(k)
    
    return(lpath)

AList={0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
print(longestPathList(AList))