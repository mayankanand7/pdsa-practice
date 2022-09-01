''' Adjacency Matrix for Directed graph '''

dedges = [(0,1,10),(0,2,80),(1,2,6),(1,4,20),(2,3,70),(4,5,50),(4,6,5),(5,6,10)]
size = 7

import numpy as np

W = np.zeros(shape=(size, size, 2))

for (i, j, w) in dedges:
    W[i,j,0] = 1
    W[i,j,1] = w

print(W)


''' Adjacency Matrix for Undirected graph '''

edges = dedges + [(j,i,w) for (i,j,w) in dedges]

UW = np.zeros(shape=(size,size,2))
for (i,j,w) in edges:
    UW[i,j,0] = 1
    UW[i,j,1] = w
print(UW)


''' Adjacency List for Directed graph '''

WL = {}
for i in range(size):
    WL[i] = []

for (i,j,d) in dedges:
    WL[i].append((j,d))

print(WL)



''' Adjacency List for Undirected graph '''

UWL = {}
for i in range(size):
    UWL[i] = []
for (i,j,d) in edges:
    UWL[i].append((j,d))
print(UWL)