# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_val = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global max_val 
        def dfs(root, depth):
            if not root:
                return
            self.max_val = max(self.max_val, depth)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root,1)
        return self.max_val
                