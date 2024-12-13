import time
import random
import multiprocessing
import matplotlib.pyplot as plt

def parallel_quick_sort(array, pool=None):

    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    if pool:

        sorted_sublists = pool.map(parallel_quick_sort_helper, [left, right])
    else:
        sorted_sublists = [parallel_quick_sort(left), parallel_quick_sort(right)]


    return sorted_sublists[0] + middle + sorted_sublists[1]


def parallel_quick_sort_helper(array):

    return parallel_quick_sort(array)


def test_parallel_sort():
    sizes = [1000, 5000, 10000, 50000]
    num_processes = [1, 2, 4, 8]
    results = {}

    for size in sizes:
        results[size] = []
        data = [random.randint(0, 100000) for _ in range(size)]

        for processes in num_processes:
            start_time = time.time()

            with multiprocessing.Pool(processes=processes) as pool:
                _ = parallel_quick_sort(data, pool=pool)

            elapsed_time = time.time() - start_time
            results[size].append(elapsed_time)
            print(f"Rozmiar: {size}, Procesy: {processes}, Czas: {elapsed_time:.4f} s")


    for size, times in results.items():
        plt.plot(num_processes, times, label=f"Rozmiar danych: {size}")

    plt.title("Wydajność równoległego QuickSort")
    plt.xlabel("Liczba procesów")
    plt.ylabel("Czas wykonania (s)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    test_parallel_sort()
