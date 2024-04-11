# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        arr = self.kthHelper(root, arr)
        return arr[k-1]
    
    def kthHelper(self, root: Optional[TreeNode], arr: List[int]) -> List[int]:
        if not root:
            return arr
        
        self.kthHelper(root.left, arr)
        arr.append(root.val)
        self.kthHelper(root.right, arr)

        return arr
        