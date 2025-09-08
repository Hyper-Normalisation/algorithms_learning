Sliding Window Pattern Overview:

Sliding window is an optimization technique for problems that are involvinfg contiguous sequences (subarrays, substrings) in arrays, strings, or linked lists. Instead of recalculating
values repeatedly for each new window, you slide the window over the data structure and update the state of it with ever increment.

When should we use sliding window:
- Longest/shortest subarray/substring that satisfies as constraint.
- Max/min sum of K elements.
- First/last occurence of a pattern.
- Fixed-size or variable size subranges.

Some clues in problem statements to know that we should use sliding window pattern:
- "Find the max/min/avg of all subarrays of size k"
- "Longest substring with at most k distinct characters"
- "Number of substrings with sum less than X"


Types of sliding windows:

Fixed Size Window:
- Window remains the size of "k" when window size "k" is known.
- move left and right pointers forward by 1 in lockstep.

Variable Size Window:
- Window gros or shrinks based on conditions.
- Often invovles a while-loop inside a for loop.
- Typical in substring or subarray problems with constraints.



