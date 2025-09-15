# LeetCode 11: Container With Most Water
# Given an integer array height,
# find two lines that together with the x-axis form a container
# that can hold the most water.

def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

