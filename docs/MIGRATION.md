# Migration Guide

This document explains how to migrate from the old single-file implementation to the new production-level ShapeCanvas library.

## What Changed

### Project Structure
- **Old**: Single file `lines_canvas_coordinates_json_data.py`
- **New**: Modular package structure with `src/shape_canvas/`

### Usage Patterns

#### Old Way (Single File)
```python
# lines_canvas_coordinates_json_data.py
import json
from PIL import Image, ImageDraw

# Load data from JSON file
with open('config.json', 'r') as json_file:
    data = json.load(json_file)

# Create canvas
canvas = create_blank_canvas(data)
canvas = create_canvas_with_lines(canvas, data)
canvas = draw_shapes_on_canvas(canvas, data)

# Save
canvas.save('output.png')
canvas.show()
```

#### New Way (Package)
```python
from shape_canvas import Canvas

# Method 1: From file
canvas = Canvas.from_file('config.json')
canvas.add_grid().load_shapes_from_config().render().save('output.png')

# Method 2: Programmatic
canvas = Canvas.create_blank(800, 600)
canvas.add_shape({
    "type": "rectangle",
    "start": [100, 100],
    "end": [200, 200],
    "fill_color": [255, 0, 0],
    "outline_color": [0, 0, 0],
    "border_width": 2
}).render().save('output.png')
```

## Migration Steps

### Step 1: Install New Package
```bash
pip install -e .
```

### Step 2: Update Configuration
Your existing JSON configuration files should work with minimal changes. The new system is backward compatible.

### Step 3: Update Import Statements
```python
# Old
from lines_canvas_coordinates_json_data import create_blank_canvas, draw_shapes_on_canvas

# New
from shape_canvas import Canvas
```

### Step 4: Update Function Calls
```python
# Old
with open('config.json', 'r') as f:
    data = json.load(f)
canvas = create_blank_canvas(data)
canvas = create_canvas_with_lines(canvas, data)
canvas = draw_shapes_on_canvas(canvas, data)

# New
canvas = Canvas.from_file('config.json')
canvas.add_grid().load_shapes_from_config().render()
```

## Benefits of Migration

1. **Better Error Handling**: Comprehensive exception handling with meaningful error messages
2. **Validation**: Input validation for all shape parameters
3. **Modularity**: Clean separation of concerns with dedicated classes
4. **Extensibility**: Easy to add new shape types
5. **Testing**: Comprehensive test suite ensures reliability
6. **Documentation**: Better documentation and examples
7. **CLI Support**: Command-line interface for batch processing
8. **Type Safety**: Type hints throughout the codebase

## Backward Compatibility

The new system maintains backward compatibility with your existing JSON configuration files. Most configurations should work without modification.

## Shape Type Mapping

All original shape types are supported:

| Original | New | Status |
|----------|-----|--------|
| `straight_line` | `straight_line` | ✅ Implemented |
| `dashed_line` | `dashed_line` | ✅ Implemented |
| `rectangle` | `rectangle` | ✅ Implemented |
| `circle` | `circle` | ✅ Implemented |
| `heart` | `heart` | ✅ Implemented |
| `star` | `star` | ✅ Implemented |
| `zigzag_line` | `zigzag_line` | 🚧 Planned |
| `wavy_line` | `wavy_line` | 🚧 Planned |
| `diamond` | `diamond` | 🚧 Planned |
| `cloud` | `cloud` | 🚧 Planned |

## Need Help?

If you encounter issues during migration:
1. Check the [examples](examples/) directory for working examples
2. Review the [API documentation](README.md#api-reference)
3. Open an issue on GitHub with your specific use case