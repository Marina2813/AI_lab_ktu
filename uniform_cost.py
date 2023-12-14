#uniform cost search

'''
 The primary goal of the uniform-cost search is to find a path to the goal node which has the lowest cumulative cost
 Uniform cost search is equivalent to BFS algorithm if the path cost of all edges is the same.
 It is implemented using priority queue
 '''
import heapq # heapq is a module in python that allows implementation of heap queue(priority queue)

def uniform_cost_search(graph,start,goal):
    visited = set()
    frontier = [(0,start,[])]
    while frontier:

        cost,current,path = heapq.heappop(frontier)

        if current == goal:
            print(f"Total cost from {start} to {goal} is {cost}")
            print("path","->".join(path+[current]))
            return cost
        
        visited.add(current)
        for neighbour,n_cost in graph[current]:
            total_cost = cost + n_cost
            new_path = path + [current]
            heapq.heappush(frontier,(total_cost,neighbour,new_path))

    return None

n = int(input("Enter the number of nodes: "))
graph = {}
for i in range(n):
    node = input("Enter the Node: ")
    k = int(input("Enter the number of associated nodes: "))
    if(k!=0):
        assoc = []
        a = ()
        for j in range(k):
            a = (input("Enter associated node: "),int(input("Enter the path cost: ")))
            assoc.append(a)
            graph[node]=assoc
    else:
        graph[node]=[]
        continue
    print()
print(graph)

start_node = input("Enter the start node: ")
goal = input("Enter the goal node: ")

result = uniform_cost_search(graph,start_node,goal)
if result is None:
    print(f"There is no path from {start_node} to {goal} ")