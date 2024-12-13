import random

# Funkcja sortowania szybkie (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Wybieramy pivot (środkowy element)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Funkcja sortowania przez wstawianie (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Generowanie losowych liczb
def generate_random_numbers(n, lower=0, upper=100):
    return [random.randint(lower, upper) for _ in range(n)]

# Weryfikacja wyników
def verify_sort(original, sorted_custom):
    return sorted(original) == sorted_custom

# Parametry
N = int(input("Podaj liczbę elementów do wylosowania: "))
lower_bound = int(input("Podaj dolny zakres losowania: "))
upper_bound = int(input("Podaj górny zakres losowania: "))

# Generowanie danych
random_numbers = generate_random_numbers(N, lower_bound, upper_bound)
print("Wylosowane liczby:", random_numbers, '\n')

# Sortowanie szybkie (Quick Sort)
quick_sorted = quick_sort(random_numbers)
print("Quick Sort:", quick_sorted,'\n')
print("Takie same quick: ", verify_sort(random_numbers, quick_sorted),'\n')

# Sortowanie przez wstawianie (Insertion Sort)
insertion_sorted = insertion_sort(random_numbers)
print("Insertion Sort:", insertion_sorted,'\n')
print("Takie same insertion", verify_sort(random_numbers, insertion_sorted))
