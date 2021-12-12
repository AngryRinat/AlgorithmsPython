import random
import heapq

random.seed(42)

#Задание1. Пузырьковая сортировка.
def bub(array: list) -> list:
    n = 1
    lenth = len(array)
    is_sorted = True
    while n < lenth:
        for i in range(lenth - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
        n += 1
        if is_sorted:
            break

    return array

#Задание2. Сортировка слиянием.
def fusion(l_array: list, r_array: list) -> list:
    c_array = []
    i = j = 0
    l_len, r_len = len(l_array), len(r_array)

    while i < len(l_array) and j < len(r_array):
        if l_array[i] < r_array[j]:
            c_array.append(l_array[i])
            i += 1
        else:
            c_array.append(r_array[j])
            j += 1
    if i < len(l_array):
        c_array += l_array[i:]
    if j < len(r_array):
        c_array += r_array[j:]
    return c_array


def merge(array: list) -> list:
    if len(array) == 1:
        return array
    mid = len(array) // 2
    l_side = merge(array[:mid])
    r_side = merge(array[mid:])
    return fusion(l_side, r_side)

#Задание 3. Нахождение медианы. Списал с вашего разбора на уроке, разбираюсь.
def median(u_list: list) -> int:
    heap = []
    for item in u_list[:len(u_list) // 2 + 1]:
        heapq.heappush(heap, item)
    for item in u_list[len(u_list) // 2 + 1:]:
        if item > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, item)
    print(heap)
    return heap[0]


if __name__ == '__main__':
    unsort = [random.randint(-100, 100) for i in range(100)]
    print(bub(unsort))

    unsort2 = [random.randint(0, 50) for i in range(10)]
    print(unsort2, merge(unsort2))

    print(median(unsort2))
