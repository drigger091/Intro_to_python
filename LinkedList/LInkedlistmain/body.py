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
      
      counter = self.count_nodes(self)

      if position < 0:

          return [False,"Linked_list not created"]

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


def Initialize ():

    L = Singlelinkedlist()

    return L