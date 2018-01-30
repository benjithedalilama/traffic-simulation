from random import random
from copy import deepcopy

class TrafficSimulation():
    def __init__(self, road_length, traffic_density, v_max, p, start_state = []):
        self.road_length = road_length
        self.traffic_density = traffic_density
        self.v_max = v_max
        self.p = p
        if not start_state:
            self.state = []
            for i in range(road_length):
                if random() < traffic_density:
                    self.state.append(v_max//2)
                else:
                    self.state.append(-1)
        else:
            self.state = start_state


    def step(self):
        length = self.road_length
        speeds = deepcopy(self.state)
        for index, speed in enumerate(self.state):
            if speed < 0:
                continue

            # count spaces in front
            j = 1
            while self.state[(index + j)%length] < 0:
                j += 1

            # accelerate, or slow down due to cars
            if speed < self.v_max and (j > speed + 1 or self.state[(index+j)%length] < 0):
                speeds[index] += 1
            elif j <= speed:
                speeds[index] = j - 1

            # random slow down
            if speeds[index] > 0 and random() < self.p:
                speeds[index] -= 1

        # update the positions
        updated_state = [-1]*length
        for index, speed in enumerate(speeds):
            if speed < 0:
                continue
            updated_state[(index + speed)%length] = speed

        # peer into the future to slow down, but dont change position
        for index, speed in enumerate(updated_state):
            if speed < 0:
                continue
            j = 1
            while updated_state[(index + j)%length] < 0:
                j += 1
            if j <= speed:
                updated_state[index] = j - 1

        # iterate the state, and please stop the hate
        self.state = updated_state

    def display(self):
        print(''.join('.' if x == -1 else str(x) for x in self.state))
