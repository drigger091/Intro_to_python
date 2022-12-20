nums =[]
#number of elemnts in a list
n = int(input("number of elements:"))
for i in range(0,n):
    add = int(input())
    nums.append(add)
print(nums)


def sort(nums):
    for i in range(1,len(nums)): # as it begins counting from the second item inthe list and the first item is alredy in the sorted list if divided
        for j in(i-1,0,-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]= nums[j+1],nums[j]
            else:
                break
    print(nums)


sort(nums)

# time compexity O(n2)



