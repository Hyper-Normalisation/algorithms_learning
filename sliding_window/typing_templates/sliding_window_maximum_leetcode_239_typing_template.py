# LeetCode 239: Sliding Window Maximum
# You are given an array nums and an integer k.
# There is a sliding window of size k moving from left to right.
# Return the maximum value in each window.

from collections import deque

def maxSlidingWindow(nums, k):
    q = deque()
    res = []

    for i in range(len(nums)):
        while q and q[0] <= i - k:
            q.popleft()

        while q and nums[q[-1]] <= nums[i]:
            q.pop()

        q.append(i)

        if i >= k - 1:
            res.append(nums[q[0]])

    return res

