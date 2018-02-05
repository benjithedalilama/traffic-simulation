from singlelanetrafficsim import SingleLaneTrafficSimulation
from trafficsim import TrafficSimulation

class MultiLaneTrafficSimulation(TrafficSimulation):

    def __init__(self, road_length, traffic_density, v_max, p, left_state = [], right_state = [], verbose = True, strategy = 'regular'):
        super().__init__(road_length, traffic_density, v_max, p, verbose = verbose, strategy = strategy)
        self.left_lane = SingleLaneTrafficSimulation(road_length, traffic_density, v_max, p, start_state=left_state, verbose = verbose, strategy = strategy)
        self.right_lane = SingleLaneTrafficSimulation(road_length, traffic_density, v_max, p, start_state=right_state, verbose = verbose, strategy = strategy)

    def step(self):
        self.left_lane.step()
        self.right_lane.step()

    def display(self):
        print(''.join('.' if x == -1 else str(x) for x in self.left_lane.state))
        print(''.join('.' if x == -1 else str(x) for x in self.right_lane.state))
