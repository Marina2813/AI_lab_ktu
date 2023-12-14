def dfs(graph,node):
    visited = set()
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for n in graph[node]:
            dfs(graph,n)

n = input("Enter the number of nodes: ")
graph = {}
for i in range(n):
    parent = input("Enter the parent node: ")
    child = input("Enter the child node: ").split()
    graph[parent]=child

g_keys = list(graph.keys())
dfs(graph,g_keys(0))