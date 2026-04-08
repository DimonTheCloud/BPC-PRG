from hangman_display import show_game_over


def test_show_game_over_win(capsys):
    show_game_over(True, "PYTHON")

    captured = capsys.readouterr()
    assert "Gratuluji" in captured.out
    assert "PYTHON" in captured.out


def test_show_game_over_loss(capsys):
    show_game_over(False, "PYTHON")

    captured = capsys.readouterr()
    assert "Konec hry" in captured.out
    assert "PYTHON" in captured.out
