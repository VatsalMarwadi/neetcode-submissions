class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        maxTime = 0
        fleets = 0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > maxTime:
                fleets += 1
                maxTime = time
        return fleets