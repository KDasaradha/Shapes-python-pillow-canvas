# Add a new dependency
poetry add requests

# Add a development dependency
poetry add --group dev pytest-mock

# Remove a dependency
poetry remove requests

# Update dependencies
poetry update

# Show installed packages
poetry show

# Activate the virtual environment
poetry shell

# Run commands in the virtual environment
poetry run python main.py
poetry run pytest
poetry run black .
poetry run flake8 .
poetry run mypy .

# Install project and dependencies
poetry install

# Install only production dependencies
poetry install --without dev

# Build the package
poetry build

# Publish to PyPI (when ready)
poetry publish

# Show project info
poetry show --tree

# Check for dependency issues
poetry check
