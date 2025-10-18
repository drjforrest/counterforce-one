"""
Pytest configuration and shared fixtures
"""

import pytest
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


@pytest.fixture(scope="session")
def project_root_path():
    """Provide project root path for tests."""
    return project_root


@pytest.fixture(scope="session")
def sample_reddit_data():
    """Provide sample Reddit data for testing."""
    return [
        {
            "id": "test1",
            "title": "HIV testing in Toronto",
            "selftext": "Where can I get anonymous HIV testing in Toronto?",
            "score": 15,
            "num_comments": 8,
            "language": "en",
            "subreddit": "askTO",
            "is_health_related": True,
        },
        {
            "id": "test2",
            "title": "Best restaurants downtown",
            "selftext": "Looking for good food recommendations",
            "score": 3,
            "num_comments": 2,
            "language": "en",
            "subreddit": "toronto",
            "is_health_related": False,
        },
        {
            "id": "test3",
            "title": "PrEP availability in Vancouver",
            "selftext": "Does anyone know about PrEP access in Vancouver?",
            "score": 22,
            "num_comments": 12,
            "language": "en",
            "subreddit": "vancouver",
            "is_health_related": True,
        },
    ]


@pytest.fixture(scope="session")
def mock_environment():
    """Provide mock environment variables for testing."""
    return {
        "REDDIT_CLIENT_ID": "test_client_id",
        "REDDIT_CLIENT_SECRET": "test_client_secret",
        "REDDIT_USER_AGENT": "TestAgent/1.0",
        "DATABASE_URL": "sqlite:///:memory:",
        "GOOGLE_TRANSLATE_API_KEY": "test_translate_key",
        "LOG_LEVEL": "DEBUG",
    }
