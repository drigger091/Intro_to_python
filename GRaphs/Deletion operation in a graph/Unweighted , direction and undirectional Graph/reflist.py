#this ref is created in accordance to adjacency list


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



def add_edgeUWD(v1,v2): #un weighted but directed graph
    if v1 not in graph:
        print(v1,"is not present in th graph")
    elif v2 not in graph:
        print(v2 , "is not present in the graph")
    else:
        graph[v1].append(v2)

def delete_node(v): # works for unweighted , directed and undirected graph
    if v not in graph:
        print(v, "is not present in the graph")
    else:
        graph.pop(v) # deleting the key value pair from the graph dictionary
        #checking the values of other keys and deleting the node from their values as well
        for i in graph:
            list1 = graph[i] # all the values from each key are getting stored in here and checking whether v is there or not
            if v in list1:
                list1.remove(v)

def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present in the graph")
    elif v2 not in graph:
        print(v2,"is not present in the graph")
    else:  #checking whether there is an edge bw the mentioned nodes
        if v2 in graph[v1]:
            graph[v1].remove(v2) #  we are accesing the v1 key in the graph dictionary and removing the value v2 in there from the list
            graph[v2].remove(v1) # similarly the vice versa needs to be done in case the edge is undirectional
        else:
            print("There is no edge between",v1, "and",v2)

# for directed graph we need not use graph[v2].remove(v1) as only connects one way


def delete_edgeD(v1,v2):
    if v1 not in graph:
        print(v1,"is not in graph")
    elif v2 not in graph:
        print(v2,"is not in graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)







add_nodes("A")

add_nodes("B")
add_nodes("C")
add_nodes("D")
add_nodes("E")
add_nodes("F")
add_edgeUWUD("D","B")# connects both D and B with each other
add_edgeUWUD("C","F") # coonectting both with both
add_edgeUWUD("A","D") # connects both of them mutually
add_edgeUWUD("B","F") # connecting both of them with each other
add_edgeUWD("F","A") # only connects F with A

add_edgeUWD("E","A")# connecting E with A not the other way
#delete_node("F")  # deleting the node function
delete_edge("F","C")
delete_edgeD("F","A")
#print("After adding nodes")
print(graph)