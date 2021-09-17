months = [  
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]

days_in_month = [
            31,
            28,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31
]

weekdays = [
            "Su",
            "Mo",
            "Tu",
            "We",
            "Th",
            "Fr",
            "Sa"    
        ]   

#--------------------Helper Functions--------------------

def center(msg: str, width: int, lean = "left", fill_char=" ") -> str:
    '''
    Concept taken from function written in class
    Centers a message within a defined width the message is placed in. 
    Default: lean='left', other option 'right'
    Default: fill_char=' ', can be any other character
    >>> center('hello', 10)
    '  hello'

    >>> center('January 2017', 20, lean='right')
    '    January 2017    '

    >>> center('2', 20,lean='right', fill_char='!')
    '!!!!!!!!!!2!!!!!!!!!'

    >>> center('', 2)
    ''

    >>> center('3.14159', 0, fill_char='K')
    '3.14159'
    '''
    length = len(msg)

    if length == 0:
        return ""

    #Leans text to left side (default), specified with parameter 'lean'
    if lean == "left":
        left_side = (width - length) // 2
        right_side = width - length - left_side
    
    #Leans text to right side, specified with parameter 'lean'
    elif lean == "right":
        right_side = (width - length) // 2
        left_side = width - length - right_side
        return f"{fill_char*left_side}{msg}{fill_char*right_side}"

    return f"{fill_char*left_side}{msg}"

def convert_month(year: int, month: int) -> tuple:
    '''
    Converts first or second month to values 12 and 13 respectively to fit in
    >>> convert_month(2020, 3)
    (2020, 3)

    >>> convert_month(1949, 1)
    (1948, 13)

    >>> convert_month(0, 0)
    (0, 0)
    '''
    if month == 1 or month == 2:
        month += 12
        year -= 1

    return (year, month)


#--------------------Main Functions--------------------


def startingDayOfWeek(month: int, year: int) -> str:
    '''
    Taken from Warmup 2b
    >>> startingDayOfWeek(2021,9)
    4

    >>> startingDayOfWeek(2020,9)
    3

    >>> startingDayOfWeek(1999, 2)
    2

    >>> startingDayOfWeek(2021, 2)
    2

    >>> startingDayOfWeek(2020, 5)
    6

    >>> startingDayOfWeek(2005, 1)
    7

    >>> startingDayOfWeek(2020, 2)
    7
    '''
    day = 1

    calc = convert_month(year, month)
    year = calc[0]
    month = calc[1]
    k = year % 100
    j = year//100
    day_of_week = (day + (13*(month+1)//5) + k + (k//4) + (j//4) - 2*j) % 7

    if day_of_week == 0:
        day_of_week = 7

    return day_of_week

def get_month_name(number: int) -> str:
    '''
    Returns the name of a month's corresponding numerical value.
    >>> get_month_name(1)
    'January'

    >>> get_month_name(12)
    'December'

    >>> get_month_name(9)
    'September'
    '''

    return months[number-1]

def monthCalendarFor(num_month: int, year: int) -> None:
    #NOTE: Code design in this function is exceptionally poor. Is there any way I could get some feedback on getting the same result in fewer lines? :)
    '''
    Prints a calendar for a given month and year.
    ---Paramteres---
    month: the month
    year: the year
    first_day: the first day of a month in integer form (i.e. 1 = Sunday, 5 = Thursday, etc.)
    num_days_month: The number of days in a month incremented by '1' because of the upper limit rule of the range() function
    ''' 

    NEW_LINE = "\n"
    LEN_CALENDAR = 20  
    CALENDER_HEIGHT = 8

    month = get_month_name(num_month)

    first_day = startingDayOfWeek(num_month, year)

    num_days_month = daysInMonth(num_month, year) + 1

    calendar = f'{(center(f"{month} {year}", LEN_CALENDAR))}\n'

    real_calender_height = 1

    #Prints weekdays with two spaces after each day unless 'i' is the last in the list, in which case it instead prints the weekday and a newline.
    for i in range(len(weekdays)):
        calendar += f"{weekdays[i] + NEW_LINE if i+1 == len(weekdays) else weekdays[i] + ' '}"
    
    real_calender_height += 1
    
    # print(f'First Day: {first_day}')
    distance = (" " *3) * (first_day-1)
    spaces = len(distance)
    # print(f"Distance: {distance}")
    calendar += str(distance)
    second_condition = (len(weekdays)+2) - first_day

    #Prints the first row of dates in the calendar
    for i in range(1, second_condition):
        calendar += f"{center(str(i), 2, lean='right') + NEW_LINE if i+1 == second_condition else center(str(i), 2, lean='right') + ' '}"

    real_calender_height += 1

    next_value = i + 1 
    
    limit_reached = False
    #prints all other rows of dates in the calendar
    for _ in range(4, 9):
        for k in range(next_value, next_value+7 if next_value+7 < num_days_month else num_days_month):
            if k+1 == num_days_month:
                calendar += f"{center(str(k), 2, lean='right')}"
                limit_reached = True
                break
            else:
                calendar += f"{center(str(k), 2, lean='right') + NEW_LINE if k == next_value + 6 else (center(str(k), 2, lean='right')) + ' '}"
        
        #Checks if all dates have been printed. Extremely poor implementation of desired outcome, in a time crunch and will have to do.
        if limit_reached:
            real_calender_height += 1
            break
        else:
            real_calender_height += 1

        next_value += 7
        
    while real_calender_height < CALENDER_HEIGHT:
        calendar += "\n"
        real_calender_height += 1

    return calendar + "\n"

def daysInMonth(month: int, year: int) -> int:
    '''
    Returns the number of days in any given month January - December. 
    ---Parameters---
        month: the month
        year: the year
    
    >>> daysInMonth(9, 2021)
    30

    >>> daysInMonth(2, 2021)
    28

    >>> daysInMonth(2, 2000)
    29

    >>> daysInMonth(2, 1900)
    28

    >>> daysInMonth(2, 1984)
    29
    '''
    if month == 2: #If the month is February (which can have 28 or 29 days depending on the year)
        if year % 4 == 0: #if year is divisible by 4
            if year % 100 == 0: #If year is start of new century, i.e. 1600, 1900, 2000 etc.
                if year % 400 == 0: #If year is divisible by 400 when it is also divisible by 100
                    return days_in_month[month - 1] + 1    #Return leap year month for February
                else:
                    return days_in_month[month - 1] #If year is divisible by 100 but not 400, not a leap year and return the default of 28 days.
            else:
                return days_in_month[month - 1] + 1 #If year is divisible by 4 but not the start of a new century

    return days_in_month[month - 1]  #if base condition is false

def main():
    '''
    Main function, program execution rooted in this function.
    '''
    user_input = input()    
    input_str = user_input.split()
    # month_name = get_month_name(int(input_str[0]))
    # days_month = daysInMonth(int(input_str[0]), int(input_str[1]))
    
    # day = int(startingDayOfWeek(int(input_str[1]), int(input_str[0])))

    calendar = monthCalendarFor(int(input_str[0]), int(input_str[1])) #Added 1 to days_month so that the range() function doesn't chop off the last day of the month

    print(calendar)

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main()

    # print(startingDayOfWeek(2, 2000))