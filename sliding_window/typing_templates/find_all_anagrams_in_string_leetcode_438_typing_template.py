# LeetCode 438: Find All Anagrams in a String
# Given two strings s and p, return all start indices of p's anagrams in s.
# You may return the answer in any order.

from collections import Counter

def findAnagrams(s, p):
    res = []
    if len(p) > len(s):
        return res

    p_count = Counter(p)
    s_count = Counter(s[:len(p)])

    if s_count == p_count:
        res.append(0)

    for i in range(len(p), len(s)):
        s_count[s[i]] = s_count.get(s[i], 0) + 1
        s_count[s[i - len(p)]] -= 1

        if s_count[s[i - len(p)]] == 0:
            del s_count[s[i - len(p)]]

        if s_count == p_count:
            res.append(i - len(p) + 1)

    return res

