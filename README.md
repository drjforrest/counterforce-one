# Counterforce-One: Health Misinformation Detection & Community Resilience Platform

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: Academic](https://img.shields.io/badge/License-Academic-green.svg)](https://opensource.org/licenses/MIT)
[![Research Ethics](https://img.shields.io/badge/Ethics-Public%20Data%20Research-orange.svg)](docs/ethics.md)

A comprehensive platform for detecting health misinformation and analyzing community resilience patterns within immigrant communities on Reddit. This research tool combines advanced natural language processing, social network analysis, and human-validated machine learning to understand how health information spreads in multilingual online communities.

## 🔬 What Makes Counterforce-One Unique

Unlike traditional misinformation detection systems that focus solely on identifying false content, **Counterforce-One takes a community-centered approach that prioritizes resilience and empowerment**. Our platform uniquely combines real-time multilingual analysis with community network modeling to understand not just what misinformation exists, but how communities naturally develop resistance and correction mechanisms. By analyzing support patterns, cross-cultural health information sharing, and community-driven fact-checking behaviors, Counterforce-One reveals the inherent strength within immigrant communities rather than just their vulnerabilities. This paradigm shift from deficit-based to asset-based research creates actionable insights that communities can use to strengthen their own information ecosystems, making it both a research tool and a platform for community empowerment.

## 🌟 Key Features

- **Multilingual Data Collection**: Automated scraping with support for 5+ languages
- **Real-time Translation**: Integrated Google Translate API for cross-language analysis
- **Community Network Analysis**: Social graph construction and resilience modeling
- **Interactive Annotation Tools**: Web-based interfaces for human validation
- **Vector Similarity Search**: PostgreSQL with pgvector for semantic analysis
- **Research Dashboard**: Comprehensive analytics and visualization suite
- **Ethics-First Design**: Built-in anonymization and privacy protection

## 🚀 Quick Start

### Prerequisites
- Python 3.12+ (recommended)
- PostgreSQL 15+ with pgvector extension
- Reddit API credentials
- Google Translate API key (optional)

### Installation

1. **Clone and setup environment:**
   ```bash
   git clone <repository-url>
   cd misinformation_gay_mens_Health
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your API credentials (see setup guide below)
   ```

3. **Initialize database:**
   ```bash
   ./tools/init_database.sh
   alembic upgrade head
   ```

4. **Run demo:**
   ```bash
   python main.py demo --limit 50
   ```

### API Setup Guide

#### Reddit API Setup
1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
2. Create new application (script type)
3. Copy credentials to `.env`:
   ```bash
   REDDIT_CLIENT_ID=your_client_id
   REDDIT_CLIENT_SECRET=your_client_secret
   REDDIT_USER_AGENT="Academic Research Tool v1.0"
   ```

#### Google Translate API (Optional)
1. Enable Google Translate API in Google Cloud Console
2. Create service account and download credentials
3. Add to `.env`:
   ```bash
   GOOGLE_TRANSLATE_CREDENTIALS_PATH=path/to/credentials.json
   ```

## 📁 Project Structure

```
misinformation_gay_mens_Health/
├── 🎯 main.py                    # Main CLI interface
├── 📦 requirements.txt           # Dependencies
├── ⚙️  config/                   # Configuration management
├── 🔧 src/                       # Core application modules
│   ├── reddit_scraper.py         # Data collection engine
│   ├── multilingual_scraper.py   # Multi-language support
│   ├── network_analysis.py       # Community analysis
│   ├── translation_service.py    # Translation pipeline
│   └── database_models.py        # Data persistence
├── 🌐 gradio_app/               # Web interfaces
│   ├── annotation_interface.py   # Annotation tool
│   ├── analytics_dashboard.py    # Research dashboard
│   └── community_resilience.py   # Network visualization
├── 🔬 examples/                 # Demonstration scripts
├── 🛠️  tools/                   # Utility scripts
├── 📊 scripts/analysis/         # Analysis workflows
├── 📚 docs/                     # Documentation
├── 🧪 tests/                    # Test suite
└── 📁 data/                     # Data storage
    ├── raw/                     # Original collected data
    ├── processed/               # Cleaned and analyzed data
    └── exports/                 # Research outputs
```

## 💼 Usage Examples

### Data Collection Workflows

```bash
# Basic data collection (file-based)
python main.py collect

# Database-persistent collection with multilingual support
python main.py collect-multilingual-db

# Translate health keywords for multilingual analysis
python main.py translate-keywords

# Quick demo with visualization
python main.py demo --limit 100
```

### Analysis and Annotation

```bash
# Launch research annotation interface
python main.py annotate-enhanced --limit 200 --subreddit askgaybros

# Community network analysis
python main.py analyze

# Generate research visualizations
python main.py visualize --data-path data/processed/study_data.json
```

### Research Dashboard Tools

```bash
# Launch comprehensive analytics dashboard
python tools/launch_research_analytics.py

# Community resilience visualization
python tools/launch_community_resilience.py

# Real-time annotation interface
python tools/launch_research_annotation.py
```

## 🎯 Research Focus Areas

### Target Communities
- **LGBTQ+ Health**: r/askgaybros, r/gay_irl, r/gaybros
- **Canadian Immigration**: r/toronto, r/vancouver, r/askTO
- **Newcomer Support**: r/NewToCanada, r/ImmigrationCanada

### Health Keywords Monitored
- **Clinical Terms**: HIV, PrEP, ARVs, syphilis, PEP, chlamydia, gonorrhoea
- **Colloquial Terms**: "the clap", "burning", Truvada, Descovy
- **Wellness Topics**: Mental health, healthcare access, community support

### Supported Languages
- English (primary)
- Tagalog, Mandarin/Cantonese, Punjabi, Spanish
- Extensible framework for additional languages

## 🔬 Research Methodology

### Data Collection Pipeline
1. **Automated Scraping**: Multi-subreddit data collection with rate limiting
2. **Language Detection**: Automatic identification of post languages
3. **Translation Services**: Real-time translation for cross-language analysis
4. **Content Classification**: ML-based health content identification
5. **Network Construction**: User interaction mapping and community detection

### Analysis Framework
- **Community Resilience Modeling**: Network-based resilience metrics
- **Misinformation Detection**: Multi-modal classification approach
- **Support Pattern Analysis**: Community help-seeking behavior
- **Cross-Cultural Analysis**: Comparative health information sharing

## 📊 Sample Research Outputs

The platform generates comprehensive research visualizations:
- **Community Network Maps**: Interactive social graphs
- **Language Distribution Analysis**: Multilingual content patterns
- **Temporal Health Trends**: Time-series analysis of health discussions
- **Support Network Visualization**: Community resilience indicators

*View examples in `data/exports/` and `demo_visualizations/`*

## 🛡️ Research Ethics & Privacy

This project follows ethical research principles for publicly available data:

- 📊 **Public Data Only**: Research uses publicly posted content on Reddit
- 🔐 **Data Anonymization**: All personal identifiers removed or hashed
- 🚫 **No Personal Data**: No collection of private or identifying information
- 📜 **Platform Compliance**: Full Reddit Terms of Service adherence
- 🔒 **Secure Handling**: Responsible data storage and access practices
- 📋 **Ethics Review Planned**: IRB/REB submission planned pending funding confirmation

For detailed ethics framework, see [docs/ethics.md](docs/ethics.md)

## 🧪 Testing & Quality Assurance

```bash
# Run test suite
python -m pytest tests/

# Check code quality
ruff check src/ tests/
black --check src/ tests/

# Validate data collection
python scripts/analysis/test_improvements.py
```

## 📈 Performance Optimization

- **Database Indexing**: Optimized PostgreSQL queries with vector indices
- **Concurrent Processing**: Multi-threaded data collection and analysis
- **Caching Layer**: Redis integration for frequently accessed data
- **Memory Management**: Efficient large dataset processing

## 🤝 Contributing

This is an active academic research project. Collaboration opportunities:

- **Research Partnerships**: Cross-institutional studies
- **Technical Contributions**: Algorithm improvements and optimizations
- **Ethical Review**: Privacy and ethics framework enhancement
- **Community Validation**: Cultural competency and community feedback

Contact the research team for collaboration inquiries.

## 📚 Documentation

- [Installation Guide](docs/installation.md)
- [API Reference](docs/api/)
- [Research Methodology](docs/methodology.md)
- [Ethics Framework](docs/ethics.md)
- [Contributing Guidelines](docs/contributing.md)

## 📄 Citation

If you use this platform in your research, please cite:

```bibtex
@software{health_misinformation_platform,
  title={Health Misinformation Detection \& Community Resilience Platform},
  author={[Research Team]},
  year={2024},
  url={https://github.com/[repository]},
  note={Academic Research Tool for Community Health Analysis}
}
```

## 📞 Support

- **Technical Issues**: Open GitHub issue with detailed description
- **Research Inquiries**: Contact research team lead
- **Ethics Questions**: Reach out to IRB liaison
- **Community Feedback**: We welcome input from studied communities

---

*This platform is designed for academic research purposes with a focus on community health and resilience. All research conducted follows institutional ethics guidelines and community-centered principles.*
