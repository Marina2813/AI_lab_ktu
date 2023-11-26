#Breadth First Search
def bfs(graph,start,goal):
    visited = []
    q = []
    q.append(start)
    while q:
        visited.append(q[0])
        node = q.pop(0)
        if node == goal:
            print(visited)
        else:
            if node in graph:
                element = graph.get(node)
                for i in element:
                    q.append(i)

n = int(input("Enter the number of nodes: "))
graph={}
for i in range(n):
    parent = input("Enter the parent node:")
    child = input("Enter the child nodes").split()
    graph[parent] = child
start = input("Enter the starting node: ")
goal = input("Enter the goal node: ")
bfs(graph,start,goal)