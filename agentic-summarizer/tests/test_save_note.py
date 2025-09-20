import os
from src.save_note import save_note

def test_save_note_creates_file(tmp_path):
    test_file = tmp_path / "example"
    content = "This is a test summary."
    result = save_note(str(test_file), content)

    expected_path = f"{test_file}.md"
    assert os.path.exists(expected_path)
    assert "Saved notes" in result

    with open(expected_path, "r", encoding="utf-8") as f:
        text = f.read()
        assert "This is a test summary." in text
        assert "— Jibril Anifowoshe" in text

def test_save_note_appends_md(tmp_path):
    test_file = tmp_path / "example.md"
    content = "Testing with extension."
    result = save_note(str(test_file), content)

    assert os.path.exists(test_file)
    assert "Saved notes" in result
