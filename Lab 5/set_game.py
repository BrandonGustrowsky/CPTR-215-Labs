from enum import Enum
import random

class Fill(Enum):
    EMPTY = 0
    SHADED = 1
    FILLED = 2
    
class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

class Shape(Enum):
    QUAD = 0
    OVAL = 1
    PYRAMID = 2

class SetCard:
    def __init__(self, number, fill, color, shape):
        '''int in [1,3], Fill, Color, Shape -> SetCard'''
        self.number=  number
        self.fill = fill
        self.color = color
        self.shape = shape

    def __str__(self):
        '''Human-readable representation of this card.
        >>> str(SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL))
        '1SBO'
        >>> str(SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD))
        '2ERQ'
        '''
        return f'{self.number}{self.fill.name[0]}{self.color.name[0]}{self.shape.name[0]}'

    def __repr__(self):
        '''Python code to recreate this card.
        >>> SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        >>> repr(SetCard(2,Fill.EMPTY,Color.RED,Shape.QUAD))
        'SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD)'
        '''
        return f'SetCard({self.number}, {self.fill}, {self.color}, {self.shape})'
    
    def set_third_value(self, original, other, Enum_type=None):
        '''Sets the third value based on the other two values.
        If an Enum_type (Enumeration) is specified, then method loops through the different names in an enumeration,
        else it assumes integer value was passed, and runs second for loop outside of Enum_type.
        '''
        if Enum_type:
            for name in Enum_type:
                if name != original and name != other:
                    return name
        for num in range(1,4):
            if num != original and num != other:
                return num
    
    def is_attribute_equal(self, original, other):
        '''Determines if two attributes of a card are equal by adding them in a set. If the set length is 1,
        the cards are equal. Otherwise the cards are not equal.
        Note: Parameters 'original' and 'other' are not a full SetCard, rather attributes of a SetCard,
        i.e. original = SetCard.number, other = SetCard.number etc.
        # >>> is_attribute_equal(FILL.SHADED, FILL.SHADED)
        # True
        # >>> is_attribute_equal(1, 3)
        # False
        '''
        card_set = {original, other}
        if len(card_set) == 1:
            return True
        else:
            return False

    def third_card(self, other):
        '''Returns the third card that makes a set with self and other.
        >>> card1 = SetCard(2, Fill.EMPTY, Color.RED, Shape.QUAD)
        >>> card2 = SetCard(1, Fill.SHADED, Color.BLUE, Shape.OVAL)
        >>> print(card1.third_card(card2))
        3FGP
        >>> print(card2.third_card(card1))
        3FGP
        '''
        if self.is_attribute_equal(self.number, other.number):
            third_number = self.number
        else:
            third_number = self.set_third_value(self.number, other.number)

        if self.is_attribute_equal(self.fill, other.fill):
            third_fill = self.fill
        else:
            third_fill = self.set_third_value(self.fill, other.fill, Fill)

        if self.is_attribute_equal(self.color, other.color):
            third_color = self.color
        else:
            third_color = self.set_third_value(self.color, other.color, Color)
            
        if self.is_attribute_equal(self.shape, other.shape):
            third_shape = self.shape
        else:
            third_shape = self.set_third_value(self.shape, other.shape, Shape)

        return SetCard(third_number, third_fill, third_color, third_shape)

def make_deck():
    '''Returns a list containing a complete Set deck with 81 unique cards.'''
    card_deck = []

    for number in range(3):
        for fill_index in range(len(Fill)):
            for color_index in range(len(Color)):
                for shape_index in range(len(Shape)):
                    card_deck.append(SetCard(number+1, Fill(fill_index), Color(color_index), Shape(shape_index)))

    return random.sample(card_deck, len(card_deck))

def cards_in_set(card1, card2, card3) -> bool:
    '''Adds 3 cards to a set. If the length of the set is 3 or 1, returns True.
    If all cards are the same, set length = 1. If all cards are different, set length = 3. 
    Returns False if set length = 2 because two cards are the same and one is different.
    >>> cards_in_set(Shape.PYRAMID, Shape.OVAL, Shape.QUAD)
    True
    >>> cards_in_set(1, 1, 2)
    False
    >>> cards_in_set(Color.BLUE, Color.BLUE, Color.BLUE)
    True
    >>> cards_in_set(Fill.EMPTY, Fill.SHADED, Fill.SHADED)
    False
    '''
    set_cards = {card1, card2, card3}
    if len(set_cards) == 1 or len(set_cards) == 3:
        return True
    else:
        return False



def is_set(card1: SetCard, card2: SetCard, card3: SetCard):
    '''Determines whether the 3 cards make a set.
    (For each of the 4 traits, all 3 cards are either the same, or all 3 are different.)
    >>> is_set(SetCard(1, Fill.EMPTY, Color.BLUE, Shape.OVAL), SetCard(2, Fill.EMPTY, Color.GREEN, Shape.OVAL), SetCard(3, Fill.EMPTY, Color.RED, Shape.OVAL))
    True
    >>> is_set(SetCard(1, Fill.EMPTY, Color.BLUE, Shape.OVAL), SetCard(1, Fill.EMPTY, Color.GREEN, Shape.OVAL), SetCard(3, Fill.EMPTY, Color.RED, Shape.OVAL))
    False
    >>> is_set(SetCard(1, Fill.EMPTY, Color.GREEN, Shape.QUAD), SetCard(2, Fill.EMPTY, Color.GREEN, Shape.PYRAMID), SetCard(3, Fill.EMPTY, Color.GREEN, Shape.PYRAMID))
    False
    '''
    if cards_in_set(card1.number, card2.number, card3.number) and cards_in_set(card1.fill, card2.fill, card3.fill) and cards_in_set(card1.color, card2.color, card3.color) and cards_in_set(card1.shape, card2.shape, card3.shape):
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()