# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k time.# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


#-------------------------------------------------------------------------------

# Key Pattern:
# Variable-size sliding window
# A frequency map to track character counts in the current window
# At any point, the window is valid if:
  #(window_size - count_of_most_frequent_char) <= k

#--------------------------------------------------------------------------------

def characterReplacement(s, k): # In this function we have a string, represented by s and a integer k.
    left = 0 # This is starting the left pointer at zero.
    max_freq = 0 # This is going to be counting the maximum frequency that is gonna be counted, and its set to 0 to begin with.
    count = defaultdict(int) # This is gonna be continually keeping count of letters that can be changed for the max_len.
    max_len = 0 # This is checking for max_len of the substring that was changed.

    for right in range(len(s)): #This is a for loop starting the right pointer.
        count[s[right]] += 1 #Every time the right pointer is moved in the for loop, the count is added to +1.
        max_freq = max(max_freq, count[s[right]]) #The max_freq is also updated and changed.

        while (right - left + 1) - max_freq > k: # This is a while loop inside the for loop showing that this is a variable sliding window pattern. This is saying that while indexed location count subtract max_freq is greater than k integers changed, we can continue the loop.
            count[s[left]] -= 1  # This is a count left and subtracting while the loop is still in condition.
            left += 1 # This is the left pointer moving.


        max_len = max(max_len, right - left + 1) # This is reassigning and caclulating the max_len

    return max_len











