# New Shapes Documentation

This document describes all the new shapes that have been added to the Shapes Python Pillow Canvas application.

## Overview

We've added **31 new shapes** across 6 categories:
- **Additional Geometric Shapes** (7 shapes)
- **Arrow Shapes** (3 shapes)
- **Text-Related Shapes** (3 shapes)
- **Decorative Shapes** (6 shapes)
- **Technical/Flowchart Shapes** (5 shapes)
- **Advanced Geometric Shapes** (4 shapes)

## Additional Geometric Shapes

### Triangle
Simple triangle shape defined by three points.
```json
{
  "type": "triangle",
  "point1": [50, 50],
  "point2": [100, 50],
  "point3": [75, 100],
  "fill_color": [255, 100, 100],
  "outline_color": [200, 50, 50],
  "border_width": 2
}
```

### Pentagon
Regular pentagon shape.
```json
{
  "type": "pentagon",
  "center": [200, 75],
  "radius": 30,
  "rotation": 0,
  "fill_color": [100, 255, 100],
  "outline_color": [50, 200, 50],
  "border_width": 2
}
```

### Hexagon
Regular hexagon shape.
```json
{
  "type": "hexagon",
  "center": [300, 75],
  "radius": 30,
  "rotation": 0,
  "fill_color": [100, 100, 255],
  "outline_color": [50, 50, 200],
  "border_width": 2
}
```

### Octagon
Regular octagon shape.
```json
{
  "type": "octagon",
  "center": [400, 75],
  "radius": 30,
  "rotation": 0,
  "fill_color": [255, 255, 100],
  "outline_color": [200, 200, 50],
  "border_width": 2
}
```

### Rhombus
Diamond-like shape with configurable width and height.
```json
{
  "type": "rhombus",
  "center": [500, 75],
  "width": 60,
  "height": 40,
  "rotation": 45,
  "fill_color": [255, 100, 255],
  "outline_color": [200, 50, 200],
  "border_width": 2
}
```

### Parallelogram
Four-sided shape with parallel opposite sides.
```json
{
  "type": "parallelogram",
  "start": [550, 50],
  "width": 60,
  "height": 40,
  "skew": 15,
  "fill_color": [100, 255, 255],
  "outline_color": [50, 200, 200],
  "border_width": 2
}
```

### Trapezoid
Four-sided shape with one pair of parallel sides.
```json
{
  "type": "trapezoid",
  "start": [650, 50],
  "bottom_width": 60,
  "top_width": 40,
  "height": 40,
  "fill_color": [255, 200, 100],
  "outline_color": [200, 150, 50],
  "border_width": 2
}
```

## Arrow Shapes

### Block Arrow
Solid arrow shape with configurable shaft and head dimensions.
```json
{
  "type": "block_arrow",
  "start": [50, 150],
  "end": [150, 150],
  "shaft_width": 20,
  "head_width": 40,
  "fill_color": [255, 0, 0],
  "outline_color": [150, 0, 0],
  "border_width": 2
}
```

### Curved Arrow
Arrow that follows a curved path.
```json
{
  "type": "curved_arrow",
  "start": [200, 150],
  "end": [300, 150],
  "curve_height": 30,
  "arrow_size": 15,
  "fill_color": [0, 255, 0],
  "border_width": 3
}
```

### Circular Arrow
Arrow that follows a circular arc.
```json
{
  "type": "circular_arrow",
  "center": [400, 150],
  "radius": 40,
  "start_angle": 0,
  "end_angle": 270,
  "arrow_size": 12,
  "fill_color": [0, 0, 255],
  "border_width": 3
}
```

## Text-Related Shapes

### Callout Bubble
Speech bubble with a pointer to a specific location.
```json
{
  "type": "callout_bubble",
  "center": [600, 150],
  "width": 80,
  "height": 50,
  "pointer_tip": [650, 200],
  "fill_color": [255, 255, 200],
  "outline_color": [200, 200, 100],
  "border_width": 2
}
```

### Thought Bubble
Cloud-like bubble with small circles leading to a point.
```json
{
  "type": "thought_bubble",
  "center": [750, 150],
  "width": 80,
  "height": 50,
  "pointer_direction": [800, 200],
  "fill_color": [200, 255, 255],
  "outline_color": [100, 200, 200],
  "border_width": 2
}
```

