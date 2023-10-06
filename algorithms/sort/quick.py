def quick_sort(iterable):
    if len(iterable) < 2:
        return iterable

    pivot = iterable[0]
    less = [i for i in iterable[1:] if i < pivot]
    greater = [i for i in iterable[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)
