from hangman_display import show_welcome_message


def test_show_welcome_message(capsys):
    show_welcome_message()

    captured = capsys.readouterr()

    assert "Vítej ve hře šibenice!" in captured.out
    assert "uhodnout tajné slovo" in captured.out
