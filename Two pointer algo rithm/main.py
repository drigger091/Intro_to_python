#here we are using two pointer algorithm to find the
#pair of numbers to render the sum

def find_pair(n,k):

    n.sort() #sorting is mandatory
    s = len(n)
    left = 0
    right = s-1

    pairs = []

    while left < right:

        if n[left] + n[right] == k:

            pairs.append((n[left],n[right])) # we are fetching a tuple inside a list

            left+=1

            right-=1

        elif n[left] + n[right] < k:

            left+=1

        else:

            right-=1
        
    return pairs


n = [1,2,3,7,8,5,6,9,10]
k = 15

print("The pair is:",find_pair(n,k))