"""
Parse metadata from ImageXpress files and paths.

A Python package for extracting metadata from ImageXpress file paths,
including well positions, site numbers, channels, plate names, dates, and more.
"""

from . import clean, parse

__version__ = "0.4.0"
__author__ = "Scott Warchal"
__email__ = "scott.warchal@ed.ac.uk"

__all__ = ["clean", "parse"]
