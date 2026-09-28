from time import perf_counter

actions = 0


def selection_sort(a):
    global actions
    n = len(a)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            actions += 1

    return a

def quick_sort(a):
    global actions
    if len(a) <= 1:
        return a

    pivot = a[len(a) // 2]

    left = []
    middle = []
    right = []

    for x in a:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)
        actions += 1

    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(a):
    global actions
    if len(a) <= 1:
        return a

    middle = len(a) // 2

    left = merge_sort(a[:middle])
    right = merge_sort(a[middle:])

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        actions += 1

    result += left[i:]
    result += right[j:]
    actions += len(left) - i + len(right) - j

    return result


with open("москва_2021.txt", "r") as f:
    a = list(map(int, f.read().split()))
print("Исходный массив:", a[:10], "...", a[-10:])

start = perf_counter()
a1 = list(set(quick_sort(a.copy())))
quick_time = perf_counter() - start
quick_actions = actions

actions = 0
start = perf_counter()
a2 = list(set(selection_sort(a.copy())))
selection_time = perf_counter() - start
selection_actions = actions

actions = 0
start = perf_counter()
a3 = list(set(merge_sort(a.copy())))
merge_time = perf_counter() - start
merge_actions = actions

print('Быстрая сортировка:')
print(a1[:10], "...", a1[-10:], f"Время: {quick_time:.6f} с, действий/перестановок: {quick_actions}")
print('Сортировка выбором:')
print(a2[:10], "...", a2[-10:], f"Время: {selection_time:.6f} с, действий/перестановок: {selection_actions}")
print('Сортировка слиянием:')
print(a3[:10], "...", a3[-10:], f"Время: {merge_time:.6f} с, действий/перестановок: {merge_actions}")
