# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        outRoot = TreeNode(root.val)
        res_queue = [outRoot]
        queue = [root]
        while queue:
            node = queue.pop(0)
            res_node = res_queue.pop(0)
            if node.right:
                res_node.left = TreeNode(node.right.val)
                res_queue.append(res_node.left)
                queue.append(node.right)
            if node.left:
                res_node.right = TreeNode(node.left.val)
                res_queue.append(res_node.right)
                queue.append(node.left)
        return outRoot