"""Canvas class for ShapeCanvas library."""

import logging
from typing import Dict, Any, List, Optional, Union, Tuple
from pathlib import Path

from PIL import Image, ImageDraw

from .config import CanvasConfig, ConfigLoader
from .shapes import ShapeFactory, BaseShape
from .exceptions import DrawingError, ConfigurationError


logger = logging.getLogger(__name__)


class Canvas:
    """Main canvas class for drawing shapes."""
    
    def __init__(self, config: Union[CanvasConfig, Dict[str, Any], str, Path]):
        """
        Initialize canvas with configuration.
        
        Args:
            config: Canvas configuration as CanvasConfig object, dict, or file path
        """
        if isinstance(config, (str, Path)):
            config_data = ConfigLoader.load_from_file(config)
            self.config = CanvasConfig.from_dict(config_data)
            self._raw_config = config_data
        elif isinstance(config, dict):
            self.config = CanvasConfig.from_dict(config)
            self._raw_config = config
        elif isinstance(config, CanvasConfig):
            self.config = config
            self._raw_config = {}
        else:
            raise ConfigurationError("Invalid configuration type")
        
        self._canvas: Optional[Image.Image] = None
        self._shapes: List[BaseShape] = []
        self._initialize_canvas()
        
        # Auto-load shapes if present in configuration
        if 'shapes' in self._raw_config:
            self.load_shapes_from_config()
            # Add grid after loading shapes if configured
            self.add_grid()
    
    def _initialize_canvas(self) -> None:
        """Initialize the blank canvas."""
        try:
            self._canvas = Image.new('RGB', self.config.size, self.config.background_color)
            logger.info(f"Canvas initialized with size {self.config.size}")
        except Exception as e:
            raise DrawingError(f"Failed to initialize canvas: {e}")
    
    def add_grid(self) -> 'Canvas':
        """Add grid lines to the canvas."""
        if not self.config.show_grid or self.config.line_interval is None:
            return self
        
        if self._canvas is None:
            raise DrawingError("Canvas not initialized")
        
        try:
            draw = ImageDraw.Draw(self._canvas)
            width, height = self.config.size
            interval = self.config.line_interval
            line_color = self.config.line_color or "gray"
            
            # Draw vertical lines
            for x in range(0, width, interval):
                draw.line([(x, 0), (x, height)], fill=line_color)
            
            # Draw horizontal lines
            for y in range(0, height, interval):
                draw.line([(0, y), (width, y)], fill=line_color)
            
            # Add coordinate labels
            num_units_x = width // interval
            num_units_y = height // interval
            
            for x in range(num_units_x + 1):
                for y in range(num_units_y + 1):
                    coords = (x * interval, y * interval)
                    draw.text(coords, f"({x * interval},{y * interval})", fill="black")
            
            logger.info(f"Grid added with interval {interval}")
        except Exception as e:
            raise DrawingError(f"Failed to add grid: {e}")
        
        return self
    
    def add_shape(self, shape_data: Dict[str, Any]) -> 'Canvas':
        """
        Add a single shape to the canvas.
        
        Args:
            shape_data: Dictionary containing shape configuration
            
        Returns:
            Self for method chaining
        """
        try:
            # Validate shape data
            ConfigLoader.validate_shape_data(shape_data)
            
            # Create shape instance
            shape = ShapeFactory.create_shape(shape_data)
            self._shapes.append(shape)
            
            logger.info(f"Added shape: {shape_data.get('type', 'unknown')}")
        except Exception as e:
            logger.error(f"Failed to add shape {shape_data.get('type', 'unknown')}: {e}")
            raise DrawingError(f"Failed to add shape: {e}")
        
        return self
    
    def add_shapes(self, shapes_data: List[Dict[str, Any]]) -> 'Canvas':
        """
        Add multiple shapes to the canvas.
        
        Args:
            shapes_data: List of shape configuration dictionaries
            
        Returns:
            Self for method chaining
        """
        for shape_data in shapes_data:
            try:
                self.add_shape(shape_data)
            except DrawingError:
                # Continue with other shapes if one fails
                continue
        
        return self
    
    def load_shapes_from_config(self) -> 'Canvas':
        """Load shapes from the original configuration."""
        if 'shapes' in self._raw_config:
            self.add_shapes(self._raw_config['shapes'])
        return self
    
    def render(self) -> 'Canvas':
        """Render all shapes on the canvas."""
        if self._canvas is None:
            raise DrawingError("Canvas not initialized")
        
        try:
            for shape in self._shapes:
                self._canvas = shape.draw(self._canvas)
            
            logger.info(f"Rendered {len(self._shapes)} shapes")
        except Exception as e:
            raise DrawingError(f"Failed to render shapes: {e}")
        
        return self
    
    def save(self, filename: Union[str, Path], format: Optional[str] = None) -> 'Canvas':
        """
        Save the canvas to a file.
        
        Args:
            filename: Output filename
            format: Image format (auto-detected from filename if not provided)
            
        Returns:
            Self for method chaining
        """
        if self._canvas is None:
            raise DrawingError("Canvas not initialized")
        
        try:
            if format:
                self._canvas.save(filename, format=format)
            else:
                self._canvas.save(filename)
            
            logger.info(f"Canvas saved to {filename}")
        except Exception as e:
            raise DrawingError(f"Failed to save canvas: {e}")
        
        return self
    
    def show(self) -> 'Canvas':
        """Display the canvas."""
        if self._canvas is None:
            raise DrawingError("Canvas not initialized")
        
        try:
            self._canvas.show()
        except Exception as e:
            logger.warning(f"Failed to display canvas: {e}")
        
        return self
    
    def get_image(self) -> Image.Image:
        """Get the PIL Image object."""
        if self._canvas is None:
            raise DrawingError("Canvas not initialized")
        return self._canvas.copy()
    
    def clear(self) -> 'Canvas':
        """Clear the canvas and reset to background color."""
        self._shapes.clear()
        self._initialize_canvas()
        return self
    
    def get_canvas_info(self) -> Dict[str, Any]:
        """Get information about the canvas."""
        return {
            "size": self.config.size,
            "background_color": self.config.background_color,
            "show_grid": self.config.show_grid,
            "line_interval": self.config.line_interval,
            "shapes_count": len(self._shapes),
            "supported_shapes": ShapeFactory.get_supported_shapes()
        }
    
    @classmethod
    def from_file(cls, config_file: Union[str, Path]) -> 'Canvas':
        """
        Create canvas from configuration file.
        
        Args:
            config_file: Path to JSON configuration file
            
        Returns:
            Canvas instance
        """
        return cls(config_file)
    
    @classmethod
    def create_blank(cls, width: int, height: int, 
                    background_color: Tuple[int, int, int] = (255, 255, 255)) -> 'Canvas':
        """
        Create a blank canvas with specified dimensions.
        
        Args:
            width: Canvas width
            height: Canvas height
            background_color: RGB background color
            
        Returns:
            Canvas instance
        """
        config = CanvasConfig(
            size=(width, height),
            background_color=background_color
        )
        return cls(config)