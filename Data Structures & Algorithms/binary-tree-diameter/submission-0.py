# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def dfs(root):
            nonlocal max_len
            if root:
                l = dfs(root.left)
                r = dfs(root.right)
                max_len = max(max_len, l+r)
                return 1 + max(l, r)
            else:
                return 0
        dfs(root)
        return max_len