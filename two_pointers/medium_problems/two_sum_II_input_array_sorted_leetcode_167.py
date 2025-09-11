# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

#Example 1:

#Input: numbers = [2,7,11,15], target = 9
#Output: [1,2]
#Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
#Example 2:

#Input: numbers = [2,3,4], target = 6
#Output: [1,3]
#Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
#Example 3:

#Input: numbers = [-1,0], target = -1
#Output: [1,2]
#Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

#--------------------------------------------------------------------------------------------

def twoSum(numbers, target): # This is the function, the question is asking us to 
    left = 0 
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1


#PsedoCode Breakdown:
# The questions is asking us to use inward two pointers as its already sorted. 
#- We are gonna define the variables left = 0, right = len(numbers) - 1 , which is starting one pointer at the end the right pointer and the left pointer at the beginning. 
#- The while loop is created and its basically checking for that if left pointer number in the array spot while the pointer is moving is less than the right, add it to the total. 
# - Then in the while loop there is an if statement that is checking if the total matches the target that the function is asking for, return the indexes of the locations for the left and right pointer. 
# - Then if not it goes into elif and else breakdowns of moiving the left and right pointers inward.











