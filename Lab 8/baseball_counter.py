from enum import Enum

class HalfInning(Enum):
    TOP = 0
    BOTTOM = 1

class BoundedCounter:
    def __init__(self, lower, upper, current_count=None, neighbor=None):
        self.lower = lower
        self.upper = upper
        self.neighbor = neighbor
        self.current_count = current_count if current_count else self.lower
    
    
    def increment(self):
        '''
        >>> x = BoundedCounter(0, 4, 0)
        >>> x.increment()
        >>> x.value() == 1
        True
        >>> x = BoundedCounter(0, 3, 1, 'outs')
        >>> x.increment()
        >>> x.value() == 2
        True
        '''
        if self.current_count == self.upper:
            if self.neighbor:
                    self.neighbor.increment()
            self.current_count = self.lower
        else:
            self.current_count += 1

    def __str__(self):
        '''
        >>> str(BoundedCounter(0, 9))
        '0'
        >>> str(BoundedCounter(2, 4))
        '2'
        '''
        return f"{self.neighbor if self.neighbor else ''}{str(self.current_count)}"
    
    def value(self):
        '''
        >>> BoundedCounter(0,4,1).value()
        1
        >>> BoundedCounter(2, 5, 4).value()
        4
        '''
        return self.current_count

    def reset(self):
        '''
        >>> x = BoundedCounter(1, 10)
        >>> x.increment()
        >>> x.reset()
        >>> str(x)
        '1'
        >>> y = BoundedCounter(2, 20)
        >>> y.increment()
        >>> y.reset()
        >>> str(y)
        '2'
        
        '''
        self.current_count = self.lower

class ListCounter:
    def __init__(self, items, neighbor=None):
        self.items = tuple(items)
        self.index = BoundedCounter(0, len(self.items) - 1, 0, neighbor)

    def increment(self):
        '''
        >>> x = ListCounter(["a", "b"])
        >>> x.increment()
        >>> x.get_value() == 'b'
        True
        >>> y = ListCounter(['c', 'd', 'e'])
        >>> y.increment()
        >>> y.increment()
        >>> y.get_value() == 'e'
        True
        '''
        self.index.increment()

    def get_value(self):
        '''
        
        '''
        return self.items[self.index.value()]
    
    def reset(self):
        self.index.reset()

class BaseballCounter():
    def __init__(self, balls=0, strikes=0, outs=0, half=HalfInning.TOP, inning=1):
        self.balls = BoundedCounter(0, 3, balls)
        self.inning = BoundedCounter(1, 9, inning)
        self.half = ListCounter(HalfInning, self.inning)
        self.outs = BoundedCounter(0, 2, outs, self.half)
        self.strikes = BoundedCounter(0, 2, strikes, self.outs)

        while self.half.get_value() != half:
            self.half.increment()
            
    def ball(self):
        '''
        >>> x = BaseballCounter()
        >>> x.ball()
        >>> x.balls.value() == 1
        True
        >>> x = BaseballCounter(1, 9, 3)
        >>> x.ball()
        >>> x.balls.value() == 2
        True
        '''
        if self.balls.value() == 3:
            self.strikes.reset()
        self.balls.increment()

    def strike(self):
        '''
        >>> x = BaseballCounter()
        >>> x.strike()
        >>> x.strikes.value() == 1
        True
        >>> x = BaseballCounter(1, 2)
        >>> x.strike()
        >>> x.strikes.value() == 0
        True
        '''
        self.strikes.increment()
        if self.strikes.value() == 0:
            self.new_batter()
        

    def out(self):
        '''
        >>> x = BaseballCounter(2, 2, 1)
        >>> x.out()
        >>> x.outs.value() == 2
        True
        >>> y = BaseballCounter(0, 2, 2)
        >>> x.out()
        >>> x.outs.value() == 0
        True
        '''
        self.outs.increment()
        if self.outs.value() == 0:
            self.new_batter()

    def new_batter(self):
        '''
        >>> x = BaseballCounter(2, 2, 1)
        >>> x.new_batter()
        >>> x.balls.value() == 0
        True
        >>> y = BaseballCounter(3, 2, 1)
        >>> y.new_batter()
        >>> y
        BaseballCounter(0, 0, 1, HalfInning.TOP, 1)
        '''
        self.balls.reset()
        self.strikes.reset()

    def new_game(self):
        '''
        >>> x = BaseballCounter(2, 2, 2, HalfInning.BOTTOM, 9)
        >>> x.new_game()
        >>> x
        BaseballCounter(0, 0, 0, HalfInning.TOP, 1)
        >>> y = BaseballCounter(1, 2, 1)
        >>> y.new_game()
        >>> y.balls.value() == 0
        True
        '''
        self.balls.reset()
        self.strikes.reset()
        self.outs.reset()
        self.half.reset()
        self.inning.reset()

    @staticmethod
    def is_plural(word, number):
        '''
        Determines if a word is plural based on a number passed.
       >>> BaseballCounter.is_plural('junior', 5)
       'juniors'
       >>> BaseballCounter.is_plural('out', 1)
       'out'
       >>> BaseballCounter.is_plural('safe', 2)
       'safes'
        '''
        if number == 1:
            return word
        else:
            return word+"s"

    def __repr__(self):
        '''
        >>> BaseballCounter(1, 1, 1, HalfInning.BOTTOM, 5)
        BaseballCounter(1, 1, 1, HalfInning.BOTTOM, 5)
        >>> BaseballCounter(2, 2, 2, HalfInning.TOP, 8)
        BaseballCounter(2, 2, 2, HalfInning.TOP, 8)
        '''
        return f"BaseballCounter({self.balls.value()}, {self.strikes.value()}, {self.outs.value()}, {self.half.get_value()}, {self.inning.value()})"

    def __str__(self):
        '''
        >>> str(BaseballCounter(3, 1, 1, HalfInning.TOP, 9))
        '3 balls, 1 strike, 1 out, top of the 9th inning'
        >>> str(BaseballCounter(2, 2, 2, HalfInning.BOTTOM, 2))
        '2 balls, 2 strikes, 2 outs, bottom of the 2nd inning'
        >>> str(BaseballCounter(2, 1, 2, HalfInning.BOTTOM, 3))
        '2 balls, 1 strike, 2 outs, bottom of the 3rd inning'

        '''
        places = ["st", "nd", "rd", "th"]
        inning_abbreviation = places[self.inning.value()-1] if self.inning.value() < 5 else "th"
        return f"{self.balls.value()} {BaseballCounter.is_plural('ball', self.balls.value())}, " \
            f"{self.strikes.value()} {BaseballCounter.is_plural('strike', self.strikes.value())}, {self.outs.value()} {BaseballCounter.is_plural('out', self.outs.value())}, "\
            f"{'top' if self.half.get_value() == HalfInning.TOP else 'bottom'} of the {self.inning.value()}{inning_abbreviation} inning"

    
if __name__ == "__main__":
    # print("\n\n\n\n\n")
    import doctest
    doctest.testmod()

  
