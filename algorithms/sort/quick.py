from typing import Sequence


def quick_sort(iterable: Sequence[int | float]) -> list[int | float]:
    if len(iterable) < 2:
        return list(iterable)

    pivot = iterable[0]
    less = [i for i in iterable[1:] if i < pivot]
    greater = [i for i in iterable[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)
