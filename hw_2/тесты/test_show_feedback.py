from hangman_display import show_feedback


def test_show_feedback_correct(capsys):
    show_feedback(True)

    captured = capsys.readouterr()
    assert "Správně" in captured.out


def test_show_feedback_incorrect(capsys):
    show_feedback(False)

    captured = capsys.readouterr()
    assert "Špatně" in captured.out
