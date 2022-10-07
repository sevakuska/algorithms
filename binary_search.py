from math import ceil, log2


def binary_search(iterable: list, item):
    low = 0
    high = len(iterable) - 1
    for i in range(ceil(log2(len(iterable)))):
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
    l = [-5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
    print(binary_search(l, 10))


if __name__ == '__main__':
    main()
