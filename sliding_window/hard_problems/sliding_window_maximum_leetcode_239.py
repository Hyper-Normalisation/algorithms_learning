# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.
 

# Example 1:

#Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
#Output: [3,3,5,5,6,7]
#Explanation: 
#Window position                Max
#---------------               -----
#[1  3  -1] -3  5  3  6  7       3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7
#Example 2:

#Input: nums = [1], k = 1
#Output: [1]
#----------------------------------------------------------------------------

#Key Trick:

#Use a Monotonic Deque to store indexes of elements in a way that:
# - The deque is always in decreasing order of values
# - The front of the deque is always the maximum value of the current window
# - Remove from back if new number is bigger (they’ll never be max again)
# - Remove from front if it's outside the window

#----------------------------------------------------------------------------

from collections import deque

def maxSlidingWindow(nums, k):
    q = deque() 
    result = []

    for i in range(len(nums)):
        while q and nums[i] > nums[q[-1]]:
            q.pop()

        q.append(i)


        if q[0] <= i - k:
            q.popleft()

        if i >-= k - 1:
            result.append(nums[q[0]])

    return result
















































