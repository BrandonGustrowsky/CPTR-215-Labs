def isStrictlyIncreasing(the_list: list) -> bool:
    '''
    >>> isStrictlyIncreasing([1, 2, 3, 4, 5])
    True

    >>> isStrictlyIncreasing([0, 1, 2, 3, 0, 1])
    False

    >>> isStrictlyIncreasing(["a", "b", "c", "d", "e"])
    True

    >>> isStrictlyIncreasing(["b", "c", "a"])
    False

    >>> isStrictlyIncreasing([2, 2, 2])
    False
    '''

    if len(the_list) == 0:
        return True

    iter = 0
    temp = the_list[0]
    for value in the_list:
        if iter == 0:
            iter += 1
            continue

        if temp >= value:
            return False
        
        temp = value
        iter += 1

    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    my_list = ["a", "b", "c", "b", "e"]

    isStrictlyIncreasing(my_list)