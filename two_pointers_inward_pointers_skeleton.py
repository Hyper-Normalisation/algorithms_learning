# Inward two pointers
left, right = 0, len(arr) - 1

while left < right:
    total = arr[left] + arr[right]
    if total == target:
        return [left, right]
    elif total < target:
        left += 1
    else:
        right -= 1

