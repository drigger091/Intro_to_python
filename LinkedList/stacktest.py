
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
      print("stack is empty")
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

    if self.head is None:
        print("There is no stack to delete!")

    else:

        temp = self.head

        while temp:
            next = temp.ref #moving to next node

            del (temp.data) #deleting current node

            temp = next

        print("deleted Stack!")


# conducting a stack operation with linkedlist
#here wer are using the beggining of the list for push and pop operations as it will happen in O(1)

print("============== Welcome to stack testing==================")
print("what wil you like to do?")
L = linkedlist()
while(True):
    print("Please select from the following")
    print("1---> push")
    print("2---> pop")
    print("3---> peek")
    print("4---> delete the list")
    print("5---> exit")

    ch = int(input("choice please?"))

    if ch == 1:
        
        n = int(input("Enter the number of Entries:"))

        for i in range(0,n):
            val = int(input("\nEnter the values:"))
            L.push(val)     
        L.display()
        print("This is the stack:")
    

    elif ch == 2:
        L.pop()
        L.display()

    elif ch == 3:
        res =L.isempty()
        if res == True:
            print("The stack is empty!")

        else :

            print("The stack is not Empty")

    



        
    elif ch == 4:
        L.delete()
        

    elif ch == 5:
        exit()

    else:
        print("inavlid choice!")


        
