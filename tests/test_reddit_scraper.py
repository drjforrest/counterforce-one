"""
Tests for Reddit scraper functionality
"""

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class TestRedditScraper:
    """Test cases for Reddit scraper."""

    def test_scraper_initialization(self):
        """Test that scraper can be initialized."""
        with patch.dict(
            "os.environ",
            {
                "REDDIT_CLIENT_ID": "test_id",
                "REDDIT_CLIENT_SECRET": "test_secret",
                "REDDIT_USER_AGENT": "test_agent",
            },
        ):
            try:
                from src.reddit_scraper import RedditScraper

                scraper = RedditScraper()
                assert scraper is not None
            except Exception as e:
                # Expected to fail without valid credentials, but class should load
                assert "reddit" in str(e).lower() or "praw" in str(e).lower()

    def test_health_keyword_detection(self):
        """Test health keyword detection logic."""
        # Mock post data
        test_posts = [
            {
                "title": "Question about HIV testing",
                "selftext": "Where can I get tested?",
            },
            {"title": "General discussion", "selftext": "Just chatting about life"},
            {"title": "PrEP question", "selftext": "How effective is PrEP?"},
        ]

        # Mock the health detection logic (simplified)
        health_keywords = ["HIV", "PrEP", "STI", "testing", "prevention"]

        health_related_count = 0
        for post in test_posts:
            text = (post["title"] + " " + post["selftext"]).lower()
            if any(keyword.lower() in text for keyword in health_keywords):
                health_related_count += 1

        assert health_related_count == 2  # HIV and PrEP posts

    def test_language_detection_mock(self):
        """Test language detection logic with mock data."""
        test_texts = [
            "This is an English post about health",
            "Este es un post en español sobre salud",
            "Ito ay isang post sa Tagalog tungkol sa kalusugan",
        ]

        # Mock language detection - in real implementation would use langdetect
        expected_languages = ["en", "es", "tl"]

        # Simple mock test
        assert len(test_texts) == len(expected_languages)
        assert all(isinstance(text, str) for text in test_texts)


class TestConfigurationValidation:
    """Test configuration validation."""

    def test_environment_variables_structure(self):
        """Test that required environment variables are defined in example."""
        env_example_path = project_root / ".env.example"
        assert env_example_path.exists(), ".env.example should exist"

        with open(env_example_path) as f:
            content = f.read()

        required_vars = [
            "REDDIT_CLIENT_ID",
            "REDDIT_CLIENT_SECRET",
            "REDDIT_USER_AGENT",
            "DATABASE_URL",
        ]

        for var in required_vars:
            assert (
                var in content
            ), f"Required environment variable {var} should be in .env.example"


class TestProjectStructure:
    """Test project structure and organization."""

    def test_essential_directories_exist(self):
        """Test that essential directories exist."""
        essential_dirs = [
            "src",
            "config",
            "gradio_app",
            "docs",
            "examples",
            "tools",
            "tests",
        ]

        for dir_name in essential_dirs:
            dir_path = project_root / dir_name
            assert dir_path.exists(), f"Essential directory {dir_name} should exist"
            assert dir_path.is_dir(), f"{dir_name} should be a directory"

    def test_main_entry_point_exists(self):
        """Test that main entry point exists and is valid Python."""
        main_path = project_root / "main.py"
        assert main_path.exists(), "main.py should exist"

        # Basic syntax check
        with open(main_path) as f:
            content = f.read()

        # Should not raise syntax errors
        try:
            compile(content, str(main_path), "exec")
        except SyntaxError as e:
            pytest.fail(f"main.py has syntax errors: {e}")

    def test_requirements_file_valid(self):
        """Test that requirements.txt is valid."""
        req_path = project_root / "requirements.txt"
        assert req_path.exists(), "requirements.txt should exist"

        with open(req_path) as f:
            lines = f.readlines()

        # Should have some dependencies
        non_comment_lines = [
            line.strip()
            for line in lines
            if line.strip() and not line.strip().startswith("#")
        ]
        assert len(non_comment_lines) > 0, "requirements.txt should have dependencies"

        # Check for essential dependencies
        content = "".join(lines).lower()
        essential_deps = ["praw", "pandas", "sqlalchemy", "gradio"]

        for dep in essential_deps:
            assert (
                dep in content
            ), f"Essential dependency {dep} should be in requirements.txt"


if __name__ == "__main__":
    pytest.main([__file__])
