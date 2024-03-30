class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashset = {}
        
        for i in nums:
            if i not in hashset:
                hashset[i] = hashset.get(i, 0)+1
            else:
                return i