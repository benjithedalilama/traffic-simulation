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

    def populate_state(self, state):
        populated_state = []
        if not state:
            for i in range(self.road_length):
                if random.random() < self.traffic_density:
                    rand_init_speed = random.choice(range(self.v_max))
                    populated_state.append(rand_init_speed)
                else:
                    populated_state.append(-1)
        else:
            populated_state = state
        return populated_state

    def get_flow(self):
        pass

    def display(self, state):
        pass
