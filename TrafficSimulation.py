from random import random
from copy import deepcopy
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
        temp_state = deepcopy(self.state)
        for index, speed in enumerate(self.state):
            if speed < 0:
                continue
            j = 1
            while self.state[(index + j)%length] < 0 and j <= speed:
                j += 1
            if speed < self.v_max and (j > speed + 1 or self.state[(index+j)%length] < 0):
                temp_state[index] += 1
            else:
                temp_state[index] = j - 1
            if temp_state[index] > 0 and random() < self.p:
                temp_state[index] -= 1
        temp_advancement_state = [-1]*length
        for index, speed in enumerate(temp_state):
            if speed < 0:
                continue
            temp_advancement_state[(index + speed)%length] = speed
        self.state = temp_advancement_state

    def display(self):
        print(''.join('.' if x == -1 else str(x) for x in self.state))

    def checkup(self, index, j, state):
        print("At cell %d with speed %d there is a car at %d with a speed of %d" % (index,state[index],(index+j)%self.road_length,state[(index+j)%self.road_length]))

ts = TrafficSimulation(100, 0.03, 5, 0.5)
ts.display()
for i in range(40):
    ts.step()
    ts.display()

print("")
ts = TrafficSimulation(100, 0.1, 5, 0.5)
ts.display()
for i in range(40):
    ts.step()
    ts.display()
