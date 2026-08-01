# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        curLevel = deque()
        curLevel.append(root)
        nextLevel = deque()
        answer = []
        while len(curLevel)>0:
            cur = []
            for n in curLevel:
                cur.append(n.val)
            answer.append(cur)
            while len(curLevel)>0:
                element = curLevel.popleft()
                if element.left is not None:
                    nextLevel.append(element.left)
                if element.right is not None:
                    nextLevel.append(element.right)
            curLevel = nextLevel
            nextLevel = deque()
        return answer
                