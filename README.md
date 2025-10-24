# parserix

Parse metadata from ImageXpress files and paths.

A Python package for extracting metadata from ImageXpress file paths, including well positions, site numbers, channels, plate names, dates, and more.

## Requirements

- Python 3.9 or higher

## Installation

### Using pip

```bash
pip install parserix
```

### Using uv (recommended)

```bash
uv add parserix
```

### Development installation

```bash
git clone https://github.com/CarragherLab/parserix.git
cd parserix
uv sync --group dev
```

## Usage

```python
from parserix import parse

filename = "/mnt/ImageXpress/screen/first_screen/HCC15691/2015-07-31/4014/val screen_B02_s1_w3E75611A2-A874-4065-BDAC-EE2467105EEB.tif"

# Extract well position
parse.img_well(filename)
# >>> "B02"

# Extract site number
parse.img_site(filename)
# >>> 1

# Extract channel number
parse.img_channel(filename)
# >>> 3

# Extract plate name
parse.plate_name(filename)
# >>> "HCC15691"

# Extract plate date as string
parse.plate_date(filename)
# >>> "2015-07-31"

# Extract plate date as datetime object
parse.plate_date(filename, as_datetime=True)
# >>> datetime.datetime(2015, 7, 31, 0, 0)

# Extract plate number
parse.plate_num(filename)
# >>> 4014

# Validate file path
parse.check_filepath(filename)
# >>> None (raises ValueError if invalid)
```

### Cleaning file lists

```python
from parserix import clean

file_list = [
    "image1.tif",
    "thumb_image.tif",  # This will be removed
    "Thumbs.db",        # This will be removed
    "image2.tif"
]

cleaned_files = clean.clean(file_list)
# >>> ["image1.tif", "image2.tif"]
```

## Development

### Setup development environment

```bash
uv sync --group dev
```

### Run tests

```bash
uv run pytest
```

### Run linting

```bash
uv run ruff check .
uv run mypy src/
```

### Build package

```bash
uv build
```

## API Reference

### parse module

- `img_filename(file_path)`: Extract filename from full path
- `path(file_path)`: Extract directory path from full path
- `img_well(img_url, char="_")`: Extract well position from filename
- `img_site(img_url, char="_")`: Extract site number from filename
- `img_channel(img_url, char="_")`: Extract channel number from filename
- `plate_name(file_path, old_path=True)`: Extract plate name from path
- `plate_date(file_path, as_datetime=False, old_path=True)`: Extract plate date
- `plate_num(file_path, old_path=True)`: Extract plate number from path
- `check_filepath(file_path, char="_")`: Validate file path format

### clean module

- `clean(file_list, ext=".tif")`: Remove thumbnails and system files from file list

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- [Repository](https://github.com/CarragherLab/parserix)
- [Issues](https://github.com/CarragherLab/parserix/issues)
- [Changelog](CHANGELOG.md)
