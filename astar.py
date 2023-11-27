# A* search is used to find shortest path in real-life situations like maps, games where there can be many hindrances
def heuristic(n):
    return h_dist[n]

def get_neighbours(i):
    if i in graph:
        return graph[i]
    else:
        return []
    

def astaralgo(start, stop):
    open_set=set(start) #set of nodes to be evaluated
    closed_set = set() #set of nodes already evaluated, initially empty
    g = {} #dictionary representing the cost of each node from the start node
    parent = {}
    g[start] = 0
    parent[start] = start
    while len(open_set)>0:
        n = -1
        for v in open_set:
            if (n==-1 or (heuristic(v)+ g[v] < heuristic(n)+g[n])):
                n=v
        if n == stop:
            pass
        else:
            for (m,weight) in get_neighbours(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parent[m] = n
                    g[m]=g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parent[m]=n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n==-1:
            print("Path does not exist!!")
            return None
        
        if n==stop:
            path =[]
            while parent[n] !=n:
                path.append(n)
                n = parent[n]
            path.append(start)
            path.reverse()
            print("The path is: {}".format(path))
            return path
        open_set.remove(n)
        closed_set.add(n)


n = int(input("Enter the number of nodes: "))
graph={}
for i in range (n):
    node = input("Enter the node: ")
    k = int(input("Enter the number of associated nodes: "))
    if(k!=0):
        assoc=[]
        a =()
        for j in range(k):
            a = (input("Enter the associated node: "),int(input("Enter the path cost: ")))
            assoc.append(a)
            graph[node] = assoc
    else:
        graph[node] = 0
        continue
    print()
print(graph)

#heuristic function from user
h_dist={}
h=int(input("Enter the number of nodes: "))
for i in range(h):
    node=input("Enter the node: ")
    dist = int(input("Enter the distance: "))
    print()
    h_dist[node]=dist
print(h_dist)

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
astaralgo(start,goal)