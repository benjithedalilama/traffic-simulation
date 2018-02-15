from singlelanetrafficsim import SingleLaneTrafficSimulation
from multilanetrafficsim import MultiLaneTrafficSimulation

sim = MultiLaneTrafficSimulation(50, .1, 5, .5, 5, 2, 2, p_change=0.5, verbose=True)

l = 5
l_o = 2
l_o_back = 2
for i in range(10):
    sim.step()

# multisim = MultiLaneTrafficSimulation(100, .1, 5, 0.5, verbose=True)
# multisim.step()
