# Quick Start Guide

Get up and running with Counterforce-One in under 5 minutes!

## Prerequisites

- Python 3.12+
- Git
- PostgreSQL 15+ (optional for basic features)

## Installation

### 1. Clone and Setup

```bash
git clone <your-repository-url>
cd misinformation_gay_mens_Health
./setup.sh
```

The setup script will:
- ✅ Check Python version
- 📦 Create virtual environment
- 🔧 Install dependencies
- ⚙️ Create `.env` file template

### 2. Configure API Credentials

Edit your `.env` file with Reddit API credentials:

```bash
# Required: Reddit API
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_secret_here
REDDIT_USER_AGENT="CounterforceOne/1.0 by YourUsername"

# Optional: Database (for full features)
DATABASE_URL=postgresql://user:pass@localhost:5432/counterforce_db
```

!!! tip "Getting Reddit API Credentials"
    1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
    2. Create a "script" application
    3. Copy the client ID and secret to your `.env` file

### 3. Quick Test

Run a quick demo to verify everything works:

```bash
# Activate virtual environment
source venv/bin/activate

# Run demo collection
python main.py demo --limit 20
```

Expected output:
```
🤝 Community Resilience Demo Results:
   • Total community posts collected: 20
   • Languages in community discussions: ['en']
   • Posts supporting newcomers: 3
   • Community data saved to: data/demo_data_20250101_120000.json
```

## Core Commands

### Data Collection

```bash
# Basic file-based collection
python main.py collect

# Database collection with multilingual support
python main.py collect-multilingual-db

# Generate keyword translations
python main.py translate-keywords
```

### Analysis Tools

```bash
# Community network analysis
python main.py analyze

# Launch annotation interface
python main.py annotate-enhanced --limit 100

# Generate visualizations
python main.py visualize --data-path data/demo_data_*.json
```

### Research Dashboards

```bash
# Comprehensive analytics dashboard
python tools/launch_research_analytics.py

# Community resilience visualization
python tools/launch_community_resilience.py

# Real-time annotation interface  
python tools/launch_research_annotation.py
```

## Example Workflow

Here's a complete research workflow:

```bash
# 1. Collect multilingual data
python main.py collect-multilingual-db

# 2. Analyze community networks
python main.py analyze

# 3. Launch annotation interface
python main.py annotate-enhanced --limit 200

# 4. Generate research visualizations
python main.py visualize --data-path data/processed/study_data.json

# 5. Launch analytics dashboard
python tools/launch_research_analytics.py
```

## Troubleshooting

### Common Issues

!!! warning "Reddit API Rate Limits"
    If you get rate limit errors, your user agent may be too generic. Make it more specific and unique.

!!! info "Database Connection Errors"
    Database features are optional. You can use file-based collection without PostgreSQL.

!!! tip "Translation Service Errors"
    Google Translate integration is optional. The platform works without it for English-only analysis.

### Getting Help

- Check the [Configuration Guide](configuration.md) for detailed setup
- Review [example scripts](examples/basic-usage.md) for usage patterns
- See [troubleshooting guides](guides/troubleshooting.md) for common issues

## Next Steps

Now that you have Counterforce-One running:

1. **Explore the Data**: Try different subreddit collections and analysis tools
2. **Set up Database**: Install PostgreSQL for full network analysis features  
3. **Research Workflow**: Follow our [research methodology](research/methodology.md)
4. **Community Analysis**: Use the platform to study community resilience patterns

🎉 **Welcome to Counterforce-One! Start exploring community resilience patterns in health misinformation.**