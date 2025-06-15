# ShapeCanvas 🎨

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A powerful and intuitive Python library for creating stunning 2D graphics and visualizations. Draw geometric shapes, decorative elements, and complex diagrams with ease using JSON-based configuration or programmatic API.

## ✨ Features

- **🎯 Simple API**: Easy-to-use interface for both beginners and advanced users
- **📋 JSON Configuration**: Define your graphics using simple JSON configuration files
- **🔧 Programmatic Control**: Full programmatic control with method chaining support
- **🎨 Rich Shape Library**: Comprehensive collection of shapes including:
  - Basic shapes (rectangles, circles, ellipses, squares)
  - Lines (straight, dashed, zigzag, wavy, arrows)
  - Polygons (regular polygons, custom coordinate polygons)
  - Decorative elements (hearts, stars, clouds, diamonds)
  - Connectors (elbow connectors with arrows)
  - Speech bubbles
- **🖼️ Canvas Management**: Flexible canvas with grid support and coordinate system
- **🎨 Styling Options**: Rich styling with colors, borders, fills, and gradients
- **💾 Multiple Formats**: Export to PNG, JPEG, BMP, TIFF
- **🔍 Validation**: Comprehensive input validation and error handling
- **🧪 Well Tested**: Extensive test suite with high code coverage
- **📚 Documentation**: Comprehensive documentation with examples

## 🚀 Quick Start

### Installation

```bash
pip install shape-canvas
```

### Basic Usage

#### Method 1: Using JSON Configuration

Create a configuration file `my_shapes.json`:

```json
{
  "canvas_size": [800, 600],
  "background_color": [255, 255, 255],
  "line_interval": 50,
  "line_color": "lightgray",
  "show_grid": true,
  "shapes": [
    {
      "type": "rectangle",
      "start": [100, 100],
      "end": [300, 200],
      "fill_color": [255, 0, 0],
      "outline_color": [0, 0, 0],
      "border_width": 3
    },
    {
      "type": "circle",
      "center": [500, 300],
      "radius": 75,
      "fill_color": [0, 255, 0],
      "outline_color": [0, 0, 0],
      "border_width": 2
    }
  ]
}
```

```python
from shape_canvas import Canvas

# Create canvas from configuration file
canvas = Canvas.from_file("my_shapes.json")

# Render and save
canvas.add_grid().load_shapes_from_config().render().save("output.png")
```

#### Method 2: Programmatic API

```python
from shape_canvas import Canvas

# Create a blank canvas
canvas = Canvas.create_blank(800, 600, background_color=(240, 248, 255))

# Add shapes programmatically
canvas.add_shape({
    "type": "star",
    "center": [400, 300],
    "size": 100,
    "fill_color": [255, 215, 0],
    "outline_color": [255, 140, 0],
    "border_width": 3,
    "num_points": 5
})

# Method chaining support
canvas.render().save("star.png").show()
```

#### Method 3: Command Line Interface

```bash
# Render from configuration file
shape-canvas my_shapes.json -o output.png --show

# With custom options
shape-canvas config.json -o result.png -f PNG --no-grid --verbose
```

## 📖 Documentation

### Supported Shapes

#### Basic Shapes

| Shape | Description | Required Parameters |
|-------|-------------|-------------------|
| `rectangle` | Rectangle with fill and border | `start`, `end`, `fill_color`, `outline_color`, `border_width` |
| `square` | Square shape | `start`, `size`, `fill_color`, `outline_color`, `border_width` |
| `circle` | Circle with center and radius | `center`, `radius`, `fill_color`, `outline_color`, `border_width` |
| `ellipse` | Ellipse shape | `start`, `end`, `fill_color`, `outline_color`, `border_width` |

#### Lines and Connectors

