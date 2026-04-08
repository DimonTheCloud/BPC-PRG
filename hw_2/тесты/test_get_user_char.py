from hangman_logic import get_user_char


def test_get_user_char_valid_input(monkeypatch):
    inputs = iter(["a"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    used = []
    char, used = get_user_char(used)

    assert char == "a"
    assert "a" in used


def test_get_user_char_rejects_invalid_then_accepts(monkeypatch):
    inputs = iter(["ab", "1", "b"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    used = []
    char, used = get_user_char(used)

    assert char == "b"
    assert used == ["b"]


def test_get_user_char_rejects_duplicate(monkeypatch):
    inputs = iter(["a", "a", "b"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    used = ["a"]
    char, used = get_user_char(used)

    assert char == "b"
    assert used == ["a", "b"]
