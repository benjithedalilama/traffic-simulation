from trafficsimulation import TrafficSimulation
# import seaborn as sns
import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt


def get_flow_array(densities, iterations, strategy):
    avg_flow_arr = []
    for density in densities:
        sim = TrafficSimulation(100, density, 5, 0.5, verbose=False, strategy=strategy)
        flow_sum = 0
        for i in range(iterations):
            sim.step()
            flow = sim.get_flow()
            flow_sum += flow
        avg_flow = flow_sum/(iterations*sim.road_length)
        avg_flow_arr.append(avg_flow)
    return avg_flow_arr

dens = np.arange(0.00,1.0,.001)
its = 200
strategies = ['rules','middle']
for strategy in strategies:
    flows = get_flow_array(dens, its, strategy)
    dens = np.array(dens)
    flows = np.array(flows)
    # df = pd.DataFrame({'density':dens, 'flow':flows})
    # ax = sns.lmplot(x='density', y='flow', fit_reg=True, data=df)
    plt.scatter(dens,flows,s=2,label='%s'%strategy)
    # z = np.polyfit(dens, flows, 3)
    # f = np.poly1d(z)
    # plt.plot(dens, f(dens))
    plt.xlabel('Density (cars per cell)')
    plt.ylabel('Flow (cars per time-step)')
    plt.title('Flow vs. Density')
    plt.grid(True)
plt.legend(loc='upper right')
plt.savefig("test.png")