| Shape | Description | Required Parameters |
|-------|-------------|-------------------|
| `straight_line` | Simple straight line | `start`, `end`, `fill_color`, `border_width` |
| `dashed_line` | Dashed line pattern | `start`, `end`, `fill_color`, `border_width`, `dash_length` |
| `zigzag_line` | Zigzag pattern line | `start`, `end`, `fill_color`, `border_width`, `amplitude`, `frequency` |
| `wavy_line` | Wavy pattern line | `start`, `end`, `fill_color`, `border_width`, `amplitude`, `frequency` |
| `line_with_arrowhead` | Line with arrow at end | `start`, `end`, `fill_color`, `outline_color`, `border_width` |
| `line_with_double_arrowhead` | Line with arrows at both ends | `start`, `end`, `fill_color`, `outline_color`, `border_width` |

#### Polygons

| Shape | Description | Required Parameters |
|-------|-------------|-------------------|
| `polygon_with_coordinates` | Custom polygon from coordinates | `coordinates`, `fill_color`, `outline_color`, `border_width` |
| `regular_polygon` | Regular polygon (triangle, hexagon, etc.) | `center`, `n_sides`, `radius`, `fill_color`, `outline_color`, `border_width` |

#### Decorative Shapes

| Shape | Description | Required Parameters |
|-------|-------------|-------------------|
| `heart` | Heart shape with rotation | `center`, `size`, `fill_color`, `outline_color`, `border_width`, `rotation_angle` |
| `star` | Multi-pointed star | `center`, `size`, `num_points`, `fill_color`, `outline_color`, `border_width` |
| `diamond` | Diamond/rhombus shape | `center`, `size`, `fill_color`, `outline_color`, `border_width` |
| `cloud` | Cloud shape from circles | `center`, `size`, `num_circles`, `fill_color`, `outline_color`, `border_width` |

### Configuration Schema

#### Canvas Configuration

```json
{
  "canvas_size": [width, height],           // Canvas dimensions
  "background_color": [r, g, b],           // RGB background color
  "line_interval": 50,                     // Grid line spacing (optional)
  "line_color": "gray",                    // Grid line color (optional)
  "show_grid": true,                       // Show grid lines (optional)
  "shapes": [...]                          // Array of shape definitions
}
```

#### Common Shape Properties

```json
{
  "type": "shape_name",                    // Shape type
  "fill_color": [r, g, b],                // Fill color (RGB)
  "outline_color": [r, g, b],             // Border color (RGB)
  "border_width": 2,                      // Border thickness
  // Shape-specific properties...
}
```

### API Reference

#### Canvas Class

```python
class Canvas:
    def __init__(self, config: Union[CanvasConfig, Dict, str, Path])
    
    # Factory methods
    @classmethod
    def from_file(cls, config_file: Union[str, Path]) -> 'Canvas'
    @classmethod
    def create_blank(cls, width: int, height: int, background_color: Tuple[int, int, int]) -> 'Canvas'
    
    # Shape management
    def add_shape(self, shape_data: Dict[str, Any]) -> 'Canvas'
    def add_shapes(self, shapes_data: List[Dict[str, Any]]) -> 'Canvas'
    def load_shapes_from_config(self) -> 'Canvas'
    
    # Rendering
    def add_grid(self) -> 'Canvas'
    def render(self) -> 'Canvas'
    def clear(self) -> 'Canvas'
    
    # Output
    def save(self, filename: Union[str, Path], format: Optional[str] = None) -> 'Canvas'
    def show(self) -> 'Canvas'
    def get_image(self) -> Image.Image
    
    # Information
    def get_canvas_info(self) -> Dict[str, Any]
```

## 🎯 Examples

### Example 1: Geometric Patterns

```python
from shape_canvas import Canvas

canvas = Canvas.create_blank(600, 600, (240, 240, 240))

# Create a pattern of circles
for i in range(3):
    for j in range(3):
        canvas.add_shape({
            "type": "circle",
            "center": [150 + i*150, 150 + j*150],
            "radius": 50,
            "fill_color": [255-i*50, 100+j*50, 150],
            "outline_color": [0, 0, 0],
            "border_width": 2
        })

canvas.render().save("pattern.png")
```

