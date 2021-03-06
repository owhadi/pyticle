import time

import numpy as np
import pandas as pd
from joblib import Parallel, delayed

from pyticle.benchmark import Benchmark
from pyticle.swarm_optimization import SwarmOptimization


class MetaSearch:
    def __init__(self, my_func, var_size, low_bound, high_bound):
        self.my_func = my_func
        self.var_size = var_size
        self.low_bound = low_bound
        self.high_bound = high_bound

    def search(self, try_num=2):

        input_list = []
        result_list = []

        for i in range(5):

            np.random.seed(i)

            pn = int(np.random.randint(low=50, high=200, size=1))
            os = max(np.random.rand() - 0.5, 0.0)
            oe = min(np.random.rand() + 0.5, 1.0)
            cf = np.random.rand(2) + 1.5
            bs = np.random.choice(["random", "clipping"], p=[0.3, 0.7])
            mi = int(np.random.randint(low=100, high=500, size=1))
            er = np.random.rand() * 0.2

            inp = dict(
                cost_func=self.my_func,
                particle_num=pn,
                omega_start=os,
                omega_end=oe,
                coef=cf,
                low_bound=self.low_bound,
                high_bound=self.high_bound,
                boundary_strategy=bs,
                var_size=self.var_size,
                max_iter_num=mi,
                elite_rate=er,
            )
            input_list.append(inp)

        result_list = Parallel(n_jobs=10)(
            delayed(self.optimization_iter)(**inp) for inp in input_list
        )
        result = pd.DataFrame(result_list).sort_values(by="obj_val")
        print(result)

    def optimization_iter(self, **kwargs):

        np.random.seed(kwargs["particle_num"] * kwargs["max_iter_num"])

        optimizer = SwarmOptimization(**kwargs)

        t0 = time.time()
        obj_val, x_opt = optimizer.optimize()
        opt_time = time.time() - t0

        output = {
            "obj_val": obj_val,
            "opt_time": time.time() - t0,
            "x_opt": x_opt,
            **kwargs,
        }
        output.pop("cost_func")

        return output


ms = MetaSearch(Benchmark.ackley, 2, -32, 32)
ms.search(try_num=50)
