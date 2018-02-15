from singlelanetrafficsim import SingleLaneTrafficSimulation
from multilanetrafficsim import MultiLaneTrafficSimulation

sim = MultiLaneTrafficSimulation(50, .1, 5, 0.5, verbose=True)

l = 5
l_o = 2
l_o_back = 2
for i in range(10):
    sim.step(l, l_o, l_o_back, .5)

# multisim = MultiLaneTrafficSimulation(100, .1, 5, 0.5, verbose=True)
# multisim.step()
