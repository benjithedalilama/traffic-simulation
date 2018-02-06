from singlelanetrafficsim import SingleLaneTrafficSimulation
from trafficsim import TrafficSimulation

class MultiLaneTrafficSimulation(TrafficSimulation):

    def __init__(self, road_length, traffic_density, v_max, p, left_lane, right_lane, verbose = True, strategy = 'regular'):
        super().__init__(road_length, traffic_density, v_max, p, verbose = verbose, strategy = strategy)
        self.left_lane = left_lane if left_lane else SingleLaneTrafficSimulation(road_length, traffic_density, v_max, p, start_state=left_lane.state, verbose = verbose, strategy = strategy)
        self.right_lane = right_lane if right_lane else SingleLaneTrafficSimulation(road_length, traffic_density, v_max, p, start_state=right_lane.state, verbose = verbose, strategy = strategy)

    def step(self):
        # basically will just make a while loop to check l spaces back in the
        # other lane if needing to switch. Then applies the probability filter
        # on whether the car will actually switch or not
        self.left_lane.step()
        self.right_lane.step()

    def display(self):
        print(''.join('.' if x == -1 else str(x) for x in self.left_lane.state))
        print(''.join('.' if x == -1 else str(x) for x in self.right_lane.state))
