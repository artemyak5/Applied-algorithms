import random
import matplotlib.pyplot as plt
import time
from main import SparseSet

def generate_sets(min_size, max_size, max_value, step):
    sets_list = []
    for size in range(min_size, max_size, step):
        sparse_set = SparseSet(max_value, size)
        for _ in range(size):
            sparse_set.insert(random.randint(0, max_value))
        sets_list.append(sparse_set)
    return sets_list

first_sets = generate_sets(46000, 56000, 100000, 500)
second_sets = generate_sets(43000, 53000, 100000, 500)

def measure_union_time():
    execution_times = []
    for i in range(len(first_sets)):
        total_time = 0
        for _ in range(100):
            start_time = time.time()
            first_sets[i].setUnion(second_sets[i])
            end_time = time.time()
            total_time += (end_time - start_time)
        execution_times.append(total_time / 1000)  # середній час на тисячу ітерацій
    return execution_times

union_times = measure_union_time()

def get_set_sizes():
    return [s.n for s in second_sets]

sizes = get_set_sizes()

plt.style.use('ggplot')
plt.figure(figsize=(12, 6))
plt.plot(sizes, union_times, marker='o', color='#88c999', linestyle='-', markersize=5)
plt.xlabel('Розмір множини')
plt.ylabel('Час виконання (секунди)')
plt.title('Час виконання об’єднання множин залежно від їх розміру')
plt.grid(True)
plt.show()
