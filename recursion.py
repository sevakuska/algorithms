'''Пример из главы 3 книги грокаем алгоритмы'''


def look_for_key(main_box):
    '''example'''
    pile = main_box.make_a_pile_to_look_through()
    # while pile is not empty:
    while pile is not None:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print('Found the key')


def look_for_key_recursive(box):
    '''recursive example'''
    for item in box:
        if item.is_a_box():
            look_for_key_recursive(item)
        elif item.is_a_key():
            return item


def count(start: int, end: int, step: int = 1):
    '''recursive example'''
    if start != end:
        print(start)
        count(start+step, end, step)


if __name__ == '__main__':
    count(10, -10, -1)
