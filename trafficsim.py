import random
from copy import deepcopy

class TrafficSimulation():

    def __init__(self, road_length, traffic_density, v_max, p, verbose = True, strategy = 'regular'):
        self.road_length = road_length
        self.traffic_density = traffic_density
        self.v_max = v_max
        self.p = p
        self.strategy = strategy
        self.verbose = verbose
        self.throughput = 0

    def step(self):
        pass

    def update_speeds(self):
        pass

    def update_positions(self):
        pass

    def get_flow(self):
        pass

    def display(self, state):
        pass
