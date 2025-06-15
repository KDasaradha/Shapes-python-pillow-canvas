#!/usr/bin/env python3
"""
Demo script showing how to use ShapeCanvas library.
"""

from pathlib import Path
from shape_canvas import Canvas, CanvasConfig


def main():
    """Demonstrate ShapeCanvas functionality."""
    
    # Example 1: Create canvas from configuration file
    print("Example 1: Loading from configuration file")
    config_file = Path(__file__).parent / "basic_shapes.json"
    
    if config_file.exists():
        canvas = Canvas.from_file(config_file)
        canvas.add_grid().load_shapes_from_config().render()
        canvas.save("example1_from_config.png")
        print("✓ Canvas created from config file and saved as 'example1_from_config.png'")
    else:
        print("⚠ Configuration file not found, skipping example 1")
    
    # Example 2: Create canvas programmatically
    print("\nExample 2: Creating canvas programmatically")
    canvas = Canvas.create_blank(600, 400, (240, 248, 255))  # Light blue background
    
    # Add shapes programmatically
    shapes = [
        {
            "type": "rectangle",
            "start": [50, 50],
            "end": [150, 100],
            "fill_color": [255, 100, 100],
            "outline_color": [200, 0, 0],
            "border_width": 2
        },
        {
            "type": "circle",
            "center": [300, 200],
            "radius": 80,
            "fill_color": [100, 255, 100],
            "outline_color": [0, 200, 0],
            "border_width": 3
        },
        {
            "type": "star",
            "center": [500, 200],
            "size": 50,
            "fill_color": [255, 255, 100],
            "outline_color": [200, 200, 0],
            "border_width": 2,
            "num_points": 6
        }
    ]
    
    canvas.add_shapes(shapes).render().save("example2_programmatic.png")
    print("✓ Programmatic canvas saved as 'example2_programmatic.png'")
    
    # Example 3: Method chaining
    print("\nExample 3: Method chaining demonstration")
    (Canvas.create_blank(400, 300)
     .add_shape({
         "type": "heart",
         "center": [200, 150],
         "size": 3,
         "fill_color": [255, 20, 147],
         "outline_color": [139, 0, 69],
         "border_width": 2,
         "rotation_angle": 0
     })
     .render()
     .save("example3_heart.png"))
    print("✓ Heart shape saved as 'example3_heart.png'")
    
    # Example 4: Canvas information
    print("\nExample 4: Canvas information")
    canvas = Canvas.create_blank(800, 600)
    canvas.add_shape({
        "type": "straight_line",
        "start": [100, 100],
        "end": [700, 500],
        "fill_color": [255, 0, 0],
        "border_width": 5
    })
    
    info = canvas.get_canvas_info()
    print(f"Canvas size: {info['size']}")
    print(f"Background color: {info['background_color']}")
    print(f"Number of shapes: {info['shapes_count']}")
    print(f"Supported shapes: {', '.join(info['supported_shapes'])}")
    
    canvas.render().save("example4_info.png")
    print("✓ Line example saved as 'example4_info.png'")
    
    print("\n🎉 All examples completed successfully!")
    print("Check the generated PNG files to see the results.")


if __name__ == "__main__":
    main()