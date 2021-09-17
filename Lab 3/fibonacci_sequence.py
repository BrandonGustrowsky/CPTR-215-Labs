def fibonacci(n: int):
    '''
    >>> fibonacci(7)
    13

    >>> fibonacci(15)
    610

    >>> fibonacci(-75)
    -1

    >>> fibonacci(0)
    0
    '''
    if n < 0:
        return -1

    answer = 0
    previous_answer = 0

    for number in range(0, n+1):

        if number == 1:
            answer += 1
            # previous_answer = 1
            continue
        
        temp = answer
        answer += previous_answer
        previous_answer = temp

    return answer

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    start_num = int(input())
    print('fibonacci({}) is {}'.format(start_num, fibonacci(start_num)))