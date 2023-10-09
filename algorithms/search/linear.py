from typing import Sequence


def linear_search(
    iterable: Sequence[int | float],
    item: int | float,
    *,
    strict: bool = False
) -> int | None:
    for i in range(len(iterable)):
        if iterable[i] == item:
            return i

    if strict:
        raise ValueError('Element not found')

    return None
