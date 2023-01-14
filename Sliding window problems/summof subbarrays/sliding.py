
n = [3,5,66,2,-5,-7,-4,100,-33]

k =3  #window size

def  max_subarray(n,k):


    s = len(n)
    max_sum = 0
    win_sum = 0

    for i in range(s):
        if i <k:
            win_sum = win_sum + n[i]
            max_sum = win_sum

        else:
            win_sum = win_sum - n[i-k] + n[i]
            max_sum = max(max_sum,win_sum)

    return max_sum

print(max_subarray(n,3))






