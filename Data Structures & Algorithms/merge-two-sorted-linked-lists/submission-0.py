# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        curr=newList
        c1, c2 = list1, list2
        while c1 or c2:
            if c1 and c2:
                if c1.val < c2.val:
                    curr.next = ListNode(c1.val)
                    curr = curr.next
                    c1 = c1.next
                else:
                    curr.next = ListNode(c2.val)
                    curr = curr.next
                    c2 = c2.next
            else :
                if c1:
                    curr.next = ListNode(c1.val)
                    curr = curr.next
                    c1 = c1.next
                else:
                    curr.next = ListNode(c2.val)
                    curr = curr.next
                    c2 = c2.next
        return newList.next
        