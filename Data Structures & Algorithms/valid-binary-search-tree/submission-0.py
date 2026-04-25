# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxVal = float("-inf")
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root:
            isValid = True
            isValid = self.isValidBST(root.left)
            if not isValid:
                return False
            if self.maxVal < root.val:
                self.maxVal = max(self.maxVal, root.val)
            else:
                return False
            isValid = self.isValidBST(root.right)
            return isValid
        else:
            return True