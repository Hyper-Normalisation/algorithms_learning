# Fixed-size sliding window
window_sum = sum(arr[:k])

for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i-k]
    # process window here

