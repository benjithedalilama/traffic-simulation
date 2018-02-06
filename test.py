from singlelanetrafficsim import SingleLaneTrafficSimulation
from multilanetrafficsim import MultiLaneTrafficSimulation

sim = SingleLaneTrafficSimulation(100, .1, 5, 0.5, verbose=True, strategy='poop')

for i in range(10):
    sim.step()

# multisim = MultiLaneTrafficSimulation(100, .1, 5, 0.5, verbose=True)
# multisim.step()
