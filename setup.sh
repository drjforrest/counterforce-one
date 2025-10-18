#!/bin/bash
set -e

echo "🚀 Setting up Health Misinformation Detection Platform..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
if [[ "$python_version" < "3.12" ]]; then
    echo "❌ Python 3.12+ is required. Found version: $python_version"
    exit 1
fi
echo "✅ Python version check passed: $python_version"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install --upgrade pip
pip install -e .

# Install development dependencies
echo "🛠️ Installing development dependencies..."
pip install -e ".[dev]"

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "⚙️ Creating .env file..."
    cp .env.example .env
    echo "📝 Please edit .env file with your API credentials"
fi

# Create necessary directories
echo "📁 Creating data directories..."
mkdir -p data/{raw,processed,exports}
mkdir -p logs

# Check PostgreSQL connection (optional)
echo "🗄️ Checking PostgreSQL connection..."
if command -v psql >/dev/null 2>&1; then
    echo "✅ PostgreSQL client found"
else
    echo "⚠️ PostgreSQL client not found. Install PostgreSQL to use database features."
fi

echo "🎉 Setup complete! Next steps:"
echo "   1. Edit .env file with your Reddit API credentials"
echo "   2. Set up PostgreSQL database (optional but recommended)"
echo "   3. Run: source venv/bin/activate"
echo "   4. Run: python main.py demo --limit 50"