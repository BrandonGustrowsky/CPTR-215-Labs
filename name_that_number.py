def find_ones(ones: dict, number: str) -> str:
    '''
    >>> find_ones({0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}, '8')
    'eight'

    >>> find_ones({0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}, '3')
    'three'
    '''
    for key in ones.keys():
        if key == int(number):
            return ones[key]

def find_teens(teens: dict, number: tuple) -> str:
    '''
    >>> find_teens({11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}, '18')
    'eighteen'

    >>> find_teens({11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}, '11')
    'eleven'
    '''
    for key in teens.keys():
        if key == int(number[0] + number[1]):
            return teens[key]

def find_tens(tens: dict, number: str) -> str:
    '''
    >>> find_tens({1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}, '3')
    'thirty'

    >>> find_tens({1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}, '7')
    'seventy'
    '''
    for key in tens.keys():
        if key == int(number):
            return tens[key]

def find_hundreds(ones: dict, number: str) -> str:
    '''
    >>> find_hundreds({0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}, '9')
    'nine hundred'

    >>> find_hundreds({0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}, '1')
    'one hundred'
    '''
    ones_place = find_ones(ones, number[0])
    return f"{ones_place} hundred"

def find_millions(the_dict: dict, iterable: int) -> str:
    '''
    Returns a prefix from 'the_dict' based on what value is held by 'iterable'

    >>> find_millions({0: 'hundred', 1: 'thousand', 2: 'million'}, 1)
    'thousand'

    >>> find_millions({7: "sextillion", 8: "septillion"}, 8)
    'septillion'
    '''

    for key in the_dict.keys():
        if key == iterable:
            return the_dict[key]

def reverse(the_list: list) -> list:
    '''
    Takes a list and reverses each individual element and returns a subsequent new list

    >>> reverse(['221', '654', '5'])
    ['122', '456', '5']

    >>> reverse(['950', '183', '192', '50'])
    ['059', '381', '291', '05']
    '''
    new_list = []
    for item in the_list:
        new_list.append(item[::-1])

    return new_list

def split_number(number: str) -> list:
    '''
    Returns a list of NUMBERS evenly split every third digit.
    'number': a number type casted to 'str' so that it can be split.
    >>> split_number('153123')
    ['321', '351']

    >>> split_number('0')
    ['0']
    '''
    number_reversed = number[::-1]
    return [number_reversed[char: char+3] for char in range(0, len(number_reversed), 3)]


def wordsFromNumber(the_number: int) -> str:
    '''
    Reads in a number that in numerical form and returns it in word form.

    >>> wordsFromNumber(12345)
    'twelve thousand three hundred forty-five'

    >>> wordsFromNumber(100)
    'one hundred'

    >>> wordsFromNumber(0)
    'zero'

    >>> wordsFromNumber(8972126728)
    'eight billion nine hundred seventy-two million one hundred twenty-six thousand seven hundred twenty-eight'
    '''
    if the_number == 0:
        return "zero"

     #value = prefix with that number of splices
    millions = {0: "hundred", 1: "thousand", 2: "million", 
                3: "billion", 4: "trillion", 5: "quadrillion", 
                6: "quintillion", 7: "sextillion", 8: "septillion", 
                9: "octillion", 10: "nonillion"
                }

    tens = {1: "ten", 2: "twenty", 3: "thirty", 4: "forty",
                5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

    teens = {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
                    19: "nineteen"}

    ones = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    number_as_word = ""

    reversed_numbers = split_number(str(the_number))
    NUMBERS = reverse(reversed_numbers)

    number = len(NUMBERS)-1
    while number >= 0:
        if int(NUMBERS[number]) != 0:
            if len(NUMBERS[number]) == 3 and int(NUMBERS[number][0]) != 0:
                hundred = find_hundreds(ones, NUMBERS[number][0])
                number_as_word += f"{hundred} "

            if len(NUMBERS[number]) == 3:
                if int(NUMBERS[number][1]) != 0:
                    if int(NUMBERS[number][1]) != 0 and int(NUMBERS[number][1] + NUMBERS[number][2]) in range(11, 20):
                        teens_digits = find_teens(teens, (NUMBERS[number][1], NUMBERS[number][2]))
                        number_as_word += f"{teens_digits} "
                        if number != 0:
                            million = find_millions(millions, number)
                            number_as_word += f"{million} "
                        number -= 1
                        continue
                    else:
                        tens_digit = find_tens(tens, NUMBERS[number][1])
                        number_as_word += f"{tens_digit}{' ' if int(NUMBERS[number][2]) == 0 else '-'}"

                if int(NUMBERS[number][2]) != 0:
                    ones_digit = find_ones(ones, NUMBERS[number][2])
                    number_as_word += f"{ones_digit} "

            elif len(NUMBERS[number]) == 2:
                if int(NUMBERS[number][0]) != 0:
                    if int(NUMBERS[number][1]) != 0 and int(NUMBERS[number][0] + NUMBERS[number][1]) in range(11, 20):
                        teens_digits = find_teens(teens, (NUMBERS[number][0], NUMBERS[number][1]))
                        number_as_word += f"{teens_digits} "
                        if number != 0:
                            million = find_millions(millions, number)
                            number_as_word += f"{million} "
                        number -= 1
                        continue
                    tens_digit = find_tens(tens, NUMBERS[number][0])
                    number_as_word += f"{tens_digit}{' ' if int(NUMBERS[number][1]) == 0 else '-'}"

                if int(NUMBERS[number][1]) != 0:
                    ones_digit = find_ones(ones, NUMBERS[number][1])
                    number_as_word += f"{ones_digit} "               

            elif len(NUMBERS[number]) == 1:
                if int(NUMBERS[number][0]) != 0:
                    ones_digit = find_ones(ones, NUMBERS[number][0])
                    number_as_word += f"{ones_digit} "
            
            if number != 0:
                million = find_millions(millions, number)
                number_as_word += f"{million} "

        number -= 1

    number_without_ending_space = number_as_word.rstrip(number_as_word[-1])
    return number_without_ending_space

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    number = 211633

    number_as_word = wordsFromNumber(number)
    print(number_as_word)
