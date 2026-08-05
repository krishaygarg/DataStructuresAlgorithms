# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, depth):
        if node is None:
            return
        if len(self.answer)==depth:
            self.answer.append(node.val)
        self.dfs(node.right,depth+1)
        self.dfs(node.left,depth+1)
                
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []
        self.dfs(root,0)
        return self.answer
