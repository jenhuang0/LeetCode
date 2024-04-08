# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = [0]
        def dfs(node, max_val):
            if not node:
                return 0
            #check if the curr code is a good node
            if node.val >= max_val:
                good[0]+=1
            
            #update the max_val
            max_val = max(node.val, max_val)

            # recur traverse the left and right subtrees
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        dfs(root, root.val)
        return good[0]
            
            
        