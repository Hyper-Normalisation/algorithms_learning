# LeetCode 424: Longest Repeating Character Replacement
# Given a string s and an integer k,
# return the length of the longest substring that can be obtained
# by replacing at most k characters so that all characters are the same.

def characterReplacement(s, k):
    count = {}
    left = 0
    max_count = 0
    max_len = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])

        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

