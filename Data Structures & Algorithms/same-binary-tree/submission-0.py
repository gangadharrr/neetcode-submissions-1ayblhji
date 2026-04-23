# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not(p or q):
            return p==q
        left_queue = [p]
        right_queue = [q]
        while left_queue and right_queue:
            left_node = left_queue.pop(0)
            right_node = right_queue.pop(0)
            if not(left_node or right_node) and left_node == right_node:
                pass
            elif left_node and right_node and left_node.val == right_node.val:
                pass
            else:
                return False
            if left_node: left_queue.append(left_node.left)
            if right_node:right_queue.append(right_node.left)
            if left_node: left_queue.append(left_node.right)
            if right_node:right_queue.append(right_node.right)
        return not (left_queue or right_queue)