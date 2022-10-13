
nums =[]
#number of elemnts in a list
n = int(input("number of elements:"))
for i in range(0,n):
    add = int(input())
    nums.append(add)
print(nums)


def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1] = temp
    print(nums)


sort(nums)
#time compelxity 0(n)
 


