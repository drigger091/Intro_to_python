# we will be using adjacency list to represent
# we will be using stack data structure


graph = {}


def add_nodes(v):

    if v in graph.keys():
        print(v,"is in graph already")
    else:
        graph[v] = []

def add_edgeUWUD(v1 ,v2):  # unweighted ,undirected

    if v1 not in graph:
        print(v1, "is not in graph")
    elif v2 not in graph:
        print(v2, "is not in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def add_edgeUwD(v1 ,v2):  #directed graph
    if v1 not in graph:
        print(v1,"is not in graph")
    elif v2 not in graph:
        print(v2,"not in graph")
    else:
        graph[v1].append(v2)

def DFS(node,graph):

    visited = set()

    if node not in graph:
        print(node,"is not in graph")
        return
    stack = []
    stack.append(node)  # pushing the first element into the stack
   
    while stack: # we will keep on iterating until the stack is empty
        current =stack.pop()  # returns the last element from the pop which we will map into visited later 
            #as it has already been traversed or not
        if current not in visited: # we are coming across the node for first time
            print(current) # we are printing the node
            visited.add(current) # once printed we are adding it to visited as we have already visited that node
            for i in graph[current]: #here we are iterating the adjacent values of each node from graph and putting them into stack
                stack.append(i)  #adjacent nodes of each dict key node will be pushed into stack








#making the graph
add_nodes("A")
add_nodes("B")
add_nodes("C")
add_nodes("D")
add_nodes("E")
add_nodes("F")
add_edgeUWUD("A","B")
add_edgeUWUD("B","E")
add_edgeUWUD("A","C")
add_edgeUWUD("A","D")
add_edgeUWUD("A","F")
add_edgeUWUD("B","D")
add_edgeUWUD("C","D")
DFS("A",graph)
#print(graph)