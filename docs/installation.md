# Installation Guide

This guide helps you set up the project locally.

## Prerequisites
- Python 3.12+
- PostgreSQL 15+ with pgvector
- Reddit API credentials

## Setup Steps
1. Clone repo and create virtualenv
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill in credentials
4. Initialize database: `./tools/init_database.sh && alembic upgrade head`
5. Run a quick demo: `python main.py demo --limit 50`