''' Adjacency matrix using numpy for a directed graph '''

V = [0,1,2,3,4]
E = [(0,1), (0,2), (1,3), (1,4), (2,4), (2,3), (3,4)]

size = len(V)


import numpy as np
AMat = np.zeros(shape=(size, size))

for (i,j) in E:
    AMat[i,j] = 1 # Assign 1 if edge exists in graph from i to j, else 0

print(AMat)


''' Adjacency matrix using nested list for a directed graph '''

BMat = []

for i in range(size):
    row = []
    for j in range(size):
        if (i,j) in E:
            row.append(1)
        else:
            row.append(0)
    BMat.append(row.copy())
print(BMat)




''' Adjacency Matrix for undirected graph using numpy 2d array '''

UE = E + [(j,i) for (i,j) in E] # In undirected graph each edge is represented by two tuple (u,v) and (v,u)

UAMat = np.zeros(shape=(size, size))

for (i, j) in UE:
    UAMat[i,j] = 1

print(UAMat)




''' Adjacency Matrix for undirected graph using nested list '''

UBat = []

for i in range(size):
    row = []
    for j in range(size):
        if (i,j) in UE:
            row.append(1)
        else:
            row.append(0)
    UBat.append(row.copy())

print(UBat)