from parserix import clean
from parserix import parse
import datetime
import pytest
import os


test_list_path = os.path.join(os.path.abspath("tests"), "images.txt")
new_test_list_path = os.path.join(os.path.abspath("tests"), "new_images.txt")

test_paths = [line.strip() for line in open(test_list_path)]
new_test_paths = [line.strip() for line in open(new_test_list_path)]

# remove rubbish mixed in with file paths
clean_paths = clean.clean(test_paths)
new_clean_paths = clean.clean(new_test_paths)

EXAMPLE_PATH = "/mnt/ImageXpress/2015-07-31 val screen/val screen/HCC15691/2015-07-31/4014/val screen_B02_s1_w1_thumb62D4A363-7C7E-40D0-8A9E-55EC6681574D.tif"
NEW_EXAMPLE_PATH = "/mnt/Datastore/IGMM/ImageXpress2020/drug-discovery/GCGR-FDA/E13FDAa1/2021-04-03/490/TimePoint_1/val screen_B02_s1_w1_thumb62D4A363-7C7E-40D0-8A9E-55EC6681574D.tif"


def test_img_filename():
    expected = "val screen_B02_s1_w1_thumb62D4A363-7C7E-40D0-8A9E-55EC6681574D.tif"
    assert parse.img_filename(EXAMPLE_PATH) == expected
    assert parse.img_filename(NEW_EXAMPLE_PATH) == expected


def test_path():
    assert parse.path(EXAMPLE_PATH) == "/mnt/ImageXpress/2015-07-31 val screen/val screen/HCC15691/2015-07-31/4014"
    assert parse.path(NEW_EXAMPLE_PATH) == "/mnt/Datastore/IGMM/ImageXpress2020/drug-discovery/GCGR-FDA/E13FDAa1/2021-04-03/490/TimePoint_1"



def test_img_well():
    filename = parse.img_filename(EXAMPLE_PATH)
    new_filename = parse.img_filename(NEW_EXAMPLE_PATH)
    assert parse.img_well(filename) == "B02"
    assert parse.img_well(new_filename) == "B02"


def test_img_site():
    filename = parse.img_filename(EXAMPLE_PATH)
    new_filename = parse.img_filename(NEW_EXAMPLE_PATH)
    assert parse.img_site(filename) == 1
    assert parse.img_site(new_filename) == 1


def test_img_channel():
    filename = parse.img_filename(EXAMPLE_PATH)
    new_filename = parse.img_filename(NEW_EXAMPLE_PATH)
    assert parse.img_channel(filename) == 1
    assert parse.img_channel(new_filename) == 1


def test_plate_name():
    assert parse.plate_name(EXAMPLE_PATH) == "HCC15691"
    assert parse.plate_name(NEW_EXAMPLE_PATH, old_path=False) == "E13FDAa1"


def test_plate_date_string():
    assert parse.plate_date(EXAMPLE_PATH, as_datetime=False) == "2015-07-31"
    assert parse.plate_date(NEW_EXAMPLE_PATH, as_datetime=False, old_path=False) == "2021-04-03"


def test_plate_date_datetime():
    ans = parse.plate_date(EXAMPLE_PATH, as_datetime=True)
    assert isinstance(ans, datetime.date)
    new_ans = parse.plate_date(NEW_EXAMPLE_PATH, as_datetime=True, old_path=False)
    assert isinstance(ans, datetime.date)
    assert isinstance(new_ans, datetime.date)


def test_plate_date_argument1():
    with pytest.raises(ValueError):
        parse.plate_date(EXAMPLE_PATH, as_datetime="not_boolean")


def test_plate_date_argument2():
    with pytest.raises(ValueError):
        parse.plate_date(EXAMPLE_PATH, as_datetime=1)


def test_plate_num():
    assert parse.plate_num(EXAMPLE_PATH) == 4014
    assert parse.plate_num(NEW_EXAMPLE_PATH, old_path=False) == 490


def test_check_filepath():
    parse.check_filepath(EXAMPLE_PATH)
    parse.check_filepath(NEW_EXAMPLE_PATH)


def test_check_filepath_too_short():
    example = "/too/short/img.tiff"
    with pytest.raises(ValueError):
        parse.check_filepath(example)


def test_check_filepath_missing_metadata():
    example = "/mnt/ImageXpress/2015-07-31 val screen/val screen/HCC15691/2015-07-31/4014/val screen_B02_s1_thumb62D4A363-7C7E-40D0-8A9E-55EC6681574D.tif"
    example_new = "/mnt/Datastore/IGMM/ImageXpress2020/drug-discovery/GCGR-FDA/E13FDAa1/2021-04-03/490/TimePoint_1/val screen_s1_w1_thumb62D4A363-7C7E-40D0-8A9E-55EC6681574D.tif"
    with pytest.raises(ValueError):
        parse.check_filepath(example)
        parse.check_filepath(example_new)

