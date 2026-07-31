# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0
    def helper(self,root, minVal):
        if root is None:
            return
        if root.val>=minVal:
            self.ans+=1
        self.helper(root.left, max(minVal, root.val))
        self.helper(root.right, max(minVal, root.val))
    def goodNodes(self, root: TreeNode) -> int:
        self.helper(root, float('-inf'))
        return self.ans