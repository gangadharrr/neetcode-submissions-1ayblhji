# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        while curr.next and curr.next.next:
            last = curr
            while last.next and last.next.next:
                last = last.next
            if last == curr:
                break
            next_curr = curr.next
            last.next.next = curr.next
            curr.next = last.next
            last.next = None
            curr = next_curr