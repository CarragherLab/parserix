"""
parse metadata from ImageXpress file paths
"""

from datetime import datetime
import os


def img_filename(file_path):
    """return the final image URL from a file path"""
    filename = str(file_path.split(os.sep)[-1])
    return filename.strip()


def path(file_path):
    """return the path up until the image URL"""
    p, _ = os.path.split(file_path)
    return p.strip()


def img_well(img_url, char="_"):
    """return well from final image URL"""
    return str(img_url.split(char)[1])


def img_site(img_url, char="_"):
    """return site from final image URL"""
    site_str = img_url.split(char)[2]
    return int("".join(x for x in site_str if x.isdigit()))


def img_channel(img_url, char="_"):
    """return site from final image URL"""
    return int(img_url.split(char)[3][1])


def plate_name(file_path, old_path=True):
    """return plate name from full image URL"""
    if old_path:
        index = -4
    else:
        index = -5
    return file_path.split(os.sep)[index]


def plate_date(file_path, as_datetime=False, old_path=True):
    """return plate date from full image URL"""
    if old_path:
        index = -3
    else:
        index = -4
    date = file_path.split(os.sep)[index]
    if as_datetime is False:
        return date
    elif as_datetime is True:
        return datetime.strptime(date, "%Y-%m-%d").date()
    else:
        raise ValueError("as_datetime needs to be a boolean")


def plate_num(file_path, old_path=True):
    """return plate number from full image URL"""
    if old_path:
        index = -2
    else:
        index = -3
    return int(file_path.split(os.sep)[index])


def check_filepath(file_path, char="_"):
    """sanity check of the file_path"""
    if len(file_path) < 20:
        raise ValueError("Filename {} too short".format(file_path))
    filename = img_filename(file_path)
    if len(filename.split(char)) < 5:
        msg = "Filename {} contains too few metadata values".format(filename)
        raise ValueError(msg)
