class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largenum = []
        heapq.heapify(largenum)

        for num in nums:
            heapq.heappush(largenum, -num)
        
        while k > 0:
            ans = heapq.heappop(largenum)
            k -= 1
        return -ans