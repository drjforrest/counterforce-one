#!/bin/bash

# Deploy MkDocs to GitHub Pages
# This script builds and deploys the documentation to the gh-pages branch

echo "🚀 Deploying Counterforce-One Documentation to GitHub Pages..."

# Check if we're in a git repository
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "❌ Error: Not in a git repository"
    exit 1
fi

# Check if main/master branch
current_branch=$(git branch --show-current)
if [[ "$current_branch" != "main" && "$current_branch" != "master" ]]; then
    echo "⚠️  Warning: You're not on main/master branch. Current: $current_branch"
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Deployment cancelled."
        exit 1
    fi
fi

# Install MkDocs if not available
if ! command -v mkdocs &> /dev/null; then
    echo "📦 Installing MkDocs dependencies..."
    pip install mkdocs mkdocs-material mkdocstrings[python] mkdocs-gen-files mkdocs-literate-nav
fi

# Commit any changes first
if [[ -n $(git status --porcelain) ]]; then
    echo "📝 You have uncommitted changes. Please commit them first:"
    git status --short
    exit 1
fi

# Deploy to GitHub Pages
echo "🔨 Building and deploying documentation..."
mkdocs gh-deploy --clean --message "Deploy documentation for commit {sha}"

echo "✅ Documentation deployed successfully!"
echo "🌐 Your site will be available at: https://[your-username].github.io/[your-repo-name]"
echo ""
echo "Note: It may take a few minutes for GitHub Pages to update."