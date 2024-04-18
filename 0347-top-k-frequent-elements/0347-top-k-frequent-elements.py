class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNum = {}

        for num in nums:
            countNum[num] = countNum.get(num, 0) + 1

        sort_count = dict(sorted(countNum.items(), key=lambda x: x[1], reverse= True))
        ans = list(sort_count.keys())[:k]
        return ans