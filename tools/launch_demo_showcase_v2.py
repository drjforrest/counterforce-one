#!/usr/bin/env python3
"""
Counterforce-One Demo Showcase - Streamlined Version
Fast-loading interactive demo for stakeholder feedback
"""

import os
import sys
import json
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import gradio as gr
import pandas as pd

# Paths
VIZ_DIR = project_root / "data" / "demo_visualizations"
HIGHLIGHT_DIR = project_root / "data" / "demo_highlight_reel"


# Load data once at startup
with open(VIZ_DIR / "dataset_stats.json", 'r') as f:
    STATS = json.load(f)

with open(VIZ_DIR / "post_summaries.json", 'r') as f:
    POSTS = json.load(f)


def create_overview():
    """Dataset overview"""
    return f"""
# 🛡️ Counterforce-One: Community Resilience Research

### Understanding how online communities respond to health misinformation

---

## 📊 Dataset at a Glance

| Metric | Count |
|--------|-------|
| **Reddit Posts** | {STATS['total_posts']:,} |
| **Comments Analyzed** | {STATS['total_comments']:,} |
| **Communities** | {STATS['subreddits']} |
| **Languages** | {STATS['languages']} |

---

## 🎯 Research Focus

**Primary Questions:**
1. How do communities self-correct health misinformation?
2. Who are the knowledge brokers providing accurate info?
3. What peer support patterns emerge?

**Communities Studied:**
- LGBTQ+ health (r/gaybros, r/askgaybros) - HIV/PrEP discussions
- Canadian immigration (r/ImmigrationCanada, r/toronto)
- Multi-lingual health content

---

## 🔬 Key Innovation

This research uses **network analysis** to visualize how health information flows through online communities, identifying both misinformation patterns and community resilience mechanisms.
"""


def create_post_card(post_idx):
    """Display one post's analysis"""
    post = POSTS[post_idx]

    severity_emoji = {1: "🟢", 2: "🟡", 3: "🟠", 4: "🔴", 5: "🔴🔴"}
    emoji = severity_emoji.get(post['severity'], "⚪")

    accuracy_emoji = {
        "accurate": "✅",
        "partially_accurate": "⚠️",
        "inaccurate": "❌",
        "not_applicable": "➖"
    }
    acc_emoji = accuracy_emoji.get(post['accuracy_label'], "")

    return f"""
## {post['title']}

**Post ID:** `{post['post_id']}`
**Engagement:** {post['score']:,} upvotes, {post['comments']} comments

---

### 📋 Annotation Results

| Dimension | Assessment |
|-----------|------------|
| **Type** | {post['annotation_type']} |
| **Accuracy** | {acc_emoji} {post['accuracy_label']} |
| **Severity** | {emoji} {post['severity']}/5 |
| **Community Response** | {post['community_response']} |

---

### 💡 Analysis Notes

{post['notes']}

---

### 🕸️ Network Visualization

[View Interactive Network Graph →](../data/demo_visualizations/network_{post['post_id']}.html)

This network shows comment reply relationships. Nodes = users, edges = replies.
"""


def create_methodology():
    """Research methods"""
    return """
## 🔬 Methodology

### Data Collection Pipeline

```
Reddit API → PostgreSQL + pgvector → Classification → Network Analysis → Annotation
```

**Technologies:**
- Python (PRAW, NetworkX, sentence-transformers)
- PostgreSQL with pgvector for semantic search
- Gradio for interactive interfaces

### Analysis Approach

1. **Automated Classification**
   - LGBTQ+ content detection
   - Health misinformation scoring
   - Language identification

2. **Network Analysis**
   - User interaction graphs
   - Centrality metrics (knowledge brokers)
   - Community detection algorithms

3. **Human Annotation** (Ground Truth)
   - 4 key posts fully annotated
   - Accuracy labeling
   - Severity assessment
   - Community response coding

### Ethical Considerations

- Public data only (Reddit posts/comments)
- De-identified analysis
- Focus on community resilience (not surveillance)
- Aiming for defensivesecurity research ethics approval
"""


