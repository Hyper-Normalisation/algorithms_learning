# Partition with two pointers
left, right = 0, len(arr) - 1

while left <= right:
    if condition_on_left:
        left += 1
    elif condition_on_right:
        right -= 1
    else:
        arr[left], arr[right] = arr[right], arr[left]

