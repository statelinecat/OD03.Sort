import random

def insertion_sort(arr):

     for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # Сдвиг элемента вправо
            j -= 1

        arr[j + 1] = key
        print(f'Итерация {i}: {arr}')


print("Создаем случайный список чисел.")

length = random.randint(1, 100)
sample_list = [random.randint(-100, 100) for _ in range(length)]

print("Исходный список:", sample_list)
print("Начинаем сортировку.")
insertion_sort(sample_list)

print("Отсортированный список:", sample_list)

