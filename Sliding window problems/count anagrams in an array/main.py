#here ideal condition
#anahram length = size of window

def anagram_count(n , k, ana):

    s = len(n)

    anagram_count = 0

    for i in range(s -k +1):

        window = n[i:i+k]

        if sorted(window) == sorted(ana):
            anagram_count+=1

    return anagram_count

n = "asdafvasdasdasdasdadas"
k = 3
ana = "das"

print(anagram_count(n,k,ana))

