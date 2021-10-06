"""date.py
Prof. O & CPTR-215
2021-09-29
2021-09-27 first draft
"""

class Date:

    LEN_MONTHS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    KEYS = list(LEN_MONTHS.keys())

    VALUES = list(LEN_MONTHS.values())

    def __init__(self, year, month, day):
        """Initializes a date given a year, month, and day.
        >>> today = Date(2021, 9, 27)
        >>> today.day
        27
        >>> Date(1776, 7, 4).year
        1776
        """
        self.year = year
        self.month = month
        self.day = day

    def day_of_week(self):
        """Determines the day of the week self falls on. 1 = Sun thru 7 = Sat.
        >>> today = Date(2021, 9, 27)
        >>> today.day_of_week()
        2
        >>> Date(2021, 9, 25).day_of_week()
        7
        >>> Date(1776, 7, 4).day_of_week()
        5
        """
        if self.month < 3:
            m = self.month + 12
            y = self.year - 1
        else:
            m = self.month
            y = self.year
        dow = (self.day + (13 * (m + 1)) // 5 + \
               y + y // 4 - y //  100 + y // 400) % 7
        return 7 if dow == 0 else dow

    def previous_day(self):
        '''
        >>> Date(1900, 3, 1).previous_day()
        Date(1900, 2, 28)
        '''
        self = Date(self.year, self.month, self.day)

        if self.is_leap_year():
            if self.month == 3 and self.day == 1:
                return Date(self.year, self.month-1, 29)

        #If self.day is the first day of the month
        if self.day == 1:
            if self.KEYS.index(self.month) != 0 and len(self.KEYS):
                index_of_day = self.KEYS.index(self.month-1)
                self.day = self.VALUES[index_of_day]
                return Date(self.year, self.month-1, self.day)

            if self.KEYS.index(self.month) == 0:
                self.month = self.KEYS[len(self.KEYS)-1]
                index_of_day = self.KEYS.index(self.month)
                self.day = self.VALUES[index_of_day]
                return Date(self.year-1, self.KEYS[len(self.KEYS)-1], self.day)
        
        if self.day == self.VALUES[self.KEYS.index(self.month)]:
            if self.KEYS.index(self.month) != 0 and len(self.KEYS):
                index_of_day = self.KEYS.index(self.month+1)
                self.day = self.VALUES[index_of_day]
                return Date(self.year, self.month+1, self.day)

            if self.KEYS.index(self.month) == len(self.KEYS):
                self.month = self.KEYS[0]
                self.day = self.VALUES[0]
                return Date(self.year+1, self.month, self.day)
            
        
        return Date(self.year, self.month, self.day-1)

    def next_day(self):
        '''
        >>> Date(2021, 5, 6).next_day()
        Date(2021, 5, 7)
        >>> Date(2020, 2, 28).next_day()
        Date(2020, 2, 29)
        >>> Date(2000, 2, 28).next_day()
        Date(2000, 2, 29)
        >>> Date(3740, 2, 1).next_day()
        Date(3740, 2, 2)
        '''

        if self.is_leap_year() and self.month == 2 and self.day == 28: 
            return Date(self.year, self.month, self.day+1)

        #If self.day is the last day of the month
        if self.day >= Date.LEN_MONTHS[self.month]:
            #If last day of year
            if self.month == 12:
                return Date(self.year+1, 1, 1)
            else:
                return Date(self.year, self.month+1, 1)
        
        return Date(self.year, self.month, self.day+1)

    def equals(self, other):
        return True if self.year == other.year and self.month == other.month and self.day == other.day else False

    def before(self, other):
        if self.year < other.year:
            return True
        if self.year == other.year:
            if self.month < other.month:
                return True
            if self.month == other.month:
                if self.day < other.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def after(self, other):
        if other.year < self.year:
            return True
        if other.year == self.year:
            if other.month < self.month:
                return True
            if other.month == self.month:
                if other.day < self.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        

    def __str__(self):
        """Returns a human-readable string representation of self
        in MMM d, yyyy format.
        >>> Date(2000, 1, 1).__str__() # not common
        'Jan 1, 2000'
        >>> str(Date(2021, 9, 27))
        'Sep 27, 2021'
        >>> independence = Date(1776, 7, 4)
        >>> print(independence)
        Jul 4, 1776
        """
        month_name = "BAD Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()[self.month]
        return f"{month_name} {self.day}, {self.year}"
    def __repr__(self):
        """Returns a string that would evaluate to an identical Date object.
        >>> Date(2021, 9, 29).__repr__() # not common
        'Date(2021, 9, 29)'
        >>> Date(1970, 12, 31)
        Date(1970, 12, 31)
        >>> repr(Date(1984, 2, 20))
        'Date(1984, 2, 20)'
        """
        return f"Date({self.year}, {self.month}, {self.day})"
    def is_leap_year(self):
        """Determines whether self is in a leap year.
                    Truth Table
            4s place  2s place  1s place
             div 4 | div 100 | div 400 | leap?
            -------+---------+---------+-------
               0         0         0       0
               0         0         1       X
               0         1         0       X
               0         1         1       X
               1         0         0       1
               1         0         1       X
               1         1         0       0
               1         1         1       1
        >>> Date(2021, 9, 29).is_leap_year()
        False
        >>> Date(1984, 4, 27).is_leap_year()
        True
        >>> Date(2000, 1, 1).is_leap_year()
        True
        >>> Date(1900, 11, 30).is_leap_year()
        False
        """
        return self.year % 400 == 0 or \
               (self.year % 4 == 0 and self.year % 100 != 0)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # print(Date(1905, 12, 31).equals(Date(1905, 2, 31)))

    print(Date(4776, 4, 17).after(Date(4776, 4, 16)))
