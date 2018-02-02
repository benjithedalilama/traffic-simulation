from trafficsimulation import TrafficSimulation
import subprocess
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.kernel_ridge import KernelRidge
from joblib import Parallel, delayed

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

dens = np.repeat(np.arange(0.0,1.0,.03),5)
its = 200
strategies = ['regular','middle']
train_size = len(dens)
for strategy in strategies:
    strat_to_be_zipped = ['strategy']*len(dens)
    its_to_be_zipped = [its]*len(dens)
    arg_instances = zip(dens, its_to_be_zipped, strat_to_be_zipped)
    start = time.time()
    flows = Parallel(n_jobs=4, backend="multiprocessing")(delayed(get_flow_array)(densities = dens[i:i+10], iterations = its, strategy = strategy) for i in range(0,len(dens),10))
    elapsed = time.time() - start
    flows = np.array(flows)
    subprocess.run(['say','Hello! %s Strategy is done parallelized in %d seconds'%(strategy,elapsed)])
    flows.flatten()
    start2 = time.time()
    flows = get_flow_array(dens, its, strategy)
    elapsed2 = time.time() - start
    flows = np.array(flows)
    subprocess.run(['say','Hello! %s Strategy is done regularly in %d seconds'%(strategy,elapsed)])
    plt.scatter(dens,flows,s=2,label='%s'%strategy)
    kr = GridSearchCV(KernelRidge(kernel='chi2', gamma=0.1), cv=5,
                  param_grid={"alpha": [1e0, 0.1, 1e-2, 1e-3],
                              "gamma": np.logspace(-2, 2, 5)})
    dens = dens.reshape(len(dens),1)
    flows = flows.reshape(len(dens),1)
    kr.fit(dens[:train_size], flows[:train_size])
    y_kr = kr.predict(dens)
    color = 'r' if strategy == 'regular' else 'g'
    plt.plot(dens, y_kr, label='%s KRR'%strategy,c=color,linewidth=1)
    plt.xlabel('Density (cars per cell)')
    plt.ylabel('Flow (total cars per time-step)')
    plt.title('Flow vs. Density')
    plt.grid(True)
plt.legend(loc='upper right')
plt.savefig("test.png")
