
#queue implemnetation using linked list

class Node:

  def __init__(self,data):
    self.data = data
    self.ref = None # address of next node

class Queue:

  def __init__(self):
    self.head = None
    self.tail = None


  def display(self):
    if self.head is None:
      print("Queue is empty")
    else:
      temp = self.head
      while temp:
        print(temp.data ,"----->",end ="")
        temp = temp.ref

  def Enqueue(self,val):
      if self.tail is None:
        print("Queue is empty, start putting letters")
        self.head = self.tail = Node(val)

      else:

        self.tail.ref = Node (val)
        self.tail = self.tail.ref
  
  def Dequeue(self):
     if self.head is None:
       return "Queue is Empty"
     else:
       temp = self.head.ref
       self.head = self.head.ref
       return temp

  def isEmpty(self):
     
      if self.head is None:
        return True

      else:
        return False

  def Size(self):
    count = 0
    temp = self.head

    if self.head is None:
      print("There is no queue yet, please make one")

    else:


      while(temp):
        count +=1

        temp = temp.ref
    return count

  def show_front(self):

    return self.head.data

  def show_last(self):

    return self.tail.data



print("============== Welcome to Queue testing==================")
print("what wil you like to do?")
L = Queue()
while(True):
    print("Please select from the following")
    print("1---> Enqueue")
    print("2---> Dequeue")
    print("3---> Size")
    print("4---> See the first element")
    print("5---> See the last element")
    print("6---> Exit")

    ch = int(input("choice please?"))

    if ch == 1:
        
        n = int(input("Enter the number of Entries:"))

        for i in range(0,n):
            val = int(input("\nEnter the values:"))
            L.Enqueue(val)     
        L.display()
        print("This is the Queue:")
    

    elif ch == 2:
        L.Dequeue()
        L.display()

    elif ch == 3:
         res = L.Size()

         if res == 0:

           print("There is no queue initiated")

         else:

           print("The number of values are",res)



        
        
    elif ch == 4:
        if L.Size() == 0:
          print("There is no Queue")
        else:
          print("The first element is",L.show_front())

    elif ch == 5:
        if L.Size() == 0:
          print("There is no Queue")
        else:
          print("The last element is",L.show_last())

    elif ch == 6:
      print(" See you later")
      exit()


    else:
      print("invalid choice!")
      






  
