import random
import matplotlib.pyplot as plt
from main import SparseSet
from test import measure_time_search

search_items = []
execution_times = []
counter = 0

while counter != 100:
    search_items.append(random.randint(0, 1000))
    counter += 1

def generate_sets(min_size, max_size, max_value, step):
    sets_list = []
    for i in range(min_size, max_size, step):
        sparse_set = SparseSet(max_value, min_size + i)
        for j in range(min_size, min_size + i):
            sparse_set.insert(random.randint(0, max_value))
        sets_list.append(sparse_set)
    return sets_list

set_collection = generate_sets(66000, 100000, 100000, 100)

def analyze_execution_time():
    for s in set_collection:
        time_spent = measure_time_search(s, search_items, 1000)
        execution_times.append(time_spent / 1000)
    return execution_times

time_results = analyze_execution_time()

def get_set_sizes():
    sizes = []
    for s in set_collection:
        sizes.append(s.n)
    return sizes

sizes = get_set_sizes()

plt.style.use('ggplot') 
plt.figure(figsize=(12, 6))
plt.plot(sizes, time_results, marker='o', color='#88c999', linestyle='-', markersize=5)
plt.xlabel('Розмір множини')
plt.ylabel('Час виконання (секунди)')
plt.grid(True)
plt.show()

