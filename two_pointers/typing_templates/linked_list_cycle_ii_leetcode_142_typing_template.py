# LeetCode 142: Linked List Cycle II
# Given the head of a linked list,
# return the node where the cycle begins. If there is no cycle, return None.

def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow2 = head
            while slow != slow2:
                slow = slow.next
                slow2 = slow2.next
            return slow
    return None

