# LeetCode 876: Middle of the Linked List
# Given the head of a singly linked list,
# return the middle node. If there are two, return the second middle.

def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

