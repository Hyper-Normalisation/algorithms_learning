# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

#------------------------------------------------------------------------------

def minSubArrayLen(target, nums): #This is the beginning of the function setting the values that will be pushed through it.
    left = 0 # This is setting the left pointer side of the sliding window as the variable to 0 
    total = 0 # This is setting the total of the window sum to 0.
    min_len = float('inf') # We intitalize this variable to infinity so we can minimize it during the loop. If no valid subarray is found, this helps us detect that case.

    for right in range(len(nums)): # We iterate over the array with the right pointer to expand the window size.
        total += nums[right] # Add the current number to the total, this expands the widow to the right
        while total >= target: # This is a while loop inside the for loops that is making the variable window move and adjust while the total is greater than or equal to the target.
            # What the while loop is doing is basically checking that every time a new number from the array enters the window and if it is less than the window continues to move, its
            # checking basically how small can the window get while mainintaing the total is greater than or equal to the target as the question asks.
            min_len = min(min_len, right - left + 1) # then we are assigning min_len to the index location and size of the array with that target.
            total -= nums[left] # We are moving the total left poiinter 
            left += 1 # moving the left pointer in the window.
 
    return 0 if min_len == float('inf') else min_len # If min_len was never updated (still inifinity), return zero - meaning no valid subarray was found. otherwise, return the smallest,
# valid length.









