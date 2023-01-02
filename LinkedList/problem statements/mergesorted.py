
class Node:

  def __init__( self,data):
    self.data = data
    self.ref = None

class Linkedlist:
  
    def __init__(self):
      self.head = None


    def display(self):

      temp  = self.head

      while temp:
        print(temp.data,"------>",end = "")
        temp = temp.ref

    def append(self,val):#adding at the end of lists
      new_node = Node(val)
      if self.head is None:
        self.head = new_node
        return
      tail = self.head

      while tail.ref:
        tail = tail.ref
      tail.ref = new_node


def mergeList(head1,head2):

  temp = None

  if head1 is None:#if list1 is empty we start returning list2
    return head2

  if head2 is None: #other wise
    return head1


  if head1.data <= head2.data:
      temp = head1

      temp.ref = mergelist(head1.ref , head2)

  else:
     temp = head2

     temp.ref = mergelist(head1 , head2.ref)


  return temp




l1 = Linkedlist()
l1.append(1)
l1.append(3)
l1.append(16)



l2 = Linkedlist()
l2.append(2)
l2.append(4)
l2.append(5)
l2.append(15)


L3 = Linkedlist()


L3.head = mergelist(l1.head,l2.head)
print("the sorted list is")
L3.display()
