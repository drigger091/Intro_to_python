#merge sort is recursive and it breaks teh data sets into halfs
#time compelxcity O(n log n)
#it does n work for each step


def mergesort(list):
    if len(list) > 1:
    
        midpoint = len(list)//2

        left = list[:midpoint]
        right = list[midpoint:]

#recursion
        mergesort(left)
        mergesort(right)
        i = 0
        j= 0
        k =0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k]= left[i]
                i+=1
            else:
                list[k]=right[j]
                j+=1
            k+=1
    #checking and adding the rest of the elements
        while i < len(left):
            list[k] = left[i]
            i+= 1
            k+=1
        while j < len(right):
            list[k]= right[j]
            j+=1
            k+=1



list1 = []

n = int(input("number of elements:"))
for i in range(0,n):
    add = int(input())
    list1.append(add)


mergesort(list1)
print(list1)










    
