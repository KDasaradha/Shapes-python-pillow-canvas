"""
ShapeCanvas - A powerful Python library for drawing geometric shapes and decorative elements.

This library provides a comprehensive set of tools for creating 2D graphics using PIL/Pillow,
with support for various shapes, lines, and decorative elements through JSON configuration.
"""

from .canvas import Canvas
from .shapes import ShapeFactory, ShapeType
from .exceptions import ShapeCanvasError, InvalidShapeError, ConfigurationError
from .config import CanvasConfig

__version__ = "1.0.0"
__author__ = "K. Dasaradha"
__email__ = "kdasaradha525@example.com"

__all__ = [
    "Canvas",
    "ShapeFactory", 
    "ShapeType",
    "CanvasConfig",
    "ShapeCanvasError",
    "InvalidShapeError",
    "ConfigurationError",
]