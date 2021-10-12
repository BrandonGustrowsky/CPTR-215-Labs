class Fraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

        a, b = numerator, denominator
        while b != 0:
            a, b = b, a % b
            
        self.numerator = numerator // a
        self.denominator = denominator // a

    def __repr__(self):
        '''
        >>> Fraction(45, 97)
        Fraction(45, 97)
        >>> Fraction(37, 42)
        Fraction(37, 42)
        >>> Fraction(4, 1)
        Fraction(4)
        '''
        return f"Fraction({self.numerator}, {self.denominator})" if self.denominator != 1 else f"Fraction({self.numerator})"

    def __str__(self):
        '''
        >>> str(Fraction(1, 3))
        '1/3'
        >>> str(Fraction(4, 16))
        '1/4'
        >>> str(Fraction(3, 1))
        '3'
        '''
        return f"{self.numerator}/{self.denominator}" if self.denominator != 1 else f"{self.numerator}"

    def __eq__(self, other):
        '''
        >>> Fraction(1, 3) == Fraction(1, 3)
        True
        >>> Fraction(5, 10) == Fraction(1, 2)
        True
        >>> Fraction(4, 7) == Fraction(7, 4)
        False
        >>> Fraction(4, 5) == Fraction(4, 9)
        False
        '''
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        '''
        >>> Fraction(1,3) < Fraction(1,2)
        True
        >>> Fraction(1,2) < Fraction(1,2)
        False
        >>> Fraction(6,21) < Fraction(8,32)
        False
        '''
        if self.denominator == other.denominator:
            return self.numerator < other.numerator
        else:
            return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        '''
        >>> Fraction(1,3) > Fraction(1,4)
        True
        >>> Fraction(2,5) > Fraction(2,5)
        False
        >>> Fraction(6,4) > Fraction(9,2)
        False
        '''
        return not self <= other

    def __le__(self, other):
        '''
        >>> Fraction(3,5) <= Fraction(7,4)
        True
        >>> Fraction(4,1) <= Fraction(3,2)
        False
        >>> Fraction(2,3) <= Fraction(2,3)
        True
        '''
        return self == other or self < other    

    def __ge__(self, other):
        '''
        >>> Fraction(3,2) >= Fraction(3,4)
        True
        >>> Fraction(2,5) >= Fraction(2,5)
        True
        '''
        return not self < other

    def __ne__(self, other):
        '''
        >>> Fraction(1,4) != Fraction(2,3)
        True
        >>> Fraction(4,5) != Fraction(4,5)
        False
        '''
        return not self == other
    

    def __add__(self, other):
        '''
        >>> Fraction(1, 3) + Fraction(2, 3)
        Fraction(1)
        '''
        return Fraction((self.denominator*other.numerator)+(self.numerator*other.denominator), self.denominator*other.denominator)

    def __sub__(self, other):
        '''
        >>> Fraction(2,3) - Fraction(1,3)
        Fraction(1, 3)
        >>> Fraction(6,5) - Fraction(1/2)
        Fraction(7, 10)
        '''
        return Fraction((int(self.numerator*other.denominator))-int((self.denominator*other.numerator)), int(self.denominator*other.denominator))

    def __mul__(self, other):
        '''
        >>> Fraction(2,3)*Fraction(5,2)
        Fraction(5, 3)
        >>> Fraction(5)*Fraction(12)
        Fraction(60)
        '''
        return Fraction(self.numerator*other.numerator, self.denominator* other.denominator)

    def __truediv__(self, other):
        '''
        >>> Fraction(5,2) / Fraction(5,4)
        Fraction(2)
        >>> Fraction(4,7) / Fraction(19,6)
        Fraction(24, 133)
        '''
        return Fraction(self.numerator*other.denominator, self.denominator*other.numerator)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
