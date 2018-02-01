import random
from copy import deepcopy

class TrafficSimulation():
    def __init__(self, road_length, traffic_density, v_max, p, start_state = [], verbose = True, strategy = 'rules'):
        self.road_length = road_length
        self.traffic_density = traffic_density
        self.v_max = v_max
        self.p = p
        self.strategy = strategy
        self.verbose = verbose
        self.throughput = 0
        if not start_state:
            self.state = []
            for i in range(road_length):
                if random.random() < traffic_density:
                    rand_init_speed = random.choice(range(v_max))
                    self.state.append(rand_init_speed)
                else:
                    self.state.append(-1)
        else:
            self.state = start_state


    def step(self):
        length = self.road_length
        speeds = deepcopy(self.state)

        if self.strategy == 'middle':
            prev_j = 0
            offset = 0

        for index, speed in enumerate(self.state):
            if speed < 0:
                continue

            # count spaces in front
            j = 1
            while self.state[(index + j)%length] < 0:
                j += 1

            # accelerate
            if speed < self.v_max and j > speed + 1:
                speeds[index] += 1

            # slow down due to cars
            if j <= speed:
                if self.strategy == 'rules':
                    speeds[index] = j - 1
                elif self.strategy == 'middle':
                    total_j = prev_j + j
                    middle = round(total_j/2)
                    offset = j - middle
                    if offset < 0:
                        speeds[index] = 0
                    else:
                        speeds[index] = offset
                    prev_j = j

            # random slow down
            if speeds[index] > 0 and random.random() < self.p:
                speeds[index] -= 1

        if self.verbose:
            self.display(speeds)

        # update the positions
        updated_state = [-1]*length
        for index, speed in enumerate(speeds):
            if speed < 0:
                continue
            updated_state[(index + speed)%length] = speed
            self.throughput += float(speed)

        # iterate the state, and please stop the hate
        self.state = updated_state

    def get_flow(self):
        # distance covered by cars divided by number of cars
        flow = self.throughput / self.road_length
        return flow

    def display(self, state):
        print(''.join('.' if x == -1 else str(x) for x in state))