### Example 2: Flowchart Elements

```python
from shape_canvas import Canvas

canvas = Canvas.create_blank(800, 400)

# Add flowchart elements
shapes = [
    # Start node
    {
        "type": "ellipse",
        "start": [50, 150],
        "end": [150, 250],
        "fill_color": [144, 238, 144],
        "outline_color": [0, 100, 0],
        "border_width": 2
    },
    # Process node
    {
        "type": "rectangle",
        "start": [200, 150],
        "end": [350, 250],
        "fill_color": [173, 216, 230],
        "outline_color": [0, 0, 139],
        "border_width": 2
    },
    # Decision node
    {
        "type": "diamond",
        "center": [500, 200],
        "size": 60,
        "fill_color": [255, 255, 0],
        "outline_color": [255, 140, 0],
        "border_width": 2
    },
    # Connecting arrows
    {
        "type": "line_with_arrowhead",
        "start": [150, 200],
        "end": [200, 200],
        "fill_color": [0, 0, 0],
        "outline_color": [0, 0, 0],
        "border_width": 2
    }
]

canvas.add_shapes(shapes).render().save("flowchart.png")
```

### Example 3: Decorative Art

```python
from shape_canvas import Canvas
import math

canvas = Canvas.create_blank(600, 600, (25, 25, 112))  # Dark blue background

# Create a mandala-like pattern
center = (300, 300)
colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (255, 0, 255)]

for i in range(5):
    angle = i * 72  # 360/5 = 72 degrees apart
    x = center[0] + 150 * math.cos(math.radians(angle))
    y = center[1] + 150 * math.sin(math.radians(angle))
    
    canvas.add_shape({
        "type": "star",
        "center": [int(x), int(y)],
        "size": 40,
        "num_points": 6,
        "fill_color": colors[i],
        "outline_color": [255, 255, 255],
        "border_width": 2
    })

# Center star
canvas.add_shape({
    "type": "star",
    "center": center,
    "size": 60,
    "num_points": 8,
    "fill_color": [255, 215, 0],
    "outline_color": [255, 255, 255],
    "border_width": 3
})

canvas.render().save("mandala.png")
```

## 🧪 Testing

Run the test suite:

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=shape_canvas --cov-report=html
```

## 🛠️ Development

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/KDASARADHA525/Shapes-python-pillow-canvas.git
cd Shapes-python-pillow-canvas

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run pre-commit hooks
pre-commit install
```

### Code Quality

```bash
# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Type checking
mypy src/
```

## 📋 Roadmap

- [ ] **Enhanced Shapes**: Add more decorative shapes (arrows, callouts, etc.)
- [ ] **Gradients**: Support for linear and radial gradients
- [ ] **Text Rendering**: Add text shapes with font support
- [ ] **Layers**: Layer management for complex compositions
- [ ] **Animation**: Support for animated GIFs
- [ ] **SVG Export**: Export to SVG format
- [ ] **Performance**: Optimize rendering for large canvases
- [ ] **Plugins**: Plugin system for custom shapes

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Pillow (PIL Fork)](https://pillow.readthedocs.io/) for image processing
- Inspired by various graphics libraries and drawing tools
- Thanks to all contributors and users of this library

## 📞 Support

- **Documentation**: [GitHub Wiki](https://github.com/KDASARADHA525/Shapes-python-pillow-canvas/wiki)
- **Issues**: [GitHub Issues](https://github.com/KDASARADHA525/Shapes-python-pillow-canvas/issues)
- **Discussions**: [GitHub Discussions](https://github.com/KDASARADHA525/Shapes-python-pillow-canvas/discussions)

---

<div align="center">

**[⭐ Star this repo](https://github.com/KDASARADHA525/Shapes-python-pillow-canvas)** if you find it useful!

Made with ❤️ by [K. Dasaradha](https://github.com/KDASARADHA525)

</div>
