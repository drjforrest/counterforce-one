#!/usr/bin/env python3
"""
Generate all visualizations needed for the demo showcase website
Creates network graphs, statistics, and visual assets
"""

import os
import sys
import json
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pandas as pd
import networkx as nx
import plotly.graph_objects as go
import plotly.express as px
from loguru import logger
from src.data_persistence import DataPersistenceManager
from src.database_models import RedditPost, RedditComment

# Output directory for visualizations
OUTPUT_DIR = project_root / "data" / "demo_visualizations"
OUTPUT_DIR.mkdir(exist_ok=True)

KEY_POSTS = ['1ls1tyz', '1lyphrb', '1la8c64', '1lhs70z']


def create_comment_network_visualization(post_id: str, post_title: str, db_manager) -> str:
    """Create network visualization for a single post's comment threads"""
    logger.info(f"Creating network for post: {post_id}")

    with db_manager.get_session() as session:
        # Get comments for this post
        comments = session.query(RedditComment).filter(
            RedditComment.post_id == post_id
        ).all()

        if not comments:
            logger.warning(f"No comments found for post {post_id}")
            return None

        # Build network
        G = nx.DiGraph()

        # Add post as root node
        G.add_node("POST", type="post", label=f"Post: {post_title[:50]}...")

        # Build comment graph
        comment_lookup = {}
        for comment in comments:
            if comment.author and comment.author != "[deleted]":
                node_id = comment.comment_id
                G.add_node(
                    node_id,
                    type="comment",
                    author=comment.author,
                    score=comment.score or 0,
                    label=comment.body[:100] if comment.body else ""
                )
                comment_lookup[comment.comment_id] = comment

                # Add edge from parent
                if comment.parent_id:
                    if comment.parent_id.startswith('t3_'):  # Reply to post
                        G.add_edge("POST", node_id)
                    elif comment.parent_id.startswith('t1_'):  # Reply to comment
                        parent_id = comment.parent_id[3:]  # Remove t1_ prefix
                        if parent_id in comment_lookup:
                            G.add_edge(parent_id, node_id)

        logger.info(f"Network has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")

        # Calculate layout
        pos = nx.spring_layout(G, k=2, iterations=50)

        # Create plotly figure
        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines'
        )

        # Node traces
        node_x = []
        node_y = []
        node_text = []
        node_size = []
        node_color = []

        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)

            if node == "POST":
                node_text.append(f"Original Post<br>{post_title[:80]}")
                node_size.append(30)
                node_color.append('#ff4444')
            else:
                node_data = G.nodes[node]
                score = node_data.get('score', 0)
                author = node_data.get('author', 'unknown')
                label = node_data.get('label', '')[:80]
                node_text.append(f"Author: {author}<br>Score: {score}<br>{label}...")
                node_size.append(10 + min(max(score, 0) * 2, 20))  # Size by score (min 0)
                node_color.append('#4477ff')

        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            text=node_text,
            marker=dict(
                size=node_size,
                color=node_color,
                line=dict(width=1, color='white')
            )
        )

        # Create figure
        fig = go.Figure(
            data=[edge_trace, node_trace],
            layout=go.Layout(
                title=dict(text=f"Comment Network: {post_title[:60]}...", font=dict(size=16)),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20, l=5, r=5, t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                plot_bgcolor='white',
                height=600
            )
        )

        # Save
        output_path = OUTPUT_DIR / f"network_{post_id}.html"
        fig.write_html(str(output_path))
        logger.success(f"Saved network visualization to {output_path}")

        # Also save as JSON for embed
        fig.write_json(str(OUTPUT_DIR / f"network_{post_id}.json"))

        return str(output_path)


