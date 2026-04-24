# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subRoot):
            out = True
            queue = [root]
            sub_queue = [subRoot]
            while sub_queue:
                node = queue.pop(0)
                sub_node = sub_queue.pop(0)
                if not((sub_node and node and sub_node.val == node.val) or (sub_node == node)):
                    return False
                if sub_node:
                    sub_queue.append(sub_node.left)
                    sub_queue.append(sub_node.right)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
            return True
        queue = [root]
        sub_queue = [subRoot]
        while queue:
            node = queue.pop(0)
            if node:
                if node.val == subRoot.val:
                    out = sameTree(node, subRoot)
                    if out:
                        return True
                queue.append(node.left)
                queue.append(node.right)
        return False