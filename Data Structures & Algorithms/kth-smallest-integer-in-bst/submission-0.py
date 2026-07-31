# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self,node):
        print(node)
        if (node==None):
            return
        else:
            self.traverse(node.left)
            if (self.count==k-1):
                self.answer = node.val
            self.count+=1
            self.traverse(node.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.answer = None
        self.k = k
        self.traverse(root)
        return self.answer