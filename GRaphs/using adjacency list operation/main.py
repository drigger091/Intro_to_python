#creating the dictionary to represent the graoh instead of a matrix

graph = {}

def add_nodes(v):
    if v in graph.keys():
        print(v,"is present in graph")
    else:
        graph[v] = []


add_nodes("A")
add_nodes("A")
add_nodes("B")
print(graph)