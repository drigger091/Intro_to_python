print("==============Welcome to LinkedList <3==================")



class Node:

  def __init__(self,data):
    self.data = data
    self.ref = None # address of next node

class Singlelinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    

    def add_nodes(self , val):

        if self.tail is None:
          self.head = self.tail = Node(val)
        else:
          self.tail.ref = Node(val)
          self.tail = self.tail.ref
        
    def display(self):
        if self.head is None:

            return False
          

        else:
            temp = self.head
            while temp:
                print(temp.data,"---->",end = "")
                temp = temp.ref
          
            return True


    def Beg_insert(self,val):
      nb = Node(val)
      nb.ref = self.head
      self.head = nb

      return True



    def push_back(self, val): 

      if self.head is None:

        return False
      ne = Node(val)
      tail = self.head   
      while tail.ref:
        tail = tail.ref

      tail.ref = ne

      return True

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



    def position_insert(self,position,val): 
      
        np = Node(val)

        counter = Singlelinkedlist.count_nodes(self)

        point = self.head
        
        

        if position < 0:
          

          return False

        if position > counter:
          
          return False

        for i in range(position-2):

          point = point.ref

        np.data = val

        np.ref = point.ref

        point.ref = np

        return True
        

    

    def delete_beg(self): 

      if self.head is None:

        return False

      else:
          temp = self.head

          self.head = temp.ref

          temp.ref = None

          return True
          

    def delete_end(self): # what happens if list is empty?

      if self.head is None:
  
        return False

      temp = self.head.ref

      tail = self.head 
      # why are we updating the tail here?
      while temp.ref is not None:

        tail = tail.ref

        temp = temp.ref

      tail.ref = None

      return True
      

    def delete_pos(self,position): # pos < 0 or pos > len(list)
    
      temp = self.head.ref

      tail = self.head
      
      counter = Singlelinkedlist.count_nodes(self)

      if position < 0:

          return False

      if position > counter:

          return False

      for i in range(position -2):

        tail = tail.ref

        temp = temp.ref

      tail.ref = temp.ref

      temp.ref = None

      return True


    def search_node(self,key): 
      
      flag = 0
      
      temp = self.head 

      if temp is None:

        flag = 0

      else:

        while temp is not None:

            if key == temp.data:

              flag +=1

              break

            temp = temp.ref

        
      return flag

          
      


    def reverse_list(self):# we need 3 pointers here

      prev = None

      current = self.head
      
      if current is None:

        return False

      else:

        while current is not None:

            temp = current.ref 
          #changibg the direcxtion of teh nodes
            current.ref = prev
          #shifting the nodes
            prev = current

            current = temp

            self.head = prev

            return True

L = Singlelinkedlist()


print("\nwhat would you like to do?")

while(True):
  print("\n1---> Create linked List")
  print("2---> Count the number of Nodes in a list")
  print("3---> Display the updated linked_list")
  print("4---> Insert a Node at the beginning")
  print("5---> Insert a Node at the end")
  print("6---> Insert a Node at a particular position")
  print("7---> Delete a Node at the begining")
  print("8---> Delete a node at the end")
  print("9---> Delete a node at a particular position")
  print("10---> Search for a key value in the list")
  print("11---> Reverse the linkedlist")
  print("12---> exit")

  ch = int(input("Enter your choice:"))

  if ch == 1:

    n = int(input("Enter the number of entries:"))

    for i in range (0,n):

      val = int(input("Enter your value:"))

      L.add_nodes(val)

      print("Number Entered Succesfully")

      
  
  elif ch == 2:

    print("The number of nodes in the list are",L.count_nodes())


  elif ch == 3:

    status =L.display()
    
    if status is True:

      print("!!!!====>The list is displayed")
    else:

      print("oops couldnt fetch that")

    

  elif ch == 4:

    x =int(input("Enter the value you wana enter:"))

    result =L.Beg_insert(x)

    print("List has been updated")

    if result is True:

          print("Number is inserted")

    else:
          print("OOps could not fetch request")

  elif ch == 5:

    x =int(input("Enter the value you wana enter:"))

    a =L.push_back(x)

    

    if a is True:

      print("List has been updated")

    else:

      print("List has not been created yet , please create one and come back")

  elif ch == 6:

    a =int(input("Enter your desired position:"))

    b =int(input("Enter the value you wana enter:"))

    a =L.position_insert(a,b)

    if a is True:

      print("List has been updated")

    else:

      print("Oops couldnt complete the request")



  elif ch == 7:

    a = L.delete_beg()

    if a is True:

      print("List has been updated")

    else:

      print("Oops couldnt complete the request")

  elif ch ==8:

    a = L.delete_end()

    if a is True:

      print("List has been updated")

    else:

      print("Oops couldnt complete the request")

  elif ch == 9:
    a =int(input("Enter your desired position:"))

    b = L.delete_pos(a)

    if b is True:

      print("List has been updated")

    else:

      print("Oops couldnt complete the request")


  elif ch == 10:

    a =int( input("Enter the key element:" ) )

    b = L.search_node(a)

    if b  == 0:

      print("The element has not been found")

    else:

      print("The element was found")

  elif ch == 11:

    a =L.reverse_list()

    if a is True:

      print("List has been reversed")

    else:

      print("Oops couldnt complete the request")


  elif ch == 12:

    break

  else:

    print("Invalid choice")
