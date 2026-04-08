import builtins
import json
from play_hangman import main


def test_main_win(monkeypatch, capsys, tmp_path):
    guesses = iter(list("python"))

    hangman_file = tmp_path / "hangman.json"
    hangman_data = ["pic"] * 7
    hangman_file.write_text(json.dumps(hangman_data))

    monkeypatch.setattr(builtins, "input", lambda _: next(guesses))
    monkeypatch.setattr("play_hangman.choose_word", lambda _: "python")
    monkeypatch.setattr(
        "play_hangman.load_pics",
        lambda file=str(hangman_file): json.loads(hangman_file.read_text()),
    )

    main()
    output = capsys.readouterr().out.lower()

    assert "gratuluji" in output
    assert "python" in output

    assert "správně" in output

    assert "slovo:" in output
    assert "použitá písmena" in output


def test_main_loss(monkeypatch, capsys, tmp_path):
    guesses = iter(list("abcdefg"))

    hangman_file = tmp_path / "hangman.json"
    hangman_data = ["h0", "h1", "h2", "h3", "h4", "h5", "h6"]
    hangman_file.write_text(json.dumps(hangman_data))

    monkeypatch.setattr(builtins, "input", lambda _: next(guesses))
    monkeypatch.setattr("play_hangman.choose_word", lambda _: "python")
    monkeypatch.setattr(
        "play_hangman.load_pics",
        lambda file=str(hangman_file): json.loads(hangman_file.read_text()),
    )

    main()
    output = capsys.readouterr().out.lower()

    assert "konec hry" in output
    assert "python" in output

    assert "špatně" in output

    assert "slovo:" in output
    assert "použitá písmena" in output

    assert "h1" in output
    assert "h2" in output


def test_main_mixed_attempts(monkeypatch, capsys, tmp_path):
    guesses = iter(list("abcptython"))

    hangman_file = tmp_path / "hangman.json"
    hangman_data = ["h0", "h1", "h2", "h3", "h4", "h5", "h6"]
    hangman_file.write_text(json.dumps(hangman_data))

    monkeypatch.setattr(builtins, "input", lambda _: next(guesses))
    monkeypatch.setattr("play_hangman.choose_word", lambda _: "python")
    monkeypatch.setattr(
        "play_hangman.load_pics",
        lambda file=str(hangman_file): json.loads(hangman_file.read_text()),
    )

    main()
    output = capsys.readouterr().out.lower()

    assert "gratuluji" in output
    assert "python" in output

    assert "správně" in output
    assert "špatně" in output

    assert "slovo:" in output
    assert "použitá písmena" in output
    assert "a, b, c, p, t, y, h, o" in output

    assert "h0" in output
    assert "h1" in output
    assert "h2" in output


def test_main_immediate_win(monkeypatch, capsys, tmp_path):
    guesses = iter(["p"])

    hangman_file = tmp_path / "hangman.json"
    hangman_data = ["x0", "x1", "x2", "x3", "x4", "x5", "x6"]
    hangman_file.write_text(json.dumps(hangman_data))

    monkeypatch.setattr(builtins, "input", lambda _: next(guesses))
    monkeypatch.setattr("play_hangman.choose_word", lambda _: "p")
    monkeypatch.setattr(
        "play_hangman.load_pics",
        lambda file=str(hangman_file): json.loads(hangman_file.read_text()),
    )

    main()
    output = capsys.readouterr().out.lower()

    assert "gratuluji" in output
    assert "p" in output

    assert "správně" in output

    assert "slovo:" in output
    assert "použitá písmena" in output
