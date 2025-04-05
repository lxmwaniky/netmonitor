# Contributor Guidelines

## Getting Started

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/lxmwaniky/netmonitor.git
   ```
3. **Set up** development environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac)
   pip install -e ".[dev]"
   ```

## Development Workflow

### Branch Naming
Use format: `[type]/[description]`  
Example: `feat/add-wifi-strength`

| Prefix    | Purpose                      |
|-----------|------------------------------|
| `feat/`   | New features                 |
| `fix/`    | Bug fixes                    |
|`docs/`    | Documentation improvements   |
| `test/`   | Test-related changes         |

### Code Standards
- Follow PEP 8 style guide
- Keep functions under 50 lines
- Use type hints for new code
- Document public methods with docstrings

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=lib --cov-report=term-missing
```

## Pull Requests

1. Ensure your branch is **rebased** on latest `main`
2. Update `CHANGELOG.md` (if applicable)
3. Open PR with:
   - Description of changes
   - Screenshots (for UI changes)
   - Test coverage report

## Report Issues

When filing bugs, include:
1. OS and Python version
2. Exact command that triggered the issue
3. Full error output
4. Steps to reproduce

## Code of Conduct

Be respectful and:
- Keep discussions focused on the code
- Accept constructive criticism
- Help maintain documentation

> **Note**: For major changes, please open an issue first to discuss the proposed changes.