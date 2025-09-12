#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i])

#Find two lines that together with the x-axis form a container, such that the container contains the most water.

#Return the maximum amount of water a container can store.

#Notice that you may not slant the container.

#Input: height = [1,8,6,2,5,4,8,3,7]
#Output: 49
#Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
#Example 2:

#Input: height = [1,1]
#Output: 1
#----------------------------------------------------------------------------------------------------

#Key Insights:
- Area = width * min(height[left], height[right])
- Use two pointer (left, right)
- Always move the pointer at the shorter height, because moving the taller one cannot increase area.

#------------------------------------------------------------------------------------------------------



def maxArea(height): # We are given an array of integers that is representing the heights of the containers.
    left, right = 0, len(height) - 1   #We define the left and right pointers, which the pointers are starting on opposite sides of the array "height".
    max_area = 0 # We are defining the max_area as this is what we are gonna be returning as its the answer to the question.

    while left < right: # This is a while loop that is gonna be checking while left is less than the right.
        width = right - left # This is defining the width variable and checking for the total width of the size of the container.
        curr_area = min(height[left], height[right]) * width #We are not calculating the surface area of the container, by finding the min between both pointers and then multiplying it by width we just calculated.
        max_area = max(max_area, curr_area) # We are now trying to calculate max_area based on pointer location and calculating of curr_aream size.


        if height[left] < height[right]: # We are now doing a if statement inside the while loop checking if the height of the left pointer is less than the
            # right pointer we are gonna continue to increase left pointer and move it.
            left += 1
        else: # Same with right pointer, subtract it and move it by 1.
            right -=1 

    return max_area # returning max_area.
























