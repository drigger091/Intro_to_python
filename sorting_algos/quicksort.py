# a pivot is used for sorting
#recursion included
def quicksort(list):
    length = len(list)
    if length <= 1:
        return list

    else:
        pivot = list.pop()

    items_greater = []
    items_lower = []

    for i in list:
        if i > pivot:
            items_greater.append(i)
        else:
            items_lower.append(i)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)


list1 = []

n = int(input("number of elements:"))
for i in range(0,n):
    add = int(input())
    list1.append(add)

print(quicksort(list1))