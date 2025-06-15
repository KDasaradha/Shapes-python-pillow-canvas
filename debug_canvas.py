#!/usr/bin/env python3
"""Debug script to identify why canvas might be blank."""

import json
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from shape_canvas.canvas import Canvas
from PIL import Image


def debug_simple_shape():
    """Test with a very simple, large shape."""
    print("🔍 Testing with simple, large shape...")
    
    config = {
        "canvas_size": [400, 300],
        "background_color": [255, 255, 255],  # White background
        "shapes": [
            {
                "type": "rectangle",
                "start": [50, 50],
                "end": [350, 250],
                "fill_color": [255, 0, 0],  # Bright red
                "outline_color": [0, 0, 0],  # Black outline
                "border_width": 5
            }
        ]
    }
    
    try:
        canvas = Canvas(config)
        result = canvas.render()
        image = canvas.get_image()
        
        # Save and analyze
        image.save("output/debug_simple.png")
        
        # Check if image has any non-white pixels
        pixels = list(image.getdata())
        white_pixels = sum(1 for p in pixels if p == (255, 255, 255))
        total_pixels = len(pixels)
        non_white_pixels = total_pixels - white_pixels
        
        print(f"   Canvas size: {image.size}")
        print(f"   Total pixels: {total_pixels}")
        print(f"   White pixels: {white_pixels}")
        print(f"   Non-white pixels: {non_white_pixels}")
        
        if non_white_pixels > 0:
            print("   ✅ Shape is visible!")
        else:
            print("   ❌ Canvas is completely white!")
            
        return non_white_pixels > 0
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def debug_coordinate_bounds():
    """Test shapes with various coordinate ranges."""
    print("\n🔍 Testing coordinate bounds...")
    
    test_shapes = [
        {
            "name": "Small coordinates",
            "shape": {
                "type": "circle",
                "center": [100, 100],
                "radius": 50,
                "fill_color": [255, 0, 0],
                "outline_color": [0, 0, 0],
                "border_width": 2
            }
        },
        {
            "name": "Large coordinates", 
            "shape": {
                "type": "circle",
                "center": [500, 400],
                "radius": 50,
                "fill_color": [0, 255, 0],
                "outline_color": [0, 0, 0],
                "border_width": 2
            }
        },
        {
            "name": "Edge coordinates",
            "shape": {
                "type": "circle",
                "center": [50, 50],
                "radius": 30,
                "fill_color": [0, 0, 255],
                "outline_color": [0, 0, 0],
                "border_width": 2
            }
        }
    ]
    
    for i, test in enumerate(test_shapes):
        print(f"   Testing: {test['name']}")
        
        config = {
            "canvas_size": [600, 500],
            "background_color": [255, 255, 255],
            "shapes": [test['shape']]
        }
        
        try:
            canvas = Canvas(config)
            canvas.render()
            image = canvas.get_image()
            
            # Check for non-white pixels
            pixels = list(image.getdata())
            non_white = sum(1 for p in pixels if p != (255, 255, 255))
            
            filename = f"output/debug_coords_{i}.png"
            image.save(filename)
            
            if non_white > 0:
                print(f"      ✅ Visible ({non_white} colored pixels) - saved as {filename}")
            else:
                print(f"      ❌ Not visible - saved as {filename}")
                
        except Exception as e:
            print(f"      ❌ Error: {e}")


def debug_color_validation():
    """Test different color formats."""
    print("\n🔍 Testing color validation...")
    
    color_tests = [
        {
            "name": "Valid RGB",
            "fill_color": [255, 100, 50],
            "outline_color": [0, 0, 0]
        },
        {
            "name": "Edge values",
            "fill_color": [0, 255, 0],
            "outline_color": [255, 0, 255]
        },
        {
            "name": "Mid-range values",
            "fill_color": [128, 128, 128],
            "outline_color": [64, 64, 64]
        }
    ]
    
    for i, test in enumerate(color_tests):
        print(f"   Testing: {test['name']}")
        
        config = {
            "canvas_size": [200, 200],
            "background_color": [255, 255, 255],
            "shapes": [
                {
                    "type": "rectangle",
                    "start": [20, 20],
                    "end": [180, 180],
                    "fill_color": test['fill_color'],
                    "outline_color": test['outline_color'],
                    "border_width": 3
                }
            ]
        }
        
        try:
            canvas = Canvas(config)
            canvas.render()
            image = canvas.get_image()
            
            filename = f"output/debug_color_{i}.png"
            image.save(filename)
            
            # Check for non-white pixels
            pixels = list(image.getdata())
            non_white = sum(1 for p in pixels if p != (255, 255, 255))
            
            if non_white > 0:
                print(f"      ✅ Rendered successfully ({non_white} colored pixels)")
            else:
                print(f"      ❌ No visible content")
                
        except Exception as e:
            print(f"      ❌ Error: {e}")


def debug_new_shapes():
    """Test some of the new shapes."""
    print("\n🔍 Testing new shapes...")
    
    new_shape_tests = [
        {
            "type": "triangle",
            "point1": [50, 50],
            "point2": [150, 50],
            "point3": [100, 150],
            "fill_color": [255, 0, 0],
            "outline_color": [0, 0, 0],
            "border_width": 2
        },
        {
            "type": "flower",
            "center": [100, 100],
            "petal_size": 30,
            "num_petals": 6,
            "fill_color": [255, 192, 203],
            "outline_color": [255, 105, 180],
            "center_color": [255, 255, 0],
            "border_width": 2
        },
        {
            "type": "sun",
            "center": [100, 100],
            "radius": 30,
            "num_rays": 8,
            "ray_length": 20,
            "fill_color": [255, 255, 0],
            "outline_color": [255, 215, 0],
            "border_width": 2
        }
    ]
    
    for i, shape in enumerate(new_shape_tests):
        print(f"   Testing: {shape['type']}")
        
        config = {
            "canvas_size": [200, 200],
            "background_color": [255, 255, 255],
            "shapes": [shape]
        }
        
        try:
            canvas = Canvas(config)
            canvas.render()
            image = canvas.get_image()
            
            filename = f"output/debug_new_{shape['type']}.png"
            image.save(filename)
            
            # Check for non-white pixels
            pixels = list(image.getdata())
            non_white = sum(1 for p in pixels if p != (255, 255, 255))
            
            if non_white > 0:
                print(f"      ✅ {shape['type']} rendered successfully ({non_white} colored pixels)")
            else:
                print(f"      ❌ {shape['type']} not visible")
                
        except Exception as e:
            print(f"      ❌ Error with {shape['type']}: {e}")


def main():
    """Run all debug tests."""
    print("🐛 Canvas Debug Tool")
    print("=" * 50)
    
    # Ensure output directory exists
    Path("output").mkdir(exist_ok=True)
    
    # Run debug tests
    tests_passed = 0
    total_tests = 4
    
    if debug_simple_shape():
        tests_passed += 1
    
    debug_coordinate_bounds()
    debug_color_validation()
    debug_new_shapes()
    
    print(f"\n📊 Summary:")
    print(f"   Basic functionality test: {'✅ PASSED' if tests_passed > 0 else '❌ FAILED'}")
    print(f"   Check the output/ folder for generated debug images.")
    
    if tests_passed == 0:
        print("\n❌ All tests failed - there might be a fundamental issue with shape rendering.")
    else:
        print("\n✅ Basic rendering works - blank canvas might be due to:")
        print("   • Shapes positioned outside canvas bounds")
        print("   • Colors too similar to background")
        print("   • Invalid shape parameters")
        print("   • Coordinate system issues")


if __name__ == "__main__":
    main()