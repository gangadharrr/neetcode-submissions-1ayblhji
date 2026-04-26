# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root:
            val = self.kthSmallest(root.left,k)
            if val != None:
                return val
            if self.count == k:
                return root.val
            else:
                self.count+=1
            val = self.kthSmallest(root.right,k)
            if val != None:
                return val