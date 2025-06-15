"""Shape classes and factory for ShapeCanvas."""

import math
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Any, List, Tuple, Optional
from PIL import Image, ImageDraw

from .exceptions import InvalidShapeError, DrawingError, ValidationError


class ShapeType(Enum):
    """Enumeration of supported shape types."""
    
    # Lines
    STRAIGHT_LINE = "straight_line"
    DASHED_LINE = "dashed_line"
    ZIGZAG_LINE = "zigzag_line"
    WAVY_LINE = "wavy_line"
    LINE_WITH_ARROWHEAD = "line_with_arrowhead"
    LINE_WITH_DOUBLE_ARROWHEAD = "line_with_double_arrowhead"
    
    # Connectors
    ELBOW_CONNECTOR = "elbow_connector"
    ELBOW_CONNECTOR_WITH_ARROWHEAD = "elbow_connector_with_arrowhead"
    ELBOW_CONNECTOR_WITH_DOUBLE_ARROWHEAD = "elbow_connector_with_double_arrowhead"
    
    # Basic shapes
    RECTANGLE = "rectangle"
    SQUARE = "square"
    CIRCLE = "circle"
    ELLIPSE = "ellipse"
    
    # Polygons
    POLYGON_WITH_COORDINATES = "polygon_with_coordinates"
    REGULAR_POLYGON = "regular_polygon"
    
    # Decorative shapes
    HEART = "heart"
    DIAMOND = "diamond"
    CLOUD = "cloud"
    STAR = "star"
    SPEECH_BUBBLE_RECTANGLE = "speech_bubble_rectangle"
    
    # Additional geometric shapes
    TRIANGLE = "triangle"
    PENTAGON = "pentagon"
    HEXAGON = "hexagon"
    OCTAGON = "octagon"
    RHOMBUS = "rhombus"
    PARALLELOGRAM = "parallelogram"
    TRAPEZOID = "trapezoid"
    
    # Arrow shapes
    BLOCK_ARROW = "block_arrow"
    CURVED_ARROW = "curved_arrow"
    CIRCULAR_ARROW = "circular_arrow"
    
    # Text-related shapes
    CALLOUT_BUBBLE = "callout_bubble"
    THOUGHT_BUBBLE = "thought_bubble"
    BANNER_RIBBON = "banner_ribbon"
    
    # More decorative shapes
    FLOWER = "flower"
    BUTTERFLY = "butterfly"
    TREE = "tree"
    SUN = "sun"
    MOON = "moon"
    LIGHTNING_BOLT = "lightning_bolt"
    
    # Technical/flowchart shapes
    OVAL_CALLOUT = "oval_callout"
    CROSS = "cross"
    PLUS_SIGN = "plus_sign"
    MINUS_SIGN = "minus_sign"
    MULTIPLICATION_SIGN = "multiplication_sign"
    
    # Advanced geometric shapes
    SPIRAL = "spiral"
    HELIX = "helix"
    SINE_WAVE_PATTERN = "sine_wave_pattern"
    FRACTAL_TREE = "fractal_tree"


