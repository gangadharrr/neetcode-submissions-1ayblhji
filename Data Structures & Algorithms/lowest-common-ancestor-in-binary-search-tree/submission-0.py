# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        p,q = min(p, q, key=lambda x:x.val), max(p, q, key=lambda x:x.val)
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val > curr.val:
                return curr
            elif p.val == curr.val:
                return p
            elif q.val == curr.val:
                return q
