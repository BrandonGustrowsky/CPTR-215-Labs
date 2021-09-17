def get_inrange_numbers(numbers: list, the_range: list) -> list:
    '''
    >>> get_inrange_numbers(["1", "2", "3", "4", "5"], ["0", "3"])
    ['1', '2', '3']

    >>> get_inrange_numbers(["5", "100", "641", "98131", "429", "3928"], ["90", "1000"])
    ['100', '641', '429']
    '''
    in_range_nums = []

    for number in numbers:
        if int(number) in range(int(the_range[0]), int(the_range[1])+1):
            in_range_nums.append(number)

    return in_range_nums

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    numbers = input()
    numbers_range = input()

    numbers_list = numbers.split()
    range_list = numbers_range.split()

    new_numbers = get_inrange_numbers(numbers_list, range_list)

    for number in new_numbers:
        print(f"{number} ", end="")