### Banner Ribbon
Ribbon-like shape with a decorative tail.
```json
{
  "type": "banner_ribbon",
  "start": [900, 125],
  "width": 100,
  "height": 50,
  "tail_length": 20,
  "fill_color": [255, 200, 200],
  "outline_color": [200, 100, 100],
  "border_width": 2
}
```

## Decorative Shapes

### Flower
Multi-petal flower with configurable number of petals.
```json
{
  "type": "flower",
  "center": [100, 300],
  "petal_size": 30,
  "num_petals": 6,
  "fill_color": [255, 150, 200],
  "outline_color": [200, 100, 150],
  "center_color": [255, 255, 0],
  "border_width": 2
}
```

### Butterfly
Butterfly shape with upper and lower wings.
```json
{
  "type": "butterfly",
  "center": [250, 300],
  "wing_size": 40,
  "fill_color": [255, 200, 0],
  "outline_color": [200, 150, 0],
  "body_color": [100, 50, 0],
  "border_width": 2
}
```

### Tree
Tree shape with trunk and crown.
```json
{
  "type": "tree",
  "base": [400, 350],
  "height": 80,
  "crown_width": 60,
  "trunk_color": [139, 69, 19],
  "crown_color": [34, 139, 34],
  "outline_color": [0, 100, 0],
  "border_width": 2
}
```

### Sun
Sun shape with rays extending outward.
```json
{
  "type": "sun",
  "center": [550, 300],
  "radius": 30,
  "num_rays": 12,
  "ray_length": 20,
  "fill_color": [255, 255, 0],
  "outline_color": [255, 200, 0],
  "border_width": 2
}
```

### Moon
Moon shape with configurable phase.
```json
{
  "type": "moon",
  "center": [700, 300],
  "radius": 30,
  "phase_offset": 30,
  "fill_color": [255, 255, 224],
  "outline_color": [200, 200, 150],
  "border_width": 2
}
```

### Lightning Bolt
Lightning bolt shape with zigzag pattern.
```json
{
  "type": "lightning_bolt",
  "start": [800, 250],
  "height": 80,
  "width": 40,
  "fill_color": [255, 255, 0],
  "outline_color": [255, 200, 0],
  "border_width": 2
}
```

## Technical/Flowchart Shapes

### Oval Callout
Oval shape with a callout line to a specific point.
```json
{
  "type": "oval_callout",
  "center": [100, 450],
  "width": 80,
  "height": 50,
  "callout_point": [150, 500],
  "fill_color": [200, 255, 200],
  "outline_color": [100, 200, 100],
  "border_width": 2
}
```

### Cross
Cross shape with configurable thickness.
```json
{
  "type": "cross",
  "center": [250, 450],
  "size": 30,
  "thickness": 8,
  "fill_color": [255, 0, 0],
  "outline_color": [200, 0, 0],
  "border_width": 2
}
```

### Plus Sign
Plus sign shape.
```json
{
  "type": "plus_sign",
  "center": [350, 450],
  "size": 30,
  "thickness": 6,
  "fill_color": [0, 255, 0],
  "border_width": 3
}
```

### Minus Sign
Minus sign shape.
```json
{
  "type": "minus_sign",
  "center": [450, 450],
  "size": 30,
  "thickness": 6,
  "fill_color": [255, 100, 0],
  "border_width": 3
}
```

### Multiplication Sign
Multiplication (X) sign shape.
```json
{
  "type": "multiplication_sign",
  "center": [550, 450],
  "size": 25,
  "thickness": 5,
  "fill_color": [150, 0, 255],
  "border_width": 3
}
```

## Advanced Geometric Shapes

### Spiral
Spiral shape with configurable turns and radius.
```json
{
  "type": "spiral",
  "center": [150, 600],
  "max_radius": 50,
  "turns": 4,
  "fill_color": [255, 100, 150],
  "border_width": 3
}
```

### Helix
3D helix shape projected to 2D.
```json
{
  "type": "helix",
  "center": [300, 600],
  "radius": 30,
  "height": 100,
  "turns": 3,
  "fill_color": [100, 150, 255],
  "border_width": 3
}
```

