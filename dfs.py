def dfs(graph,node):
    visited = set()
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph,neighbour)

n = int(input("Enter the number of nodes: "))
graph = {}
for i in range(n):
    parent = input("Enter the parent node: ")
    child = input(f"Enter the child nodes of {parent}: ").split()
    graph[parent] = child

g_keys = list(graph.keys())
dfs(graph,g_keys[0])