# Configuration Guide

This guide walks you through configuring the Health Misinformation Detection Platform for your research environment.

## Environment Setup

### 1. Create Environment File

Copy the example environment file and customize it:

```bash
cp .env.example .env
```

### 2. Reddit API Configuration

!!! info "Reddit API Setup"
    You'll need to create a Reddit application to get API credentials.

1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps)
2. Click "Create App" or "Create Another App"
3. Choose "script" as the application type
4. Fill in your application details

Add your credentials to `.env`:

```bash
# Reddit API Configuration
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT="MisinformationResearch/1.0 by YourUsername"
```

### 3. Database Configuration

!!! warning "Database Required"
    PostgreSQL with pgvector extension is required for full functionality.

```bash
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/misinformation_db
```

### 4. Translation Services (Optional)

For multilingual analysis, configure Google Translate:

```bash
# API Keys for Translation Services
GOOGLE_TRANSLATE_API_KEY=your_google_translate_api_key
```

### 5. Application Settings

Customize application behavior:

```bash
# Gradio Configuration
GRADIO_SHARE=False
GRADIO_PORT=7860

# Data Collection Settings
MAX_POSTS_PER_SUBREDDIT=1000
DATA_COLLECTION_INTERVAL_HOURS=24

# Analysis Settings
MIN_COMMENT_LENGTH=10
MAX_NETWORK_NODES=5000

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/misinformation_analysis.log
```

### 6. Vector Database Settings

```bash
# pgvector database settings
PGVECTOR_DIMENSION=384
EMBEDDING_MODEL=all-MiniLM-L6-v2

# Semantic analysis settings
SIMILARITY_THRESHOLD=0.7
CLUSTERING_MIN_POSTS=5
PROPAGATION_TIME_WINDOW_HOURS=72
```

## Database Setup

### PostgreSQL Installation

=== "macOS"

    ```bash
    # Using Homebrew
    brew install postgresql@15
    brew install pgvector
    ```

=== "Ubuntu/Debian"

    ```bash
    sudo apt update
    sudo apt install postgresql-15 postgresql-15-pgvector
    ```

=== "Docker"

    ```bash
    docker run --name postgres-pgvector \
      -e POSTGRES_PASSWORD=your_password \
      -e POSTGRES_DB=misinformation_db \
      -p 5432:5432 \
      -d pgvector/pgvector:pg15
    ```

### Database Initialization

1. **Create Database:**
   ```bash
   createdb misinformation_db
   ```

2. **Run Migrations:**
   ```bash
   alembic upgrade head
   ```

3. **Verify Setup:**
   ```bash
   python -c "from src.database_setup import test_connection; test_connection()"
   ```

## Configuration Validation

### Test Your Setup

```bash
# Test Reddit API connection
python -c "from src.reddit_scraper import RedditScraper; RedditScraper().test_connection()"

# Test database connection
python -c "from src.data_persistence import DataPersistenceManager; DataPersistenceManager().test_connection()"

# Test translation service (if configured)
python -c "from src.translation_service import TranslationService; TranslationService().test_connection()"
```

### Configuration Troubleshooting

!!! tip "Common Issues"
    - **Reddit API Rate Limits**: Ensure your user agent is descriptive and unique
    - **Database Connection**: Verify PostgreSQL service is running and credentials are correct
    - **Translation API**: Check Google Cloud credentials and API key validity
    - **Permissions**: Ensure the application has write access to data/ and logs/ directories

## Next Steps

With your configuration complete, you can:

1. [Run the quick start tutorial](quickstart.md)
2. [Explore data collection workflows](guides/data-collection.md)
3. [Set up annotation interfaces](guides/annotation.md)
