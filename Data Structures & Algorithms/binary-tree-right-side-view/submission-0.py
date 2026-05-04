# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        out = [root.val]
        queue = [root]
        next_queue = []
        while queue or next_queue:
            node = queue.pop(0)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
            if len(queue) ==0:
                if next_queue:
                    out.append(next_queue[-1].val)
                queue = next_queue
                next_queue = []
        return out

        