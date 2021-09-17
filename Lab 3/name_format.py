def format_name(name: str) -> str:
    '''
    >>> format_name("John Crayon Stop")
    'Stop, J.C.'

    >>> format_name("Sam Allen")
    'Allen, S.'

    >>> format_name("Adam C Y")
    'Y, A.C.'
    '''
    name_list = name.split()
    if len(name_list) == 3:
        return f"{name_list[2]}, {name_list[0][0]}.{name_list[1][0]}."
    elif len(name_list) == 2:
        return f"{name_list[1]}, {name_list[0][0]}."


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    username = input()

    format = format_name(username)
    print(format)