# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self,root):
        if root is None:
            return None, None
        left, leftAns = self.helper(root.left)
        right, rightAns = self.helper(root.right)
        if left is not None and right is not None:            
            return max(max(left, right),0)+root.val, max(max(leftAns, rightAns),max(left,0)+root.val+max(right,0)) 
        elif left is None and right is not None:
            return max(right,0)+root.val, max(rightAns, root.val+max(right,0))
        elif left is not None and right is None:
            return max(left,0)+root.val, max(leftAns, root.val+max(left,0))
        else:
            return root.val, root.val
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _, ans = self.helper(root)
        return ans