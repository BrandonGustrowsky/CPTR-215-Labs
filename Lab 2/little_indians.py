def print_sequence(number: int = 10) -> None:
    '''
    >>> print_sequence()
    1 little, 2 little, 3 little Indians;
    4 little, 5 little, 6 little Indians;
    7 little, 8 little, 9 little Indians;
    10 little Indian boys.

    >>> print_sequence(6)
    1 little, 2 little, 3 little Indians;
    4 little, 5 little, 6 little Indian boys.
    '''
    for i in range(number-1):
        print(i+1, end=' little Indians;\n' if (i+1)%3 == 0 and i != 0 else ' little, ')

    print(f"{number} little Indian boys.")

# if __name__ == "__main__":
    import doctest
    doctest.testmod()