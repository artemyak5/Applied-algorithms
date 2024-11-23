import time
import tracemalloc
from counters import Counter  

def measure_performance(sort_function, arr):
    import sys
    sys.setrecursionlimit(100000)

    from copy import deepcopy
    arr_copy = deepcopy(arr)

    counter = Counter()

    tracemalloc.start()

    start_time = time.time()
    sort_function(arr_copy, counter)
    end_time = time.time()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time = end_time - start_time
    memory_used = peak / 10**6

    metrics = {
        'execution_time': execution_time,
        'comparisons': counter.comparison_count,
        'copies': counter.copy_count,
        'memory_used': memory_used
    }

    return metrics, arr_copy
