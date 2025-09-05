# Contributing to UBS Coding Challenge 2025

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## How to Contribute

### Reporting Issues
- Use the GitHub issue tracker to report bugs
- Include detailed information about your environment
- Provide steps to reproduce the issue
- Include relevant error messages or logs

### Suggesting Features
- Open an issue with the "enhancement" label
- Describe the feature in detail
- Explain why it would be useful
- Consider backwards compatibility

### Submitting Code Changes

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/ubs-coding-challenge-2025.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation as needed

4. **Test your changes**
   ```bash
   # Run tests
   pytest tests/ -v
   
   # Test both servers
   python test_client.py
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: detailed description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Use a clear title and description
   - Reference any related issues
   - Include screenshots if relevant

## Code Style Guidelines

### Python Code
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write descriptive variable and function names
- Add docstrings to functions and classes

### API Design
- Follow RESTful conventions
- Use appropriate HTTP status codes
- Include comprehensive error handling
- Document all endpoints

### Testing
- Write tests for new features
- Maintain or improve test coverage
- Test both happy path and error cases
- Include integration tests for API endpoints

## Development Setup

1. **Clone and setup**
   ```bash
   git clone <your-fork>
   cd ubs-coding-challenge-2025
   pip install -r requirements.txt
   cp .env.template .env
   ```

2. **Run development servers**
   ```bash
   # Terminal 1: Flask
   cd flask_app && python app.py
   
   # Terminal 2: FastAPI  
   cd fastapi_app && uvicorn main:app --reload --port 8000
   ```

3. **Run tests**
   ```bash
   pytest tests/ -v
   python test_client.py
   ```

## Project Structure

When adding new features, follow the existing structure:

```
├── flask_app/              # Flask-specific code
├── fastapi_app/           # FastAPI-specific code
├── tests/                 # All test files
├── docs/                  # Additional documentation (if needed)
└── scripts/               # Utility scripts
```

## Release Process

1. Update version numbers in relevant files
2. Update CHANGELOG.md with new features and fixes
3. Create a release tag
4. Update documentation if needed

## Questions?

If you have questions about contributing:
- Open an issue with the "question" label
- Check existing issues and discussions
- Review the project documentation

Thank you for contributing! 🚀
