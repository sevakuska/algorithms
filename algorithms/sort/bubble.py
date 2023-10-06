def bubble_sort(iterable):
    iterable_ = iterable[:]
    iterations = len(iterable_) - 1

    for _ in range(iterations):
        for i in range(iterations):
            if iterable_[i] > iterable_[i+1]:
                iterable_[i], iterable_[i+1] = iterable_[i+1], iterable_[i]

    return iterable_
