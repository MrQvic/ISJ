## Function: gen_quiz

```python
def gen_quiz(qpool : list, *indexes : int, altcodes='ABCDEF', quiz = None) -> list:
```

### Parameters:

- `qpool` (list): A list of pairs where each pair consists of a question and a list of answers.
- `*indexes` (int): Arbitrary number of indexes into the 'qpool' list.
- `altcodes` (str, optional): A sequence that can be iterated over using a 'for' loop and returns strings that are to be prefixed (along with ': ') before each of the answers. Defaults to 'ABCDEF'.
- `quiz` (list, optional): The initial form of the quiz in the form of a list of pairs where each pair consists of a question and a list of formatted answers. Defaults to an empty list.

### Returns:

- `list`: The final form of the quiz.

### Description:

The function generates a quiz from a pool of questions. It takes in a list of pairs where each pair consists of a question and a list of answers. It also takes in an arbitrary number of indexes into the 'qpool' list. The function also accepts an optional parameter 'altcodes' which is a sequence that can be iterated over using a 'for' loop and returns strings that are to be prefixed (along with ': ') before each of the answers. If the 'altcodes' sequence is shorter than the list of possible answers in any of the lists, only the given number of answers is included in the final quiz. By default, the answers are marked with letters and there are a maximum of 6 possible answers, so 'altcodes' = 'ABCDEF'. If the initial form of the quiz is not specified, a new quiz is created with items according to the defined indexes. The default value is therefore an empty quiz. The function returns the final form of the quiz. If any of the indexes into the 'qpool' list are out of range, or if there is another error processing a specific index, the following is printed: "Ignoring index <number> - <exception text>".