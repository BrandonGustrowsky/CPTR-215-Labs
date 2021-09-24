"""Sliding Puzzle
Prof. O and _____
2021-09-16 first draft

A Sliding Puzzle is represented by a string
whose length is a perfect square
of an integer in [2, 6] (i.e., 4, 9, 16, 25, or 36).
It contains only digits (0-9) and capital letters (A-Z),
exactly ONE of which (typically 0) is "empty"
and is represented by a hyphen (-).

On screen, however, the layout is an NxN square.
Legal moves consist of sliding a tile
up, down, left, or right (but never diagonally)
into the empty spot (-).

The puzzle is in the "solved" state when
all its digits and letters are in ascending order
(with digits before letters, as in ASCII and Unicode)
and the empty spot is at the beginning or end
(never in the middle).

References:
https://mathworld.wolfram.com/15Puzzle.html
https://lorecioni.github.io/fifteen-puzzle-game/
https://15puzzle.netlify.app/
"""

from typing import Tuple

def rows_from_puzzle(puzzle : str) -> str:
    """Returns a string with a newline between rows of the puzzle.

    >>> rows_from_puzzle('-123')
    '-1\\n23'

    >>> rows_from_puzzle('-12345678')
    '-12\\n345\\n678'

    >>> rows_from_puzzle('-123456789ABCDEF')
    '-123\\n4567\\n89AB\\nCDEF'
    """

    newline_puzzle = ""

    LEN_OF_ROW = {n*n: n for n in range(2, 7)}
    size = LEN_OF_ROW[len(puzzle)]

    NEWLINE = "\n"

    for i in range(0, len(puzzle)):
        newline_puzzle += f"{puzzle[i]}{NEWLINE if (i+1)%size == 0 and i < len(puzzle)-1 else ''}"

    return newline_puzzle

def is_solved(puzzle : str) -> bool:
    """Determines whether puzzle is solved (as defined above).
    >>> is_solved('-123456789ACBDEF')
    False

    >>> is_solved('1-23')
    False

    >>> is_solved('12345678-')
    True

    >>> is_solved('12345678ABCDEF-')
    True
    """
    temp = puzzle[0]
    if puzzle[0] == "-" or puzzle[len(puzzle)-1] == "-":
        puzzle = puzzle.replace("-", "")
        for pos in range(len(puzzle)):
            if puzzle[pos] < temp:
                return False
            
            temp = puzzle[pos]

        return True
    
    return False

def search_list(puzzle: list, item: str) -> tuple:
    '''
    Searches a list of lists for certain values and returns the values in a tuple.
    >>> search_list([['1','2'], ['-','3']], 3)
    (0, 0)
    
    >>> search_list([['1','2', '3'], ['4', '5', '6'], ['7', '8', '-']], 4)
    (0, 0)
    '''
    tile_row = 0
    tile_column = 0

    for lst in range(len(puzzle)):
        if item in puzzle[lst]:
            tile_row = lst
            for pos in range(len(puzzle[lst])):
                if item == puzzle[lst][pos]:
                    tile_column = pos
    
    return (tile_row, tile_column)

def is_legal_move(puzzle : str, tile_to_move : str) -> bool:
    """Determines whether it is possible to move tile_to_move into the empty spot.
    >>> is_legal_move('12-3', '2')
    False

    >>> is_legal_move('12345-678', '8')
    True

    >>> is_legal_move('12-345678', '7')
    False

    >>> is_legal_move('1-23456AB7C8DFEG', 'F')
    False

    """
    LEN_OF_ROW = {n*n: n for n in range(2, 7)}

    size = LEN_OF_ROW[len(puzzle)]
    puzzle_list = [list(puzzle[start:start+size]) for start in range(0, len(puzzle), size)]

    tiles_coords = search_list(puzzle_list, tile_to_move)
    space_coords = search_list(puzzle_list, "-")

    added_coords = abs(tiles_coords[0] - space_coords[0]) + abs(tiles_coords[1] - space_coords[1])

    if added_coords == 1:
        return True
    else:
        return False

def puzzle_with_move(puzzle : str, tile_to_move : str) -> str:
    """Move tile_to_move into the empty slot (-).
    >>> puzzle_with_move('123456-78', '7')
    '1234567-8'

    >>> puzzle_with_move('1-23', '3')
    '132-'
    """
    space = 0
    tile = 0

    puzzle = list(puzzle)
    for char in range(len(puzzle)):
        if puzzle[char] == tile_to_move:
            tile = char
        if puzzle[char] == "-":
            space = char

    puzzle[tile], puzzle[space] = puzzle[space], puzzle[tile]

    return ''.join(puzzle)

def space_puzzle(puzzle : str) -> str:
    return " " + " ".join(rows_from_puzzle(puzzle))

def play_puzzle(puzzle : str) -> None:
    moves = 0
    while not is_solved(puzzle):
        print(f"\nCurrent puzzle state:\n{space_puzzle(puzzle)}")
        tile_to_move = "-"
        moves += 1
        print(f"Move #{moves}")
        while not is_legal_move(puzzle, tile_to_move):
            tile_to_move = input("Which tile would you like to move into the empty spot? ")        
        puzzle = puzzle_with_move(puzzle, tile_to_move)
    print(f"\nSolved!\n{space_puzzle(puzzle)}")
    print(f"You solved the puzzle in {moves} moves!")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    # play_puzzle("-231")