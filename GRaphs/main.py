

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


#before performing we check whther v1 and v2 in nodes
def add_edge(v1,v2): #undirected graph and inweighted graphso no weights
    if v1 not in nodes:
        print(v1,"is not present in the nodes")
    elif v2  not in nodes:
        print(v2,"is not present in the nodes")
    else:
         index1 = nodes.index(v1) #getting the index from node list and change accoording in the graph maxtrix
         index2 = nodes.index(v2)
         graph[index1][index2] = 1
         graph[index2][index1] = 1

def add_edgeWeighted(v1 ,v2 , cost):#undirected weighted graph
    if v1 not in nodes:
        print(v1,"is not present in the nodes")
    elif v2  not in nodes:
        print(v2,"is not present in the nodes")
    else:
         index1 = nodes.index(v1) #getting the index from node list and change accoording in the graph maxtrix
         index2 = nodes.index(v2)
         graph[index1][index2] = cost
         graph[index2][index1] = cost

def add_edgeDW(v1,v2,cost): #here the edge is conected from v1 to v2 only change in v1 row and v2 column
    if v1 not in nodes:
        print(v1,"not present in nodes")
    elif v2 not in nodes:
        print(v2,"is not present in the nodes")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2]= cost




def print_graph():

    for i in range(node_count):

        for j in range(node_count):
            print(format(graph[i][j],"<3"), end =" ")
        print ()




#print("Before adding nodes:")
#print(nodes)
#print(graph)
add_node("A")
add_node("B")
add_node("C")
add_node("D")
print("After adding nodes:")
add_edge("A","B") # adding edge between A and B
add_edgeWeighted("A","B",10)
add_edgeWeighted("A","D",5)
add_edgeDW("C","D",4)

print(nodes)
#print(graph)
print_graph()
print(node_count)

# it is all zero as there are no edges added till yet so no connection


