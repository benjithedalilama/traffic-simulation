from singlelanetrafficsim import SingleLaneTrafficSimulation
from multilanetrafficsim import MultiLaneTrafficSimulation
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.kernel_ridge import KernelRidge

def get_flow_array(densities, iterations, strategy, l_tuple=(), mode='single'):
    avg_flow_arr = []
    if mode == 'multi': l, l_o, l_o_back = l_tuple
    for density in densities:
        if mode == 'single':
            sim = SingleLaneTrafficSimulation(100, density, 5, 0.5, verbose=False, strategy=strategy)
        elif mode == 'multi':
            sim = MultiLaneTrafficSimulation(100, density, 5, 0.5, l, l_o, l_o_back, p_change=0.5, verbose=False, strategy=strategy)
        flow_sum = 0
        for i in range(iterations):
            sim.step()
            flow = sim.get_flow()
            flow_sum += flow
        avg_flow = flow_sum/(iterations*sim.road_length)
        avg_flow_arr.append(avg_flow)
    return avg_flow_arr

def analyze_and_plot(l_tuple=(), mode='single'):
    dens = np.repeat(np.arange(0.0,1.0,.01),5)
    its = 200
    strategies = ['regular','middle']
    train_size = len(dens)
    for strategy in strategies:
        flows = get_flow_array(dens, its, strategy, l_tuple=l_tuple, mode=mode)
        flows = np.array(flows)
        plt.scatter(dens,flows,s=2,label='%s'%strategy)
        kr = GridSearchCV(KernelRidge(kernel='chi2', gamma=0.1), cv=5,
                      param_grid={"alpha": [1e0, 0.1, 1e-2, 1e-3],
                                  "gamma": np.logspace(-2, 2, 5)})
        dens = dens.reshape(len(dens),1)
        flows = flows.reshape(len(flows),1)
        kr.fit(dens[:train_size], flows[:train_size])
        y_kr = kr.predict(dens)
        color = 'r' if strategy == 'regular' else 'g'
        plt.plot(dens, y_kr, label='%s KRR'%strategy,c=color,linewidth=1)
        plt.xlabel('Density (cars per cell)')
        plt.ylabel('Flow (total cars per time-step)')
        if mode == 'multi':
            l, l_o, l_o_back = l_tuple
            plt.title('Flow vs. Density for %s Lane Simulation, l:%d l_o:%d l_o_back:%d'%(mode.capitalize(),l,l_o,l_o_back))
        elif mode == 'single':
            plt.title('Flow vs. Density for %s Lane Simulation'%mode.capitalize())
        plt.grid(True)
    plt.legend(loc='upper right')
    plt.savefig("test%s.png"%mode)
    plt.gcf().clear()

l = 3
l_o = 3
l_o_back = 3

l_tuple = (l, l_o, l_o_back)
analyze_and_plot()
analyze_and_plot(l_tuple=l_tuple,mode='multi')
