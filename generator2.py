"""
4. * Необязательное задание. Написать генератор, аналогичный генератору
из задания 2, но обрабатывающий списки с любым уровнем вложенности.
Шаблон и тест в коде ниже:
"""

import types

def flat_generator(list_of_list):
    for listing in list_of_list:
        if type(listing) is list:
            yield from flat_generator(listing)
        else:
            yield listing

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)

    print(list(flat_generator(list_of_lists_2)))

if __name__ == '__main__':
    test_4()