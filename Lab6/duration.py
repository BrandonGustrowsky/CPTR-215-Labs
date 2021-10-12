# import math
class Duration:
#FIXME find out the number of seconds in a week and day.
    TIME_ABBREVIATIONS = {"w": 604800, "d": 86400, "h": 3600, "m": 60, "s": 1}

    def __init__(self, *args):
        '''Initializes in three different formats and calculates the value in seconds.
        Formats:
        1) Three integer params - Duration(8, 34, 19)
        2) One string with numbers seperated by ':' - Duration("14:58:8")
        3) One string with abbreviations for specified time - Duration("4d7m27s")
            See the TIME_ABBREVIATIONS dictionary (under class declaration) for full list 
            of accepted abbreviations.
        '''
        #If the time entered is negative
        self.isNegative = False
        args = list(args)
        #If 3 integers were entered, execute this block - Ex: Duration(4:21:57)
        if len(args) == 3:
            for index in range(3):
                if args[index] < 0:
                    self.isNegative = True
                    args[index] = abs(args[index])

            self.hours = args[0]
            self.minutes = args[1]
            self.seconds = self.hours * 3600 + self.minutes * 60 + args[2]
            self.original_seconds = self.seconds
            self.seconds = abs(self.seconds)
   
        #If 1 string was entered:
        elif len(args) == 1:
            if type(args[0]) == int:
                if args[0] < 0:
                    self.isNegative = True
                self.seconds = abs(args[0])
            #If the time was entered in the format of Duration("1:40:12")
            elif ":" in args[0]:
                parameters = args[0].split(":")
                for index in range(3):
                    if int(parameters[index]) < 0:
                        self.isNegative = True
                        parameters[index] = abs(int(parameters[index]))
                self.hours = int(parameters[0])
                self.minutes = int(parameters[1])
                self.seconds = self.hours * 3600 + self.minutes * 60 + int(parameters[2])
            #If the time was entered in the format of Duration("1hr40m12s") 
            else:
                #FIXME Finish implementing isNegative to function
                time_in_seconds = 0
                #Convert *args to a string so it can be spliced
                entered_time = str(args[0])
                #Check if any key from the dict is in the string
                for key, value in self.TIME_ABBREVIATIONS.items():
                    if key in entered_time:
                        #convert the time to seconds and add it to the overall time, which is in seconds
                        time_in_seconds += int(entered_time[0:entered_time.find(key)]) * value
                        if time_in_seconds < 0:
                            self.isNegative = True
                            time_in_seconds = abs(time_in_seconds)
                        #Remove every character from the string that has been accessed.
                        entered_time = entered_time[entered_time.find(key)+1:len(entered_time)]
                self.seconds = time_in_seconds
                self.original_seconds = self.seconds
                self.seconds = abs(self.seconds)

    def time(self):
        '''Returns the time in seconds.
        >>> Duration(25).time()
        25
        >>> Duration(1,2,3).time()
        3723
        >>> Duration('-2m5s').time()
        -125
        '''
        return -self.seconds if self.isNegative == True else self.seconds

    def convert_time_from_seconds(self):
        '''Converts seconds to proper amount of time in 'hours:minutes:seconds' format.
            >>> Duration(4, 0, 53).convert_time_from_seconds()
            '4:00:53'
            >>> Duration(-6, 5, 27).convert_time_from_seconds()
            '-6:05:27'
        '''
        units = [3600, 60]
        return_this_str = f"{'-' if self.isNegative == True else ''}"
        time = abs(self.seconds)
        increment = 0
        for index in range(2):
            return_this_str += f"{'00:' if index != 0 and time // units[index] == 0 else '0:' if index == 0 and str(time // units[index]) == 0 else '0' + str(time // units[index]) + ':' if time // units[index] < 10 and index != 0 else str(time // units[index]) + ':'}"
            time -= (time // units[index]) * units[index]
            increment += 1
        
        return_this_str += f"{'0' + str(time) if time < 10 else str(time)}"
        return return_this_str
        
    def __str__(self):
        '''
        >>> str(Duration(4, 0, 53))
        '4:00:53'
        >>> str(Duration("2d4h7m"))
        '52:07:00'
        '''
        return self.convert_time_from_seconds()

    def __repr__(self):
        '''
        >>> Duration(4,0,53)
        Duration('4:00:53')
        >>> Duration('1h4m2s')
        Duration('1:04:02')
        >>> Duration(54)
        Duration('0:00:54')
        '''

        return f"Duration('{self.convert_time_from_seconds()}')"

    def __eq__(self, other):
        '''
        >>> Duration(1,2,3) == Duration(1,2,4)
        False
        >>> Duration(45) == Duration(45)
        True
        >>> Duration(4) == Duration(-4)
        False
        '''
        return self.time() == other.time()

    def __lt__(self, other):
        '''
        >>> Duration('4h5m2s') < Duration(4,5,1)
        False
        >>> Duration(24) < Duration('3:04:24')
        True
        >>> Duration(-92) < Duration('-1:03:5')
        False
        '''
        return self.time() < other.time()

    def __gt__(self, other):
        '''
        >>> Duration(25) > Duration(24)
        True
        >>> Duration('2:34:12') > Duration(5, 12, 46)
        False
        >>> Duration('2d2m2s') > Duration(12345)
        True
        '''
        return self.time() > other.time()

    def __le__(self, other):
        '''
        >>> Duration(67) <= Duration(-54)
        False
        >>> Duration(12) <= Duration(12)
        True
        >>> Duration(4,3,2) <= Duration(6,5,12)
        True
        '''
        return self.time() < other.time() or self.time() == other.time()

    def __ge__(self, other):
        '''
        >>> Duration(123) >= Duration('1d2m')
        False
        >>> Duration('1h') >= Duration(3600)
        True
        >>> Duration(7654) >= Duration(987)
        True
        '''
        return self.time() > other.time() or self.time() == other.time()

    def __ne__(self, other):
        '''
        >>> Duration(8765) != Duration(8765)
        False
        >>> Duration('6h3m') != Duration('1:02:04')
        True
        >>> Duration('-5h1s') != Duration(5,0,1)
        True
        '''
        return self.time() != other.time()

    def __add__(self, other):
        '''
        >>> Duration(45) + Duration(67)
        Duration('0:01:52')
        >>> Duration('1h') + 45
        Duration('1:00:45')
        >>> Duration(-65) + 12
        Duration('-0:00:53')
        '''
        if type(other) == int:
            return Duration(self.time() + other)
        return (Duration(self.time() + other.time()))

    def __mul__(self, other):
        '''
        >>> Duration(6) * Duration(12)
        Duration('0:01:12')
        >>> Duration('1h') * 2
        Duration('2:00:00')
        >>> Duration(-8) * 15
        Duration('-0:02:00')
        '''
        if type(other) == int:
            return Duration(self.time() * other)
        return Duration(self.time() * other.time())

    def __sub__(self, other):
        '''
        >>> Duration('1h') - Duration(0,45,0)
        Duration('0:15:00')
        >>> Duration('1:00:01') - 120
        Duration('0:58:01')
        >>> Duration(45) - Duration(95)
        Duration('-0:00:50')
        '''
        if type(other) == int:
            return Duration(self.time() - other)
        return Duration(self.time() - other.time())

    def __truediv__(self, other):
        '''
        >>> Duration('1h') / Duration(0,30,0)
        Duration('0:00:02')
        >>> Duration('5m2s') / 46
        Duration('0:00:06')
        >>> Duration('-12:00:00') / Duration(60)
        Duration('-0:12:00')
        '''
        if type(other) == int:
            return Duration(self.time() // other)
        return Duration(self.time() // other.time())
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
            