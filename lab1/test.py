import random
import time
from main import SparseSet

M = SparseSet(100000, 85000)
n = 85000
for i in range(n):
    M.insert(random.randint(15000, 100000))

not_in_M = [random.randint(0, 15000) for _ in range(15000)]

in_M = [random.randint(15000, 100000) for _ in range(15000)]

def measure_time_search(set_, elements, reps):
    total_time = 0
    for elem in elements:
        for _ in range(reps):
            start_time = time.time()
            set_.search(elem)
            end_time = time.time()
            total_time += (end_time - start_time)
    return total_time

time_not_in_M = measure_time_search(M, not_in_M, 1000)
print(f"Час пошуку елементів, яких немає в множині (15,000 елементів по 1000 разів): {time_not_in_M} секунд")

time_in_M = measure_time_search(M, in_M, 1000)
print(f"Час пошуку елементів, які є в множині (15,000 елементів по 1000 разів): {time_in_M} секунд")


def measure_time_union(reps):
    total_time = 0
    for _ in range(reps):
        K = SparseSet(66000, 66000)
        for i in range(66000):
            K.insert(random.randint(0, 66000))

        M = SparseSet(132000, 66000)
        for i in range(66000):
            M.insert(random.randint(64000, 132000))

        start_time = time.time()
        union_set = K.setUnion(M)
        end_time = time.time()
        
        total_time += (end_time - start_time)
        
    return total_time

time_union = measure_time_union(1000)
print(f"Час виконання 1000 об'єднань двох множин по 66,000 елементів: {time_union} секунд")
