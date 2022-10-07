def find_smallest_index(iterable: list):
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


def selection_sort(iterable: list):
    new_list = []
    for i in range(len(iterable)):
        smallest = find_smallest_index(iterable)
        new_list.append(iterable.pop(smallest))
    return new_list


def main():
    l = [0, 3, 4, 1, 5, 9, 8, 7, 6, 2]
    print(selection_sort(l))


if __name__ == '__main__':
    main()
