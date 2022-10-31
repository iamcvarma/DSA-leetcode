# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'N'
        return str(root.val)+','+self.serialize(root.left)+','+ self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(',')[::-1]
        def build():
            curr = arr.pop()
            if curr=='N':return None
            root = TreeNode(int(curr))
            root.left = build()
            root.right = build()
            return root
        return build()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))