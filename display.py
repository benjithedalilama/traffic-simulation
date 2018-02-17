from singlelanetrafficsim import SingleLaneTrafficSimulation

sim = SingleLaneTrafficSimulation(100, .1, 5, .5, verbose=True)

for i in range(40):
    sim.step()