class BaseShape(ABC):
    """Abstract base class for all shapes."""
    
    def __init__(self, data: Dict[str, Any]):
        """Initialize shape with data."""
        self.data = data
        self.validate()
    
    @abstractmethod
    def validate(self) -> None:
        """Validate shape-specific data."""
        pass
    
    @abstractmethod
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw the shape on the canvas."""
        pass
    
    def _get_color(self, key: str, default: Tuple[int, int, int] = (0, 0, 0)) -> Tuple[int, int, int]:
        """Get color from data with validation."""
        color = self.data.get(key, default)
        if isinstance(color, (list, tuple)) and len(color) == 3:
            # Validate that all color values are integers in the range 0-255
            if all(isinstance(x, int) and 0 <= x <= 255 for x in color):
                return tuple(color)
            else:
                raise ValidationError(f"Color values for {key} must be integers between 0 and 255")
        raise ValidationError(f"Invalid color format for {key}")
    
    def _get_point(self, key: str) -> Tuple[int, int]:
        """Get point coordinates from data with validation."""
        point = self.data.get(key)
        if point and isinstance(point, (list, tuple)) and len(point) == 2:
            return tuple(point)
        raise ValidationError(f"Invalid point format for {key}")
    
    def _get_int(self, key: str, default: int = 0, min_val: Optional[int] = None) -> int:
        """Get integer value from data with validation."""
        value = self.data.get(key, default)
        if not isinstance(value, int):
            raise ValidationError(f"Invalid integer value for {key}")
        if min_val is not None and value < min_val:
            raise ValidationError(f"Value for {key} must be >= {min_val}")
        return value


class StraightLine(BaseShape):
    """Straight line shape."""
    
    def validate(self) -> None:
        """Validate straight line data."""
        self._get_point('start')
        self._get_point('end')
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw straight line on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        
        draw.line([start, end], fill=fill_color, width=border_width)
        return canvas


class DashedLine(BaseShape):
    """Dashed line shape."""
    
    def validate(self) -> None:
        """Validate dashed line data."""
        self._get_point('start')
        self._get_point('end')
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
        self._get_int('dash_length', 10, min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw dashed line on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        dash_length = self._get_int('dash_length', 10)
        
        is_drawing_dash = True
        current_position = start
        
        # Calculate direction vector
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance == 0:
            return canvas
            
        # Normalize direction
        unit_x = dx / distance
        unit_y = dy / distance
        
        current_distance = 0
        
        while current_distance < distance:
            remaining_distance = distance - current_distance
            segment_length = min(dash_length, remaining_distance)
            
            next_position = (
                start[0] + (current_distance + segment_length) * unit_x,
                start[1] + (current_distance + segment_length) * unit_y
            )
            
            if is_drawing_dash:
                draw.line([current_position, next_position], fill=fill_color, width=border_width)
            
            current_position = next_position
            current_distance += segment_length
            is_drawing_dash = not is_drawing_dash
        
        return canvas


class Rectangle(BaseShape):
    """Rectangle shape."""
    
    def validate(self) -> None:
        """Validate rectangle data."""
        self._get_point('start')
        self._get_point('end')
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw rectangle on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        draw.rectangle([start, end], fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class Circle(BaseShape):
    """Circle shape."""
    
    def validate(self) -> None:
        """Validate circle data."""
        self._get_point('center')
        self._get_int('radius', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw circle on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        radius = self._get_int('radius')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        bbox = [
            (center[0] - radius, center[1] - radius),
            (center[0] + radius, center[1] + radius)
        ]
        draw.ellipse(bbox, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class Heart(BaseShape):
    """Heart shape."""
    
    def validate(self) -> None:
        """Validate heart data."""
        self._get_point('center')
        self._get_int('size', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
        self._get_int('rotation_angle', 0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw heart on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        size = self._get_int('size')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        rotation_angle = self._get_int('rotation_angle', 0)
        num_points = self.data.get('num_points', 100)
        
        def rotate_point(point: Tuple[float, float], angle_degrees: float, center_point: Tuple[int, int]) -> Tuple[float, float]:
            """Rotate a point around a center."""
            angle_rad = math.radians(angle_degrees)
            x, y = point
            cx, cy = center_point
            new_x = (x - cx) * math.cos(angle_rad) - (y - cy) * math.sin(angle_rad) + cx
            new_y = (x - cx) * math.sin(angle_rad) + (y - cy) * math.cos(angle_rad) + cy
            return (new_x, new_y)
        
        def heart_equation(t: float) -> Tuple[float, float]:
            """Calculate heart shape coordinates."""
            x = size * (16 * math.sin(t)**3)
            y = size * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
            return rotate_point((x + center[0], y + center[1]), rotation_angle, center)
        
        points = [heart_equation(2 * math.pi * t / num_points) for t in range(num_points)]
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        
        return canvas


class Star(BaseShape):
    """Star shape."""
    
    def validate(self) -> None:
        """Validate star data."""
        self._get_point('center')
        self._get_int('size', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
        self._get_int('num_points', 5, min_val=3)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw star on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        size = self._get_int('size')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        num_points = self._get_int('num_points', 5)
        
        x, y = center
        points = []
        
        for i in range(num_points * 2):
            angle = 2 * math.pi * i / (num_points * 2)
            radius = size if i % 2 == 0 else size * 0.4
            points.extend([x + radius * math.cos(angle), y + radius * math.sin(angle)])
        
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class Ellipse(BaseShape):
    """Ellipse shape."""
    
    def validate(self) -> None:
        """Validate ellipse data."""
        self._get_point('start')
        self._get_point('end')
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw ellipse on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        bbox = [start, end]
        draw.ellipse(bbox, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class Diamond(BaseShape):
    """Diamond shape."""
    
    def validate(self) -> None:
        """Validate diamond data."""
        self._get_point('center')
        self._get_int('size', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw diamond on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        size = self._get_int('size')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        # Diamond points: top, right, bottom, left
        points = [
            (x, y - size),      # top
            (x + size, y),      # right
            (x, y + size),      # bottom
            (x - size, y)       # left
        ]
        
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class Square(BaseShape):
    """Square shape."""
    
    def validate(self) -> None:
        """Validate square data."""
        self._get_point('start')
        self._get_int('size', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw square on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        size = self._get_int('size')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        end = (start[0] + size, start[1] + size)
        draw.rectangle([start, end], fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class Cloud(BaseShape):
    """Cloud shape."""
    
    def validate(self) -> None:
        """Validate cloud data."""
        self._get_point('center')
        self._get_int('size', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw cloud on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        size = self._get_int('size')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        
        # Draw multiple overlapping circles to create cloud shape
        # Main body (largest circle)
        draw.ellipse([(x - size, y - size//2), (x + size, y + size//2)], 
                    fill=fill_color, outline=outline_color, width=border_width)
        
        # Left puff
        draw.ellipse([(x - size//2, y - size//3), (x + size//3, y + size//3)], 
                    fill=fill_color, outline=outline_color, width=border_width)
        
        # Right puff  
        draw.ellipse([(x - size//3, y - size//3), (x + size//2, y + size//3)], 
                    fill=fill_color, outline=outline_color, width=border_width)
        
        # Top puff
        draw.ellipse([(x - size//3, y - size), (x + size//3, y)], 
                    fill=fill_color, outline=outline_color, width=border_width)
        
        return canvas


class ZigzagLine(BaseShape):
    """Zigzag line shape."""
    
    def validate(self) -> None:
        """Validate zigzag line data."""
        self._get_point('start')
        self._get_point('end')
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
        self._get_int('zigzag_height', 10, min_val=1)
        self._get_int('zigzag_frequency', 5, min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw zigzag line on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        zigzag_height = self._get_int('zigzag_height', 10)
        zigzag_frequency = self._get_int('zigzag_frequency', 5)
        
        # Calculate zigzag points
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        length = math.sqrt(dx*dx + dy*dy)
        
        if length == 0:
            return canvas
            
        # Unit vector along the line
        ux = dx / length
        uy = dy / length
        
        # Perpendicular unit vector
        px = -uy
        py = ux
        
        points = [start]
        
        for i in range(1, zigzag_frequency):
            t = i / zigzag_frequency
            base_x = start[0] + t * dx
            base_y = start[1] + t * dy
            
            # Alternate zigzag direction
            offset = zigzag_height if i % 2 == 1 else -zigzag_height
            zigzag_x = base_x + offset * px
            zigzag_y = base_y + offset * py
            
            points.append((zigzag_x, zigzag_y))
            
        points.append(end)
        
        # Draw the zigzag
        for i in range(len(points) - 1):
            draw.line([points[i], points[i + 1]], fill=fill_color, width=border_width)
        
        return canvas


class WavyLine(BaseShape):
    """Wavy line shape."""
    
    def validate(self) -> None:
        """Validate wavy line data."""
        self._get_point('start')
        self._get_point('end')
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
        self._get_int('wave_amplitude', 10, min_val=1)
        self._get_int('wave_frequency', 3, min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw wavy line on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        wave_amplitude = self._get_int('wave_amplitude', 10)
        wave_frequency = self._get_int('wave_frequency', 3)
        
        # Calculate wave points
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        length = math.sqrt(dx*dx + dy*dy)
        
        if length == 0:
            return canvas
            
        # Unit vector along the line
        ux = dx / length
        uy = dy / length
        
        # Perpendicular unit vector
        px = -uy
        py = ux
        
        points = []
        num_points = max(20, int(length / 5))  # More points for smoother waves
        
        for i in range(num_points + 1):
            t = i / num_points
            base_x = start[0] + t * dx
            base_y = start[1] + t * dy
            
            # Sine wave offset
            wave_offset = wave_amplitude * math.sin(2 * math.pi * wave_frequency * t)
            wave_x = base_x + wave_offset * px
            wave_y = base_y + wave_offset * py
            
            points.append((wave_x, wave_y))
        
        # Draw the wave
        for i in range(len(points) - 1):
            draw.line([points[i], points[i + 1]], fill=fill_color, width=border_width)
        
        return canvas


class LineWithArrowhead(BaseShape):
    """Line with arrowhead shape."""
    
    def validate(self) -> None:
        """Validate line with arrowhead data."""
        self._get_point('start')
        self._get_point('end')
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
        self._get_int('arrow_size', 10, min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw line with arrowhead on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        arrow_size = self._get_int('arrow_size', 10)
        
        # Draw the line
        draw.line([start, end], fill=fill_color, width=border_width)
        
        # Calculate arrowhead
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        length = math.sqrt(dx*dx + dy*dy)
        
        if length > 0:
            # Unit vector
            ux = dx / length
            uy = dy / length
            
            # Arrowhead points
            arrow_left = (
                end[0] - arrow_size * ux - arrow_size * 0.5 * uy,
                end[1] - arrow_size * uy + arrow_size * 0.5 * ux
            )
            arrow_right = (
                end[0] - arrow_size * ux + arrow_size * 0.5 * uy,
                end[1] - arrow_size * uy - arrow_size * 0.5 * ux
            )
            
            # Draw arrowhead
            draw.polygon([end, arrow_left, arrow_right], fill=fill_color)
        
        return canvas


class RegularPolygon(BaseShape):
    """Regular polygon shape."""
    
    def validate(self) -> None:
        """Validate regular polygon data."""
        self._get_point('center')
        self._get_int('radius', min_val=1)
        self._get_int('n_sides', 3, min_val=3)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
        self._get_int('rotation', 0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw regular polygon on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        radius = self._get_int('radius')
        n_sides = self._get_int('n_sides', 6)
        rotation = self._get_int('rotation', 0)
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        points = []
        rotation_radians = math.radians(rotation)
        
        for i in range(n_sides):
            angle = 2 * math.pi * i / n_sides + rotation_radians
            px = x + radius * math.cos(angle)
            py = y + radius * math.sin(angle)
            points.append((px, py))
        
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class SpeechBubbleRectangle(BaseShape):
    """Speech bubble rectangle shape."""
    
    def validate(self) -> None:
        """Validate speech bubble rectangle data."""
        self._get_point('start')
        self._get_point('end')
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
        self._get_int('tail_size', 10, min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw speech bubble rectangle on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        tail_size = self._get_int('tail_size', 10)
        
        # Draw main rectangle
        draw.rectangle([start, end], fill=fill_color, outline=outline_color, width=border_width)
        
        # Draw speech bubble tail (triangle)
        center_x = (start[0] + end[0]) // 2
        tail_points = [
            (center_x - tail_size, end[1]),
            (center_x + tail_size, end[1]),
            (center_x, end[1] + tail_size)
        ]
        draw.polygon(tail_points, fill=fill_color, outline=outline_color, width=border_width)
        
        return canvas


class PolygonWithCoordinates(BaseShape):
    """Polygon with custom coordinates shape."""
    
    def validate(self) -> None:
        """Validate polygon with coordinates data."""
        coordinates = self.data.get('coordinates')
        if not coordinates or not isinstance(coordinates, list) or len(coordinates) < 3:
            raise ValidationError("coordinates must be a list of at least 3 points")
        for point in coordinates:
            if not isinstance(point, (list, tuple)) or len(point) != 2:
                raise ValidationError("Each coordinate must be a [x, y] pair")
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw polygon with coordinates on canvas."""
        draw = ImageDraw.Draw(canvas)
        coordinates = self.data.get('coordinates')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        # Convert coordinates to tuples
        points = [tuple(point) for point in coordinates]
        
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class LineWithDoubleArrowhead(BaseShape):
    """Line with double arrowhead shape."""
    
    def validate(self) -> None:
        """Validate line with double arrowhead data."""
        self._get_point('start')
        self._get_point('end')
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
        self._get_int('arrow_size', 10, min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw line with double arrowhead on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        arrow_size = self._get_int('arrow_size', 10)
        
        # Draw the line
        draw.line([start, end], fill=fill_color, width=border_width)
        
        # Calculate direction vector
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        length = math.sqrt(dx*dx + dy*dy)
        
        if length > 0:
            # Unit vector
            ux = dx / length
            uy = dy / length
            
            # Arrowhead at end
            arrow_left_end = (
                end[0] - arrow_size * ux - arrow_size * 0.5 * uy,
                end[1] - arrow_size * uy + arrow_size * 0.5 * ux
            )
            arrow_right_end = (
                end[0] - arrow_size * ux + arrow_size * 0.5 * uy,
                end[1] - arrow_size * uy - arrow_size * 0.5 * ux
            )
            
            # Arrowhead at start (reverse direction)
            arrow_left_start = (
                start[0] + arrow_size * ux - arrow_size * 0.5 * uy,
                start[1] + arrow_size * uy + arrow_size * 0.5 * ux
            )
            arrow_right_start = (
                start[0] + arrow_size * ux + arrow_size * 0.5 * uy,
                start[1] + arrow_size * uy - arrow_size * 0.5 * ux
            )
            
            # Draw both arrowheads
            draw.polygon([end, arrow_left_end, arrow_right_end], fill=fill_color)
            draw.polygon([start, arrow_left_start, arrow_right_start], fill=fill_color)
        
        return canvas


class ElbowConnector(BaseShape):
    """Elbow connector shape."""
    
    def validate(self) -> None:
        """Validate elbow connector data."""
        self._get_point('start')
        self._get_point('end')
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw elbow connector on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        
        # Create elbow: start -> middle -> end
        # Middle point creates the 90-degree turn
        middle = (end[0], start[1])  # Horizontal first, then vertical
        
        # Draw two line segments
        draw.line([start, middle], fill=fill_color, width=border_width)
        draw.line([middle, end], fill=fill_color, width=border_width)
        
        return canvas


class ElbowConnectorWithArrowhead(BaseShape):
    """Elbow connector with arrowhead shape."""
    
    def validate(self) -> None:
        """Validate elbow connector with arrowhead data."""
        self._get_point('start')
        self._get_point('end')
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
        self._get_int('arrow_size', 10, min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw elbow connector with arrowhead on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        arrow_size = self._get_int('arrow_size', 10)
        
        # Create elbow: start -> middle -> end
        middle = (end[0], start[1])  # Horizontal first, then vertical
        
        # Draw two line segments
        draw.line([start, middle], fill=fill_color, width=border_width)
        draw.line([middle, end], fill=fill_color, width=border_width)
        
        # Add arrowhead at the end
        # Calculate direction from middle to end
        dx = end[0] - middle[0]
        dy = end[1] - middle[1]
        length = math.sqrt(dx*dx + dy*dy)
        
        if length > 0:
            # Unit vector
            ux = dx / length
            uy = dy / length
            
            # Arrowhead points
            arrow_left = (
                end[0] - arrow_size * ux - arrow_size * 0.5 * uy,
                end[1] - arrow_size * uy + arrow_size * 0.5 * ux
            )
            arrow_right = (
                end[0] - arrow_size * ux + arrow_size * 0.5 * uy,
                end[1] - arrow_size * uy - arrow_size * 0.5 * ux
            )
            
            # Draw arrowhead
            draw.polygon([end, arrow_left, arrow_right], fill=fill_color)
        
        return canvas


class ElbowConnectorWithDoubleArrowhead(BaseShape):
    """Elbow connector with double arrowhead shape."""
    
    def validate(self) -> None:
        """Validate elbow connector with double arrowhead data."""
        self._get_point('start')
        self._get_point('end')
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
        self._get_int('arrow_size', 10, min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw elbow connector with double arrowhead on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        arrow_size = self._get_int('arrow_size', 10)
        
        # Create elbow: start -> middle -> end
        middle = (end[0], start[1])  # Horizontal first, then vertical
        
        # Draw two line segments
        draw.line([start, middle], fill=fill_color, width=border_width)
        draw.line([middle, end], fill=fill_color, width=border_width)
        
        # Add arrowhead at the start (direction from start to middle)
        dx1 = middle[0] - start[0]
        dy1 = middle[1] - start[1]
        length1 = math.sqrt(dx1*dx1 + dy1*dy1)
        
        if length1 > 0:
            ux1 = dx1 / length1
            uy1 = dy1 / length1
            
            arrow_left_start = (
                start[0] + arrow_size * ux1 - arrow_size * 0.5 * uy1,
                start[1] + arrow_size * uy1 + arrow_size * 0.5 * ux1
            )
            arrow_right_start = (
                start[0] + arrow_size * ux1 + arrow_size * 0.5 * uy1,
                start[1] + arrow_size * uy1 - arrow_size * 0.5 * ux1
            )
            
            draw.polygon([start, arrow_left_start, arrow_right_start], fill=fill_color)
        
        # Add arrowhead at the end (direction from middle to end)
        dx2 = end[0] - middle[0]
        dy2 = end[1] - middle[1]
        length2 = math.sqrt(dx2*dx2 + dy2*dy2)
        
        if length2 > 0:
            ux2 = dx2 / length2
            uy2 = dy2 / length2
            
            arrow_left_end = (
                end[0] - arrow_size * ux2 - arrow_size * 0.5 * uy2,
                end[1] - arrow_size * uy2 + arrow_size * 0.5 * ux2
            )
            arrow_right_end = (
                end[0] - arrow_size * ux2 + arrow_size * 0.5 * uy2,
                end[1] - arrow_size * uy2 - arrow_size * 0.5 * ux2
            )
            
            draw.polygon([end, arrow_left_end, arrow_right_end], fill=fill_color)
        
        return canvas


# Additional Geometric Shapes

class Triangle(BaseShape):
    """Triangle shape."""
    
    def validate(self) -> None:
        """Validate triangle data."""
        self._get_point('point1')
        self._get_point('point2')
        self._get_point('point3')
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw triangle on canvas."""
        draw = ImageDraw.Draw(canvas)
        point1 = self._get_point('point1')
        point2 = self._get_point('point2')
        point3 = self._get_point('point3')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        points = [point1, point2, point3]
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class Pentagon(BaseShape):
    """Pentagon shape."""
    
    def validate(self) -> None:
        """Validate pentagon data."""
        self._get_point('center')
        self._get_int('radius', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
        self._get_int('rotation', 0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw pentagon on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        radius = self._get_int('radius')
        rotation = self._get_int('rotation', 0)
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        points = []
        rotation_radians = math.radians(rotation)
        
        for i in range(5):
            angle = 2 * math.pi * i / 5 + rotation_radians
            px = x + radius * math.cos(angle)
            py = y + radius * math.sin(angle)
            points.append((px, py))
        
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class Hexagon(BaseShape):
    """Hexagon shape."""
    
    def validate(self) -> None:
        """Validate hexagon data."""
        self._get_point('center')
        self._get_int('radius', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
        self._get_int('rotation', 0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw hexagon on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        radius = self._get_int('radius')
        rotation = self._get_int('rotation', 0)
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        points = []
        rotation_radians = math.radians(rotation)
        
        for i in range(6):
            angle = 2 * math.pi * i / 6 + rotation_radians
            px = x + radius * math.cos(angle)
            py = y + radius * math.sin(angle)
            points.append((px, py))
        
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class Octagon(BaseShape):
    """Octagon shape."""
    
    def validate(self) -> None:
        """Validate octagon data."""
        self._get_point('center')
        self._get_int('radius', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
        self._get_int('rotation', 0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw octagon on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        radius = self._get_int('radius')
        rotation = self._get_int('rotation', 0)
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        points = []
        rotation_radians = math.radians(rotation)
        
        for i in range(8):
            angle = 2 * math.pi * i / 8 + rotation_radians
            px = x + radius * math.cos(angle)
            py = y + radius * math.sin(angle)
            points.append((px, py))
        
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class Rhombus(BaseShape):
    """Rhombus shape."""
    
    def validate(self) -> None:
        """Validate rhombus data."""
        self._get_point('center')
        self._get_int('width', min_val=1)
        self._get_int('height', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
        self._get_int('rotation', 0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw rhombus on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        width = self._get_int('width')
        height = self._get_int('height')
        rotation = self._get_int('rotation', 0)
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        # Rhombus points: top, right, bottom, left
        points = [
            (x, y - height // 2),      # top
            (x + width // 2, y),       # right
            (x, y + height // 2),      # bottom
            (x - width // 2, y)        # left
        ]
        
        # Apply rotation if specified
        if rotation != 0:
            rotation_radians = math.radians(rotation)
            cos_r = math.cos(rotation_radians)
            sin_r = math.sin(rotation_radians)
            rotated_points = []
            for px, py in points:
                rx = (px - x) * cos_r - (py - y) * sin_r + x
                ry = (px - x) * sin_r + (py - y) * cos_r + y
                rotated_points.append((rx, ry))
            points = rotated_points
        
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class Parallelogram(BaseShape):
    """Parallelogram shape."""
    
    def validate(self) -> None:
        """Validate parallelogram data."""
        self._get_point('start')
        self._get_int('width', min_val=1)
        self._get_int('height', min_val=1)
        self._get_int('skew', 0)  # Horizontal skew amount
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw parallelogram on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        width = self._get_int('width')
        height = self._get_int('height')
        skew = self._get_int('skew', 0)
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = start
        # Parallelogram points with skew
        points = [
            (x + skew, y),                    # top-left (skewed)
            (x + width + skew, y),            # top-right (skewed)
            (x + width, y + height),          # bottom-right
            (x, y + height)                   # bottom-left
        ]
        
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class Trapezoid(BaseShape):
    """Trapezoid shape."""
    
    def validate(self) -> None:
        """Validate trapezoid data."""
        self._get_point('start')
        self._get_int('bottom_width', min_val=1)
        self._get_int('top_width', min_val=1)
        self._get_int('height', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw trapezoid on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        bottom_width = self._get_int('bottom_width')
        top_width = self._get_int('top_width')
        height = self._get_int('height')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = start
        # Calculate top offset to center the top edge
        top_offset = (bottom_width - top_width) // 2
        
        # Trapezoid points
        points = [
            (x + top_offset, y),                    # top-left
            (x + top_offset + top_width, y),        # top-right
            (x + bottom_width, y + height),         # bottom-right
            (x, y + height)                         # bottom-left
        ]
        
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


# Arrow Shapes

class BlockArrow(BaseShape):
    """Block arrow shape."""
    
    def validate(self) -> None:
        """Validate block arrow data."""
        self._get_point('start')
        self._get_point('end')
        self._get_int('shaft_width', min_val=1)
        self._get_int('head_width', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw block arrow on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        shaft_width = self._get_int('shaft_width')
        head_width = self._get_int('head_width')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        # Calculate direction vector
        dx = end[0] - start[0]
        dy = end[1] - start[1]
        length = math.sqrt(dx*dx + dy*dy)
        
        if length == 0:
            return canvas
        
        # Unit vectors
        ux = dx / length
        uy = dy / length
        px = -uy  # Perpendicular
        py = ux
        
        # Arrow head length (proportion of total length)
        head_length = min(length * 0.3, head_width)
        shaft_length = length - head_length
        
        # Calculate points
        shaft_start_1 = (start[0] + px * shaft_width // 2, start[1] + py * shaft_width // 2)
        shaft_start_2 = (start[0] - px * shaft_width // 2, start[1] - py * shaft_width // 2)
        
        shaft_end_1 = (start[0] + ux * shaft_length + px * shaft_width // 2, 
                      start[1] + uy * shaft_length + py * shaft_width // 2)
        shaft_end_2 = (start[0] + ux * shaft_length - px * shaft_width // 2, 
                      start[1] + uy * shaft_length - py * shaft_width // 2)
        
        head_base_1 = (start[0] + ux * shaft_length + px * head_width // 2, 
                      start[1] + uy * shaft_length + py * head_width // 2)
        head_base_2 = (start[0] + ux * shaft_length - px * head_width // 2, 
                      start[1] + uy * shaft_length - py * head_width // 2)
        
        # Block arrow points
        points = [
            shaft_start_1, shaft_end_1, head_base_1, end, head_base_2, shaft_end_2, shaft_start_2
        ]
        
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        return canvas


class CurvedArrow(BaseShape):
    """Curved arrow shape."""
    
    def validate(self) -> None:
        """Validate curved arrow data."""
        self._get_point('start')
        self._get_point('end')
        self._get_int('curve_height', min_val=1)
        self._get_int('arrow_size', 10, min_val=1)
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw curved arrow on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        end = self._get_point('end')
        curve_height = self._get_int('curve_height')
        arrow_size = self._get_int('arrow_size', 10)
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        
        # Calculate control point for quadratic Bezier curve
        mid_x = (start[0] + end[0]) // 2
        mid_y = (start[1] + end[1]) // 2 - curve_height
        
        # Generate curve points using quadratic Bezier
        points = []
        num_points = 50
        for i in range(num_points + 1):
            t = i / num_points
            # Quadratic Bezier formula: B(t) = (1-t)²P0 + 2(1-t)tP1 + t²P2
            x = (1-t)**2 * start[0] + 2*(1-t)*t * mid_x + t**2 * end[0]
            y = (1-t)**2 * start[1] + 2*(1-t)*t * mid_y + t**2 * end[1]
            points.append((x, y))
        
        # Draw the curved line
        for i in range(len(points) - 1):
            draw.line([points[i], points[i + 1]], fill=fill_color, width=border_width)
        
        # Add arrowhead at the end
        dx = points[-1][0] - points[-2][0]
        dy = points[-1][1] - points[-2][1]
        length = math.sqrt(dx*dx + dy*dy)
        
        if length > 0:
            ux = dx / length
            uy = dy / length
            
            arrow_left = (
                end[0] - arrow_size * ux - arrow_size * 0.5 * uy,
                end[1] - arrow_size * uy + arrow_size * 0.5 * ux
            )
            arrow_right = (
                end[0] - arrow_size * ux + arrow_size * 0.5 * uy,
                end[1] - arrow_size * uy - arrow_size * 0.5 * ux
            )
            
            draw.polygon([end, arrow_left, arrow_right], fill=fill_color)
        
        return canvas


class CircularArrow(BaseShape):
    """Circular arrow shape."""
    
    def validate(self) -> None:
        """Validate circular arrow data."""
        self._get_point('center')
        self._get_int('radius', min_val=1)
        self._get_int('start_angle', 0)
        self._get_int('end_angle', 270)
        self._get_int('arrow_size', 10, min_val=1)
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw circular arrow on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        radius = self._get_int('radius')
        start_angle = self._get_int('start_angle', 0)
        end_angle = self._get_int('end_angle', 270)
        arrow_size = self._get_int('arrow_size', 10)
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        
        # Draw arc
        bbox = [x - radius, y - radius, x + radius, y + radius]
        draw.arc(bbox, start_angle, end_angle, fill=fill_color, width=border_width)
        
        # Add arrowhead at the end of the arc
        end_angle_rad = math.radians(end_angle)
        end_x = x + radius * math.cos(end_angle_rad)
        end_y = y + radius * math.sin(end_angle_rad)
        
        # Calculate tangent direction at end point
        tangent_angle = end_angle_rad + math.pi / 2
        tx = math.cos(tangent_angle)
        ty = math.sin(tangent_angle)
        
        # Arrowhead points
        arrow_left = (
            end_x - arrow_size * tx - arrow_size * 0.5 * ty,
            end_y - arrow_size * ty + arrow_size * 0.5 * tx
        )
        arrow_right = (
            end_x - arrow_size * tx + arrow_size * 0.5 * ty,
            end_y - arrow_size * ty - arrow_size * 0.5 * tx
        )
        
        draw.polygon([(end_x, end_y), arrow_left, arrow_right], fill=fill_color)
        
        return canvas


# Text-related Shapes

class CalloutBubble(BaseShape):
    """Callout bubble shape."""
    
    def validate(self) -> None:
        """Validate callout bubble data."""
        self._get_point('center')
        self._get_int('width', min_val=1)
        self._get_int('height', min_val=1)
        self._get_point('pointer_tip')
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw callout bubble on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        width = self._get_int('width')
        height = self._get_int('height')
        pointer_tip = self._get_point('pointer_tip')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        # Main oval bubble
        bbox = [x - width//2, y - height//2, x + width//2, y + height//2]
        draw.ellipse(bbox, fill=fill_color, outline=outline_color, width=border_width)
        
        # Pointer triangle
        # Find closest point on ellipse to pointer tip
        angle = math.atan2(pointer_tip[1] - y, pointer_tip[0] - x)
        ellipse_x = x + (width//2) * math.cos(angle) * 0.8
        ellipse_y = y + (height//2) * math.sin(angle) * 0.8
        
        # Triangle points for pointer
        side_angle1 = angle + math.pi/6
        side_angle2 = angle - math.pi/6
        pointer_size = min(width, height) // 8
        
        side_point1 = (
            ellipse_x + pointer_size * math.cos(side_angle1),
            ellipse_y + pointer_size * math.sin(side_angle1)
        )
        side_point2 = (
            ellipse_x + pointer_size * math.cos(side_angle2),
            ellipse_y + pointer_size * math.sin(side_angle2)
        )
        
        draw.polygon([pointer_tip, side_point1, side_point2], 
                    fill=fill_color, outline=outline_color, width=border_width)
        
        return canvas


class ThoughtBubble(BaseShape):
    """Thought bubble shape."""
    
    def validate(self) -> None:
        """Validate thought bubble data."""
        self._get_point('center')
        self._get_int('width', min_val=1)
        self._get_int('height', min_val=1)
        self._get_point('pointer_direction')
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw thought bubble on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        width = self._get_int('width')
        height = self._get_int('height')
        pointer_direction = self._get_point('pointer_direction')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        # Main cloud-like bubble with multiple overlapping circles
        main_bbox = [x - width//2, y - height//2, x + width//2, y + height//2]
        draw.ellipse(main_bbox, fill=fill_color, outline=outline_color, width=border_width)
        
        # Additional bumps for cloud effect
        bump_size = min(width, height) // 6
        for i in range(4):
            angle = 2 * math.pi * i / 4
            bump_x = x + (width//3) * math.cos(angle)
            bump_y = y + (height//3) * math.sin(angle)
            bump_bbox = [bump_x - bump_size, bump_y - bump_size, 
                        bump_x + bump_size, bump_y + bump_size]
            draw.ellipse(bump_bbox, fill=fill_color, outline=outline_color, width=border_width)
        
        # Small circles leading to pointer direction
        dx = pointer_direction[0] - x
        dy = pointer_direction[1] - y
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance > 0:
            ux = dx / distance
            uy = dy / distance
            
            # Draw decreasing circles
            for i in range(3):
                circle_distance = (width//2) + (i + 1) * 20
                circle_size = max(3, 8 - i * 2)
                circle_x = x + ux * circle_distance
                circle_y = y + uy * circle_distance
                
                circle_bbox = [circle_x - circle_size, circle_y - circle_size,
                              circle_x + circle_size, circle_y + circle_size]
                draw.ellipse(circle_bbox, fill=fill_color, outline=outline_color, width=border_width)
        
        return canvas


class BannerRibbon(BaseShape):
    """Banner ribbon shape."""
    
    def validate(self) -> None:
        """Validate banner ribbon data."""
        self._get_point('start')
        self._get_int('width', min_val=1)
        self._get_int('height', min_val=1)
        self._get_int('tail_length', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw banner ribbon on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        width = self._get_int('width')
        height = self._get_int('height')
        tail_length = self._get_int('tail_length')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = start
        
        # Main rectangle body
        main_points = [
            (x, y),
            (x + width - tail_length, y),
            (x + width - tail_length, y + height),
            (x, y + height)
        ]
        
        # Ribbon tail (triangle cut)
        tail_points = [
            (x + width - tail_length, y),
            (x + width, y + height//2),
            (x + width - tail_length, y + height)
        ]
        
        # Combine main body and tail
        ribbon_points = [
            (x, y),
            (x + width - tail_length, y),
            (x + width, y + height//2),
            (x + width - tail_length, y + height),
            (x, y + height)
        ]
        
        draw.polygon(ribbon_points, fill=fill_color, outline=outline_color, width=border_width)
        
        return canvas


# More Decorative Shapes

class Flower(BaseShape):
    """Flower shape."""
    
    def validate(self) -> None:
        """Validate flower data."""
        self._get_point('center')
        self._get_int('petal_size', min_val=1)
        self._get_int('num_petals', 6, min_val=3)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_color('center_color', (255, 255, 0))  # Default yellow center
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw flower on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        petal_size = self._get_int('petal_size')
        num_petals = self._get_int('num_petals', 6)
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        center_color = self._get_color('center_color', (255, 255, 0))
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        
        # Draw petals as ellipses
        for i in range(num_petals):
            angle = 2 * math.pi * i / num_petals
            petal_center_x = x + (petal_size * 0.7) * math.cos(angle)
            petal_center_y = y + (petal_size * 0.7) * math.sin(angle)
            
            # Petal ellipse bbox
            petal_bbox = [
                petal_center_x - petal_size//3,
                petal_center_y - petal_size//2,
                petal_center_x + petal_size//3,
                petal_center_y + petal_size//2
            ]
            
            draw.ellipse(petal_bbox, fill=fill_color, outline=outline_color, width=border_width)
        
        # Draw flower center
        center_size = petal_size // 3
        center_bbox = [x - center_size, y - center_size, x + center_size, y + center_size]
        draw.ellipse(center_bbox, fill=center_color, outline=outline_color, width=border_width)
        
        return canvas


class Butterfly(BaseShape):
    """Butterfly shape."""
    
    def validate(self) -> None:
        """Validate butterfly data."""
        self._get_point('center')
        self._get_int('wing_size', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_color('body_color', (0, 0, 0))  # Default black body
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw butterfly on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        wing_size = self._get_int('wing_size')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        body_color = self._get_color('body_color', (0, 0, 0))
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        
        # Upper wings (larger)
        upper_wing_size = wing_size
        # Left upper wing
        left_upper_bbox = [x - wing_size - upper_wing_size//2, y - wing_size, 
                          x - 5, y - 5]
        draw.ellipse(left_upper_bbox, fill=fill_color, outline=outline_color, width=border_width)
        
        # Right upper wing
        right_upper_bbox = [x + 5, y - wing_size, 
                           x + wing_size + upper_wing_size//2, y - 5]
        draw.ellipse(right_upper_bbox, fill=fill_color, outline=outline_color, width=border_width)
        
        # Lower wings (smaller)
        lower_wing_size = wing_size // 2
        # Left lower wing
        left_lower_bbox = [x - wing_size, y + 5, 
                          x - 5, y + lower_wing_size + 5]
        draw.ellipse(left_lower_bbox, fill=fill_color, outline=outline_color, width=border_width)
        
        # Right lower wing
        right_lower_bbox = [x + 5, y + 5, 
                           x + wing_size, y + lower_wing_size + 5]
        draw.ellipse(right_lower_bbox, fill=fill_color, outline=outline_color, width=border_width)
        
        # Body (vertical line)
        body_width = max(3, border_width + 1)
        draw.line([(x, y - wing_size), (x, y + lower_wing_size)], 
                 fill=body_color, width=body_width)
        
        # Antennae
        antenna_length = wing_size // 3
        draw.line([(x - 2, y - wing_size), (x - 5, y - wing_size - antenna_length)], 
                 fill=body_color, width=1)
        draw.line([(x + 2, y - wing_size), (x + 5, y - wing_size - antenna_length)], 
                 fill=body_color, width=1)
        
        return canvas


class Tree(BaseShape):
    """Tree shape."""
    
    def validate(self) -> None:
        """Validate tree data."""
        self._get_point('base')
        self._get_int('height', min_val=1)
        self._get_int('crown_width', min_val=1)
        self._get_color('trunk_color', (139, 69, 19))  # Brown
        self._get_color('crown_color', (34, 139, 34))  # Forest green
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw tree on canvas."""
        draw = ImageDraw.Draw(canvas)
        base = self._get_point('base')
        height = self._get_int('height')
        crown_width = self._get_int('crown_width')
        trunk_color = self._get_color('trunk_color', (139, 69, 19))
        crown_color = self._get_color('crown_color', (34, 139, 34))
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = base
        
        # Tree trunk
        trunk_width = crown_width // 6
        trunk_height = height // 3
        trunk_points = [
            (x - trunk_width, y),
            (x + trunk_width, y),
            (x + trunk_width, y - trunk_height),
            (x - trunk_width, y - trunk_height)
        ]
        draw.polygon(trunk_points, fill=trunk_color, outline=outline_color, width=border_width)
        
        # Tree crown (multiple overlapping circles for natural look)
        crown_center_y = y - trunk_height - crown_width//3
        
        # Main crown circle
        main_crown_bbox = [x - crown_width//2, crown_center_y - crown_width//2,
                          x + crown_width//2, crown_center_y + crown_width//2]
        draw.ellipse(main_crown_bbox, fill=crown_color, outline=outline_color, width=border_width)
        
        # Additional crown circles for fuller look
        for i in range(4):
            angle = 2 * math.pi * i / 4
            offset_x = (crown_width//4) * math.cos(angle)
            offset_y = (crown_width//4) * math.sin(angle)
            
            extra_crown_size = crown_width // 3
            extra_crown_bbox = [
                x + offset_x - extra_crown_size//2,
                crown_center_y + offset_y - extra_crown_size//2,
                x + offset_x + extra_crown_size//2,
                crown_center_y + offset_y + extra_crown_size//2
            ]
            draw.ellipse(extra_crown_bbox, fill=crown_color, outline=outline_color, width=border_width)
        
        return canvas


class Sun(BaseShape):
    """Sun shape."""
    
    def validate(self) -> None:
        """Validate sun data."""
        self._get_point('center')
        self._get_int('radius', min_val=1)
        self._get_int('num_rays', 8, min_val=4)
        self._get_int('ray_length', min_val=1)
        self._get_color('fill_color', (255, 255, 0))  # Yellow
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw sun on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        radius = self._get_int('radius')
        num_rays = self._get_int('num_rays', 8)
        ray_length = self._get_int('ray_length')
        fill_color = self._get_color('fill_color', (255, 255, 0))
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        
        # Draw sun rays
        for i in range(num_rays):
            angle = 2 * math.pi * i / num_rays
            
            # Ray start (at circle edge)
            start_x = x + radius * math.cos(angle)
            start_y = y + radius * math.sin(angle)
            
            # Ray end
            end_x = x + (radius + ray_length) * math.cos(angle)
            end_y = y + (radius + ray_length) * math.sin(angle)
            
            draw.line([(start_x, start_y), (end_x, end_y)], 
                     fill=fill_color, width=max(2, border_width))
        
        # Draw sun center circle
        sun_bbox = [x - radius, y - radius, x + radius, y + radius]
        draw.ellipse(sun_bbox, fill=fill_color, outline=outline_color, width=border_width)
        
        return canvas


class Moon(BaseShape):
    """Moon shape."""
    
    def validate(self) -> None:
        """Validate moon data."""
        self._get_point('center')
        self._get_int('radius', min_val=1)
        self._get_int('phase_offset', 0)  # 0=full, positive=waning, negative=waxing
        self._get_color('fill_color', (255, 255, 224))  # Light yellow
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw moon on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        radius = self._get_int('radius')
        phase_offset = self._get_int('phase_offset', 0)
        fill_color = self._get_color('fill_color', (255, 255, 224))
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        
        if phase_offset == 0:
            # Full moon - simple circle
            moon_bbox = [x - radius, y - radius, x + radius, y + radius]
            draw.ellipse(moon_bbox, fill=fill_color, outline=outline_color, width=border_width)
        else:
            # Crescent moon - create by overlapping circles
            main_bbox = [x - radius, y - radius, x + radius, y + radius]
            
            # Create a temporary image for masking
            temp_img = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
            temp_draw = ImageDraw.Draw(temp_img)
            
            # Draw full moon
            temp_draw.ellipse(main_bbox, fill=fill_color + (255,), outline=outline_color + (255,), width=border_width)
            
            # Draw shadow circle to create crescent
            shadow_offset = abs(phase_offset)
            shadow_x = x + (shadow_offset * radius // 100)
            shadow_bbox = [shadow_x - radius, y - radius, shadow_x + radius, y + radius]
            
            # Use black with alpha for shadow effect
            temp_draw.ellipse(shadow_bbox, fill=(0, 0, 0, 200))
            
            # Paste the temp image onto the main canvas
            canvas.paste(temp_img, (0, 0), temp_img)
        
        return canvas


class LightningBolt(BaseShape):
    """Lightning bolt shape."""
    
    def validate(self) -> None:
        """Validate lightning bolt data."""
        self._get_point('start')
        self._get_int('height', min_val=1)
        self._get_int('width', min_val=1)
        self._get_color('fill_color', (255, 255, 0))  # Yellow
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw lightning bolt on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        height = self._get_int('height')
        width = self._get_int('width')
        fill_color = self._get_color('fill_color', (255, 255, 0))
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = start
        
        # Lightning bolt zigzag pattern
        points = [
            (x, y),                           # top
            (x + width//3, y + height//3),    # first bend
            (x - width//6, y + height//3),    # left jut
            (x + width//6, y + 2*height//3),  # middle
            (x - width//3, y + 2*height//3),  # left jut 2
            (x, y + height),                  # bottom
            (x + width//4, y + 2*height//3),  # right side up
            (x + width//2, y + 2*height//3),  # right jut
            (x + width//6, y + height//3),    # up to first bend
            (x + width//2, y + height//3),    # right jut top
            (x + width//3, y)                 # top right
        ]
        
        draw.polygon(points, fill=fill_color, outline=outline_color, width=border_width)
        
        return canvas


# Technical/Flowchart Shapes

class OvalCallout(BaseShape):
    """Oval callout shape."""
    
    def validate(self) -> None:
        """Validate oval callout data."""
        self._get_point('center')
        self._get_int('width', min_val=1)
        self._get_int('height', min_val=1)
        self._get_point('callout_point')
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw oval callout on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        width = self._get_int('width')
        height = self._get_int('height')
        callout_point = self._get_point('callout_point')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        
        # Main oval
        oval_bbox = [x - width//2, y - height//2, x + width//2, y + height//2]
        draw.ellipse(oval_bbox, fill=fill_color, outline=outline_color, width=border_width)
        
        # Callout line
        draw.line([center, callout_point], fill=outline_color, width=border_width)
        
        # Small circle at callout point
        circle_size = 3
        circle_bbox = [callout_point[0] - circle_size, callout_point[1] - circle_size,
                      callout_point[0] + circle_size, callout_point[1] + circle_size]
        draw.ellipse(circle_bbox, fill=fill_color, outline=outline_color, width=border_width)
        
        return canvas


class Cross(BaseShape):
    """Cross shape."""
    
    def validate(self) -> None:
        """Validate cross data."""
        self._get_point('center')
        self._get_int('size', min_val=1)
        self._get_int('thickness', min_val=1)
        self._get_color('fill_color')
        self._get_color('outline_color')
        self._get_int('border_width', min_val=0)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw cross on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        size = self._get_int('size')
        thickness = self._get_int('thickness')
        fill_color = self._get_color('fill_color')
        outline_color = self._get_color('outline_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        
        # Vertical bar
        vertical_points = [
            (x - thickness//2, y - size),
            (x + thickness//2, y - size),
            (x + thickness//2, y + size),
            (x - thickness//2, y + size)
        ]
        draw.polygon(vertical_points, fill=fill_color, outline=outline_color, width=border_width)
        
        # Horizontal bar
        horizontal_points = [
            (x - size, y - thickness//2),
            (x + size, y - thickness//2),
            (x + size, y + thickness//2),
            (x - size, y + thickness//2)
        ]
        draw.polygon(horizontal_points, fill=fill_color, outline=outline_color, width=border_width)
        
        return canvas


class PlusSign(BaseShape):
    """Plus sign shape."""
    
    def validate(self) -> None:
        """Validate plus sign data."""
        self._get_point('center')
        self._get_int('size', min_val=1)
        self._get_int('thickness', min_val=1)
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw plus sign on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        size = self._get_int('size')
        thickness = self._get_int('thickness')
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        
        # Vertical line
        draw.line([(x, y - size), (x, y + size)], fill=fill_color, width=thickness)
        
        # Horizontal line
        draw.line([(x - size, y), (x + size, y)], fill=fill_color, width=thickness)
        
        return canvas


class MinusSign(BaseShape):
    """Minus sign shape."""
    
    def validate(self) -> None:
        """Validate minus sign data."""
        self._get_point('center')
        self._get_int('size', min_val=1)
        self._get_int('thickness', min_val=1)
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw minus sign on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        size = self._get_int('size')
        thickness = self._get_int('thickness')
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        
        # Horizontal line
        draw.line([(x - size, y), (x + size, y)], fill=fill_color, width=thickness)
        
        return canvas


class MultiplicationSign(BaseShape):
    """Multiplication sign shape."""
    
    def validate(self) -> None:
        """Validate multiplication sign data."""
        self._get_point('center')
        self._get_int('size', min_val=1)
        self._get_int('thickness', min_val=1)
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw multiplication sign on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        size = self._get_int('size')
        thickness = self._get_int('thickness')
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        
        # Diagonal line (top-left to bottom-right)
        draw.line([(x - size, y - size), (x + size, y + size)], fill=fill_color, width=thickness)
        
        # Diagonal line (top-right to bottom-left)
        draw.line([(x + size, y - size), (x - size, y + size)], fill=fill_color, width=thickness)
        
        return canvas


# Advanced Geometric Shapes

class Spiral(BaseShape):
    """Spiral shape."""
    
    def validate(self) -> None:
        """Validate spiral data."""
        self._get_point('center')
        self._get_int('max_radius', min_val=1)
        self._get_int('turns', 3, min_val=1)
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw spiral on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        max_radius = self._get_int('max_radius')
        turns = self._get_int('turns', 3)
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        
        # Generate spiral points
        points = []
        num_points = turns * 50  # More points for smoother spiral
        
        for i in range(num_points):
            angle = 2 * math.pi * turns * i / num_points
            radius = max_radius * i / num_points
            
            px = x + radius * math.cos(angle)
            py = y + radius * math.sin(angle)
            points.append((px, py))
        
        # Draw spiral as connected line segments
        for i in range(len(points) - 1):
            draw.line([points[i], points[i + 1]], fill=fill_color, width=border_width)
        
        return canvas


class Helix(BaseShape):
    """Helix shape."""
    
    def validate(self) -> None:
        """Validate helix data."""
        self._get_point('center')
        self._get_int('radius', min_val=1)
        self._get_int('height', min_val=1)
        self._get_int('turns', 3, min_val=1)
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw helix on canvas."""
        draw = ImageDraw.Draw(canvas)
        center = self._get_point('center')
        radius = self._get_int('radius')
        height = self._get_int('height')
        turns = self._get_int('turns', 3)
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = center
        
        # Generate helix points
        points = []
        num_points = turns * 30  # Points per turn
        
        for i in range(num_points):
            angle = 2 * math.pi * turns * i / num_points
            z_progress = i / num_points  # Progress along height
            
            # 3D to 2D projection (simple orthographic)
            px = x + radius * math.cos(angle)
            py = y - height//2 + height * z_progress
            points.append((px, py))
        
        # Draw helix as connected line segments
        for i in range(len(points) - 1):
            draw.line([points[i], points[i + 1]], fill=fill_color, width=border_width)
        
        return canvas


class SineWavePattern(BaseShape):
    """Sine wave pattern shape."""
    
    def validate(self) -> None:
        """Validate sine wave pattern data."""
        self._get_point('start')
        self._get_int('width', min_val=1)
        self._get_int('amplitude', min_val=1)
        self._get_int('frequency', 1, min_val=1)
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw sine wave pattern on canvas."""
        draw = ImageDraw.Draw(canvas)
        start = self._get_point('start')
        width = self._get_int('width')
        amplitude = self._get_int('amplitude')
        frequency = self._get_int('frequency', 1)
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        
        x, y = start
        
        # Generate sine wave points
        points = []
        num_points = width  # One point per pixel width
        
        for i in range(num_points + 1):
            progress = i / num_points
            wave_x = x + width * progress
            wave_y = y + amplitude * math.sin(2 * math.pi * frequency * progress)
            points.append((wave_x, wave_y))
        
        # Draw sine wave as connected line segments
        for i in range(len(points) - 1):
            draw.line([points[i], points[i + 1]], fill=fill_color, width=border_width)
        
        return canvas


class FractalTree(BaseShape):
    """Fractal tree shape."""
    
    def validate(self) -> None:
        """Validate fractal tree data."""
        self._get_point('base')
        self._get_int('height', min_val=1)
        self._get_int('levels', 4, min_val=1)
        self._get_int('angle', 45, min_val=1)
        self._get_color('fill_color')
        self._get_int('border_width', min_val=1)
    
    def draw(self, canvas: Image.Image) -> Image.Image:
        """Draw fractal tree on canvas."""
        draw = ImageDraw.Draw(canvas)
        base = self._get_point('base')
        height = self._get_int('height')
        levels = self._get_int('levels', 4)
        angle = self._get_int('angle', 45)
        fill_color = self._get_color('fill_color')
        border_width = self._get_int('border_width', 1)
        
        def draw_branch(start_point, direction_angle, length, level):
            """Recursively draw fractal tree branches."""
            if level <= 0:
                return
            
            # Calculate end point
            end_x = start_point[0] + length * math.cos(math.radians(direction_angle))
            end_y = start_point[1] - length * math.sin(math.radians(direction_angle))
            end_point = (end_x, end_y)
            
            # Draw branch
            draw.line([start_point, end_point], fill=fill_color, width=max(1, border_width - level + 1))
            
            # Recursively draw sub-branches
            if level > 1:
                new_length = length * 0.7  # Reduce length for sub-branches
                draw_branch(end_point, direction_angle + angle, new_length, level - 1)
                draw_branch(end_point, direction_angle - angle, new_length, level - 1)
        
        # Start drawing from base, going upward (90 degrees)
        draw_branch(base, 90, height, levels)
        
        return canvas


class ShapeFactory:
    """Factory class for creating shape instances."""
    
    _shape_registry: Dict[ShapeType, type] = {
        # Existing shapes
        ShapeType.STRAIGHT_LINE: StraightLine,
        ShapeType.DASHED_LINE: DashedLine,
        ShapeType.RECTANGLE: Rectangle,
        ShapeType.CIRCLE: Circle,
        ShapeType.HEART: Heart,
        ShapeType.STAR: Star,
        ShapeType.ELLIPSE: Ellipse,
        ShapeType.DIAMOND: Diamond,
        ShapeType.SQUARE: Square,
        ShapeType.CLOUD: Cloud,
        ShapeType.ZIGZAG_LINE: ZigzagLine,
        ShapeType.WAVY_LINE: WavyLine,
        ShapeType.LINE_WITH_ARROWHEAD: LineWithArrowhead,
        ShapeType.LINE_WITH_DOUBLE_ARROWHEAD: LineWithDoubleArrowhead,
        ShapeType.ELBOW_CONNECTOR: ElbowConnector,
        ShapeType.ELBOW_CONNECTOR_WITH_ARROWHEAD: ElbowConnectorWithArrowhead,
        ShapeType.ELBOW_CONNECTOR_WITH_DOUBLE_ARROWHEAD: ElbowConnectorWithDoubleArrowhead,
        ShapeType.REGULAR_POLYGON: RegularPolygon,
        ShapeType.POLYGON_WITH_COORDINATES: PolygonWithCoordinates,
        ShapeType.SPEECH_BUBBLE_RECTANGLE: SpeechBubbleRectangle,
        
        # Additional geometric shapes
        ShapeType.TRIANGLE: Triangle,
        ShapeType.PENTAGON: Pentagon,
        ShapeType.HEXAGON: Hexagon,
        ShapeType.OCTAGON: Octagon,
        ShapeType.RHOMBUS: Rhombus,
        ShapeType.PARALLELOGRAM: Parallelogram,
        ShapeType.TRAPEZOID: Trapezoid,
        
        # Arrow shapes
        ShapeType.BLOCK_ARROW: BlockArrow,
        ShapeType.CURVED_ARROW: CurvedArrow,
        ShapeType.CIRCULAR_ARROW: CircularArrow,
        
        # Text-related shapes
        ShapeType.CALLOUT_BUBBLE: CalloutBubble,
        ShapeType.THOUGHT_BUBBLE: ThoughtBubble,
        ShapeType.BANNER_RIBBON: BannerRibbon,
        
        # More decorative shapes
        ShapeType.FLOWER: Flower,
        ShapeType.BUTTERFLY: Butterfly,
        ShapeType.TREE: Tree,
        ShapeType.SUN: Sun,
        ShapeType.MOON: Moon,
        ShapeType.LIGHTNING_BOLT: LightningBolt,
        
        # Technical/flowchart shapes
        ShapeType.OVAL_CALLOUT: OvalCallout,
        ShapeType.CROSS: Cross,
        ShapeType.PLUS_SIGN: PlusSign,
        ShapeType.MINUS_SIGN: MinusSign,
        ShapeType.MULTIPLICATION_SIGN: MultiplicationSign,
        
        # Advanced geometric shapes
        ShapeType.SPIRAL: Spiral,
        ShapeType.HELIX: Helix,
        ShapeType.SINE_WAVE_PATTERN: SineWavePattern,
        ShapeType.FRACTAL_TREE: FractalTree,
        
        # All shapes implemented!
    }
    
    @classmethod
    def create_shape(cls, shape_data: Dict[str, Any]) -> BaseShape:
        """Create a shape instance from data."""
        if 'type' not in shape_data:
            raise InvalidShapeError("Shape data must contain 'type' field")
        
        shape_type_str = shape_data['type']
        
        try:
            shape_type = ShapeType(shape_type_str)
        except ValueError:
            raise InvalidShapeError(f"Unknown shape type: {shape_type_str}")
        
        if shape_type not in cls._shape_registry:
            raise InvalidShapeError(f"Shape type {shape_type_str} is not implemented yet")
        
        shape_class = cls._shape_registry[shape_type]
        
        try:
            return shape_class(shape_data)
        except Exception as e:
            raise DrawingError(f"Failed to create {shape_type_str}: {e}")
    
    @classmethod
    def register_shape(cls, shape_type: ShapeType, shape_class: type) -> None:
        """Register a new shape type."""
        if not issubclass(shape_class, BaseShape):
            raise InvalidShapeError("Shape class must inherit from BaseShape")
        cls._shape_registry[shape_type] = shape_class
    
    @classmethod
    def get_supported_shapes(cls) -> List[str]:
        """Get list of supported shape types."""
        return [shape_type.value for shape_type in cls._shape_registry.keys()]