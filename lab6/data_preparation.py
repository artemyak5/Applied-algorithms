import random

def generate_sorted_data(n):
    return list(range(n))

def generate_random_data(n):
    return [random.randint(0, n) for _ in range(n)]

def generate_almost_sorted_data(n):
    arr = list(range(n))
    num_swaps = int(n * 0.05)  
    for _ in range(num_swaps):
        i, j = random.sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def generate_reversed_data(n):
    return list(range(n, 0, -1))

def generate_few_unique_data(n):
    unique_values = [random.randint(0, 10) for _ in range(5)]
    return [random.choice(unique_values) for _ in range(n)]
