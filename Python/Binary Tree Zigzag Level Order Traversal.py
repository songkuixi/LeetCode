from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]
        odd = True
        while len(queue) > 0:
            temp = []
            n = len(queue)
            for i in range(n):
                node = queue[0]
                temp.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                queue = queue[1:]
            res.append(temp if odd else temp[::-1])
            odd = not odd
        return res
