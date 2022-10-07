'''BINARY SEARCH'''


from math import ceil, log2


def binary_search(iterable, item):
    '''Binary search algorithm'''
    low = 0
    high = len(iterable) - 1
    for _ in range(ceil(log2(len(iterable)))):
        mid = (low + high) // 2
        guess = iterable[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def main():
    '''Entry point.'''
    test_list = [-5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
    print(binary_search(test_list, 10))


if __name__ == '__main__':
    main()
