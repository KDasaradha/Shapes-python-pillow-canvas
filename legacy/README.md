# Legacy Code

This directory contains the original implementation of the ShapeCanvas project.

## Files

- `lines_canvas_coordinates_json_data.py` - Original monolithic implementation with all shape drawing functions

## Migration Notes

The legacy code has been superseded by the modern modular implementation in the `src/` directory. The new implementation provides:

- Better code organization with separate modules
- Comprehensive error handling
- Type hints and documentation
- Unit tests
- CLI interface
- Proper packaging

## Usage of Legacy Code

The legacy code can still be used for reference or backward compatibility, but it's recommended to use the new implementation in `src/shape_canvas/` for new projects.

The legacy code was designed to work with JSON configuration files located in the `config/` directory.