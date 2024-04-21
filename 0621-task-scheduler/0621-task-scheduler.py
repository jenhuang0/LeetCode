class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # have a max heap and a queue
        # the max heap will start as the frequency of eahc task 
        # and then will be popped from the heap and pushed to the queue
        
        # the queue will have the frequency left and the time it can be inserted again which is the current len (time) + n
        
        # since there is no max heap in python
        # we will use a min heap and negative it's values
        
        frequencies = Counter(tasks).values()
        
        maxheap = []
        heapq.heapify(maxheap)
        
        for freq in frequencies:
            heapq.heappush(maxheap, freq * -1)

        ans = 0
        q = deque()
        
        while maxheap or q:
            
            if q and q[0][0] == ans:
                heapq.heappush(maxheap, q[0][1])
                q.popleft()
            
            if maxheap:
                current_task = heapq.heappop(maxheap)
            
            current_task += 1
            ans += 1
            
            if current_task < 0:
                q.append((ans+n, current_task))
                
        return ans
        