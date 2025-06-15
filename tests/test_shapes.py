"""Tests for shape classes."""

import pytest
from PIL import Image

from shape_canvas.shapes import ShapeFactory, ShapeType, StraightLine, Rectangle, Circle
from shape_canvas.exceptions import InvalidShapeError, ValidationError


class TestShapeFactory:
    """Test cases for ShapeFactory."""
    
    def test_create_straight_line(self):
        """Test creating a straight line shape."""
        shape_data = {
            "type": "straight_line",
            "start": [10, 10],
            "end": [100, 100],
            "fill_color": [255, 0, 0],
            "border_width": 2
        }
        
        shape = ShapeFactory.create_shape(shape_data)
        assert isinstance(shape, StraightLine)
    
    def test_create_rectangle(self):
        """Test creating a rectangle shape."""
        shape_data = {
            "type": "rectangle",
            "start": [10, 10],
            "end": [100, 50],
            "fill_color": [0, 255, 0],
            "outline_color": [0, 0, 0],
            "border_width": 1
        }
        
        shape = ShapeFactory.create_shape(shape_data)
        assert isinstance(shape, Rectangle)
    
    def test_create_circle(self):
        """Test creating a circle shape."""
        shape_data = {
            "type": "circle",
            "center": [50, 50],
            "radius": 25,
            "fill_color": [0, 0, 255],
            "outline_color": [0, 0, 0],
            "border_width": 1
        }
        
        shape = ShapeFactory.create_shape(shape_data)
        assert isinstance(shape, Circle)
    
    def test_invalid_shape_type(self):
        """Test handling of invalid shape type."""
        shape_data = {
            "type": "invalid_shape",
            "start": [10, 10],
            "end": [100, 100]
        }
        
        with pytest.raises(InvalidShapeError):
            ShapeFactory.create_shape(shape_data)
    
    def test_missing_type(self):
        """Test handling of missing type field."""
        shape_data = {
            "start": [10, 10],
            "end": [100, 100]
        }
        
        with pytest.raises(InvalidShapeError):
            ShapeFactory.create_shape(shape_data)
    
    def test_get_supported_shapes(self):
        """Test getting list of supported shapes."""
        supported = ShapeFactory.get_supported_shapes()
        assert isinstance(supported, list)
        assert len(supported) > 0
        assert "straight_line" in supported
        assert "rectangle" in supported
        assert "circle" in supported


class TestShapeValidation:
    """Test cases for shape validation."""
    
    def test_straight_line_validation(self):
        """Test straight line validation."""
        # Valid data
        valid_data = {
            "start": [10, 10],
            "end": [100, 100],
            "fill_color": [255, 0, 0],
            "border_width": 2
        }
        shape = StraightLine(valid_data)
        assert shape is not None
        
        # Invalid data - missing start
        with pytest.raises(ValidationError):
            StraightLine({"end": [100, 100], "fill_color": [255, 0, 0], "border_width": 2})
        
        # Invalid data - invalid color
        with pytest.raises(ValidationError):
            StraightLine({
                "start": [10, 10],
                "end": [100, 100],
                "fill_color": [256, 0, 0],  # Invalid color value
                "border_width": 2
            })
    
    def test_rectangle_validation(self):
        """Test rectangle validation."""
        # Valid data
        valid_data = {
            "start": [10, 10],
            "end": [100, 50],
            "fill_color": [0, 255, 0],
            "outline_color": [0, 0, 0],
            "border_width": 1
        }
        shape = Rectangle(valid_data)
        assert shape is not None
        
        # Invalid data - negative border width
        with pytest.raises(ValidationError):
            Rectangle({
                "start": [10, 10],
                "end": [100, 50],
                "fill_color": [0, 255, 0],
                "outline_color": [0, 0, 0],
                "border_width": -1
            })
    
    def test_circle_validation(self):
        """Test circle validation."""
        # Valid data
        valid_data = {
            "center": [50, 50],
            "radius": 25,
            "fill_color": [0, 0, 255],
            "outline_color": [0, 0, 0],
            "border_width": 1
        }
        shape = Circle(valid_data)
        assert shape is not None
        
        # Invalid data - zero radius
        with pytest.raises(ValidationError):
            Circle({
                "center": [50, 50],
                "radius": 0,
                "fill_color": [0, 0, 255],
                "outline_color": [0, 0, 0],
                "border_width": 1
            })


class TestShapeDrawing:
    """Test cases for shape drawing."""
    
    def test_straight_line_drawing(self):
        """Test straight line drawing."""
        shape_data = {
            "start": [10, 10],
            "end": [100, 100],
            "fill_color": [255, 0, 0],
            "border_width": 2
        }
        
        shape = StraightLine(shape_data)
        canvas = Image.new('RGB', (200, 200), (255, 255, 255))
        
        result = shape.draw(canvas)
        assert isinstance(result, Image.Image)
        assert result.size == (200, 200)
    
    def test_rectangle_drawing(self):
        """Test rectangle drawing."""
        shape_data = {
            "start": [10, 10],
            "end": [100, 50],
            "fill_color": [0, 255, 0],
            "outline_color": [0, 0, 0],
            "border_width": 1
        }
        
        shape = Rectangle(shape_data)
        canvas = Image.new('RGB', (200, 200), (255, 255, 255))
        
        result = shape.draw(canvas)
        assert isinstance(result, Image.Image)
        assert result.size == (200, 200)
    
    def test_circle_drawing(self):
        """Test circle drawing."""
        shape_data = {
            "center": [50, 50],
            "radius": 25,
            "fill_color": [0, 0, 255],
            "outline_color": [0, 0, 0],
            "border_width": 1
        }
        
        shape = Circle(shape_data)
        canvas = Image.new('RGB', (200, 200), (255, 255, 255))
        
        result = shape.draw(canvas)
        assert isinstance(result, Image.Image)
        assert result.size == (200, 200)