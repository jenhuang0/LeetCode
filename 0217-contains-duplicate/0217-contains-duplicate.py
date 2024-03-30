class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numdict = {}
        for i in nums:
            if i not in numdict:
                numdict[i] = numdict.get(i, 0 )+1
            else:
                return True
        return False