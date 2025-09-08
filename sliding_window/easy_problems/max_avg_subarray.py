# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 
# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

# --------------------------------------------------------------------------------


def max_sum_subarray_k(nums, k):
    window_sum = sum(nums[:k]) # Intitalize the sum of the first window of size k.
    max_sum = window_sum # Track the maximum sum found so far.

    for i in range(k, len(nums)): # Slide the window from index k to the end of the array.
        window_sum += nums[i] - nums [i - k] # Add the incoming element, remove the outgoing element in the window.
        max_sum = max(max)sum, window_sum) # Update max_sum if the current window sum is greater.

    return max_sum #Return the maximum sum found among all windows.
                # If the question wants the "Maximum Average you divde the max_sum with "k" like: return max_sum / k" which will return the avg.
