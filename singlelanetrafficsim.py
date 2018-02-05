import random
from copy import deepcopy
from trafficsim import TrafficSimulation

class SingleLaneTrafficSimulation(TrafficSimulation):

    def __init__(self, road_length, traffic_density, v_max, p, start_state = [], verbose = True, strategy = 'regular'):
        super().__init__(road_length, traffic_density, v_max, p, verbose = verbose, strategy = strategy)
        self.state = []
        self.state = self.populate_state(start_state)

    def step(self):
        if self.strategy == 'middle':
            prev_j = 0
            offset = 0

        speeds = self.update_speeds()

        if self.verbose:
            self.display(speeds)

        updated_state = self.update_positions(speeds)

        # iterate the state, and please stop the hate
        self.state = updated_state

    def update_speeds(self):
        length = self.road_length
        speeds = deepcopy(self.state)

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
                if self.strategy == 'regular':
                    speeds[index] = j - 1
                elif self.strategy == 'middle':
                    total_j = prev_j + j
                    # the round() function is making sure if the space between
                    # is even, the car will be further back instead of closer to tailgating
                    # not sure how this behavior propagates back
                    middle = round(total_j/2)
                    offset = j - middle
                    # example: [4......3...5]
                    # cars cant move backwards on a highway, so just make them
                    # stop. Keep in mind the state of the road before actual
                    # movement happens is displayed if sim is verbose
                    if offset < 0:
                        speeds[index] = 0
                    else:
                        speeds[index] = offset
                    prev_j = j

            # random slow down
            if speeds[index] > 0 and random.random() < self.p:
                speeds[index] -= 1
        return speeds

    def update_positions(self, state):
        length = self.road_length
        # update the positions
        updated_state = [-1]*length
        for index, speed in enumerate(state):
            if speed < 0:
                continue
            updated_state[(index + speed)%length] = speed
            self.throughput += float(speed)

        return updated_state

    def get_flow(self):
        # distance covered by cars divided by length of road
        flow = self.throughput / self.road_length
        return flow

    def display(self, state):
        print(''.join('.' if x == -1 else str(x) for x in state))