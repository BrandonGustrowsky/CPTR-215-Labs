class Date:
    DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    LEN_MONTHS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    KEYS = list(LEN_MONTHS.keys())

    VALUES = list(LEN_MONTHS.values())

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def is_leap_year(cls, year):
        """
        >>> Date.is_leap_year(2021)
        False
        >>> Date.is_leap_year(2000)
        True
        >>> Date.is_leap_year(8036)
        True
        >>> Date.is_leap_year(3000)
        False
        """
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    def __repr__(self):
        '''
        >>> Date(2011, 5, 4)
        Date(2011, 5, 4)
        >>> Date(1995, 3, 27)
        Date(1995, 3, 27)
        '''
        return f"Date({self.year}, {self.month}, {self.day})"

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
        if Date.is_leap_year(self.year) and self.month == 2 and self.day == 28: 
            return Date(self.year, self.month, self.day+1)

        #If self.day is the last day of the month
        if self.day >= Date.LEN_MONTHS[self.month]:
            #If last day of year
            if self.month == 12:
                return Date(self.year+1, 1, 1)
            else:
                return Date(self.year, self.month+1, 1)
        
        return Date(self.year, self.month, self.day+1)

    def previous_day(self):
        '''
        >>> Date(2021, 5, 6).previous_day()
        Date(2021, 5, 5)
        >>> Date(2020, 3, 1).previous_day()
        Date(2020, 2, 29)
        >>> Date(2000, 3, 1).previous_day()
        Date(2000, 2, 29)
        >>> Date(3740, 1, 1).previous_day()
        Date(3739, 12, 31)
        '''
        if Date.is_leap_year(self.year) and self.month == 3 and self.day == 1: 
            return Date(self.year, self.month-1, 29)

        #If self.day is the first day of the month
        if self.day == 1:
            #If first day of year
            if self.month == 1:
                return Date(self.year-1, 12, 31)
            else:
                return Date(self.year, self.month-1, self.LEN_MONTHS[self.month-1])
        
        return Date(self.year, self.month, self.day-1)

    def __add__(self, number):
        '''
        >>> Date(2011, 5, 3) + 4
        Date(2011, 5, 7)
        >>> Date(1950, 1, 28) + 5
        Date(1950, 2, 2)
        >>> Date(2020, 2, 27) + 2
        Date(2020, 2, 29)
        >>> Date(2019, 1, 1) + 365
        Date(2020, 1, 1)
        >>> Date(1999, 12, 25) + 7
        Date(2000, 1, 1)
        '''
        if type(number) == int:
            if number < 0:
                return self.__sub__(abs(number))
            else:
                new_date = Date(self.year, self.month, self.day)
                for _ in range(1, number+1):
                    new_date = Date(new_date.year, new_date.month, new_date.day).next_day()
                
            return new_date

    def get_days_to_current_day(self):
        '''
        >>> Date(2020, 4, 6).get_days_to_current_day()
        97
        >>> Date(1900, 3, 30).get_days_to_current_day()
        89
        >>> Date(2013, 6, 12).get_days_to_current_day()
        163
        '''
        month_offset = 0
        for i in range(self.month-1):
            if i == 1 and Date.is_leap_year(self.year):
                month_offset += 29
            else:
                month_offset += self.DAYS_PER_MONTH[i]
        
        return month_offset + self.day

    def __sub__(self, other):
        '''
        >>> Date(2000, 1, 3) - 4
        Date(1999, 12, 30)
        >>> Date(1900, 4, 29) - 29
        Date(1900, 3, 31)
        >>> Date(1900, 3, 5) - 10
        Date(1900, 2, 23)
        >>> Date(2021, 7, 14) - Date(2021, 7, 10)
        4
        >>> Date(2021, 11, 17) - Date(2020, 11, 12)
        370
        '''
        if type(other) == int:
            if other < 0:
                return self.__add__(abs(other))
            else:
                new_date = Date(self.year, self.month, self.day)
                for _ in range(1, other+1):
                    new_date = Date(new_date.year, new_date.month, new_date.day).previous_day()

                return new_date

        elif type(other) == Date:
            year_offset = 0
            if self < other:
                return -(other - self)
            if self.year != other.year:
                for year in range(other.year, self.year):
                    year_offset += 366 if Date.is_leap_year(year) else 365
                    
            return year_offset + self.get_days_to_current_day() - other.get_days_to_current_day()

    def __eq__(self, other):
        '''
        >>> Date(2020, 1, 1) == Date(2020, 1, 2)
        False
        >>> Date(1945, 6, 20) == Date(1945, 6, 20)
        True
        >>> Date(1886, 12, 27) == Date(1886, 4, 6)
        False
        '''
        if self.year == other.year:
            if self.month == other.month:
                if self.day == other.day:
                    return True

        return False

    def __ne__(self, other):
        '''
        >>> Date(5, 4, 2) != Date(5, 4, 2)
        False
        >>> Date(5668, 12, 9) != Date(5668, 12, 10)
        True
        >>> Date(3219, 5, 17) != Date(2139, 7, 15)
        True
        '''
        return not self == other

    def __lt__(self, other):
        '''
        >>> Date(6543, 6, 29) < Date(8731, 3, 21)
        True
        >>> Date(8912, 5, 2) < Date(8912, 5, 2)
        False
        >>> Date(5821, 7, 27) < Date(9128, 4, 2)
        True
        >>> Date(3451, 8, 13) < Date(3812, 9, 14)
        True
        '''
        if self.year < other.year:
            return True
        if self.year == other.year:
            if self.month < other.month:
                return True
            if self.month == other.month:
                if self.day < other.day:
                    return True
        return False

    def __gt__(self, other):
        '''
        >>> Date(1823, 3, 2) > Date(1823, 4, 2)
        False
        >>> Date(7381, 4, 29) > Date(8182, 4, 1)
        False
        >>> Date(1999, 10, 19) > Date(1999, 10, 18)
        True
        '''
        return not self <= other

    def __le__(self, other):
        '''
        >>> Date(9812, 2, 1) <= Date(8912, 2, 1)
        False
        >>> Date(7812, 5, 4) <= Date(7812, 5, 4)
        True
        >>> Date(1234, 12, 9) <= Date(3412, 6, 17)
        True
        '''
        return  self < other or self == other

    def __ge__(self, other):
        '''
        >>> Date(3451, 8, 13) >= Date(1831, 9, 3)
        True
        >>> Date(1982, 11, 24) >= Date(1982, 11, 24)
        True
        >>> Date(8312, 7, 15) >= Date(8923, 9, 2)
        False
        '''
        return not self < other

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(Date(8035, 5, 5) + 453)