#!/usr/bin/env python3

# ukol za 2 body
def first_odd_or_even(numbers : list[int]) -> int:
    """
    Returns 0 if there is the same number of even numbers and odd numbers
    in the input list of ints, or there are only odd or only even numbers.
    Returns the first odd number in the input list if the list has more even
    numbers.
    Returns the first even number in the input list if the list has more odd 
    numbers.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        int: The first odd or even number based on the conditions.

    Examples:
        >>> first_odd_or_even([2,4,2,3,6])
        3
        >>> first_odd_or_even([3,5,4])
        4
        >>> first_odd_or_even([2,4,3,5])
        0
        >>> first_odd_or_even([2,4])
        0
        >>> first_odd_or_even([3])
        0
    """
    even_count = 0
    odd_count = 0
    first_even = None
    first_odd = None
    
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
            if first_even is None:
                first_even = number

        else:
            odd_count += 1
            if first_odd is None:
                first_odd = number
                
    if even_count == odd_count or even_count == 0 or odd_count == 0:
        return 0
    
    elif even_count > odd_count:
        return first_odd
    
    else:
        return first_even
    

# ukol za 3 body
def to_pilot_alpha(word: str) -> list[str]:
    """Returns a list of pilot alpha codes corresponding to the input word

    Args:
        word (str): The input word for which pilot alpha codes are to be generated.

    Returns:
        list[str]: A list of pilot alpha codes corresponding to the input word.

    Examples:
        >>> to_pilot_alpha('Smrz')
        ['Sierra', 'Mike', 'Romeo', 'Zulu']
    """

    pilot_alpha = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot',
        'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike',
        'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango',
        'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']

    pilot_alpha_list = []

    for letter in word:
        if not letter.isalpha(): #skip if word contains anything else than letter
            continue

        letter = letter.capitalize()
        position = ord(letter) - ord('A') #find the position of the alpha code (letter - 65)
        pilot_alpha_list.append(pilot_alpha[position])
     
    return pilot_alpha_list

if __name__ == "__main__":
    print(to_pilot_alpha('Smrz'))
    print(first_odd_or_even([2,4,3,5]))
