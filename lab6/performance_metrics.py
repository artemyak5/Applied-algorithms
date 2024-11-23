import time
import tracemalloc

def measure_performance(sort_function, arr):
    import sys
    sys.setrecursionlimit(100000)  

    
    from copy import deepcopy
    arr_copy = deepcopy(arr)

    
    global comparison_count
    global copy_count
    comparison_count = 0
    copy_count = 0

    tracemalloc.start()

    start_time = time.time()
    result = sort_function(arr_copy)
    end_time = time.time()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time = end_time - start_time
    memory_used = peak / 10**6 

    metrics = {
        'execution_time': execution_time,
        'comparisons': comparison_count,
        'copies': copy_count,
        'memory_used': memory_used
    }

    return metrics, result
