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
add_edgeUWUD("D","B")# connects both D and B with each other
add_edgeUWUD("C","F") # coonectting both with both
add_edgeUWUD("A","D") # connects both of them mutually
add_edgeUWUD("B","F") # connecting both of them with each other
add_edgeUWD("F","A") # only connects F with A

add_edgeUWD("E","A")# connecting E with A not the other way
delete_node("F")  # deleting the node function

print("After adding nodes")
print(graph)