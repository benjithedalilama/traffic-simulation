class TrafficSimulation():
    def __init__(self, road_length, traffic_density, v_max, p, start_state):
        self.road_length = road_length
        self.traffic_density = traffic_density
        self.v_max = v_max
        self.p = p
        self.state = start_state

    def update(self):
        state = self.state
        for index, position_speed in enumerate(state):
            # if there isn't a car, check next cell
            if position_speed == -1: continue
            # accelerate if slower than max velocity and there is room to do so
            if position_speed < self.v_max and state[index+1] == -1:
                state[index] += 1



    def display(self):
        print(''.join('.' if x == -1 else str(x) for x in self.state))
