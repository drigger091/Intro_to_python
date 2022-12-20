#merge sort is recursive and it breaks teh data sets into halfs
#time compelxcity O(n log n)
#it does n work for each step









list1 =[]

#number of elemnts in a list
n = int(input("number of elements:"))
for i in range(0,n):
    add = int(input())
    list1.append(add)
print(list1)

list2 =[]

#number of elemnts in a list
n = int(input("number of elements:"))
for i in range(0,n):
    add = int(input())
    list2.append(add)
print(list2)



class arraymerger:
    
    def __init__(self,list1,list2):
        self.list1 = list1
        self.list2 = list2
    
    def merge(self):
        x=[]
        i=0
        j=0

        while (i<len(list1) and j< len(list2)):
            if(list1[i]<list2[j]):
                x.append(list1[i])
                i= i+1
            elif(list1[i]>list2[j]):
                x.append(list2[j])
                j= j+1
            else:
                x.append(list1[i])
                x.append(list2[j])
                j = j+1
                i = i=1
        print(len(x))
        return x

ob = arraymerger(list1,list2)


print(ob.merge())
