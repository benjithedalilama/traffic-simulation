from singlelanetrafficsim import SingleLaneTrafficSimulation
from trafficsim import TrafficSimulation
from copy import deepcopy
import random

class MultiLaneTrafficSimulation(TrafficSimulation):

    def __init__(self, road_length, traffic_density, v_max, p, left_lane=[], right_lane=[], verbose = True, strategy = 'regular'):
        super().__init__(road_length, traffic_density, v_max, p, verbose = verbose, strategy = strategy)
        self.left_lane = left_lane if left_lane else SingleLaneTrafficSimulation(road_length, traffic_density, v_max, p, verbose = verbose, strategy = strategy)
        self.right_lane = right_lane if right_lane else SingleLaneTrafficSimulation(road_length, traffic_density, v_max, p, verbose = verbose, strategy = strategy)

    def step(self, l, l_o, l_o_back, p_change):
        left_prev_j = 0
        right_prev_j = 0
        left = self.left_lane
        right = self.right_lane
        temp_left_state = deepcopy(left.state)
        temp_right_state = deepcopy(right.state)
        for i, speed_tuple in enumerate(zip(left.state, right.state)):
            # No cars at index
            if speed_tuple[0] < 0 and speed_tuple[1] < 0:
                continue
            # Two cars side by side
            if speed_tuple[0] >= 0 and speed_tuple[1] >= 0:
                continue

            left_not_empty = len(set(left.state)) != 1
            right_not_empty = len(set(right.state)) != 1
            # count spaces in front
            left_j = 1
            while left.state[(i + left_j)%left.road_length] < 0 and left_not_empty:
                left_j += 1

            right_j = 1
            while right.state[(i + right_j)%right.road_length] < 0 and right_not_empty:
                right_j += 1

            # if the car is in the left lane, else the right lane
            if speed_tuple[1] == -1:
                gap, gap_o, gap_o_back = left_j, right_j, right_prev_j
            else:
                gap, gap_o, gap_o_back = right_j, left_j, left_prev_j

            # change lanes
            if gap < l and gap_o > l_o and gap_o_back > l_o_back and random.random() < p_change:
                temp_left_state[i], temp_right_state[i] = right.state[i], left.state[i]

            left_prev_j = left_j
            right_prev_j = right_j

        right.state = temp_right_state
        left.state = temp_left_state

        left.step()
        right.step()

    def display(self):
        print(''.join('.' if x == -1 else str(x) for x in self.left_lane.state))
        print(''.join('.' if x == -1 else str(x) for x in self.right_lane.state))
