# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2025-01-27

### Added
- Modern Python package structure with `src/` layout
- `pyproject.toml` configuration replacing `setup.py`
- Comprehensive package metadata including classifiers and keywords
- MIT License file
- Development dependencies (pytest, ruff, mypy)
- Python 3.9+ support
- Enhanced documentation and README

### Changed
- Moved package files from `parserix/` to `src/parserix/`
- Updated package imports to use relative imports
- Enhanced `__init__.py` with version information and proper API exposure
- Updated minimum Python version to 3.9

### Removed
- Legacy `setup.py` file
- Old package directory structure

## [0.2] - Previous Release

### Added
- Initial release with basic ImageXpress metadata parsing functionality
- Support for parsing well positions, site numbers, channels, plate names, and dates
- File cleaning utilities for removing thumbnails and system files
