# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def helper(self,node, subRoot):
        if node is None and subRoot is None:
            return True
        if node is not None and subRoot is not None:
            if (node.val!=subRoot.val):
                return False
            else:
                return self.helper(node.left,subRoot.left) and self.helper(node.right,subRoot.right)
        return False
    def check(self,node,subRoot):
        if node is None:
            return False
        if (self.helper(node,subRoot)):
            return True
        return self.check(node.left,subRoot) or self.check(node.right,subRoot)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.check(root,subRoot)
        