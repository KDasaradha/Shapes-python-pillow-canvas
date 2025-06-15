#!/usr/bin/env python3
"""
Main application demonstrating the modernized ShapeCanvas library.

This file shows how to use the new production-level ShapeCanvas library
with support for all shapes (old and new) through JSON configuration files.
"""

import logging
import json
from pathlib import Path
from shape_canvas.canvas import Canvas
from shape_canvas.shapes import ShapeFactory
from shape_canvas.exceptions import ShapeCanvasError


def setup_logging():
    """Setup logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def main():
    """Main application entry point."""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # Ensure output directory exists
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        
        # Check if original config file exists
        original_config = Path("config/lines_canvas_coordinates_json_data_input_json.json")
        
        if original_config.exists():
            logger.info("Using original configuration file...")
            
            try:
                # Load from original configuration
                canvas = Canvas(original_config)
                
                # Render canvas
                result = canvas.render()
                
                # Get the rendered image and save it
                output_file = output_dir / "original_config_output.png"
                canvas.save(str(output_file))
                logger.info(f"✓ Canvas rendered from original config and saved as '{output_file}'")
                
                # Display canvas info
                info = canvas.get_canvas_info()
                logger.info(f"Canvas Info: {info['size'][0]}x{info['size'][1]}, {info['shapes_count']} shapes")
                
            except Exception as e:
                logger.error(f"Error processing original config: {e}")
                logger.info("Continuing with demo...")
        
        # Check if new shapes demo exists
        demo_config = Path("examples/all_new_shapes_demo.json")
        
        if demo_config.exists():
            logger.info("Running new shapes demo...")
            
            try:
                # Load and render the new shapes demo
                canvas = Canvas(demo_config)
                result = canvas.render()
                
                # Save the result
                demo_output_file = output_dir / "all_new_shapes_demo.png"
                canvas.save(str(demo_output_file))
                logger.info(f"✓ New shapes demo rendered and saved as '{demo_output_file}'")
                
                # Display info
                info = canvas.get_canvas_info()
                logger.info(f"Demo Info: {info['size'][0]}x{info['size'][1]}, {info['shapes_count']} shapes")
                
            except Exception as e:
                logger.error(f"Error processing demo config: {e}")
        
        # Create a comprehensive demo with all shape types
        logger.info("Creating comprehensive demo with all shape types...")
        
        # Demo configuration with various shape types (both old and new)
        comprehensive_demo = {
            "canvas_size": [1000, 800],
            "background_color": [240, 248, 255],  # Light blue background
            "show_grid": True,
            "line_interval": 50,
            "line_color": "lightgray",
            "shapes": [
                # Basic shapes
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
                    "center": [100, 200],
                    "radius": 40,
                    "fill_color": [100, 255, 100],
                    "outline_color": [0, 200, 0],
                    "border_width": 2
                },
                # New geometric shapes
                {
                    "type": "triangle",
                    "point1": [200, 50],
                    "point2": [250, 50],
                    "point3": [225, 100],
                    "fill_color": [255, 255, 100],
                    "outline_color": [200, 200, 0],
                    "border_width": 2
                },
                {
                    "type": "hexagon",
                    "center": [300, 75],
                    "radius": 30,
                    "rotation": 0,
                    "fill_color": [255, 150, 255],
                    "outline_color": [200, 100, 200],
                    "border_width": 2
                },
                # Arrow shapes
                {
                    "type": "block_arrow",
                    "start": [400, 60],
                    "end": [500, 90],
                    "shaft_width": 15,
                    "head_width": 30,
                    "fill_color": [255, 165, 0],
                    "outline_color": [255, 140, 0],
                    "border_width": 2
                },
                # Decorative shapes
                {
                    "type": "star",
                    "center": [150, 300],
                    "size": 40,
                    "num_points": 5,
                    "fill_color": [255, 215, 0],
                    "outline_color": [184, 134, 11],
                    "border_width": 2
                },
                {
                    "type": "flower",
                    "center": [300, 300],
                    "petal_size": 25,
                    "num_petals": 6,
                    "fill_color": [255, 192, 203],
                    "outline_color": [255, 105, 180],
                    "center_color": [255, 255, 0],
                    "border_width": 2
                },
                {
                    "type": "sun",
                    "center": [450, 300],
                    "radius": 25,
                    "num_rays": 8,
                    "ray_length": 15,
                    "fill_color": [255, 255, 0],
                    "outline_color": [255, 215, 0],
                    "border_width": 2
                },
                # Technical shapes
                {
                    "type": "plus_sign",
                    "center": [600, 100],
                    "size": 20,
                    "thickness": 4,
                    "fill_color": [0, 255, 0],
                    "border_width": 2
                },
                {
                    "type": "cross",
                    "center": [700, 100],
                    "size": 20,
                    "thickness": 6,
                    "fill_color": [255, 0, 0],
                    "outline_color": [200, 0, 0],
                    "border_width": 2
                },
                # Advanced shapes
                {
                    "type": "spiral",
                    "center": [600, 300],
                    "max_radius": 35,
                    "turns": 3,
                    "fill_color": [128, 0, 128],
                    "border_width": 2
                },
                {
                    "type": "sine_wave_pattern",
                    "start": [50, 450],
                    "width": 200,
                    "amplitude": 20,
                    "frequency": 2,
                    "fill_color": [0, 100, 200],
                    "border_width": 2
                }
            ]
        }
        
        try:
            # Create and render comprehensive demo
            canvas = Canvas(comprehensive_demo)
            result = canvas.render()
            
            # Save the comprehensive demo
            comp_output_file = output_dir / "comprehensive_demo.png"
            canvas.save(str(comp_output_file))
            logger.info(f"✓ Comprehensive demo created and saved as '{comp_output_file}'")
            
            # Display info
            info = canvas.get_canvas_info()
            logger.info(f"Comprehensive Demo: {info['size'][0]}x{info['size'][1]}, {info['shapes_count']} shapes")
            
        except Exception as e:
            logger.error(f"Error creating comprehensive demo: {e}")
        
        # Show all supported shapes
        supported_shapes = ShapeFactory.get_supported_shapes()
        logger.info(f"✓ Total supported shapes: {len(supported_shapes)}")
        logger.info("📋 All supported shapes:")
        for i, shape in enumerate(sorted(supported_shapes), 1):
            logger.info(f"   {i:2d}. {shape}")
        
        logger.info("\n🎉 Application completed successfully!")
        logger.info("📁 Check the 'output' folder for generated images.")
        logger.info("📖 See 'docs/NEW_SHAPES.md' for complete documentation.")
        
    except ShapeCanvasError as e:
        logger.error(f"ShapeCanvas error: {e}")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())