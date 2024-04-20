class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        heapq.heapify(distance)
        print (distance)
        # heapq.heappush(distance, [2, [2,3]])
        # print(distance)

        for point in points:
            dis = abs(point[0]**2 + point[1]**2)
            heapq.heappush(distance,(dis, point))
        ans = []
        print(distance)
        while k > 0:
            dis, point = heapq.heappop(distance)
            ans.append(point)
            k -= 1
        return ans
        
        

