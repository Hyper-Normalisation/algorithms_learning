# Givenbinary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# -----------------------------------------------------------------------

def longestOnes(nums, k):
    left = 0 # Intializing the left boundary of the sliding window pattern.
    zeros = 0 # Tracks the number of 0's that are in the current window.
    max_len = 0 # Tracks the length of the longest valid window so far.
 
    for right in range(len(nums)): # This is a for loop that is starting the right pointer of the window and moving it over the range of the array.
        if nums[right] == 0: # While the for loop is happening, a if statement is used to check the right pointer location int is equal to zero.
            zeros += 1 # If it is equal to zero in the if statement, then we subtract 1 from zeros total.

        while zeros > k: # This is a while lop inside the for loop that is checking to see if zeros is greater than k value that is given in the function.\
                if nums[left] == 0: #if the nums left pointer is equal to zero than we subtract zeros with a 1.
                    zeros -= 1
                left += 1 # We continue to mvoe the left pointer.


        max_len = max(max_len, right - left + 1) # We then calculate the max_len of the consecutive 1's via figuring out the index of the max_len.

    return max_len # return max length to the function.



