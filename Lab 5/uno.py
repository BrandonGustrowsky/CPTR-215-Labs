import random

class UnoCard:

    RANKS = ["S", "D", "R", "W", "F"]

    def __init__(self, color, rank):
        self.color = color
        self.rank = rank

    def can_be_played_on(self, other):
        '''Takes another card and determines whether this card can be played on it. 
        following standard rules (matches color or number/symbol, or is a Wild/Draw Four).
        >>> UnoCard("Y", "2").can_be_played_on(UnoCard("Y", "4"))
        True
        >>> UnoCard("R", "3").can_be_played_on(UnoCard("G", "3"))
        True
        >>> UnoCard("K", "F").can_be_played_on(UnoCard("B", "D"))
        True
        >>> UnoCard("Y", "5").can_be_played_on(UnoCard("G", "8"))
        False
        '''
        #If two cards' either have the same color or same face value, return True
        if self.color == other.color or self.rank == other.rank:
            return True
        #If color is black always return True
        elif self.color == "K":
            return True
        else:
            return False

    def score_value(self):
        '''Returns the value of this card at the end of the game (rank for number cards,
        20 for Skip, Draw Two, and Reverse, and 50 for Wild/Draw Four cards).
        >>> UnoCard("Y", "7").score_value()
        7
        >>> UnoCard("K", "W").score_value()
        50
        >>> UnoCard("B", "R").score_value()
        20
        '''
        #If self.rank can be converted to an integer, return it's integer value
        if self.rank not in self.RANKS:
            return int(self.rank)
        #If self.rank is a non-integer character, determine what the character is and return it's corresponding value
        else:
            for index in range(len(self.RANKS)):
                if self.RANKS[index] == self.rank:
                    #If the index of the correct element is in [0, 2] of the self.RANKS list. Either a Draw Two, Reverse, or Skip
                    if index in range(3):
                        return 20
                    else:
                        #Must be a Wild Card, which has a value of 50.
                        return 50


    def __str__(self):
        '''Returns human-readable representation of the card.
        >>> str(UnoCard("R", "1"))
        'R1'
        >>> str(UnoCard("G", "S"))
        'GS'
        >>> str(UnoCard("Y", "9"))
        'Y9'
        '''
        return f"{self.color}{self.rank}"

    def __repr__(self):
        '''Returns Python-executable string representation of the card
        >>> UnoCard("R", "1")
        UnoCard('R', '1')
        >>> UnoCard("K", "W")
        UnoCard('K', 'W')
        >>> UnoCard("B", "R")
        UnoCard('B', 'R')
        '''
        return f"UnoCard('{self.color}', '{self.rank}')"

def create_numbered_cards(color: str, the_range: range) -> list:
    '''Returns a list with all cards with a specific color and numerical value. The numerical value is expressed as a range.
    '''
    cards_list = []
    for number in the_range:
        cards_list.append(UnoCard(color, number))
    # print(cards_list)
    return cards_list
    
def create_wild_cards(card_type: str) -> list:
    cards = []
    for _ in range(4):
        cards.append(UnoCard("K", card_type))

    return cards

def create_deck():
    '''Returns a complete, shuffled Uno deck as a list of 108 UnoCard objects.
    '''
    full_deck = []
    card_colors = ["R", "G", "B", "Y"]
    card_ranks = ["S", "D", "R"]
    #Create all numbered cards
    for color in card_colors:
        full_deck += create_numbered_cards(color, range(10))
        full_deck += create_numbered_cards(color, range(1, 10))

        #Creates Skip, Draw Two, and Reverse Cards
        for pos in range(3):
            #Creates two of each card
            for _ in range(2):
                full_deck.append(UnoCard(color, card_ranks[pos]))

    #Create wild and draw four cards
    full_deck += create_wild_cards("W")
    full_deck += create_wild_cards("F")

    return random.sample(full_deck, len(full_deck))

def deal_hands(deck, num_hands):
    '''returns a tuple of num_hands lists of 7 cards dealt from deck, 1 to each hand at a time (not all 7 to 
    a single hand consecutively). Removes the cards that were dealt from the "top" of the deck (starting at position 0).
    '''
    #Creates the correct number of lists and stores them in a tuple
    tuple_of_hands = tuple(list() for _ in range(num_hands))

    for _ in range(7): 
        for elem in tuple_of_hands:
            elem.append(deck[0])
            deck.pop(0)

    return tuple_of_hands
def hand_score(hand: list) -> int:
    '''Takes a list of UnoCards and returns the total score for that hand.
    >>> hand_score([UnoCard("R", "3"), UnoCard("G", "9")])
    12
    >>> hand_score([UnoCard("R", "9"), UnoCard("G", "R"), UnoCard("K", "F")])
    79
    '''
    score = 0
    for card in hand:
        score += card.score_value()
    return score

if __name__ == "__main__":
    import doctest
    doctest.testmod()
