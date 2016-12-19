# Parse metadata from ImageXpress paths and file names

example:
```python
from parserix import parse_paths


filename = "/mnt/ImageXpress/screen/first_screen/HCC15691/2015-07-31/4014/val screen_B02_s1_w3E75611A2-A874-4065-BDAC-EE2467105EEB.tif"

parse_paths.get_img_well(filename)
    >>> "B02"

parse_paths.get_img_site(filename)
    >>> 1

parse_paths.get_plate_name(filename)
    >>> "HCC15691"

parse_paths.get_plate_date(filename)
    >>> "2015-07-31"
```