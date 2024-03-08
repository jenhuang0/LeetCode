class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], (target-position[i])/ speed[i]))
        cars = sorted(cars)
        print(cars)
        stack = []
        for car in cars[::-1]:
            if not stack or car[1] > stack[-1][1]:
                stack.append(car)
        print(stack)
        return len(stack)

        
