#!/usr/bin/env python3
"""Test script to verify grid functionality."""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from shape_canvas.canvas import Canvas


def test_grid_visibility():
    """Test that grid lines are visible."""
    print("🔍 Testing grid visibility...")
    
    config = {
        "canvas_size": [400, 300],
        "background_color": [255, 255, 255],  # White background
        "show_grid": True,
        "line_interval": 50,
        "line_color": "gray",
        "shapes": [
            {
                "type": "circle",
                "center": [200, 150],
                "radius": 30,
                "fill_color": [255, 0, 0],
                "outline_color": [0, 0, 0],
                "border_width": 2
            }
        ]
    }
    
    try:
        canvas = Canvas(config)
        result = canvas.render()
        image = canvas.get_image()
        
        # Save the test image
        image.save("output/grid_test.png")
        
        # Check for gray pixels (grid lines)
        pixels = list(image.getdata())
        gray_pixels = sum(1 for p in pixels if p == (128, 128, 128))  # Gray color
        light_gray_pixels = sum(1 for p in pixels if 100 <= p[0] <= 200 and p[0] == p[1] == p[2])  # Light gray range
        
        print(f"   Canvas size: {image.size}")
        print(f"   Total pixels: {len(pixels)}")
        print(f"   Gray pixels found: {gray_pixels}")
        print(f"   Light gray pixels found: {light_gray_pixels}")
        
        if gray_pixels > 0 or light_gray_pixels > 100:
            print("   ✅ Grid lines are visible!")
            return True
        else:
            print("   ❌ No grid lines detected!")
            return False
            
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def test_different_grid_settings():
    """Test different grid configurations."""
    print("\n🔍 Testing different grid settings...")
    
    grid_configs = [
        {"interval": 25, "color": "lightgray", "name": "Fine grid"},
        {"interval": 100, "color": "darkgray", "name": "Coarse grid"},
        {"interval": 50, "color": "blue", "name": "Blue grid"}
    ]
    
    for i, grid_config in enumerate(grid_configs):
        print(f"   Testing: {grid_config['name']}")
        
        config = {
            "canvas_size": [300, 200],
            "background_color": [255, 255, 255],
            "show_grid": True,
            "line_interval": grid_config["interval"],
            "line_color": grid_config["color"],
            "shapes": [
                {
                    "type": "rectangle",
                    "start": [50, 50],
                    "end": [150, 100],
                    "fill_color": [255, 100, 100],
                    "outline_color": [200, 0, 0],
                    "border_width": 2
                }
            ]
        }
        
        try:
            canvas = Canvas(config)
            canvas.render()
            image = canvas.get_image()
            
            filename = f"output/grid_test_{i}_{grid_config['name'].replace(' ', '_').lower()}.png"
            image.save(filename)
            
            print(f"      ✅ {grid_config['name']} rendered - saved as {filename}")
            
        except Exception as e:
            print(f"      ❌ Error with {grid_config['name']}: {e}")


def test_coordinate_labels():
    """Test if coordinate labels are showing."""
    print("\n🔍 Testing coordinate labels...")
    
    config = {
        "canvas_size": [200, 150],
        "background_color": [255, 255, 255],
        "show_grid": True,
        "line_interval": 50,
        "line_color": "gray",
        "shapes": []  # No shapes, just grid
    }
    
    try:
        canvas = Canvas(config)
        canvas.render()
        image = canvas.get_image()
        
        filename = "output/grid_coordinates_test.png"
        image.save(filename)
        
        print(f"   ✅ Grid with coordinates saved as {filename}")
        print("   📝 Check the image to see if coordinate labels (0,0), (50,0), etc. are visible")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False


def main():
    """Run all grid tests."""
    print("🔲 Grid Functionality Test")
    print("=" * 40)
    
    # Ensure output directory exists
    Path("output").mkdir(exist_ok=True)
    
    # Run tests
    tests_passed = 0
    total_tests = 3
    
    if test_grid_visibility():
        tests_passed += 1
    
    test_different_grid_settings()
    
    if test_coordinate_labels():
        tests_passed += 1
    
    print(f"\n📊 Grid Test Summary:")
    print(f"   Tests passed: {tests_passed}/{total_tests}")
    print(f"   Check the output/ folder for grid test images")
    
    if tests_passed >= 2:
        print("\n✅ Grid functionality is working!")
    else:
        print("\n❌ Grid functionality needs attention!")


if __name__ == "__main__":
    main()