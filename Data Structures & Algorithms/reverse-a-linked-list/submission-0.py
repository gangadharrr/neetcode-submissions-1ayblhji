class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        outCurr = None
        while curr:
            print(curr.val)
            node = ListNode(curr.val)
            node.next = outCurr
            outCurr = node
            curr = curr.next
        return outCurr