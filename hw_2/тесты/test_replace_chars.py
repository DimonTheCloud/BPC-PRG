from hangman_logic import replace_chars


def test_replace_chars_single_occurrence():
    state = "______"
    new_state = replace_chars(state, "PYTHON", "P")

    assert new_state == "P_____"


def test_replace_chars_multiple_occurrences():
    state = "______"
    new_state = replace_chars(state, "BANANA", "A")

    assert new_state == "_A_A_A"


def test_replace_chars_no_change():
    state = "______"
    new_state = replace_chars(state, "PYTHON", "Z")

    assert new_state == state
