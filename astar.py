# A* search is used to find shortest path in real-life situations like maps, games where there can be many hindrances
import heapq
def heuristic(n):
    return h_dist[n]

def a_star_search(graph,start,goal):
    visited = set()
    priq = [(0,start,[])]

    while priq:
        cost,current,path = heapq.heappop(priq)

        if current == goal:
            return path+[current]
        
        if current not in visited:
            visited.add(current)
            for neighbour,n_cost in graph[current]:
                if neighbour not in visited:
                    total_cost = cost + n_cost
                    pri = total_cost + heuristic(neighbour)
                    new_path = path+[current]
                    heapq.heappush(priq,(pri,neighbour,new_path))
    
    return None
                               


#n = int(input("Enter the number of nodes: "))
graph = {}

'''for i in range (n):
    node = input("Enter the node name: ")
    k = int(input("Enter the number of associated nodes: "))
    if(k!=0):
        assoc = []
        a = ()
        for i in range (k):
            a = (input("Enter the associated node"),int(input("Enter the path cost: ")))
            assoc.append(a)
            graph[node] = assoc
    else:
        graph[node] = []
        continue
    print()
print(graph)

h_dist = {}
h = int(input("Enter thr number of nodes: "))
for i in range(h):
    node = input("Enter the node: ")
    h_cost = input("Enter the heuristic cost")
    print()
    h_dist[node]=h_cost
print(h_dist)

'''

graph={
    'A':[('B',6),('F',3)],
    'B':[('A',6),('D',2),('C',3)],
    'C':[('B',3),('D',1),('E',5)],
    'D':[('B',2),('C',1),('E',8)],
    'E':[('D',8),('C',5),('I',5),('J',5)],
    'F':[('A',3),('G',1),('H',7)],
    'G':[('F',1),('I',3)],
    'H':[('F',7),('I',2)],
    'I':[('E',5),('G',3),('H',2),('J',3)],
    'J':[('I',3),('E',5)]
}

h_dist={'A':10,'B':8,'C':5,'D':7,'E':3,'F':6,'G':5,'I':1,'J':0,'H':3}

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

result = a_star_search(graph,start,goal)
print(result)