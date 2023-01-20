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

def add_edgeWD(v1,v2,cost): # weighted and directed graph
    if v1 not in graph:
        print(v1,"is not present in the Graph")
    elif v2 not in graph:
        print(v2,"is not present in th graph")
    else:
        list1 = [v2,cost]
        graph[v1].append(list1)

def add_edgeUWD(v1,v2): #un weighted but directed graph
    if v1 not in graph:
        print(v1,"is not present in th graph")
    elif v2 not in graph:
        print(v2 , "is not present in the graph")
    else:
        graph[v1].append(v2)

def delete_node(v): # works for unweighted and weighted directed and undirected graph
    if v not in graph:
        print(v, "is not present in the graph")
    else:
        graph.pop(v) # deleting the key value pair from the graph dictionary
        #checking the values of other keys and deleting the node from their values as well
        for i in graph:
            list1 = graph[i] # all the values from each key are getting stored in here and checking whether v is there or not
            if v in list1:
                list1.remove(v)










add_nodes("A")

add_nodes("B")
add_nodes("C")
add_nodes("D")
add_nodes("E")
add_nodes("F")
add_edgeUWUD("D","B")
add_edgeUWUD("A","F")
add_edgeUWUD("B","F")
add_edgeWUD("A","B",10)
add_edgeWUD("A","C",5)
add_edgeWD("E","D",20)
add_edgeUWD("E","A")
delete_node("F")

print("After adding nodes")
print(graph)