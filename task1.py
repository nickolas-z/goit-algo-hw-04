import random
import timeit
import matplotlib.pyplot as plt
from helpers import print_execution_time, print_header, print_footer
from colorama import init, Fore

def insertion_sort(data)->None:
    """ Сортування вставками """
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def merge_sort(data)->None:
    """ Сортування злиттям """
    if len(data) > 1:
        mid = len(data) // 2
        L = data[:mid]
        R = data[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Злиття двох половин
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
            k += 1

        # Перевірка, чи залишилися елементи
        while i < len(L):
            data[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            data[k] = R[j]
            j += 1
            k += 1

def timsort(data)->None:
    """ Сортування TimSort (вбудоване) """
    return sorted(data)


def generate_random_list(size) -> list:
    """Генерація списку для сортування"""
    return [random.randint(0, size) for _ in range(size)]


def generate_sorted_list(size) -> list:
    """Генерація відсортованого списку"""
    return list(range(size))


def generate_reverse_sorted_list(size) -> list:
    """Генерація відсортованого списку у зворотньому порядку"""
    return list(range(size, 0, -1))


def measure_time(sort_func, data)->float:
    """ Вимірювання часу сортування """
    setup_code = f"from __main__ import {sort_func.__name__}"
    stmt = f"{sort_func.__name__}({data})"
    times = timeit.repeat(stmt=stmt, setup=setup_code, repeat=3, number=1)
    return min(times)

@print_execution_time
def main()->None:
    """ Головна функція """
    # Створення списку для сортування
    data_types = ["Випадкові", "Відсортовані", "Зворотно відсортовані"]
    sizes = [1000, 5000, 10000, 20000, 50000, 100000]

    sorting_algorithms = {
        "Сортування вставками": insertion_sort,
        "Сортування злиттям": merge_sort,
        "Timsort": timsort,
    }

    results = {
        "Випадкові": {alg: [] for alg in sorting_algorithms},
        "Відсортовані": {alg: [] for alg in sorting_algorithms},
        "Зворотно відсортовані": {alg: [] for alg in sorting_algorithms},
    }

    for size in sizes:
        # Генерація наборів даних
        random_data = generate_random_list(size)
        sorted_data = generate_sorted_list(size)
        reverse_sorted_data = generate_reverse_sorted_list(size)

        datasets = {
            "Випадкові": random_data,
            "Відсортовані": sorted_data,
            "Зворотно відсортовані": reverse_sorted_data,
        }

        for data_type, data in datasets.items():
            for alg_name, alg_func in sorting_algorithms.items():
                # Для сортування вставками обмежимо розмір масиву до 20,000
                if alg_name == "Сортування вставками" and size > 20000:
                    results[data_type][alg_name].append(None)
                    continue
                time_taken = measure_time(alg_func, data)
                results[data_type][alg_name].append(time_taken)
                print(
                    f"Розмір: {size}, Дані: {data_type}, Алгоритм: {alg_name}, Час: {time_taken}"
                )

    # Побудова графіків
    for data_type in data_types:
        plt.figure(figsize=(10, 6))
        for alg_name in sorting_algorithms:
            times = results[data_type][alg_name]
            # Фільтруємо None значення
            filtered_sizes = [size for i, size in enumerate(sizes) if times[i] is not None]
            filtered_times = [t for t in times if t is not None]
            plt.plot(filtered_sizes, filtered_times, marker="o", label=alg_name)
        plt.title(f"Порівняння часу виконання на {data_type.lower()} даних")
        plt.xlabel("Розмір масиву")
        plt.ylabel("Час виконання (секунди)")
        plt.legend()
        plt.grid(True)
        plt.xticks(sizes)
        plt.savefig(f"{data_type}_data_plot.png")
        plt.show()

# Запуск програми
if __name__ == "__main__":
    init(autoreset=True)
    print_header("Сортування масивів")
    main()
    print_footer("Розрахунки завершено.")
