# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n==1 and head.next == None:
            return head.next
        else:
            n-=1
            prev = None
            curr = head
            last = head
            while n and last:
                last = last.next
                n-=1
            while last.next:
                prev = curr
                curr = curr.next
                last= last.next
            if prev:
                prev.next = curr.next
                return head
            else:
                return curr.next

        