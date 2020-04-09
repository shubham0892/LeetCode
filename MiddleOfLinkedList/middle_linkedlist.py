# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 1
        current = head
        while head.next != None:
            count += 1
            head = head.next
        middle = int(count / 2)
        for i in range(middle):
            current = current.next
        return current