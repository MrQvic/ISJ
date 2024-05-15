#xmrkva04 - Adam Mrkva

def gen_quiz(qpool : list, *indexes : int, altcodes='ABCDEF', quiz = None) -> list:
    """
    The function 'gen_quiz' is defined in the file named isj_proj5_login.py and it has 4 parameters:

    Parameters:
    qpool (list): A list of pairs where each pair consists of a question and a list of answers.
    *indexes (int): Arbitrary number of indexes into the 'qpool' list.
    altcodes (str, optional): A sequence that can be iterated over using a 'for' loop and returns strings that are to be prefixed (along with ': ') before each of the answers. Defaults to 'ABCDEF'.
    quiz (list, optional): The initial form of the quiz in the form of a list of pairs where each pair consists of a question and a list of formatted answers. Defaults to an empty list.

    If any of the indexes into the 'qpool' list are out of range, or if there is another error processing a specific index, the following is printed:
    "Ignoring index <number> - <exception text>"
    (somewhat nonsensically to standard output, not to standard error output, for doctest to work)

    If the 'altcodes' sequence is shorter than the list of possible answers in any of the lists, only the given number of answers (you can use the zip(altcodes, answers) construction) is included in the final quiz. By default, the answers are marked with letters and there are a maximum of 6 possible answers, so 'altcodes' = 'ABCDEF'.

    If the initial form of the quiz is not specified, a new quiz is created with items according to the defined indexes. The default value is therefore an empty quiz.

    Returns:
    list: The final form of the quiz.
    """
    if quiz is None:
        quiz = []
    for index in indexes:
        try:
            question, answers = qpool[index]
            format = [code + ": " + answer for code, answer in zip(altcodes, answers)]
            quiz.append((question, format))
        except Exception as e:
            print("Ignoring index " + str(index) + " - " + str(e))
    return quiz


#test_qpool1 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
#existing_quiz1 = [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2'])]
#print(gen_quiz(test_qpool1, -2, 0, altcodes = ('10', '20', '30'), quiz = existing_quiz1))
#[('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2']), ('Question3', ['10: Answer1', '20: Answer2', '30: Answer3']), ('Question1', ['10: Answer1', '20: Answer2', '30: Answer3'])]

#test_qpool2 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
#existing_quiz2 = [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2'])]
#not_used = gen_quiz(test_qpool2, -2, 0, altcodes = ('1', '2', '3'), quiz = existing_quiz2)
#print(existing_quiz2)
#[('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2']), ('Question3', ['1: Answer1', '2: Answer2', '3: Answer3']), ('Question1', ['1: Answer1', '2: Answer2', '3: Answer3'])]
#
#test_qpool3 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
#existing_quiz3 = [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2'])]
#not_used1 = gen_quiz(test_qpool3, 0, 2, altcodes = ('i', 'ii', 'iii'), quiz = existing_quiz3)
#not_used2 = gen_quiz(test_qpool3, 1, altcodes = ('i', 'ii', 'iii'), quiz = existing_quiz3)
#print(existing_quiz3)
#[('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2']), ('Question1', ['i: Answer1', 'ii: Answer2', 'iii: Answer3']), ('Question3', ['i: Answer1', 'ii: Answer2', 'iii: Answer3']), ('Question2', ['i: Answer1', 'ii: Answer2', 'iii: Answer3'])]
#
#test_qpool4 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
#print(gen_quiz(test_qpool4, 0, 1, -1))
#[('Question1', ['A: Answer1', 'B: Answer2', 'C: Answer3', 'D: Answer4']), ('Question2', ['A: Answer1', 'B: Answer2', 'C: Answer3']), ('Question4', ['A: Answer1', 'B: Answer2'])]
#
#test_qpool5 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
#not_used = gen_quiz(test_qpool5, 0, altcodes = '123456')
#print(gen_quiz(test_qpool5, 0, altcodes = '123456'))
#[('Question1', ['1: Answer1', '2: Answer2', '3: Answer3', '4: Answer4'])]
#
#test_qpool6 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
#existing_quiz6 = [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2'])]
#print(gen_quiz(test_qpool6, quiz = existing_quiz6))
#[('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2'])]
#
#test_qpool7 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
#print(gen_quiz(test_qpool7, 0, 4, 2, altcodes = ['101','201']))
#Ignoring index 4 - list index out of range
#[('Question1', ['101: Answer1', '201: Answer2']), ('Question3', ['101: Answer1', '201: Answer2'])]