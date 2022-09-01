''' Adjacency list creation using dictionary for given directed graph '''

V = [0,1,2,3,4]
E = [(0,1), (0,2), (1,3), (1,4), (2,4), (2,3), (3,4)]

size = len(V)
AList = {}

for i in range(size):
    AList[i] = []

for (i,j) in E:
    AList[i].append(j)

print(AList)




''' Adjacency list creation using dictionary for given undirected graph '''

UE = E + [(j,i) for (i,j) in E]

UAList = {}

for i in range(size):
    UAList[i] = []

for (i,j) in UE:
    UAList[i].append(j)

print(UAList)