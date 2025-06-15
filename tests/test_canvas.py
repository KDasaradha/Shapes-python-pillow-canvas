"""Tests for Canvas class."""

import pytest
import tempfile
import json
from pathlib import Path
from PIL import Image

from shape_canvas import Canvas, CanvasConfig
from shape_canvas.exceptions import DrawingError, ConfigurationError


class TestCanvas:
    """Test cases for Canvas class."""
    
    def test_create_blank_canvas(self):
        """Test creating a blank canvas."""
        canvas = Canvas.create_blank(800, 600, (255, 255, 255))
        assert canvas.config.size == (800, 600)
        assert canvas.config.background_color == (255, 255, 255)
        
        image = canvas.get_image()
        assert image.size == (800, 600)
    
    def test_canvas_from_config_dict(self):
        """Test creating canvas from configuration dictionary."""
        config = {
            "canvas_size": [400, 300],
            "background_color": [200, 200, 200]
        }
        canvas = Canvas(config)
        assert canvas.config.size == (400, 300)
        assert canvas.config.background_color == (200, 200, 200)
    
    def test_canvas_from_config_file(self):
        """Test creating canvas from configuration file."""
        config = {
            "canvas_size": [500, 400],
            "background_color": [100, 150, 200],
            "shapes": []
        }
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(config, f)
            f.flush()
            
            canvas = Canvas.from_file(f.name)
            assert canvas.config.size == (500, 400)
            assert canvas.config.background_color == (100, 150, 200)
    
    def test_add_shape(self):
        """Test adding a shape to canvas."""
        canvas = Canvas.create_blank(400, 300)
        shape_data = {
            "type": "rectangle",
            "start": [50, 50],
            "end": [150, 100],
            "fill_color": [255, 0, 0],
            "outline_color": [0, 0, 0],
            "border_width": 2
        }
        
        canvas.add_shape(shape_data)
        info = canvas.get_canvas_info()
        assert info["shapes_count"] == 1
    
    def test_add_shapes(self):
        """Test adding multiple shapes to canvas."""
        canvas = Canvas.create_blank(400, 300)
        shapes = [
            {
                "type": "rectangle",
                "start": [50, 50],
                "end": [150, 100],
                "fill_color": [255, 0, 0],
                "outline_color": [0, 0, 0],
                "border_width": 2
            },
            {
                "type": "circle",
                "center": [200, 150],
                "radius": 30,
                "fill_color": [0, 255, 0],
                "outline_color": [0, 0, 0],
                "border_width": 2
            }
        ]
        
        canvas.add_shapes(shapes)
        info = canvas.get_canvas_info()
        assert info["shapes_count"] == 2
    
    def test_render_and_save(self):
        """Test rendering and saving canvas."""
        canvas = Canvas.create_blank(200, 150)
        canvas.add_shape({
            "type": "circle",
            "center": [100, 75],
            "radius": 25,
            "fill_color": [255, 0, 0],
            "outline_color": [0, 0, 0],
            "border_width": 1
        })
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
            canvas.render().save(f.name)
            
            # Verify file was created and is a valid image
            saved_image = Image.open(f.name)
            assert saved_image.size == (200, 150)
    
    def test_clear_canvas(self):
        """Test clearing canvas."""
        canvas = Canvas.create_blank(400, 300)
        canvas.add_shape({
            "type": "rectangle",
            "start": [50, 50],
            "end": [150, 100],
            "fill_color": [255, 0, 0],
            "outline_color": [0, 0, 0],
            "border_width": 2
        })
        
        assert canvas.get_canvas_info()["shapes_count"] == 1
        
        canvas.clear()
        assert canvas.get_canvas_info()["shapes_count"] == 0
    
    def test_invalid_config(self):
        """Test handling of invalid configuration."""
        with pytest.raises(ConfigurationError):
            Canvas("nonexistent_file.json")
        
        with pytest.raises(ConfigurationError):
            Canvas({"invalid": "config"})
    
    def test_canvas_info(self):
        """Test getting canvas information."""
        canvas = Canvas.create_blank(800, 600, (255, 255, 255))
        info = canvas.get_canvas_info()
        
        assert info["size"] == (800, 600)
        assert info["background_color"] == (255, 255, 255)
        assert info["shapes_count"] == 0
        assert isinstance(info["supported_shapes"], list)
        assert len(info["supported_shapes"]) > 0