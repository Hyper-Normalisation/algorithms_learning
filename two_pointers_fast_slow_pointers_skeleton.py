# Fast/slow pointers
slow, fast = head, head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # cycle detected

