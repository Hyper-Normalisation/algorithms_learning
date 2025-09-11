# Two Pointers Main Concepts and Pattern Notes:

What Is Two Pointers:
- A technique where two pointers are used to iterate through a data structure (usually an array, string, or linked list) from different points at the same
time -- often one from each end of one moving faster than the other.


Core Types of Two Pointers:
1. Inward Two Pointers:
	- Set Up:
		- left = 0 , right = len(arr) - 1
		- Move inward based on conditions.
	- Examples:
		- Two Sum II
		- Valid Palindrome
		- Container With Most Water

2. Fast and Slow Pointers:
	- Used when: Detecting cycles, finding midpoints in linked lists.
	- Set Up:
		- slow = head, fast = head.next
		= fast moves 2 steps, slow moves 1 step.
	- Examples:
		- Detect Cycle
		- Middle of Linked List.
		- Remove Nth Node From End.
	
3. Read + Write (Overwrite/Compress)
	- Used When: Modifying arrays in place (removing duplicates, zeroes, etc.)
	- Set Up:
		- read scans input.
		- write keeps position to overwrite.
	- Examples:
		- Remove Duplicates.
		- Move Zeroes.
		- Remove Element.

4. Walk Together:
	- Used When: Merging or comparing two arrays, strings, or lists.
	- Set Up:
		- Advance both pointer based on comparison.
	- Examples:
		 - Merge sorted arrays.
		 - Compare version numbers.
		 - String compression problems.

--------------------------------------------------------------------------------------------

Things to look for in problems to know which type of pattern to use:
- "Sorted" = use inward pointers.
- "in-place" = use overwrite technique.
- "cycle" or "middle" = use fast/slow
- "k from end" = offset pointers.
- "longest/shortest valid substring" = variable window(overlaps with sliding window).

















