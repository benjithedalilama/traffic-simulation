from singlelanetrafficsim import SingleLaneTrafficSimulation
from multilanetrafficsim import MultiLaneTrafficSimulation

multisim = MultiLaneTrafficSimulation(100, .1, 5, 0.5, verbose=True)

for i in range(20):
    multisim.step()
