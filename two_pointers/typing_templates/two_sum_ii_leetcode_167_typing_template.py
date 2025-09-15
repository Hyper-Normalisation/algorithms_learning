# LeetCode 167: Two Sum II - Input Array Is Sorted
# Given a sorted array numbers and an integer target,
# return indices of the two numbers such that they add up to target.

def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1

