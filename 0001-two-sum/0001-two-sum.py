class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numdict = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff not in numdict:
                numdict[v] = i
            else:
                return (i, numdict[diff])