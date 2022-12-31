

import body as bd

bd.Initialize()
def run(L):

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
