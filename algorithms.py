from math import log2, ceil


def binary_search(iterable, item):
    low = 0
    high = len(iterable) - 1
    count = ceil(log2(len(iterable)))
    for _ in range(count):
        middle = (low + high) // 2
        guess = iterable[middle]
        if guess == item:
            return middle
        elif guess < item:
            low = middle + 1
        else:
            high = middle - 1
    return -1


def two_point(iterable, k):
    left_index = 0
    right_index = len(iterable) - 1
    while left_index < right_index:
        if iterable[left_index] + iterable[right_index] == k:
            return (iterable[left_index], iterable[right_index])
        elif iterable[left_index] + iterable[right_index] > k:
            right_index -= 1
        else:
            left_index += 1
    return (None, None)


def recursive_sum(lterable):
    if not lterable:
        return 0
    return lterable[0] + recursive_sum(lterable[1:])


def find_smallest(iterable):
    if len(iterable) == 0:
        raise ValueError
    if len(iterable) == 1:
        return 0
    smallest = iterable[0]
    smallest_index = 0
    for i in range(1, len(iterable)):
        if smallest > iterable[i]:
            smallest = iterable[i]
            smallest_index = i
    return smallest_index


def selection_sort(iterable):
    new_list = []
    for _ in range(len(iterable)):
        smallest = find_smallest(iterable)
        new_list.append(iterable.pop(smallest))
    return new_list


def quick_sort(iterable):
    if len(iterable) < 2:
        return iterable
    pivot = iterable[0]
    less = [i for i in iterable[1:] if i < pivot]
    greater = [i for i in iterable[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
