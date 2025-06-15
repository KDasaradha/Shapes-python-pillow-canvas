# Security Policy

## Supported Versions

We actively support the following versions of ShapeCanvas:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in ShapeCanvas, please report it responsibly:

### 🔒 Private Disclosure

For security-related issues, please **DO NOT** open a public GitHub issue. Instead:

1. **Email**: Send details to [security@shapes-canvas.dev](mailto:security@shapes-canvas.dev)
2. **Include**:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### 🕐 Response Timeline

- **Initial Response**: Within 48 hours
- **Vulnerability Assessment**: Within 1 week
- **Fix Development**: Within 2 weeks (depending on severity)
- **Release**: Security fixes are released as soon as possible

### 🏆 Recognition

We appreciate security researchers who help keep ShapeCanvas secure:
- Credit in security advisory (if desired)
- Acknowledgment in release notes
- Hall of fame listing

## Security Considerations

### Input Validation

ShapeCanvas includes comprehensive input validation:
- JSON schema validation
- Parameter bounds checking
- Type validation
- File path sanitization

### Memory Safety

- Canvas size limits to prevent memory exhaustion
- Automatic cleanup of temporary resources
- Bounds checking for shape coordinates

### File Operations

- Secure file handling with proper error handling
- No arbitrary file execution
- Input sanitization for file paths

## Best Practices

When using ShapeCanvas in production:

### 1. Input Validation
```python
# Always validate user input
try:
    canvas = Canvas.from_file(user_config_file)
except ConfigurationError as e:
    # Handle invalid configuration
    logger.error(f"Invalid configuration: {e}")
```

### 2. Resource Limits
```python
# Set reasonable canvas size limits
MAX_CANVAS_SIZE = 4096
if width > MAX_CANVAS_SIZE or height > MAX_CANVAS_SIZE:
    raise ValueError("Canvas size exceeds maximum allowed")
```

### 3. Error Handling
```python
# Proper error handling
try:
    canvas.render().save(output_file)
except DrawingError as e:
    # Handle drawing errors gracefully
    logger.error(f"Drawing failed: {e}")
```

### 4. File Path Validation
```python
# Validate file paths
import os
if not os.path.basename(output_path) == output_path:
    raise ValueError("Invalid output path")
```

## Dependency Security

ShapeCanvas has minimal dependencies:
- **Pillow**: Well-maintained, actively patched
- **Standard Library**: Python built-ins only

We regularly update dependencies and monitor for security advisories.

## Threat Model

### In Scope
- Input validation bypasses
- Memory exhaustion attacks
- File system access beyond intended scope
- Code injection through configuration

### Out of Scope
- DoS through excessive computation (rate limiting should be implemented by users)
- Physical security of systems running ShapeCanvas
- Social engineering attacks
- Third-party integration security (user's responsibility)

## Security Updates

Security updates are released:
- As patch releases (e.g., 1.0.1)
- With clear security advisory
- Through all distribution channels (PyPI, GitHub)

Subscribe to our security announcements:
- GitHub Security Advisories
- Release notifications
- Security mailing list

## Contact

For security concerns:
- **Email**: security@shapes-canvas.dev
- **PGP Key**: Available on request
- **Response Time**: 48 hours maximum

Thank you for helping keep ShapeCanvas secure! 🔒