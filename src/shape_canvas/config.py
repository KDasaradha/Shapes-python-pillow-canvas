"""Configuration classes for ShapeCanvas."""

import json
from dataclasses import dataclass
from typing import Dict, List, Any, Tuple, Union, Optional
from pathlib import Path

from .exceptions import ConfigurationError, ValidationError


@dataclass
class CanvasConfig:
    """Configuration for canvas properties."""
    
    size: Tuple[int, int]
    background_color: Tuple[int, int, int]
    line_interval: Optional[int] = None
    line_color: Optional[str] = None
    show_grid: bool = False
    
    def __post_init__(self):
        """Validate configuration after initialization."""
        self.validate()
    
    def validate(self) -> None:
        """Validate canvas configuration."""
        if not isinstance(self.size, (tuple, list)) or len(self.size) != 2:
            raise ValidationError("Canvas size must be a tuple/list of two integers")
        
        if not all(isinstance(x, int) and x > 0 for x in self.size):
            raise ValidationError("Canvas size must contain positive integers")
        
        if not isinstance(self.background_color, (tuple, list)) or len(self.background_color) != 3:
            raise ValidationError("Background color must be a tuple/list of three integers (RGB)")
        
        if not all(isinstance(x, int) and 0 <= x <= 255 for x in self.background_color):
            raise ValidationError("Background color values must be integers between 0 and 255")
        
        if self.line_interval is not None and (not isinstance(self.line_interval, int) or self.line_interval <= 0):
            raise ValidationError("Line interval must be a positive integer")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CanvasConfig':
        """Create CanvasConfig from dictionary."""
        try:
            return cls(
                size=tuple(data['canvas_size']),
                background_color=tuple(data['background_color']),
                line_interval=data.get('line_interval'),
                line_color=data.get('line_color'),
                show_grid=data.get('show_grid', bool(data.get('line_interval')))
            )
        except KeyError as e:
            raise ConfigurationError(f"Missing required configuration key: {e}")
        except (TypeError, ValueError) as e:
            raise ConfigurationError(f"Invalid configuration value: {e}")


class ConfigLoader:
    """Utility class for loading configuration from various sources."""
    
    @staticmethod
    def load_from_file(file_path: Union[str, Path]) -> Dict[str, Any]:
        """Load configuration from JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise ConfigurationError(f"Configuration file not found: {file_path}")
        except json.JSONDecodeError as e:
            raise ConfigurationError(f"Invalid JSON in configuration file: {e}")
        except Exception as e:
            raise ConfigurationError(f"Error loading configuration file: {e}")
    
    @staticmethod
    def load_from_dict(data: Dict[str, Any]) -> Dict[str, Any]:
        """Load configuration from dictionary."""
        if not isinstance(data, dict):
            raise ConfigurationError("Configuration must be a dictionary")
        return data
    
    @staticmethod
    def validate_shape_data(shape_data: Dict[str, Any]) -> None:
        """Validate individual shape data."""
        if 'type' not in shape_data:
            raise ValidationError("Shape data must contain 'type' field")
        
        shape_type = shape_data['type']
        
        # Common validations for all shapes
        if 'fill_color' in shape_data:
            color = shape_data['fill_color']
            if not isinstance(color, (list, tuple)) or len(color) != 3:
                raise ValidationError(f"Invalid fill_color for {shape_type}")
            if not all(isinstance(x, int) and 0 <= x <= 255 for x in color):
                raise ValidationError(f"Invalid fill_color values for {shape_type}")
        
        if 'outline_color' in shape_data:
            color = shape_data['outline_color']
            if not isinstance(color, (list, tuple)) or len(color) != 3:
                raise ValidationError(f"Invalid outline_color for {shape_type}")
            if not all(isinstance(x, int) and 0 <= x <= 255 for x in color):
                raise ValidationError(f"Invalid outline_color values for {shape_type}")
        
        if 'border_width' in shape_data:
            width = shape_data['border_width']
            if not isinstance(width, int) or width < 0:
                raise ValidationError(f"Invalid border_width for {shape_type}")