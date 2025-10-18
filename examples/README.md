# Examples Directory

This directory contains demonstration scripts showing how to use the platform.

## Available Examples

### 1. Quick Start Demo
```bash
python examples/quick_demo.py
```
Basic demonstration of data collection and analysis.

### 2. Multilingual Collection Demo
```bash
python examples/multilingual_demo.py
```
Shows multilingual data collection with translation.

### 3. Community Analysis Demo
```bash
python examples/community_analysis_demo.py
```
Demonstrates network analysis and community resilience metrics.

### 4. Research Workflow Demo
```bash
python examples/research_workflow_demo.py
```
End-to-end research workflow from collection to visualization.

## Legacy Examples

The following scripts are legacy demonstrations from development:
- `proof_of_concept.py` - Original proof of concept
- `real_data_research_demo.py` - Research data demonstration
- `simple_real_data_demo.py` - Simplified research demo
- `run_multilingual_collection.py` - Multilingual collection script

## Prerequisites

All examples require:
- Valid Reddit API credentials in `.env` file
- Python dependencies installed (`pip install -r requirements.txt`)
- PostgreSQL database set up (for database-enabled examples)

## Sample Data

Some examples may create sample data in `data/examples/` for testing purposes.