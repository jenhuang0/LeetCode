class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = [ -f for f in freq.values()]
        heapq.heapify(maxHeap)

        q = deque() #pairs of [-f, idletime]
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                f = 1 + heapq.heappop(maxHeap)
                if f != 0:
                    q.append([f, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
