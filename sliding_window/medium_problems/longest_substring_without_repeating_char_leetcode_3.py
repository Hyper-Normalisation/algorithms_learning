# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

#-----------------------------------------------------------------------------------------

# Key Pattern:
# Variable-size sliding window
# Use a set to track characters in the current window
# When a duplicate is found, shrink window from the left until valid again

#----------------------------------------------------------------------------------------

def lengthOfLongestSubstring(s): # This is setting up the function and pushing the string "s" through it.
    seen = set() #This is using the variable called "seen" as a set() which is smart as it can only hold unique characters being that data structure.
    left = 0 #This is setting the left pointer to 0.
    max_len = 0 # This is gonna be tracking the max_len which is gonna be starting at 0.

    for right in range(len(s)): #This is a for loop that is starting the right pointer and moving it through the string.
        while s[right] in seen: #If duplicates are found, shrink window freom the left until valid.
            seen.remove(s[left]) #Remove left-character.
            left += 1
        seen.add(s[right]) # Add current character to the window.
        max_len = max(max_len, right - left + 1) # Updating max window length.

    return max_len # returning that max_len to the function.









