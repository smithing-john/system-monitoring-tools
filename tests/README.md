# Test Suite

Unit tests for system monitoring tools.

## Running Tests

Run all tests:
```bash
python -m unittest discover tests/
```

Run specific test file:
```bash
python tests/test_monitor.py
```

Run with verbose output:
```bash
python -m unittest discover tests/ -v
```

## Test Coverage

Current test coverage:
- Monitor functions: ~70%
- Network monitoring: ~60%
- Logger utilities: ~75%
- Utils functions: ~80%

## Adding New Tests

Create test files with `test_` prefix in the `tests/` directory.
Follow the existing test structure.

## Continuous Integration

Tests are automatically run on:
- Push to main branch
- Pull requests
- Tagged releases

---
*Tests keep the monitoring reliable!*