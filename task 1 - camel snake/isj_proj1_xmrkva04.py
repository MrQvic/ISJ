#!/usr/bin/env python3

import re

# ukol za 3 body
def camel_to_snake_case(name):
    """Transfer camelCaseNames to snake_case_names.

    This function takes a string `name` in camel case format and converts it to snake case format.

    Args:
        name (str): The camel case string to be converted.

    Returns:
        str: The converted string in snake case format.

    Examples:
        >>> camel_to_snake_case('camelCaseNameAllowed')
        'camel_case_name_allowed'
        >>> camel_to_snake_case('longVATNumber')
        'long_vat_number'
    """

    inbetween = re.compile(r'''
                            (
                                (?<=[a-z])(?=[A-Z])|(?=[A-Z][a-z])
                            )
                            ''', re.VERBOSE)
    return inbetween.sub(r'_', name).lower()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
