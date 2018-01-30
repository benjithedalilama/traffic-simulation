from trafficsimulation import TrafficSimulation
import os
import time

# these are for a very simple animation
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def pause():
    time.sleep(0.1)

# not animated
sim = TrafficSimulation(100, 0.1, 5, 0.5)
for i in range(40):
    sim.step()
    # sim.display()
#
# # animated
# sim = TrafficSimulation(100, 0.1, 5, 0.5)
# sim.display()
# for i in range(40):
#     pause()
#     cls()
#     sim.step()
#     sim.display()
#
# sim = TrafficSimulation()
