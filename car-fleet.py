class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = {}
        for i in range(len(position)):
            cars[position[i]] = speed[i]
        cars = sorted(cars.items(), reverse = True)
        stack = []
        for pair in cars:
            stack.append((target-pair[0])/pair[1])
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)
