# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, leftB, rightB):

            if not node:
                return True
            if not (leftB <node.val <rightB):
                return False
            
            if (valid(node.left, leftB, node.val) and valid(node.right, node.val, rightB)):
                return True
        return valid(root, float("-inf"), float("inf"))