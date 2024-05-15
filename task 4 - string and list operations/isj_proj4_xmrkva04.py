#!/usr/bin/env python3

from itertools import permutations

def all_permutations_substrings(a_str):
    """Generates all permutations of all substrings of the input string
    """

    return set(
        ''.join(item)
        for length in range(len(a_str)+1)
        for item in permutations(a_str, length))

# max 2 points
def match_permutations_substrings(string : str, words : list[str]) -> set[str]:
    """Generates all permutations of all substrings of the input string and
       returns a set of input words that match one of the permutations.

    Args:
        string (str): The input string.
        words (list[str]): The list of words to match against the permutations.

    Returns:
        set[str]: A set of words that match one of the permutations.

    Examples:
        >>> match_permutations_substrings('okna', ['a', 'z', 'v', 'o', 'k', 'ok', 'ano', 'no', 'hlava', 'oko', 'noky', 'nok', 'on', 'ona', 'ony'])
        {'no', 'o', 'ona', 'ano', 'a', 'nok', 'ok', 'k', 'on'}

        >>> match_permutations_substrings('opak', ['ok', 'pak', 'pako', 'ano', 'noha', 'oka', 'kap', 'kopa', 'kopat', 'ona', 'okap'])
        {'kopa', 'ok', 'oka', 'pako', 'pak', 'okap', 'kap'}
    """
    # permutations as a set
    perms = all_permutations_substrings(string)
    
    return {word for word in words if any(word in perm for perm in perms)}


# max 1 point
def uniq_srt(it: list) -> list:
    """
    Returns the input sequence unified and sorted (according to the values)

    Args:
        it (list): The input sequence to be unified and sorted.

    Returns:
        list: The input sequence after removing duplicate elements and sorting it.

    Examples:
        >>> uniq_srt([3, 3, 5, 3, 4, 2, 4])
        [2, 3, 4, 5]

        >>> uniq_srt('abrakadabra')
        ['a', 'b', 'd', 'k', 'r']
    """
    return sorted(set(it))


# max 2 points
def uniq_orig_order(it: list) -> list:
    """
    Returns a new list containing unique elements from the input sequence,
    ordered by the order of their first appearance.

    Args:
        it (list): The input sequence.

    Returns:
        list: A new list containing unique elements from the input sequence,
        ordered by the order of their first appearance.

    Examples:
        >>> uniq_orig_order([3, 3, 5, 3, 4, 2, 4])
        [3, 5, 4, 2]

        >>> uniq_orig_order('abrakadabra')
        ['a', 'b', 'r', 'k', 'd']
    """

    seen = set()
    return [item for item in it if not (item in seen or seen.add(item))]


if __name__ == "__main__":
    print(match_permutations_substrings('opak', ['ok', 'pak', 'pako', 'ano', 'noha', 'oka', 'kap', 'kopa', 'kopat', 'ona', 'okap']))
    print(uniq_srt('abrakadabra'))
    print(uniq_orig_order('abrakadabra'))