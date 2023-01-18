

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


def print_graoh():

    for i in range(node_count):

        for j in range(node_count):
            print(graph[i][j], end =" ")
        print ()




print("Before adding nodes:")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("C")
print("After adding nodes:")
print(nodes)
print(graph)
print_graoh()
print(node_count)

# it is all zero as there are no edges added till yet so no connection


