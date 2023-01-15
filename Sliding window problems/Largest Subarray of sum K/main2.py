def largest_subarray(data, k):
    max_length = float('-inf')
    current_sum = 0
    start = 0
    s = len(data)
    for i in range(s):
        current_sum += data[i]
        while current_sum > k:
            current_sum -= data[start]
            start += 1
        if current_sum == k:
            max_length = max(max_length, i - start + 1)
    return max_length

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 15
print(largest_subarray(data, k))