import pandas as pd
from pyticle.benchmark import Benchmark
from pyticle.meta_search import MetaSearch

def test_meta_search_execution():
    ms = MetaSearch(cost_func=Benchmark.ackley, var_size=2, low_bound=-32, high_bound=32)
    result = ms.search(try_num=3, n_jobs=1)
    if not isinstance(result, pd.DataFrame):
        raise TypeError(f'meta_search results should be '
        f'pandas.DataFrame, and not {type(result)}')
    if result.shape[0] != 3:
        raise ValueError(f'meta_search results should have 3 rows, and not {result.shape[0]}')   
    if result.shape[1] != 13:
        raise ValueError(f'meta_search results should have 13 columns, and not {result.shape[1]}')   
    if len(result.loc[0, 'x_opt']) != 2:
        raise ValueError(f'meta_search x* should be in 2D space, and not {len(result.loc[0, "x_opt"])}')   

