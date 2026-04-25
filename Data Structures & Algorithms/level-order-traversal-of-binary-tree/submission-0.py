# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        out=[]
        queue = [root]
        next_queue = []
        inner_out = []
        while queue or next_queue:
            node = queue.pop(0)
            inner_out.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
            if len(queue) == 0:
                out.append(inner_out)
                inner_out = []
                queue = next_queue
                next_queue = []
        return out

        