# Contributing to ShapeCanvas 🎨

Thank you for your interest in contributing to ShapeCanvas! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Shapes-python-pillow-canvas.git
   cd Shapes-python-pillow-canvas
   ```

2. **Set up development environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

3. **Run tests to ensure everything works**
   ```bash
   pytest
   ```

## 🎯 Ways to Contribute

### 🐛 Bug Reports

When filing a bug report, please include:
- Python version and operating system
- ShapeCanvas version
- Minimal code to reproduce the issue
- Expected vs actual behavior
- Screenshots if applicable

Use our [bug report template](https://github.com/KDASARADHA525/Shapes-python-pillow-canvas/issues/new?template=bug_report.md).

### ✨ Feature Requests

For feature requests, please:
- Check existing issues to avoid duplicates
- Describe the use case and benefits
- Provide examples or mockups if possible
- Consider implementation complexity

Use our [feature request template](https://github.com/KDASARADHA525/Shapes-python-pillow-canvas/issues/new?template=feature_request.md).

### 💻 Code Contributions

#### Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the coding standards (see below)
   - Add tests for new functionality
   - Update documentation if needed

3. **Run quality checks**
   ```bash
   make check  # Runs formatting, linting, type checking, and tests
   ```

4. **Commit your changes**
   ```bash
   git commit -m "feat: add amazing new feature"
   ```

5. **Push and create a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

#### Coding Standards

- **Code Style**: We use [Black](https://black.readthedocs.io/) for formatting
- **Linting**: [Flake8](https://flake8.pycqa.org/) for code quality
- **Type Hints**: Use type hints throughout
- **Docstrings**: Use Google-style docstrings
- **Testing**: Aim for >90% test coverage

#### Adding New Shapes

To add a new shape type:

1. **Create the shape class** in `src/shape_canvas/shapes.py`:
   ```python
   class YourShape(BaseShape):
       def validate(self) -> None:
           # Validate shape-specific parameters
           pass
       
       def draw(self, canvas: Image.Image) -> Image.Image:
           # Implement drawing logic
           pass
   ```

2. **Register the shape** in `ShapeFactory._shape_registry`

3. **Add tests** in `tests/test_shapes.py`

4. **Update documentation** with examples

### 📚 Documentation

Documentation contributions are highly valued:
- Fix typos and improve clarity
- Add examples and tutorials
- Improve API documentation
- Create video tutorials or blog posts

## 🧪 Testing

### Running Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=src/shape_canvas --cov-report=html

# Specific test file
pytest tests/test_canvas.py

# Specific test
pytest tests/test_canvas.py::TestCanvas::test_create_blank_canvas
```

### Writing Tests

- Place tests in the `tests/` directory
- Use descriptive test names
- Test both success and failure cases
- Include edge cases
- Mock external dependencies

Example:
```python
def test_circle_with_valid_parameters(self):
    """Test circle creation with valid parameters."""
    shape_data = {
        "center": [100, 100],
        "radius": 50,
        "fill_color": [255, 0, 0],
        "outline_color": [0, 0, 0],
        "border_width": 2
    }
    shape = Circle(shape_data)
    assert shape is not None
```

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Tests pass locally
- [ ] Code is formatted with Black
- [ ] No linting errors
- [ ] Type checking passes
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated (if applicable)

### PR Description

Include in your PR description:
- Summary of changes
- Related issue numbers
- Breaking changes (if any)
- Screenshots/examples (if applicable)

### Review Process

1. Automated checks will run
2. Maintainers will review your code
3. Address any feedback
4. Once approved, your PR will be merged

## 🎨 Code Style Guide

### Python Code

```python
# Good
def create_shape(shape_data: Dict[str, Any]) -> BaseShape:
    """Create a shape instance from configuration data.
    
    Args:
        shape_data: Dictionary containing shape configuration
        
    Returns:
        Shape instance
        
    Raises:
        InvalidShapeError: If shape type is not supported
    """
    if "type" not in shape_data:
        raise InvalidShapeError("Shape data must contain 'type' field")
    
    return ShapeFactory.create_shape(shape_data)
```

### Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` new features
- `fix:` bug fixes
- `docs:` documentation changes
- `style:` code style changes
- `refactor:` code refactoring
- `test:` test additions/changes
- `chore:` maintenance tasks

Examples:
```
feat: add gradient support for shapes
fix: resolve memory leak in canvas rendering
docs: add tutorial for custom shapes
```

## 🏆 Recognition

Contributors are automatically recognized:
- Added to README contributors section
- Listed in release notes for their contributions
- Eligible for special contributor badges

## 🤝 Code of Conduct

We follow the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). Please read it before participating.

## ❓ Questions?

- Open a [discussion](https://github.com/KDASARADHA525/Shapes-python-pillow-canvas/discussions)
- Join our community chat
- Email maintainers for sensitive issues

Thank you for contributing to ShapeCanvas! 🎉