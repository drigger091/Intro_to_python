class Node:

  def __init__(self,data):
    self.data = data
    self.ref = None # address of next node

class linkedlist:

  def __init__(self):
    self.head = None
    self.tail = None

  def display(self):
    if self.head is None:
      print("linked list is empty")
    else:
      temp = self.head
      while temp:
        print(temp.data ,"----->",end ="")
        temp = temp.ref

  def push(self,val):

    new_node = Node(val)
    new_node.ref = self.head
    self.head = new_node

    


  def pop(self):

    if self.head is None:
      print("The Stack is Empty")

    else:
        temp = self.head
        self.head = temp.ref
        temp.ref = None
        print("\nThe last elememt is cleared")


  def isempty(self):
      if self.head is None:
        return True

      else:
        return False

  def delete(self):

    temp = self.head

    while temp:
      next = temp.ref #moving to next node

      del temp.data #deleting current node

      temp = next



#create a stack
L = linkedlist()

n = int(input("Enter the number of Entries:"))

for i in range(0,n):
  val = int(input("\nEnter the values:"))
  L.push(val)
L.display()
print("This is the stack:")

L.pop()
L.display()



