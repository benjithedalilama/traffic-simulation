from trafficsimulation import TrafficSimulation
# import seaborn as sns
import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt


def get_flow_array(densities, iterations):
    avg_flow_arr = []
    for density in densities:
        sim = TrafficSimulation(100,density,5,.5, verbose=False)
        flow_sum = 0
        for i in range(iterations):
            sim.step()
            flow = sim.get_flow()
            flow_sum += flow
        avg_flow = flow_sum/(iterations*sim.road_length)
        avg_flow_arr.append(avg_flow)
    return avg_flow_arr

dens = np.arange(0.01,1.0,.01)
its = 200

flows = get_flow_array(dens, its)
dens = np.array(dens)
flows = np.array(flows)
# df = pd.DataFrame({'density':dens, 'flow':flows})
# ax = sns.lmplot(x='density', y='flow', fit_reg=True, data=df)
plt.scatter(dens,flows,s=2)
z = np.polyfit(dens, flows, 3)
f = np.poly1d(z)
plt.plot(dens, f(dens))
plt.xlabel('density (cars per cell)')
plt.ylabel('Flow (cars per time-step)')
plt.title('Flow vs. Density')
plt.grid(True)
plt.savefig("test.png")
raise Exception