### Sine Wave Pattern
Sine wave pattern with configurable frequency and amplitude.
```json
{
  "type": "sine_wave_pattern",
  "start": [400, 600],
  "width": 150,
  "amplitude": 30,
  "frequency": 3,
  "fill_color": [255, 150, 100],
  "border_width": 3
}
```

### Fractal Tree
Recursive tree structure with configurable levels and branching angle.
```json
{
  "type": "fractal_tree",
  "base": [700, 650],
  "height": 60,
  "levels": 5,
  "angle": 30,
  "fill_color": [100, 200, 100],
  "border_width": 2
}
```

## Usage Examples

### Basic Usage
```python
from shape_canvas.canvas import Canvas

# Create a configuration with new shapes
config = {
    "canvas_size": [800, 600],
    "background_color": [255, 255, 255],
    "shapes": [
        {
            "type": "flower",
            "center": [400, 300],
            "petal_size": 40,
            "num_petals": 8,
            "fill_color": [255, 100, 150],
            "outline_color": [200, 50, 100],
            "center_color": [255, 255, 0],
            "border_width": 2
        }
    ]
}

# Create and render canvas
canvas = Canvas(config)
result = canvas.render()
result.save("my_flower.png")
```

### Combining Shapes
You can combine multiple new shapes in a single canvas:

```python
config = {
    "canvas_size": [800, 600],
    "background_color": [255, 255, 255],
    "shapes": [
        # Sun in the sky
        {
            "type": "sun",
            "center": [150, 100],
            "radius": 40,
            "num_rays": 12,
            "ray_length": 25,
            "fill_color": [255, 255, 0],
            "outline_color": [255, 200, 0],
            "border_width": 2
        },
        # Tree on the ground
        {
            "type": "tree",
            "base": [400, 500],
            "height": 100,
            "crown_width": 80,
            "trunk_color": [139, 69, 19],
            "crown_color": [34, 139, 34],
            "outline_color": [0, 100, 0],
            "border_width": 2
        },
        # Flower near the tree
        {
            "type": "flower",
            "center": [600, 450],
            "petal_size": 30,
            "num_petals": 6,
            "fill_color": [255, 150, 200],
            "outline_color": [200, 100, 150],
            "center_color": [255, 255, 0],
            "border_width": 2
        }
    ]
}
```

## Color Validation

All shapes now include proper color validation. Color values must be integers between 0 and 255 (inclusive). Invalid color values will raise a `ValidationError`.

```python
# Valid color
"fill_color": [255, 100, 50]

# Invalid color (will raise ValidationError)
"fill_color": [256, 100, 50]  # 256 is out of range
"fill_color": [255, 100]      # Missing blue component
"fill_color": [-1, 100, 50]   # Negative value
```

## Testing

All new shapes have been thoroughly tested. You can run the test suite:

```bash
# Run all tests
python -m pytest tests/

# Run new shapes test
python test_new_shapes.py

# Generate demo image with all shapes
python -c "
from shape_canvas.canvas import Canvas
import json
with open('examples/all_new_shapes_demo.json', 'r') as f:
    config = json.load(f)
canvas = Canvas(config)
result = canvas.render()
result.save('all_shapes_demo.png')
"
```

## Shape Parameters Reference

### Common Parameters
Most shapes support these common parameters:
- `fill_color`: [R, G, B] - Fill color (integers 0-255)
- `outline_color`: [R, G, B] - Outline color (integers 0-255)
- `border_width`: integer - Width of the border/outline

### Position Parameters
- `center`: [x, y] - Center position
- `start`: [x, y] - Starting position
- `point1`, `point2`, etc.: [x, y] - Specific point coordinates

### Size Parameters
- `radius`: integer - Radius for circular shapes
- `width`, `height`: integer - Dimensions
- `size`: integer - General size parameter

### Special Parameters
- `rotation`: integer - Rotation angle in degrees
- `num_petals`, `num_rays`: integer - Number of elements
- `frequency`, `amplitude`: integer - Wave properties
- `levels`: integer - Recursion depth for fractals

## Conclusion

These 31 new shapes greatly expand the capabilities of the Shapes Python Pillow Canvas application, providing a comprehensive set of drawing primitives for creating complex diagrams, illustrations, and artistic compositions.