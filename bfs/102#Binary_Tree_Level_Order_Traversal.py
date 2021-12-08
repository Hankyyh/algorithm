# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        dq = deque()
        dq.append(root)
        while dq:
            size = len(dq)
            cur = []
            for i in range(size):
                pop = dq.popleft()
                cur.append(pop.val)
                if pop.left:
                    dq.append(pop.left)
                if pop.right:
                    dq.append(pop.right)
            res.append(cur)

        return res


        