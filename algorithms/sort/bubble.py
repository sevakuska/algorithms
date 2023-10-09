from typing import Sequence


def bubble_sort(iterable: Sequence[int | float]) -> list[int | float]:
    iterable_ = list(iterable)
    iterations = len(iterable_) - 1

    for _ in range(iterations):
        for i in range(iterations):
            j = i + 1
            if iterable_[i] > iterable_[j]:
                iterable_[i], iterable_[j] = iterable_[j], iterable_[i]

    return iterable_
