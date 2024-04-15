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
            return ""
        res = []
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("#")
        print(res)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        q = [root]
        i = 1
        while q:
            node = q.pop(0)
            if values[i] != "#":
                left = TreeNode(int(values[i]))
                node.left = left
                q.append(left)
            i += 1
            if values[i] != "#":
                right = TreeNode(int(values[i]))
                node.right = right
                q.append(right)
            i += 1 
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))