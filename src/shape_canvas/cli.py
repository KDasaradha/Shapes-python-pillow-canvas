"""Command-line interface for ShapeCanvas."""

import argparse
import sys
import logging
from pathlib import Path
from typing import Optional

from . import Canvas, __version__
from .exceptions import ShapeCanvasError


def setup_logging(verbose: bool = False) -> None:
    """Setup logging configuration."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="ShapeCanvas - Draw geometric shapes on canvas using JSON configuration",
        prog="shape-canvas"
    )
    
    parser.add_argument(
        "--version", 
        action="version", 
        version=f"ShapeCanvas {__version__}"
    )
    
    parser.add_argument(
        "config",
        help="JSON configuration file path"
    )
    
    parser.add_argument(
        "-o", "--output",
        default="output.png",
        help="Output image file path (default: output.png)"
    )
    
    parser.add_argument(
        "-f", "--format",
        choices=["PNG", "JPEG", "BMP", "TIFF"],
        help="Output image format (auto-detected from filename if not specified)"
    )
    
    parser.add_argument(
        "--no-grid",
        action="store_true",
        help="Disable grid even if specified in config"
    )
    
    parser.add_argument(
        "--show",
        action="store_true",
        help="Display the canvas after rendering"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    setup_logging(args.verbose)
    logger = logging.getLogger(__name__)
    
    try:
        # Validate input file
        config_path = Path(args.config)
        if not config_path.exists():
            logger.error(f"Configuration file not found: {config_path}")
            sys.exit(1)
        
        # Create canvas from configuration
        logger.info(f"Loading configuration from {config_path}")
        canvas = Canvas.from_file(config_path)
        
        # Disable grid if requested
        if args.no_grid:
            canvas.config.show_grid = False
        
        # Process canvas
        logger.info("Processing canvas...")
        canvas.add_grid().load_shapes_from_config().render()
        
        # Save output
        output_path = Path(args.output)
        logger.info(f"Saving canvas to {output_path}")
        canvas.save(output_path, format=args.format)
        
        # Show canvas if requested
        if args.show:
            logger.info("Displaying canvas...")
            canvas.show()
        
        # Print canvas info
        info = canvas.get_canvas_info()
        logger.info(f"Canvas rendered successfully: {info['size'][0]}x{info['size'][1]} with {info['shapes_count']} shapes")
        
    except ShapeCanvasError as e:
        logger.error(f"ShapeCanvas error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        logger.info("Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()