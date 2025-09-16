# Monotonic deque sliding window
from collections import deque
dq = deque()

for i in range(len(arr)):
    if dq and dq[0] <= i - k:
        dq.popleft()

    while dq and arr[dq[-1]] < arr[i]:
        dq.pop()

    dq.append(i)

    if i >= k - 1:
        # front of deque = max in window
        result.append(arr[dq[0]])

