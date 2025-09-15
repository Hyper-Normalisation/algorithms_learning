# LeetCode 141: Linked List Cycle
# Given the head of a linked list,
# return true if there is a cycle, otherwise false.

def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

