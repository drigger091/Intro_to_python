nums =[]
#number of elemnts in a list
n = int(input("number of elements:"))
for i in range(0,n):
    add = int(input())
    nums.append(add)
print(nums)

#selection sort is based on finding the min value
#time complexity is 0(n^2)

def sort(nums):
    for i in range(0,len(nums)-1):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j]> nums[minpos]:
                minpos = j


        temp = nums[i]
        nums[i]= nums[minpos]
        nums[minpos]= temp

        print(nums)
        print(nums[::-1])

sort(nums)