#creating the dictionary to represent the graoh instead of a matrix

graph = {}

def add_nodes(v):
    if v in graph.keys():
        print(v,"is present in graph")
    else:
        graph[v] = []

def add_edgeUWUD(v1,v2): #undirected and unweighted graph
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


#here it is a nested list the first value will be the value and the cost
def add_edgeWUD(v1,v2,cost): #undirected and weighted graph
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)

add_nodes("A")
add_nodes("A")
add_nodes("B")
add_nodes("C")
#add_edgeUWUD("A","B")
add_edgeWUD("A","B",10)
add_edgeWUD("A","C",5)
print(graph)