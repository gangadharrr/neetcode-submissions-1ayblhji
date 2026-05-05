"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        newList = Node(head.val)
        curr = head
        newCurr = newList
        ref_map = {id(curr): newCurr}
        while curr.next:
            newCurr.next = Node(curr.next.val)
            newCurr = newCurr.next
            curr = curr.next
            ref_map[id(curr)] = newCurr

        curr = head
        newCurr = newList
        while curr:
            newCurr.random = ref_map.get(id(curr.random), None)
            curr = curr.next
            newCurr = newCurr.next
        return newList
        