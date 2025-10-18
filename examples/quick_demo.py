#!/usr/bin/env python3
"""
Quick demonstration of the Health Misinformation Detection Platform
This script shows basic data collection and analysis capabilities.
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from loguru import logger
from src.reddit_scraper import RedditScraper
from src.network_analysis import NetworkAnalyzer


def main():
    """Run quick demonstration of platform capabilities."""
    logger.info("🚀 Starting Health Misinformation Platform Quick Demo")

    # Check environment setup
    env_file = project_root / ".env"
    if not env_file.exists():
        logger.error(
            "❌ .env file not found. Please copy .env.example to .env and configure it."
        )
        return

    logger.info("✅ Environment file found")

    # Demonstrate data collection
    logger.info("📊 Demonstrating data collection...")
    try:
        scraper = RedditScraper()

        # Collect a small sample from one subreddit
        demo_data = scraper.scrape_subreddit("askgaybros", limit=10)

        logger.info(f"✅ Collected {len(demo_data)} posts for demonstration")

        # Show basic statistics
        languages = {}
        health_related = 0

        for post in demo_data:
            lang = post.get("language", "unknown")
            languages[lang] = languages.get(lang, 0) + 1

            if post.get("is_health_related", False):
                health_related += 1

        logger.info(f"📈 Demo Statistics:")
        logger.info(f"   • Languages detected: {list(languages.keys())}")
        logger.info(f"   • Health-related posts: {health_related}/{len(demo_data)}")

    except Exception as e:
        logger.error(f"❌ Data collection failed: {e}")
        logger.info("💡 Tip: Check your Reddit API credentials in .env file")
        return

    # Demonstrate network analysis capabilities
    logger.info("🌐 Demonstrating network analysis...")
    try:
        analyzer = NetworkAnalyzer()

        # Try to build a user network from database
        # (This might fail if database is not set up, which is expected)
        try:
            network_data = analyzer.build_user_network()
            if network_data and network_data.get("nodes"):
                logger.info(
                    f"✅ Network analysis: {len(network_data['nodes'])} community members found"
                )
            else:
                logger.info(
                    "ℹ️ No database network data available (database not set up)"
                )
        except Exception:
            logger.info(
                "ℹ️ Database network analysis not available (expected for quick demo)"
            )

    except Exception as e:
        logger.warning(f"⚠️ Network analysis demonstration limited: {e}")

    logger.info("🎉 Quick demo completed successfully!")
    logger.info("🔗 Next steps:")
    logger.info("   • Set up PostgreSQL database for full functionality")
    logger.info("   • Try: python main.py demo --limit 50")
    logger.info("   • Try: python main.py collect-multilingual")
    logger.info("   • Explore other examples in examples/ directory")


if __name__ == "__main__":
    main()
