from os import name


weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sabbath"]

def nameForDayOfWeekNumber(dayNumber: int) -> str:
    '''
    >>> nameForDayOfWeekNumber(1)
    'Sunday'

    >>> nameForDayOfWeekNumber(7)
    'Saturday'

    >>> nameForDayOfWeekNumber(5)
    'Thursday'

    >>> nameForDayOfWeekNumber(2)
    'Monday'
    '''
    for day in range(len(weekdays)):
        if dayNumber-1 == day:
            return weekdays[day]

def convert_month(year: int, month: int) -> tuple:
    if month == 1 or month == 2:
        month += 12
        year -= 1

    return (year, month)

def dayOfWeekForDate(year: int, month: int, day: int) -> str:
    '''
    >>> dayOfWeekForDate(2021,9,9)
    5

    >>> dayOfWeekForDate(2020,9,9)
    4

    >>> dayOfWeekForDate(1999, 2, 27)
    7

    >>> dayOfWeekForDate(2021, 2, 28)
    1

    >>> dayOfWeekForDate(2020, 5, 3)
    1

    >>> dayOfWeekForDate(2005, 1, 1)
    7

    >>> dayOfWeekForDate(2020, 2, 29)
    7
    '''
    calc = convert_month(year, month)
    year = calc[0]
    # print(f"year: {year}")
    month = calc[1]
    k = year % 100
    j = year//100
    day_of_week = (day + (13*(month+1)//5) + k + (k//4) + (j//4) - 2*j) % 7

    # print(day_of_week)


    if day_of_week == 0:
        day_of_week = 7

    return day_of_week


if __name__ == "__main__":
    import doctest
    doctest.testmod()

