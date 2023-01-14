n = [1,4,-555,2,3,4,-68,-7,8,10]


def max_subarray(n):

    max_sum = 0
    for i in range(len(n)):

        cuurent_sum = 0

        for j in range(i, len(n)):

            cuurent_sum = cuurent_sum + n[j]

            max_sum = max(max_sum,cuurent_sum)

    return max_sum

print ("The max__sum is",max_subarray(n))



