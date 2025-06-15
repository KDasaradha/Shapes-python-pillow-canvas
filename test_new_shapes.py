#!/usr/bin/env python3
"""Test script for new shapes functionality."""

import json
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from shape_canvas.canvas import Canvas
from shape_canvas.shapes import ShapeFactory


def test_individual_shapes():
    """Test individual new shapes to ensure they work."""
    
    # Test geometric shapes
    geometric_shapes = [
        {
            "type": "triangle",
            "point1": [50, 50],
            "point2": [100, 50],
            "point3": [75, 100],
            "fill_color": [255, 100, 100],
            "outline_color": [200, 50, 50],
            "border_width": 2
        },
        {
            "type": "pentagon",
            "center": [200, 75],
            "radius": 30,
            "rotation": 0,
            "fill_color": [100, 255, 100],
            "outline_color": [50, 200, 50],
            "border_width": 2
        },
        {
            "type": "hexagon",
            "center": [300, 75],
            "radius": 30,
            "rotation": 0,
            "fill_color": [100, 100, 255],
            "outline_color": [50, 50, 200],
            "border_width": 2
        }
    ]
    
    # Test arrow shapes
    arrow_shapes = [
        {
            "type": "block_arrow",
            "start": [50, 150],
            "end": [150, 150],
            "shaft_width": 20,
            "head_width": 40,
            "fill_color": [255, 0, 0],
            "outline_color": [150, 0, 0],
            "border_width": 2
        },
        {
            "type": "curved_arrow",
            "start": [200, 150],
            "end": [300, 150],
            "curve_height": 30,
            "arrow_size": 15,
            "fill_color": [0, 255, 0],
            "border_width": 3
        }
    ]
    
    # Test decorative shapes
    decorative_shapes = [
        {
            "type": "flower",
            "center": [100, 300],
            "petal_size": 30,
            "num_petals": 6,
            "fill_color": [255, 150, 200],
            "outline_color": [200, 100, 150],
            "center_color": [255, 255, 0],
            "border_width": 2
        },
        {
            "type": "sun",
            "center": [250, 300],
            "radius": 30,
            "num_rays": 8,
            "ray_length": 20,
            "fill_color": [255, 255, 0],
            "outline_color": [255, 200, 0],
            "border_width": 2
        }
    ]
    
    # Test advanced shapes
    advanced_shapes = [
        {
            "type": "spiral",
            "center": [150, 450],
            "max_radius": 50,
            "turns": 3,
            "fill_color": [255, 100, 150],
            "border_width": 3
        },
        {
            "type": "fractal_tree",
            "base": [300, 500],
            "height": 60,
            "levels": 4,
            "angle": 30,
            "fill_color": [100, 200, 100],
            "border_width": 2
        }
    ]
    
    all_test_shapes = geometric_shapes + arrow_shapes + decorative_shapes + advanced_shapes
    
    # Test each shape
    for i, shape in enumerate(all_test_shapes):
        try:
            test_config = {
                "canvas_size": [400, 550],
                "background_color": [255, 255, 255],
                "shapes": [shape]
            }
            canvas = Canvas(test_config)
            result = canvas.render()
            print(f"✓ Shape {shape['type']} rendered successfully")
        except Exception as e:
            print(f"✗ Shape {shape['type']} failed: {e}")
            return False
    
    print(f"\n✓ All {len(all_test_shapes)} individual shapes tested successfully!")
    return True


def test_all_shapes_demo():
    """Test the complete demo file with all shapes."""
    try:
        # Load the demo file
        with open("examples/all_new_shapes_demo.json", "r") as f:
            config = json.load(f)
        
        # Create canvas
        canvas = Canvas(config)
        
        # Render and save
        result = canvas.render()
        result.save("output/all_new_shapes_test.png")
        
        print(f"✓ All new shapes demo rendered successfully!")
        print(f"✓ Output saved to: output/all_new_shapes_test.png")
        print(f"✓ Total shapes rendered: {len(config['shapes'])}")
        
        return True
        
    except Exception as e:
        print(f"✗ Demo test failed: {e}")
        return False


def main():
    """Main test function."""
    print("Testing new shapes functionality...\n")
    
    # Test individual shapes
    print("Testing individual shapes:")
    individual_success = test_individual_shapes()
    
    print("\n" + "="*50 + "\n")
    
    # Test complete demo
    print("Testing complete demo:")
    demo_success = test_all_shapes_demo()
    
    print("\n" + "="*50 + "\n")
    
    if individual_success and demo_success:
        print("🎉 All tests passed! New shapes are working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1


if __name__ == "__main__":
    exit(main())