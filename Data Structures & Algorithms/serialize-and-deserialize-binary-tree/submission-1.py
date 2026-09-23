# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serializeHelper(self,root):
        if (root is None):
            self.encoding.append("N")
            return
        self.encoding.append(str(root.val))
        self.serializeHelper(root.left)
        self.serializeHelper(root.right)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.encoding = []
        self.serializeHelper(root)
        return ",".join(self.encoding)
        

    def deserializeHelper(self,data):
        if (data[self.nodeIndex]=="N"):
            self.nodeIndex+=1
            return None
        currentNode = TreeNode(data[self.nodeIndex])
        self.nodeIndex+=1
        currentNode.left = self.deserializeHelper(data)
        currentNode.right = self.deserializeHelper(data)

        return currentNode

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.nodeIndex = 0
        return self.deserializeHelper(data.split(","))
         
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))