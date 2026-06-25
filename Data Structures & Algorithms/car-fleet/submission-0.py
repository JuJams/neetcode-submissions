class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        # car pairs
        cars = []
        for i in range(n):
            cars.append([position[i],speed[i]])
        print(cars)

        # sort by decreasing
        cars.sort(key = lambda x: x[0], reverse = True)
        print (cars)

        fleets = 0
        slowest_time = 0

        for pos,spd in cars:
            time = (target - pos)/spd
            # print(time)

            if time > slowest_time:
                fleets += 1
                slowest_time = time
        return fleets

