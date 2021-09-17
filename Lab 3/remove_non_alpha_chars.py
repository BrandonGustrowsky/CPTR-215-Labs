alphabet = "abcdefghijklmnopqrstuvwxyz"

def remove_non_alpha_chars(the_string: str) -> str:
    '''
    >>> remove_non_alpha_chars("-Hel10 W0R4d!!")
    'HelWRd'

    >>> remove_non_alpha_chars("6 i5 gre@teR?")
    'igreteR'
    
    >>> remove_non_alpha_chars("1 %(&!0@)")
    ''
    '''
    new_string = ""
    for char in the_string:
        if char.lower() in alphabet:
            new_string += char
        
    return new_string

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    user_string = input()
    new_string = remove_non_alpha_chars(user_string)
    print(new_string)
