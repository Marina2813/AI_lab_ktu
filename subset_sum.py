import numpy as np 

n = int(input("Enter the number of nodes: "))
graph = {}
solution = {}

for i in range(n):
    parent = input("Enter the parent: ")
    child = input("Enter the children nodes: ").split()
    graph[parent]=child
    soln = input("Enter solutions: ").split()
    solution[parent] = soln

print('graph is ',graph)

for i in solution:
    for j in range(0,len(solution[i])):
        solution[i][j] = int(solution[i][j])
print('Solution is: ',solution)

r = input("Enter the start node: ")
sum = int(input("Enter the target sum: "))
visited = []
flagbfs = flagdfs = 0
seqbfs = seqdfs = []

def bfs(graph,root,sum,solution):
    frontier = []
    explored = []
    frontier.append(root)
    while frontier:
        node = frontier.pop(0)
        explored.append(node)
        print(node)
        if np.sum(solution[node])==sum:
            global flagbfs
            flagbfs = 1
            global seqbfs
            seqbfs = solution[node]
            return
        for a in graph[node]:
            if a not in explored:
                frontier.append(a)

def dfs(visited,graph,node,sum,solution):
    if node not in visited:
        print(node)
        visited.append(node)
        if np.sum(solution[node])==sum:
            global flagdfs
            flagdfs = 1
            global seqdfs
            seqdfs = solution[node]
        for neighbour in graph[node]:
            if flagdfs!=1:
                dfs(visited,graph,neighbour,sum,solution)

print("BFS TRAVERSAL: ")
bfs(graph,r,sum,solution)
print("DFS TRAVERSAL: ")
bfs(visited,graph,r,sum,solution)

print("Sequence found using dfs: ",seqdfs)
print("sequence using bfs is",seqbfs)