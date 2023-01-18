

nodes = []  # keeping the count if the nodes added in the graph
graph = []     #used to determin the adjaceny matrix for edges and nodes

node_count = 0

def add_node(v):

    global node_count  #updating a global variable
    if v in nodes:
        print("The Node is already present in the graph")
    else:
        node_count = node_count +1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []

        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


print("Before adding nodes:")
print(nodes)
print(graph)
add_node("A")
print("After adding nodes:")
print(nodes)
print(graph)