def create_findings():
    """Key insights"""
    return """
## 💡 Preliminary Findings

### 1. ✅ Communities Self-Correct Effectively

Even posts with 2,000+ upvotes get constructive criticism:
- **"U=U" post**: Accurate science, but top comment adds trust/adherence nuance
- Pattern: Community adds protective context to health claims

### 2. ⚠️ Subtle Misinformation is Trickier

The "HIV is life altering" post demonstrates the challenge:
- Contains real science with legitimate citations
- But: Alarmist framing suggests treatment failure
- Mixed community response - hard to debunk "partially true" claims

### 3. ❤️ Peer Support Networks Are Powerful

"Recently diagnosed" post shows:
- 30+ year HIV survivors mentoring newly diagnosed
- Practical advice + emotional support combined
- Knowledge flows naturally through community

### 4. 📚 Knowledge Gaps Persist

PrEP/condoms discussion reveals:
- Some don't know PrEP only prevents HIV (not other STIs)
- Community self-educates about drug-resistant gonorrhea
- Ongoing health literacy need

---

## 🎯 Research Impact

**For Public Health:**
- Understand natural health information diffusion
- Identify community educators for partnership
- Design interventions aligned with community norms

**For Platform Design:**
- Early misinformation detection signals
- Amplify peer education features
- Support community resilience mechanisms
"""


def launch_showcase():
    """Create and launch showcase"""

    with gr.Blocks(
        title="Counterforce-One Demo",
        theme=gr.themes.Soft()
    ) as demo:

        gr.Markdown(create_overview())

        gr.Markdown("---")
        gr.Markdown("## 📊 Subreddit Distribution")
        gr.HTML(f'<iframe src="file://{VIZ_DIR}/subreddit_distribution.html" width="100%" height="500px"></iframe>')

        gr.Markdown("---")
        gr.Markdown("## 🔍 Featured Case Studies")

        post_selector = gr.Radio(
            choices=[
                f"Post {i+1}: {POSTS[i]['title'][:60]}..."
                for i in range(len(POSTS))
            ],
            label="Select a post to explore",
            value=f"Post 1: {POSTS[0]['title'][:60]}..."
        )

        post_display = gr.Markdown(create_post_card(0))

        def update_post(selection):
            idx = int(selection.split("Post ")[1].split(":")[0]) - 1
            return create_post_card(idx)

        post_selector.change(update_post, inputs=[post_selector], outputs=[post_display])

        gr.Markdown("---")
        gr.Markdown(create_methodology())

        gr.Markdown("---")
        gr.Markdown(create_findings())

        gr.Markdown("""
---

## 🚀 Next Steps

**Short Term:**
- Annotate 20-30 posts for robust ground truth
- Train ML classifier
- Expand network analysis to all top 30 posts

**Medium Term:**
- Temporal analysis (misinformation spread over time)
- Knowledge broker identification at scale
- Intervention design recommendations

**Long Term:**
- Cross-platform comparison
- Real-time misinformation early warning system
- Public health partnership

---

## 💬 Share Your Feedback!

**What would help?**
- More visualizations?
- Different analysis angles?
- Specific research questions to explore?

---

<div style="text-align: center; padding: 30px; background: #f8f9fa; border-radius: 10px; margin-top: 50px;">
    <h3>🛡️ Counterforce-One</h3>
    <p>Community Resilience to Health Misinformation</p>
    <p style="font-size: 0.9em; color: #666;">
        Built with Python • PostgreSQL • NetworkX • Gradio<br>
        October 2025
    </p>
</div>
""")

    return demo


def main():
    print("=" * 70)
    print("🛡️  Counterforce-One Demo Showcase")
    print("=" * 70)
    print()
    print("🌐 Starting web server...")
    print()
    print(f"📊 Loaded {len(POSTS)} annotated posts")
    print(f"🕸️  Generated {len(list(VIZ_DIR.glob('network_*.html')))} network visualizations")
    print()
    print("🔗 Access at: http://localhost:7860")
    print("📤 Set share=True to get public link for remote feedback")
    print()

    demo = launch_showcase()
    demo.launch(
        server_port=7860,
        share=False,  # Change to True for public sharing link
        show_error=True
    )


if __name__ == "__main__":
    main()
