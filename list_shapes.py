#!/usr/bin/env python3
"""Script to list all supported shapes in the application."""

import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent / "src"))

from shape_canvas.shapes import ShapeFactory


def main():
    """List all supported shapes."""
    shapes = ShapeFactory.get_supported_shapes()
    shapes.sort()
    
    print("🎨 Shapes Python Pillow Canvas - Supported Shapes")
    print("=" * 55)
    print(f"Total shapes available: {len(shapes)}")
    print()
    
    # Group shapes by category
    categories = {
        "Basic Shapes": [
            "straight_line", "dashed_line", "rectangle", "square", 
            "circle", "ellipse"
        ],
        "Geometric Shapes": [
            "triangle", "pentagon", "hexagon", "octagon", "rhombus", 
            "parallelogram", "trapezoid", "diamond", "regular_polygon"
        ],
        "Arrow Shapes": [
            "line_with_arrowhead", "line_with_double_arrowhead", 
            "block_arrow", "curved_arrow", "circular_arrow"
        ],
        "Connector Shapes": [
            "elbow_connector", "elbow_connector_with_arrowhead",
            "elbow_connector_with_double_arrowhead", "zigzag_line", "wavy_line"
        ],
        "Decorative Shapes": [
            "heart", "star", "cloud", "flower", "butterfly", "tree", 
            "sun", "moon", "lightning_bolt"
        ],
        "Text/Callout Shapes": [
            "speech_bubble_rectangle", "callout_bubble", "thought_bubble",
            "banner_ribbon", "oval_callout"
        ],
        "Technical/Symbol Shapes": [
            "cross", "plus_sign", "minus_sign", "multiplication_sign"
        ],
        "Advanced Shapes": [
            "spiral", "helix", "sine_wave_pattern", "fractal_tree",
            "polygon_with_coordinates"
        ]
    }
    
    for category, category_shapes in categories.items():
        available_shapes = [s for s in category_shapes if s in shapes]
        if available_shapes:
            print(f"📂 {category}:")
            for shape in available_shapes:
                print(f"   • {shape}")
            print()
    
    # Show any uncategorized shapes
    categorized = set()
    for category_shapes in categories.values():
        categorized.update(category_shapes)
    
    uncategorized = [s for s in shapes if s not in categorized]
    if uncategorized:
        print("📂 Other Shapes:")
        for shape in uncategorized:
            print(f"   • {shape}")
        print()
    
    print("💡 Usage:")
    print("   To use any shape, set the 'type' field to one of the above values.")
    print("   For examples, see: examples/all_new_shapes_demo.json")
    print("   For documentation, see: docs/NEW_SHAPES.md")


if __name__ == "__main__":
    main()