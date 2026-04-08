import json
from hangman_display import load_pics


def test_load_pics(tmp_path):
    data = ["pic1", "pic2", "pic3"]

    file = tmp_path / "hangman.json"
    with open(file, "w") as f:
        json.dump(data, f)

    result = load_pics(file)

    assert result == data


def test_load_pics_default_filename(tmp_path, monkeypatch):
    file_path = tmp_path / "hangman.json"

    data = ["pic1", "pic2"]
    with open(file_path, "w") as f:
        json.dump(data, f)

    monkeypatch.chdir(tmp_path)

    result = load_pics()

    assert result == data
