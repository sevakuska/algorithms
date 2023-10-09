from typing import Sequence
from math import ceil
from math import log2


def binary_search(
    iterable: Sequence[int | float],
    item: int | float,
    *,
    strict: bool = False
) -> int | None:
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

    if strict:
        raise ValueError('Element not found')

    return None
