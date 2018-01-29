from random import random
import numpy as np

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
        for index, speed in enumerate(self.state):
            if speed < 0:
                continue
            # elif speed < self.v_max and self.state[(index+1)%length] < 0:
            #     self.state[index] += 1
            j = 1
            while self.state[(index + j)%length] < 0 and j <= speed:
                j += 1
                self.state[index] = min(j - 1, self.v_max)
            print("At cell %d there is a car %d cells ahead with a speed of %d" % (index,j,self.state[(index+j)%length]))

    def display(self):
        print(''.join('.' if x == -1 else str(x) for x in self.state))

ts = TrafficSimulation(10, 0.5, 5, 0.05)
ts.display()
ts.step()
