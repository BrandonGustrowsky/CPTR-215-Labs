def get_total_days(age: int) -> int:
    '''
    >>> get_total_days(20)
    7305

    >>> get_total_days(0)
    0
    >>> get_total_days(100)
    36524

    >>> get_total_days(200000)
    73048000
    '''
    days = age * 365.24

    return round(days)

def get_age(year: int) -> int:
    '''
        >>> get_age(2002)
        19

        >>> get_age(2021)
        0

        >>> get_age(2020)
        1

        >>> get_age(1990)
        31
    '''
    return 2021 - year

def print_year(year: int) -> None:
    print(f"\nYou entered: {year}")

def main():
    born_year = int(input("Enter the year you were born (4 digits, i.e., 1998): "))
    print_year(born_year)

    age = get_age(born_year)
    print(f"On your birthday this year, you'll be {age} years old.")

    days = get_total_days(age)
    print(f"You'll have lived {int(days)}±1 days.")


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main()
