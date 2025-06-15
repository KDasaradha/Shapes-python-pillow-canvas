"""Custom exceptions for ShapeCanvas library."""


class ShapeCanvasError(Exception):
    """Base exception for ShapeCanvas library."""
    pass


class InvalidShapeError(ShapeCanvasError):
    """Raised when an invalid shape type is encountered."""
    pass


class ConfigurationError(ShapeCanvasError):
    """Raised when there's an error in configuration."""
    pass


class DrawingError(ShapeCanvasError):
    """Raised when there's an error during drawing operations."""
    pass


class ValidationError(ShapeCanvasError):
    """Raised when validation fails."""
    pass