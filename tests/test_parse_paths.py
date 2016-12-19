from parserix import clean
from parserix import parse_paths
import pytest
import os

test_list_path = os.path.join(os.path.abspath("tests"), "images.txt")
test_paths = [line.strip() for line in open(test_list_path)]

# remove rubbish mixed in with file paths
clean_paths = clean.clean(test_paths)

eg = "/mnt/ImageXpress/2015-07-31 val screen/val screen/HCC15691/2015-07-31/4014/val screen_B02_s1_w1_thumb62D4A363-7C7E-40D0-8A9E-55EC6681574D.tif"
def test_get_img_filename():
    filename = parse_paths.get_img_filename(eg)
    assert filename == "val screen_B02_s1_w1_thumb62D4A363-7C7E-40D0-8A9E-55EC6681574D.tif"


def test_get_img_well():
    filename = parse_paths.get_img_filename(eg)
    assert parse_paths.get_img_well(filename) == "B02"


def test_get_img_site():
    filename = parse_paths.get_img_filename(eg)
    assert parse_paths.get_img_site(filename) == 1


def test_get_img_channel():
    filename = parse_paths.get_img_filename(eg)
    assert parse_paths.get_img_channel(filename) == 1


def test_get_plate_name():
    assert parse_paths.get_plate_name(eg) == "HCC15691"


def test_get_plate_date():
    assert parse_paths.get_plate_date(eg) == "2015-07-31"


def test_get_plate_num():
    assert parse_paths.get_plate_num(eg) == 4014


def test_check_filepath():
    parse_paths.check_filepath(eg)


def test_check_filepath_too_short():
    example = "/too/short/img.tiff"
    with pytest.raises(ValueError):
        parse_paths.check_filepath(example)


def test_check_filepath_missing_metadata():
    example = "/mnt/ImageXpress/2015-07-31 val screen/val screen/HCC15691/2015-07-31/4014/val screen_B02_s1_thumb62D4A363-7C7E-40D0-8A9E-55EC6681574D.tif"
    with pytest.raises(ValueError):
        parse_paths.check_filepath(example)
