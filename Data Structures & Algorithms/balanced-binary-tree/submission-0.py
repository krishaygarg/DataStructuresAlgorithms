# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if root is None:
            return True, 0
        statusLeft, heightLeft = self.helper(root.left)
        statusRight, heightRight = self.helper(root.right)
        if (not (statusLeft and statusRight)):
            return False, 0
        if (abs(heightLeft-heightRight)<=1):
            return True, max(heightLeft, heightRight)+1
        return False, 0
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        status, height = self.helper(root)
        return status