class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        needtime = []
        for i in range(len(position)):
            needtime.append((position[i],speed[i]))
        cars = sorted(needtime)
        stack = []

        for p,s in cars[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)