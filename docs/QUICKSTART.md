# 🚀 ShapeCanvas Quick Start Guide

<div align="center">

**Get up and running with ShapeCanvas in under 5 minutes!**

[![Install](https://img.shields.io/badge/1️⃣-Install-blue?style=for-the-badge)](#-step-1-installation)
[![Configure](https://img.shields.io/badge/2️⃣-Configure-green?style=for-the-badge)](#-step-2-create-your-first-shape)
[![Run](https://img.shields.io/badge/3️⃣-Run-orange?style=for-the-badge)](#-step-3-run-the-application)
[![Advanced](https://img.shields.io/badge/4️⃣-Advanced-purple?style=for-the-badge)](#-step-4-advanced-usage)

</div>

---

## 🎯 **Complete Step-by-Step Tutorial**

### 📦 **Step 1: Installation**

Choose your preferred installation method:

<details>
<summary><b>🌟 Method A: Quick Install (Recommended)</b></summary>

```bash
# Navigate to the project directory
cd "c:/Users/K_Dasaradh/Desktop/tardigrade/kdsr_repos/Shapes-python-pillow-canvas"

# Install the package
pip install -e .
```

**✅ Verification:**
```bash
shape-canvas --version
```
*Expected output:* `ShapeCanvas 1.0.0`

</details>

<details>
<summary><b>🔧 Method B: Development Install</b></summary>

```bash
# Clone and navigate
cd "c:/Users/K_Dasaradh/Desktop/tardigrade/kdsr_repos/Shapes-python-pillow-canvas"

# Install with development dependencies
pip install -e ".[dev]"

# Verify installation
python -c "from shape_canvas import Canvas; print('✅ Installation successful!')"
```

</details>

<details>
<summary><b>🐍 Method C: Python Only</b></summary>

```bash
# Just install required dependencies
pip install Pillow>=10.0.0

# Add the src directory to Python path
cd "c:/Users/K_Dasaradh/Desktop/tardigrade/kdsr_repos/Shapes-python-pillow-canvas"
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"  # Linux/Mac
# OR
set PYTHONPATH=%PYTHONPATH%;%cd%\src  # Windows
```

</details>

---

### 🎨 **Step 2: Create Your First Shape**

#### **Option A: Use Existing Configuration (Easiest)**

Your original configuration file should already exist. Let's use it:

```bash
# Check if your original config exists
ls lines_canvas_coordinates_json_data_input_json.json

# If it exists, run it with the new system
shape-canvas lines_canvas_coordinates_json_data_input_json.json -o my_first_output.png --show
```

#### **Option B: Create a Simple Configuration**

Create a new file `my_shapes.json`:

```json
{
  "canvas_size": [800, 600],
  "background_color": [245, 245, 245],
  "line_interval": 50,
  "line_color": "lightgray",
  "show_grid": true,
  "shapes": [
    {
      "type": "circle",
      "center": [200, 200],
      "radius": 75,
      "fill_color": [255, 100, 100],
      "outline_color": [200, 50, 50],
      "border_width": 3
    },
    {
      "type": "rectangle",
      "start": [400, 150],
      "end": [600, 250],
      "fill_color": [100, 255, 100],
      "outline_color": [50, 200, 50],
      "border_width": 2
    },
    {
      "type": "star",
      "center": [400, 400],
      "size": 60,
      "num_points": 5,
      "fill_color": [255, 215, 0],
      "outline_color": [184, 134, 11],
      "border_width": 2
    }
  ]
}
```

#### **Option C: Use Pre-made Examples**

```bash
# Use the included example
shape-canvas examples/basic_shapes.json -o example_output.png --show
```

---

### ⚡ **Step 3: Run the Application**

#### **🎯 Method 1: Command Line Interface (Recommended)**

<table>
<tr>
<td width="60%">

**Basic Usage:**
```bash
# Simple render
shape-canvas my_shapes.json

# Custom output name
shape-canvas my_shapes.json -o my_artwork.png

# Show result immediately
shape-canvas my_shapes.json -o result.png --show

# Different format
shape-canvas my_shapes.json -o result.jpg -f JPEG

# Disable grid
shape-canvas my_shapes.json --no-grid

# Verbose output
shape-canvas my_shapes.json -v
```

</td>
<td width="40%">

**🎨 Result:**
- Creates beautiful graphics
- Shows progress in terminal
- Opens image automatically (with --show)
- Saves in your preferred format

**💡 Pro Tips:**
- Use `-v` for debugging
- Use `--show` to preview immediately
- Support for PNG, JPEG, BMP, TIFF

</td>
</tr>
</table>

#### **🐍 Method 2: Python Script**

Create `my_script.py`:

```python
#!/usr/bin/env python3
from shape_canvas import Canvas

# Method 1: From configuration file
canvas = Canvas.from_file("my_shapes.json")
canvas.add_grid().load_shapes_from_config().render().save("output.png")
print("✅ Created from config file!")

# Method 2: Programmatic creation
canvas = Canvas.create_blank(600, 400, (240, 248, 255))

# Add a beautiful heart
canvas.add_shape({
    "type": "heart",
    "center": [300, 200],
    "size": 3,
    "fill_color": [255, 20, 147],
    "outline_color": [139, 0, 69],
    "border_width": 3,
    "rotation_angle": 0
})

# Render and save
canvas.render().save("heart.png")
print("✅ Created programmatically!")

# Method 3: Method chaining (Advanced)
(Canvas.create_blank(400, 300)
    .add_shape({"type": "star", "center": [200, 150], "size": 50, "num_points": 6, "fill_color": [255, 215, 0]})
    .render()
    .save("star.png")
    .show())  # This will display the result
print("✅ Created with method chaining!")
```

Run it:
```bash
python my_script.py
```

#### **🎮 Method 3: Interactive Python**

```python
# Start Python interpreter
python

# Interactive session
>>> from shape_canvas import Canvas
>>> canvas = Canvas.create_blank(400, 300)
>>> canvas.add_shape({"type": "circle", "center": [200, 150], "radius": 50, "fill_color": [255, 0, 0]})
>>> canvas.render().save("interactive.png")
>>> canvas.show()  # Display the result
>>> exit()
```

---

### 🔥 **Step 4: Advanced Usage**

#### **🎨 Batch Processing**

Create multiple images at once:

```bash
# Process all JSON files in a directory
for config in *.json; do
    shape-canvas "$config" -o "${config%.json}.png"
done

# Or using PowerShell (Windows)
Get-ChildItem *.json | ForEach-Object { shape-canvas $_.Name -o ($_.BaseName + ".png") }
```

#### **🚀 Advanced Python Usage**

<details>
<summary><b>🎯 Dynamic Shape Generation</b></summary>

```python
from shape_canvas import Canvas
import random
import math

# Create a dynamic art piece
canvas = Canvas.create_blank(800, 600, (20, 20, 40))

# Generate random circles
for i in range(50):
    canvas.add_shape({
        "type": "circle",
        "center": [random.randint(50, 750), random.randint(50, 550)],
        "radius": random.randint(10, 30),
        "fill_color": [
            random.randint(100, 255),
            random.randint(100, 255), 
            random.randint(100, 255)
        ],
        "outline_color": [255, 255, 255],
        "border_width": 1
    })

canvas.render().save("random_art.png")
print("🎨 Created dynamic art!")
```

</details>

<details>
<summary><b>📊 Data Visualization</b></summary>

```python
from shape_canvas import Canvas

# Sample data
sales_data = [30, 45, 60, 35, 80, 55, 70]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']

canvas = Canvas.create_blank(800, 500, (245, 245, 245))

# Create bar chart
for i, value in enumerate(sales_data):
    height = value * 4  # Scale factor
    canvas.add_shape({
        "type": "rectangle",
        "start": [100 + i*90, 400 - height],
        "end": [170 + i*90, 400],
        "fill_color": [100, 150, 255],
        "outline_color": [50, 100, 200],
        "border_width": 2
    })

canvas.render().save("sales_chart.png")
print("📊 Created data visualization!")
```

</details>

<details>
<summary><b>🎮 Game Asset Creation</b></summary>

```python
from shape_canvas import Canvas

def create_game_character():
    canvas = Canvas.create_blank(200, 200, (100, 100, 100))
    
    # Character parts
    shapes = [
        # Head
        {"type": "circle", "center": [100, 60], "radius": 25, 
         "fill_color": [255, 220, 177], "outline_color": [0, 0, 0], "border_width": 2},
        
        # Body
        {"type": "rectangle", "start": [80, 85], "end": [120, 140], 
         "fill_color": [100, 100, 255], "outline_color": [0, 0, 0], "border_width": 2},
        
        # Eyes
        {"type": "circle", "center": [92, 55], "radius": 3, 
         "fill_color": [0, 0, 0], "outline_color": [0, 0, 0], "border_width": 1},
        {"type": "circle", "center": [108, 55], "radius": 3, 
         "fill_color": [0, 0, 0], "outline_color": [0, 0, 0], "border_width": 1},
    ]
    
    canvas.add_shapes(shapes).render().save("game_character.png")
    return canvas

# Create multiple characters
for i in range(3):
    char = create_game_character()
    print(f"🎮 Created game character {i+1}!")
```

</details>

---

## 🎯 **Common Use Cases**

<table>
<tr>
<td width="33%">

### **📊 Data Visualization**
```bash
# Create charts from data
shape-canvas data_chart.json -o chart.png

# Batch process reports
for data in reports/*.json; do
    shape-canvas "$data" -o "charts/$(basename $data .json).png"
done
```

**Perfect for:**
- Sales reports
- Analytics dashboards  
- Scientific data
- Business presentations

</td>
<td width="33%">

### **🎨 Creative Design**
```python
# Logo creation
canvas = Canvas.create_blank(400, 400)
canvas.add_shape({
    "type": "star",
    "center": [200, 200],
    "size": 80,
    "num_points": 5,
    "fill_color": [255, 215, 0]
})
canvas.render().save("logo.png")
```

**Perfect for:**
- Logo design
- Icon creation
- Art projects
- Social media graphics

</td>
<td width="33%">

### **📚 Educational Content**
```json
{
  "canvas_size": [600, 400],
  "shapes": [{
    "type": "circle",
    "center": [300, 200],
    "radius": 100,
    "fill_color": [200, 200, 255]
  }]
}
```

**Perfect for:**
- Geometry lessons
- Math visualizations
- Diagrams
- Educational materials

</td>
</tr>
</table>

---

## 🔧 **Troubleshooting**

<details>
<summary><b>❌ Common Issues & Solutions</b></summary>

### **Issue: "ModuleNotFoundError: No module named 'shape_canvas'"**

**Solutions:**
```bash
# Option 1: Install the package
pip install -e .

# Option 2: Add to Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"

# Option 3: Check you're in the right directory
cd "c:/Users/K_Dasaradh/Desktop/tardigrade/kdsr_repos/Shapes-python-pillow-canvas"
```

### **Issue: "Shape type X is not implemented yet"**

**Solutions:**
```bash
# Check supported shapes
python -c "from shape_canvas.shapes import ShapeFactory; print(ShapeFactory.get_supported_shapes())"

# Use supported shapes only:
# ✅ straight_line, dashed_line, rectangle, circle, heart, star
# ⏳ Coming soon: ellipse, diamond, cloud, polygons, etc.
```

### **Issue: "File not found" errors**

**Solutions:**
```bash
# Check file exists
ls my_shapes.json

# Use absolute path
shape-canvas "C:/full/path/to/config.json" -o output.png

# Check current directory
pwd
```

### **Issue: "Permission denied" when saving**

**Solutions:**
```bash
# Check write permissions
ls -la output_directory/

# Save to a different location
shape-canvas config.json -o ~/Desktop/output.png

# Run with appropriate permissions
sudo shape-canvas config.json -o /path/to/output.png  # Linux/Mac
```

</details>

<details>
<summary><b>🐛 Debug Mode</b></summary>

Enable verbose logging to see what's happening:

```bash
# CLI with verbose output
shape-canvas config.json -v -o output.png

# Python with logging
import logging
logging.basicConfig(level=logging.DEBUG)

from shape_canvas import Canvas
canvas = Canvas.from_file("config.json")
canvas.render().save("output.png")
```

This will show:
- Configuration loading details
- Shape creation progress  
- Rendering information
- File saving status

</details>

---

## ✅ **Verification Checklist**

Before you finish, make sure everything works:

- [ ] **Installation successful**: `shape-canvas --version` works
- [ ] **Basic functionality**: Can create a simple shape
- [ ] **File operations**: Can save and load configurations
- [ ] **CLI works**: Command-line interface responds
- [ ] **Python API works**: Can import and use the package
- [ ] **Examples run**: `python examples/demo.py` completes successfully

---

## 🎉 **Success! You're Ready to Create**

<div align="center">

### **🚀 You now have a powerful graphics creation tool!**

**Try these next:**
- Explore the [examples](examples/) directory
- Create your own shape configurations
- Build data visualizations
- Design logos and graphics
- Contribute new features

**Need help?**
- 📖 [Full Documentation](README.md)
- 💬 [Community Discussions](https://github.com/KDASARADHA525/Shapes-python-pillow-canvas/discussions)
- 🐛 [Report Issues](https://github.com/KDASARADHA525/Shapes-python-pillow-canvas/issues)

</div>

---

<div align="center">

**Happy creating with ShapeCanvas! 🎨**

*Made with ❤️ by [K. Dasaradha](https://github.com/KDASARADHA525)*

</div>