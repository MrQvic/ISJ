## Functions

### match_permutations_substrings(string, words)

This function generates all permutations of all substrings of the input string and returns a set of input words that match one of the permutations.

#### Parameters

- `string` (str): The input string.
- `words` (list[str]): The list of words to match against the permutations.

#### Returns

- A set of words that match one of the permutations.

### uniq_srt(it)

This function returns the input sequence unified and sorted (according to the values).

#### Parameters

- `it` (list): The input sequence to be unified and sorted.

#### Returns

- The input sequence after removing duplicate elements and sorting it.

### uniq_orig_order(it)

This function returns a new list containing unique elements from the input sequence, ordered by the order of their first appearance.

#### Parameters

- `it` (list): The input sequence.

#### Returns

- A new list containing unique elements from the input sequence, ordered by the order of their first appearance.

## Usage

To use this script, simply import the functions from it in your Python code, or run the script directly to see some example usage of the functions.

```python
if __name__ == "__main__":
    print(match_permutations_substrings('opak', ['ok', 'pak', 'pako', 'ano', 'noha', 'oka', 'kap', 'kopa', 'kopat', 'ona', 'okap']))
    print(uniq_srt('abrakadabra'))
    print(uniq_orig_order('abrakadabra'))
```

This will output the results of the functions when called with the provided example inputs.