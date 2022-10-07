'''Файл, в котором реализуется алгоритм двух указателей'''
def two_point(iterable, k):
    '''Алгоритм двух указателей'''
    left_index = 0
    right_index = len(iterable) -1
    while left_index != right_index:
        if iterable[left_index] + iterable[right_index] == k:
            return [iterable[left_index], iterable[right_index]]
        elif iterable[left_index] + iterable[right_index] > k:
            right_index -= 1
        else:
            left_index += 1
    return []


def main():
    '''Входная точка'''
    nums = [-5, -2, 4, 7, 8, 12, 16, 17, 32, 44, 48]
    print(two_point(nums, 24))


if __name__ == '__main__':
    main()
