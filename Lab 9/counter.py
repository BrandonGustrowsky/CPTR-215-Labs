"""counters.py - Connectable Counters

Prof. O & CPTR-215
2021-10-28 extract neighbor functionality
2021-10-27 add more polymorphism
2021-10-25 explore inheritance
2021-10-22 add doctests
2021-10-13 fix 12-hour clock using composition
2021-10-11 4-bit counter, 24-hour clock, (broken) 12-hour clock
2021-10-01 first draft

To Do:
- finish SC constructor - DONE
- add starting value parameter to BC, LC, EC, & FLC
- match existing classes to class diagram
- create EnumCounter (?), Date, Clock12, and Clock24 classes ----- NOT CREATING EnumCounter
- add lots of doctests
"""

class Neighbor:
    """Neighbor represents an object that can:
    1) Connect to one or more neighbors (and be connected to also), and
    2) Notify those neighbors when it overflows,
        asking them to increment or reset themselves.
    """
    def __init__(self):
        self.increment_neighbors = [] #List of neighbors
        self.reset_neighbors = []   #List of neighbors
    def __str__(self):
        return (str(self.get_neighbor()) if self.get_neighbor() != None \
            else "") + str(self.get_value())
    def increment(self):
        self.notify_increment()
        self.notify_reset()
    def reset(self):
        pass
    def get_value(self):
        pass
    def add_increment(self, new_neighbor):
        if new_neighbor not in self.increment_neighbors:
            self.increment_neighbors.append(new_neighbor)
        return self
    def remove_increment(self, old_neighbor):
        if old_neighbor in self.increment_neighbors:
            self.increment_neighbors.remove(old_neighbor)
    def notify_increment(self):
        """Notifies all increment neighbors of overflow"""
        for neighbor in self.increment_neighbors:
            neighbor.increment()
    def add_reset(self, new_neighbor):
        if new_neighbor not in self.reset_neighbors:
            self.reset_neighbors.append(new_neighbor)
        return self
    def remove_reset(self, old_neighbor):
        if old_neighbor in self.reset_neighbors:
            self.reset_neighbors.remove(old_neighbor)
    def notify_reset(self):
        for neighbor in self.reset_neighbors:
            neighbor.reset()
    def get_neighbor(self):
        """Returns first neighbor, for printing"""
        return self.increment_neighbors[0] \
               if len(self.increment_neighbors) >= 1 \
               else None

class BoundedCounter(Neighbor):
    #Added Starting Value
    def __init__(self, lower_bound, upper_bound, starting_value=None):
        """
        >>> bit = BoundedCounter(0, 1)
        >>> bit == None
        False
        >>> type(bit) == BoundedCounter
        True
        >>> bit.lower_bound
        0
        >>> bit.upper_bound
        1
        >>> bit.current_value
        0
        """
        super().__init__()
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.starting_value = starting_value
        self.current_value = self.starting_value if self.starting_value != None else self.lower_bound
    def increment(self):
        """
        >>> digit = BoundedCounter(0, 9)
        >>> digit.increment()
        >>> digit.current_value
        1
        >>> for _ in range(8): digit.increment()
        >>> digit.get_value()
        9
        >>> digit.increment()
        >>> digit.get_value()
        0
        """
        if self.current_value == self.upper_bound:
            self.current_value = self.lower_bound
            self.notify_increment()
            self.notify_reset()
        else:
            self.current_value += 1
    def reset(self):
        self.current_value = self.lower_bound
    def get_value(self):
        return self.current_value        

class ListCounter(BoundedCounter):
    #Added Starting Value
    def __init__(self, items, starting_value=None):
        self.items = tuple(items)
        self.starting_value = starting_value
        #Used the 'index()' method to grab the index of starting_value item in the list
        super().__init__(0, len(self.items) - 1, self.items.index(self.starting_value) if self.starting_value in self.items else None)
    def get_value(self):
        return self.items[super().get_value()]
    
class FixedLengthCounter(BoundedCounter):
    #Added Starting Value
    def __init__(self, lo, hi, length, starting_value=None):
        self.starting_value = starting_value
        super().__init__(lo, hi, starting_value)
        self.length = length
    def get_value(self):
        return f"{super().get_value():0{self.length}}"
    
class StaticConnector(Neighbor):
    def __init__(self, string):
        super().__init__()
        self.string = string
    def get_value(self):
        return self.string

class Clock12:
    def __init__(self, h, m):
        self.h = h
        self.m = m

        self.ampm = ListCounter(["AM", "PM"])
        self.space = StaticConnector(" ").add_increment(self.ampm)
        self.hour = ListCounter([12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], self.h).add_increment(self.space)
        self.colon = StaticConnector(":").add_increment(self.hour)
        self.minute = FixedLengthCounter(0, 59, 2, self.m).add_increment(self.colon)
    
    def __str__(self):
        return f"{self.minute}" 

    def next_minute(self):
        self.minute.increment()

class Clock24:
    def __init__(self, h, m):
        self.h = h
        self.m = m

        self.hour = FixedLengthCounter(0, 23, 2, self.h)
        self.colon = StaticConnector(":").add_increment(self.hour)
        self.minute = FixedLengthCounter(0, 59, 2, self.m).add_increment(self.colon)

    def __str__(self):
        return f"{self.minute}"

    def next_minute(self):
        return self.minute.increment()

class Date:
    DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

        self.year = BoundedCounter(1753, 9999, self.y)
        self.dash = StaticConnector("-").add_increment(self.year)
        self.month = FixedLengthCounter(1, 12, 2, self.m).add_increment(self.dash)
        self.dash = StaticConnector("-").add_increment(self.month)
        self.day = FixedLengthCounter(1, self.DAYS_PER_MONTH[self.m-1], 2, self.d).add_increment(self.dash)

    def __str__(self):
        return f"{self.day}"

    def __repr__(self):
        return f"Date({self.y}, {self.m}, {self.d})"

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

        if Date.is_leap_year(self.y) and self.m == 2 and self.d == 28: 
            return Date(self.y, self.m, self.d+1)

        #If self.day is the last day of the month
        if self.d >= Date.DAYS_PER_MONTH[self.m-1]:
            #If last day of year
            if self.m == 12:
                return Date(self.y+1, 1, 1)
            else:
                return Date(self.y, self.m+1, 1)
        
        return Date(self.y, self.m, self.d+1)

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()

    # bit4 = FixedLengthCounter(0, 1, 2)
    # plus = StaticConnector("+").add_increment(bit4)
    # bit2 = BoundedCounter(0, 1).add_increment(plus)
    # dash = StaticConnector("-").add_increment(bit2)
    # bit1 = BoundedCounter(0, 1).add_increment(dash)
    # list1 = ListCounter(["am", "pm"], "pm")

    # for _ in range(20):
    #     print(bit1)
    #     bit1.increment()

    date1 = Date(1929, 2, 28)
 

    print((date1).next_day())
