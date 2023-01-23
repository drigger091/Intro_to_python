

# we are using adjacency list representation
# we are using recursive approach


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



def DFS(node,visited,graph):  #depth first search algo

    if node not in graph:
        print(node,"is not in graph")
        return
    
    if node not in visited:

        print(node)
        visited.add(node) # if visited the node gets added to the visited set
        #after getting the node we check its adjacent nodes
        for i in graph[node]: # we are accesing the list of values for each key to get the adjacent points
            DFS(i,visited,graph)
    
    



visited = set()  # as we are using recursive functon we don have to refresh it instead passing it on as a paraeter
#list can be used but set is efficient as no repeat values to be allowed

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


#print(graph)
#DFS("B",visited,graph)
DFS("K",visited,graph)




