import random
from hangman_logic import choose_word


def test_choose_word_test_case1():
    words = ["python", "java", "csharp"]
    random.seed(1)
    assert choose_word(words) == "python"


def test_choose_word_test_case2():
    words = ["python", "java", "csharp"]
    random.seed(0)
    assert choose_word(words) == "java"
