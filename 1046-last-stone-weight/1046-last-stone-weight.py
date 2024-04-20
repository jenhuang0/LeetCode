class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        heapq.heapify(max_heap)

        for stone in stones:
            heapq.heappush(max_heap, -stone)
        print(max_heap)
        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            push_back = x-y
            heapq.heappush(max_heap, push_back)
        if max_heap:
            ans = heapq.heappop(max_heap)
            return -ans
        else:
            return None