print("==============Welcome to LinkedList <3==================")



class Node:

  def __init__(self,data):
    self.data = data
    self.ref = None # address of next node

class Singlelinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    
        
    def display(self):
        if self.head is None:
            print( "The linked list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"---->",end = "")
                temp = temp.ref


    def Beg_insert(self,val):
      nb = Node(val)
      nb.ref = self.head
      self.head = nb



    def push_back(self, val): 
      ne = Node(val)
      tail = self.head   
      while tail.ref:
        tail = tail.ref

      tail.ref = ne

    def count_nodes(self):

      temp = self.head
      count = 0

      if temp is None:
        print("There is no count")

      else:

        while temp is not None:
          count +=1
          temp = temp.ref

        return count

      #print("The number of nodes is ",count)



    def position_insert(self,position,val): # what happens if pos > len(list), if pos < 0 ?
        np = Node(val)
        counter = Singlelinkedlist.count_nodes(self)
        point = self.head
        print("The list has been updated")
        

        if position < 0:
          print("Please make sure position is more than 0")

        if position > counter:
          print("Not that many number of Nodes")

        for i in range(position-2):
          point = point.ref
        np.data = val
        np.ref = point.ref
        point.ref = np
        print("The list has been updated")

    def Beg_insert(self,val):
      nb = Node(val)
      nb.ref = self.head
      self.head = nb
      print("The list has been updated")

    def push_back(self, val): # this should be O(1) if we already have the tail
      ne = Node(val)
      tail = self.head
      while tail.ref:
        tail = tail.ref

      tail.ref = ne
      print("The list has been updated")


    def delete_beg(self): # what happens if list is empty?

      if self.head is None:
        print("There is no list to delete")
      else:
          temp = self.head
          self.head = temp.ref
          temp.ref = None
          print("The list has been updated")

    def delete_end(self): # what happens if list is empty?
      temp = self.head.ref
      tail = self.head # why are we updating the tail here?
      while temp.ref is not None:
        tail = tail.ref
        temp = temp.ref

      tail.ref = None
      print("The list has been updated")

    def delete_pos(self,position): # pos < 0 or pos > len(list)
    
      temp = self.head.ref
      tail = self.head
      
      counter = Singlelinkedlist.count_nodes(self)

      if position < 0:
          print("Please make sure position is more than 0")

      if position > counter:
          print("Not that many number of Nodes")

      for i in range(position -2):
        tail = tail.ref
        temp = temp.ref

      tail.ref = temp.ref
      temp.ref = None
      print("The list has been updated")


    def search_node(self,key): 
      flag = 0
      
      temp = self.head 

      if temp is None:
        print("There is no list")

      else:
        while temp is not None:
            if key == temp.data:
              flag == 1
              break
            temp = temp.ref

          
      if flag == 1:
        print("The Element has been found in the list")
      else:
        print("The Element was not found")


    def reverse_list(self):# we need 3 pointers here
      prev = None
      current = self.head
      
      if current is None:
        print("There is no linked List")
      else:

        while current is not None:
            temp = current.ref # don't name the temp variable ref! This can be confusing to the  reader
          #changibg the direcxtion of teh nodes
            current.ref = prev
          #shifting the nodes
            prev = current
            current = temp
            self.head = prev
            print("The list has been reversed")

L = Singlelinkedlist()
n = Node(10)
L.head = n
n1 = Node(20)
n.ref = n1
n2 = Node(30)
n1.ref = n2
L.display()


print("\nwhat would you like to do?")

while(True):
  print("\n1---> Count the number of Nodes in a list")
  print("2---> Display the updated linked_list")
  print("3---> Insert a Node at the beginning")
  print("4---> Insert a Node at the end")
  print("5---> Insert a Node at a particular position")
  print("6---> Delete a Node at the begining")
  print("7---> Delete a node at the end")
  print("8---> Delete a node at a particular position")
  print("9---> Search for a key value in the list")
  print("10---> Reverse the linkedlist")
  print("11---> exit")

  ch = int(input("Enter your choice:"))

  if ch == 1:
    print("The number of nodes in the list are",L.count_nodes())


  elif ch == 2:
    L.display()

  elif ch == 3:
    x =int(input("Enter the value you wana enter:"))
    L.Beg_insert(x)

  elif ch == 4:
    x =int(input("Enter the value you wana enter:"))
    L.push_back(x)

  elif ch == 5:
      a =int(input("Enter your desired position:"))
      b =int(input("Enter the value you wana enter:"))
      L.position_insert(a,b)

  elif ch == 6:
    L.delete_beg()

  elif ch ==7:
    L.delete_end()

  elif ch == 8:
    a =int(input("Enter your desired position:"))
    L.delete_pos(a)

  elif ch == 9:
    a =int(input("Enter the key element:"))
    L.search_node(a)

  elif ch == 10:
    L.reverse_list()

  elif ch == 11:
    break

  else:
    print("Invalid choice")
