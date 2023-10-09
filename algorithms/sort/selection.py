from typing import Sequence


def selection_sort(iterable: Sequence[int | float]) -> list[int | float]:
    iterable_ = list(iterable)
    sorted_iterable = []

    while iterable_:
        sorted_iterable.append(
            iterable_.pop(
                iterable_.index(min(iterable_))
            )
        )

    return sorted_iterable
