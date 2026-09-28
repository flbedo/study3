def selection_sort(a):
    n = len(a)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

    return a

def quick_sort(a):
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

    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(a):
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

    result += left[i:]
    result += right[j:]

    return result


a = [5, 2, 8, 1, 4]

a1 = quick_sort(a)
a2 = selection_sort(a)
a3 = merge_sort(a)

print(a1)
print(a2)
print(a3)