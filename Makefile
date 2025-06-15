# Makefile for ShapeCanvas project

.PHONY: help install install-dev test test-coverage lint format type-check clean build docs demo

# Default target
help:
	@echo "ShapeCanvas Development Commands"
	@echo "================================"
	@echo "install       Install package in production mode"
	@echo "install-dev   Install package in development mode with dev dependencies"
	@echo "test          Run test suite"
	@echo "test-coverage Run tests with coverage report"
	@echo "lint          Run code linting (flake8)"
	@echo "format        Format code (black)"
	@echo "type-check    Run type checking (mypy)"
	@echo "clean         Clean build artifacts"
	@echo "build         Build package for distribution"
	@echo "demo          Run demo examples"
	@echo "help          Show this help message"

# Installation
install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

# Testing
test:
	pytest

test-coverage:
	pytest --cov=src/shape_canvas --cov-report=html --cov-report=term-missing

# Code quality
lint:
	flake8 src/ tests/ examples/

format:
	black src/ tests/ examples/

type-check:
	mypy src/

# Maintenance
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

# Building
build: clean
	python -m build

# Demo
demo:
	python examples/demo.py

# Development workflow
dev-setup: install-dev
	@echo "Development environment ready!"
	@echo "Run 'make test' to ensure everything works."

# Quality check (run before committing)
check: format lint type-check test
	@echo "All quality checks passed! ✅"

# CI pipeline
ci: install-dev format lint type-check test-coverage
	@echo "CI pipeline completed successfully! 🎉"