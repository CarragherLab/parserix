"""
clean image lists, removing thumbnails and any weird files/directories that
OS' like to add.
"""

def clean(file_list, ext=".tif"):
    """remove thumbnails and detritus"""
    wanted_files = []
    for f in file_list:
        if f.endswith(ext):
            if "thumb" not in f:
                wanted_files.append(f)
    return wanted_files
