"""Setup configuration for ShapeCanvas package."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="shape-canvas",
    version="1.0.0",
    author="K. Dasaradha",
    author_email="kdasaradha525@example.com",
    description="A powerful Python library for drawing geometric shapes and decorative elements on canvas using PIL/Pillow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KDASARADHA525/Shapes-python-pillow-canvas",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "shape-canvas=shape_canvas.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "shape_canvas": ["examples/*.json", "examples/*.py"],
    },
)