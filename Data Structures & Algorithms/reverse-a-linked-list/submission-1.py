class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        outCurr = None
        curr = head 
        while curr:
            node = ListNode(curr.val)
            node.next = outCurr
            outCurr = node
            curr = curr.next
        return outCurr