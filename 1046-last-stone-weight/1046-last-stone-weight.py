class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #we can use heapify and reverse it so the max will be the tree on top
        max_heap = []
        heapq.heapify(max_heap)
        
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            new_num = x - y

            if new_num != 0:
                heapq.heappush(max_heap, new_num)

        return -heapq.heappop(max_heap) if max_heap else 0