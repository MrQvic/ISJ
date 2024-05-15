#!/usr/bin/env python3

# ukol za 2 body
def she_says_he_says(she_says):
    """Replaces y/i, removes spaces, and returns the reversed string.

    Args:
        she_says (str): The input string.

    Returns:
        str: The reversed string after replacing y/i and removing spaces.

    Examples:
        >>> she_says_he_says('ma rymu')
        'umiram'
    """

    phonetic_she_says = she_says.replace("y", "i")  # replace y
    compact = phonetic_she_says.replace(" ", "")    # remove spaces
    he_says = compact[::-1]                         # reverse string
    print(he_says)
    return he_says


# ukol za 3 body
def solfege(title_hymn: str) -> str:
    """Partitions the input string to (an optional) title, ': ', and the hymn,
       takes a sublist starting from the first string, skipping always two 
       other strings, and ending 3 strings from the end, returns the result 
       as a string with ', ' as a separator

    Args:
        title_hymn (str): The input string containing the title (optional) and the hymn.

    Returns:
        str: The result as a string with ', ' as a separator.

    Examples:
        >>> solfege('Hymn of St. John: Ut queant laxis re sonare fibris mi ra gestorum fa muli tuorum sol ve polluti la bii reatum Sancte Iohannes')
        'Ut, re, mi, fa, sol, la'

        >>> solfege('Ut queant laxis re sonare fibris mi ra gestorum fa muli tuorum sol ve polluti la bii reatum Sancte Iohannes')
        'Ut, re, mi, fa, sol, la'
    """
    
    # the input string partitioned to the title (if given) and the actual hymn
    possible_title, sep, hymn = title_hymn.partition(": ") if ": " in title_hymn else (None, ': ', title_hymn)

    # the hymn as a list of strings separated by ' '
    hymn_list = hymn.split()                                               
    hymn_list = hymn_list[:-3]
    
    # skipping always two strings, and ending 3 strings from the end
    skip2 = hymn_list[::3]                                                   

    # the skip2 list as a string, ', ' as a separator
    skip2_str = ', '.join(skip2)                                               

    return skip2_str


if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    pass
