# Tests

This directory contains the test suite for the Health Misinformation Detection Platform.

## Running Tests

### Run All Tests
```bash
pytest tests/
```

### Run with Coverage
```bash
pytest tests/ --cov=src --cov-report=html
```

### Run Specific Test File
```bash
pytest tests/test_reddit_scraper.py -v
```

### Run Tests with Output
```bash
pytest tests/ -v -s
```

## Test Structure

- `conftest.py` - Pytest configuration and shared fixtures
- `test_reddit_scraper.py` - Tests for Reddit scraping functionality
- `test_project_structure.py` - Tests for project organization and setup

## Test Categories

### Unit Tests
Tests for individual components and functions:
- Reddit scraper initialization
- Health keyword detection
- Language detection logic
- Configuration validation

### Integration Tests  
Tests for component interactions:
- Database connectivity
- API integrations
- Data pipeline workflows

### Structure Tests
Tests for project organization:
- Directory structure validation
- File existence checks
- Dependencies validation

## Adding New Tests

When adding new functionality:

1. Create test files following the `test_*.py` pattern
2. Use descriptive test names: `test_feature_does_expected_behavior`
3. Include both positive and negative test cases
4. Use fixtures for common test data
5. Mock external dependencies (APIs, databases)

## Test Data

Test fixtures provide sample data:
- `sample_reddit_data` - Mock Reddit posts for testing
- `mock_environment` - Environment variables for testing
- `project_root_path` - Path utilities for tests

## Continuous Integration

These tests are designed to run in CI environments without requiring:
- Real Reddit API credentials
- Live database connections
- External API access

Mock objects and fixtures simulate these dependencies for testing.