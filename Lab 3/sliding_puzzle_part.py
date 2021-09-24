"""Sliding Puzzle
Prof. O and Brandon Gustrowsky
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
    >>> rows_from_puzzle('1-23')
    '1 -
     2 3'

    >>> rows_from_puzzle('1-2345678')
    '1 - 2
     3 4 5
     6 7 8'
    """

    LEN_OF_ROW = {n*n: n for n in range(2, 7)}

    size = LEN_OF_ROW[len(puzzle)]
    
    puzzle_list = [puzzle[pos: pos+size] for pos in range(0, len(puzzle), size)]
    
    puzzle_with_newline = ""
    for line in puzzle_list:
        puzzle_with_newline += line
        puzzle_with_newline += "\n"
    


    return puzzle_with_newline  # TODO: write tests and replace this stub

def is_solved(puzzle : str) -> bool:
    """Determines whether puzzle is solved (as defined above).
    >>> is_solved(['-', '1', '2', '3', '4', '5', '6', '7', '8'])
    True

    >>> is_solved(['1', '2', '3', '-', '4', '5', '6', '7', '8'])
    False
    """
    try:
        temp_num = int(puzzle[0]) - 1
    
    except ValueError:
        temp_num = int(puzzle[1]) - 1
    
    if puzzle[0] == "-" or puzzle[len(puzzle)-1] == "-":
        for item in range(len(puzzle)):
            if item >= 9:
                break
            if puzzle[item] == "-":
                continue
            if int(puzzle[item]) <= temp_num:
                return False
            else:
                temp_num = int(puzzle[item])

        if len(puzzle) >= 9:
            temp_letter = ""
            for letter in range(9, len(puzzle)):
                if letter == 9:
                    temp_letter = puzzle[letter]
                    continue

                if puzzle[letter] >= temp_letter:
                    return False
                else:
                    temp_letter = puzzle[letter]

            return True

    return False
 # TODO: write tests and replace this stub

def is_legal_move(puzzle : str, tile_to_move : str) -> bool:
    """Determines whether it is possible to move tile_to_move into the empty spot. 
    >>> is_legal_move('12-3', '3')
    True

    >>> is_legal_move('12-3', '2')
    False

    """

    LEN_OF_ROW = {n*n: n for n in range(2, 7)}

    size = LEN_OF_ROW[len(puzzle)]

    space = "-"

    if tile_to_move == space:
        return False

    for char in range(len(puzzle)):
        if puzzle[char] == tile_to_move:
            #If tile in far left column
            if tile_to_move in puzzle[0::size]:
                #if in top left corner
                if tile_to_move == puzzle[0]:
                    if puzzle[char+1] == space or puzzle[char+size] == space:
                        return True
                #If tile in bottom left corner
                if tile_to_move == puzzle[len(puzzle) - size]:
                    if puzzle[char+1] == space or puzzle[char-size] == space:
                        return True
                if size > 2:
                    if puzzle[char+1] == space or puzzle[char+size] == space or puzzle[char-size] == space:
                        return True
            
            #If tile in far right column
            if tile_to_move in puzzle[size-1::size]:
                if tile_to_move == puzzle[size-1]:
                    #If tile in top right corner
                    if puzzle[char-1] == space or puzzle[char+size] == space:
                        return True
                    #If tile in bottom right corner
                if tile_to_move == puzzle[len(puzzle)-1]:
                    if puzzle[char-1] == space or puzzle[char-size] == space:
                        return True
                elif size > 2:
                    if puzzle[char-1] == space or puzzle[char-size] == space or puzzle[char+size] == space:
                        if char - size > 0:
                            return True
                        
            
            #if there are no edge numbers (not corners) then the following if's don't apply
            if size == 2:
                return False
            
            #if tile on top row
            if tile_to_move in puzzle[1:size-1]:
                if puzzle[char+1] == space or puzzle[char-1] == space or puzzle[char+size] == space:
                    return True

            #if tile in bottom row
            if tile_to_move in puzzle[len(puzzle)-size+1: len(puzzle)-1]:
                if puzzle[char+1] == space or puzzle[char-1] == space or puzzle[char-size] == space:
                    return True

            #if tile not on corners of puzzle
            if tile_to_move not in puzzle[0::size] and tile_to_move not in puzzle[size-1::size] and tile_to_move not in puzzle[1:size-1] and tile_to_move not in puzzle[len(puzzle)-size+1: len(puzzle)-1]:
                if puzzle[char+1] == space or puzzle[char-1] == space or puzzle[char+size] == space or puzzle[char-size] == space:
                    return True


    return False

def puzzle_with_move(puzzle : str, tile_to_move : str) -> str:
    """Move tile_to_move into the empty slot (-).

    >>> puzzle_with_move('12-3', '3')
    '123-'

    >>> puzzle_with_move('-132', '1')
    '1-32'
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
    
    # import doctest
    # doctest.testmod()
    
    play_puzzle("")