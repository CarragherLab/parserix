from parserix import clean
import os

# stupid testings paths
test_list_path = os.path.join(os.path.abspath("tests"), "images.txt")

# test file paths
test_paths = [line.strip() for line in open(test_list_path)]

def test_clean_removes_something():
    """clean actually removes something"""
    assert len(test_paths) > len(clean.clean(test_paths))


def test_clean_removes_db_files():
    """parserix.clean removes Thumbs.db file left by windows"""
    cleaned_up = clean.clean(test_paths)
    assert "Thumbs.db" not in cleaned_up


def test_clean_removes_thumbnails():
    """parserix.clean removes thumbnail images"""
    cleaned_up = clean.clean(test_paths)
    for line in cleaned_up:
        assert "thumb" not in line
