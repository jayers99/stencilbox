# my_test_tool

A test CLI tool

## Installation

```bash
# Clone and install
git clone <repo-url>
cd my_test_tool
pipenv install --dev
pipenv install -e .
```

## Usage

```bash
# Show help
pipenv run my-test-tool --help

# Show version
pipenv run my-test-tool --version
```

## Development

```bash
# Run tests
pipenv run pytest

# Format code
pipenv run black .

# Lint
pipenv run ruff check .

# Type check
pipenv run mypy src/
```

## License

MIT
