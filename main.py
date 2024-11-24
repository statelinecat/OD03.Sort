# Алгоритм сортировки вставками (insertion sort) имеет временную сложность O(n^2) в худшем
# и среднем случае и O(n) в лучшем случае, когда массив уже отсортирован.
# Эти показатели обусловлены вложенными циклами: внешний цикл проходит по всем элементам массива,
# а внутренний цикл может проходить по почти каждому элементу для вставки текущего элемента.



import random

def insertion_sort(arr):

     for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  
            j -= 1

        arr[j + 1] = key
        print(f'Итерация {i}: {arr}')


print("Создаем случайный список чисел.")

length = random.randint(1, 10)
sample_list = [random.randint(-10, 10) for _ in range(length)]

print("Исходный список:", sample_list)
print("Начинаем сортировку.")
insertion_sort(sample_list)

print("Отсортированный список:", sample_list)

