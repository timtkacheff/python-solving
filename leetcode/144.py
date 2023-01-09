from typing import Optional, List


# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def traverse(node):
            if not node:
                return

            answer.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return answer


