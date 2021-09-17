def integer_to_reverse_binary(number: int) -> str:
    '''
    >>> integer_to_reverse_binary(2)
    '01'

    >>> integer_to_reverse_binary(9)
    '1001'

    >>> integer_to_reverse_binary(16)
    '00001'

    '''
    binary_str = ""
    while number > 0:
        if number % 2 == 0:
            binary_str += "0"
        else:
            binary_str += "1"
        
        number //= 2

    return binary_str

def reverse_string(the_string: str) -> str:
    '''
    >>> reverse_string("Hi")
    'iH'

    >>> reverse_string("651")
    '156'

    >>> reverse_string("")
    ''

    '''
    
    return the_string[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    user_number = int(input())
    reverse_binary = integer_to_reverse_binary(user_number)
    correct_binary = reverse_string(reverse_binary)
    print(correct_binary)
