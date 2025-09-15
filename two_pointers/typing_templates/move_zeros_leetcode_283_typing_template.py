# LeetCode 283: Move Zeroes
# Given an integer array nums, move all 0's to the end
# while maintaining the relative order of the non-zero elements.

def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