def create_dataset_overview():
    """Create overview statistics visualization"""
    logger.info("Creating dataset overview")

    db_manager = DataPersistenceManager()

    with db_manager.get_session() as session:
        posts = session.query(RedditPost).all()
        comments = session.query(RedditComment).all()

        # Statistics
        stats = {
            "total_posts": len(posts),
            "total_comments": len(comments),
            "subreddits": len(set(p.subreddit for p in posts if p.subreddit)),
            "languages": len(set(p.language for p in posts if p.language)),
        }

        # Top subreddits
        subreddit_counts = pd.DataFrame([
            {"subreddit": p.subreddit} for p in posts if p.subreddit
        ])
        top_subreddits = subreddit_counts['subreddit'].value_counts().head(10)

        # Create bar chart
        fig = go.Figure(data=[
            go.Bar(
                x=top_subreddits.index,
                y=top_subreddits.values,
                marker_color='#4477ff'
            )
        ])

        fig.update_layout(
            title="Top 10 Subreddits by Post Count",
            xaxis_title="Subreddit",
            yaxis_title="Number of Posts",
            plot_bgcolor='white',
            height=400
        )

        fig.write_html(str(OUTPUT_DIR / "subreddit_distribution.html"))

        # Save stats as JSON
        with open(OUTPUT_DIR / "dataset_stats.json", 'w') as f:
            json.dump(stats, f, indent=2)

        logger.success(f"Dataset statistics: {stats}")
        return stats


def create_post_summary_cards():
    """Create summary data for the 4 key posts"""
    logger.info("Creating post summary cards")

    db_manager = DataPersistenceManager()
    annotations_df = pd.read_csv(project_root / "data/demo_highlight_reel/annotation_template_RECOMMENDED.csv")

    summaries = []

    with db_manager.get_session() as session:
        for post_id in KEY_POSTS:
            post = session.query(RedditPost).filter(RedditPost.post_id == post_id).first()
            comments_count = session.query(RedditComment).filter(
                RedditComment.post_id == post_id
            ).count()

            annotation = annotations_df[annotations_df['post_id'] == post_id].iloc[0]

            summary = {
                "post_id": post_id,
                "title": post.title if post else "Unknown",
                "score": int(post.score) if post and post.score else 0,
                "comments": int(comments_count),
                "annotation_type": str(annotation['annotation_type']),
                "accuracy_label": str(annotation['accuracy_label']),
                "severity": int(annotation['severity']),
                "community_response": str(annotation['community_response']),
                "notes": str(annotation['notes'])
            }
            summaries.append(summary)

    # Save as JSON
    with open(OUTPUT_DIR / "post_summaries.json", 'w') as f:
        json.dump(summaries, f, indent=2)

    logger.success(f"Created {len(summaries)} post summaries")
    return summaries


def main():
    """Generate all demo visualizations"""
    print("=" * 70)
    print("🎨 Generating Demo Visualizations")
    print("=" * 70)
    print()

    db_manager = DataPersistenceManager()

    print("📊 Step 1: Dataset Overview")
    stats = create_dataset_overview()
    print(f"  ✓ Total posts: {stats['total_posts']}")
    print(f"  ✓ Total comments: {stats['total_comments']}")
    print(f"  ✓ Subreddits: {stats['subreddits']}")
    print()

    print("📝 Step 2: Post Summary Cards")
    summaries = create_post_summary_cards()
    print(f"  ✓ Created summaries for {len(summaries)} posts")
    print()

    print("🕸️  Step 3: Network Visualizations")
    with db_manager.get_session() as session:
        for post_id in KEY_POSTS:
            post = session.query(RedditPost).filter(RedditPost.post_id == post_id).first()
            if post:
                result = create_comment_network_visualization(post_id, post.title, db_manager)
                if result:
                    print(f"  ✓ {post.title[:50]}...")

    print()
    print("=" * 70)
    print("✅ Visualization Generation Complete!")
    print("=" * 70)
    print()
    print(f"📁 Output directory: {OUTPUT_DIR}")
    print()
    print("Generated files:")
    for file in OUTPUT_DIR.glob("*"):
        print(f"  • {file.name}")
    print()
    print("🚀 Ready to build showcase website!")


if __name__ == "__main__":
    main()
