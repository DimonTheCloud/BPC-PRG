from hangman_display import show_game_state


def test_show_game_state_no_hangman(capsys):
    show_game_state("____", ["X"], 0, ["A", "B"])

    captured = capsys.readouterr()

    assert "Slovo: ____" in captured.out
    assert "Použitá písmena: A, B" in captured.out


def test_show_game_state_with_hangman(capsys):
    hangman = ["0", "1", "2", "3", "4", "5", "6"]

    show_game_state("____", hangman, 2, ["A"])

    captured = capsys.readouterr()

    assert "2" in captured.out
