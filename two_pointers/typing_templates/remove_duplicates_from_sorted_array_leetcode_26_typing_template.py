# LeetCode 26: Remove Duplicates from Sorted Array
# Given a sorted array nums, remove duplicates in-place
# so each unique element appears once. Return the count.

def removeDuplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

