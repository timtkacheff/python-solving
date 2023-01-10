from typing import Optional


# Given the roots of two binary trees p and q,
# write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical,
# and the nodes have the same value.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val == q.val:
            return True

        return self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.right)
            
