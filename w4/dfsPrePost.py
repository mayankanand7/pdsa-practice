''' Used to detect cycles in the graph '''

(visited, pre, post) = ({}, {}, {})

def dfsInitPrePost(AList):
    for i in AList.keys():
        visited[i] = False
        (pre[i], post[i]) = (-1, -1)
    
    return

def dfsPrePost(AList, v, count):
    visited[v] = True
    pre[v] = count
    count = count + 1

    for k in AList[v]:
        if not visited[k]:
            dfsPrePost(AList, k, count)

    post[v] = count
    count = count + 1
    
    return(count)