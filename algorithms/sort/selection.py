def selection_sort(iterable):
    sorted_iterable = []

    while iterable:
        sorted_iterable.append(
            iterable.pop(
                iterable.index(min(iterable))
            )
        )

    return sorted_iterable
