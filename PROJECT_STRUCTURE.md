# Project Structure

This document describes the organized structure of the ShapeCanvas project.

## Directory Structure

```
Shapes-python-pillow-canvas/
├── .gitignore                    # Git ignore file
├── .vscode/                      # VS Code settings
├── LICENSE                       # MIT License
├── README.md                     # Main project README
├── requirements.txt              # Python dependencies
├── setup.py                      # Package setup configuration
├── pyproject.toml               # Modern Python project configuration
├── pytest.ini                   # Pytest configuration
├── Makefile                     # Build and development tasks
├── main.py                      # Main application entry point
│
├── src/                         # Source code (modern implementation)
│   └── shape_canvas/           # Main package
│       ├── __init__.py         # Package initialization
│       ├── canvas.py           # Canvas class
│       ├── shapes.py           # Shape classes and factory
│       ├── config.py           # Configuration handling
│       ├── exceptions.py       # Custom exceptions
│       └── cli.py              # Command-line interface
│
├── tests/                       # Unit tests
│   ├── __init__.py
│   ├── test_canvas.py          # Canvas tests
│   └── test_shapes.py          # Shape tests
│
├── examples/                    # Usage examples
│   ├── demo.py                 # Demo script
│   └── basic_shapes.json       # Example configuration
│
├── config/                      # Configuration files
│   └── lines_canvas_coordinates_json_data_input_json.json
│
├── legacy/                      # Legacy code (archived)
│   ├── README.md               # Legacy documentation
│   └── lines_canvas_coordinates_json_data.py
│
└── docs/                        # Documentation
    ├── CHANGELOG.md
    ├── CONTRIBUTING.md
    ├── DOCUMENTATION_INDEX.md
    ├── HOW-TO-RUN.md
    ├── MIGRATION.md
    ├── Notes.md
    ├── QUICKSTART.md
    ├── SECURITY.md
    └── UPGRADE_SUMMARY.md
```

## Key Components

### Source Code (`src/shape_canvas/`)
- **Modern, modular implementation**
- Clean separation of concerns
- Type hints and comprehensive documentation
- Error handling and validation

### Tests (`tests/`)
- Comprehensive unit tests
- Test coverage for all major components
- Uses pytest framework

### Examples (`examples/`)
- Working examples and demos
- Configuration file examples
- Usage documentation

### Configuration (`config/`)
- JSON configuration files
- Shape definitions and canvas settings

### Legacy (`legacy/`)
- Original monolithic implementation
- Kept for reference and backward compatibility
- Not recommended for new development

### Documentation (`docs/`)
- All project documentation
- Setup guides, API docs, migration notes
- Contributing guidelines

## Development Workflow

1. **Modern Development**: Use code in `src/shape_canvas/`
2. **Testing**: Run tests from `tests/` directory
3. **Examples**: Check `examples/` for usage patterns
4. **Configuration**: Place configs in `config/` directory
5. **Documentation**: Update docs in `docs/` directory

## Installation and Usage

```bash
# Install in development mode
pip install -e .

# Run main application
python main.py

# Run tests
pytest

# Run examples
python examples/demo.py
```

This structure provides clear separation between different types of files and makes the project much more maintainable and professional.