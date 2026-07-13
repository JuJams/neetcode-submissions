class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # use a stack to keep track of the times
        # if the top of the stack is >= the new time then add it to the same carFleet
        # if not add a new element in the stack
        # the length of the stack is the number of fleets
        # or just use a variable to eep track of the fleets after sorting
        cars = []
        for i in range(len(speed)):
            cars.append([position[i],speed[i]])
        print (cars)

        # sort by position
        cars.sort(key = lambda x: x[0], reverse = True)
        print(cars)

        fleets = 0
        car_fleet = 0

        for pos,spd in cars:
            time = (target-pos)/spd
            if time > car_fleet:
                car_fleet = time
                fleets += 1
        return fleets
