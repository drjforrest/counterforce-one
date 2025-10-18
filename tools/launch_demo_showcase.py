#!/usr/bin/env python3
"""
Launch the Counterforce-One Demo Showcase Website
Interactive demonstration of the research project for stakeholder feedback
"""

import json
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from loguru import logger

import gradio as gr
import pandas as pd

# Paths
VIZ_DIR = project_root / "data" / "demo_visualizations"
HIGHLIGHT_DIR = project_root / "data" / "demo_highlight_reel"


def load_project_data():
    """Load all project data for showcase"""
    # Load dataset stats
    with open(VIZ_DIR / "dataset_stats.json") as f:
        stats = json.load(f)

    # Load post summaries
    with open(VIZ_DIR / "post_summaries.json") as f:
        post_summaries = json.load(f)

    # Load annotations
    annotations_df = pd.read_csv(HIGHLIGHT_DIR / "annotation_template_RECOMMENDED.csv")

    return stats, post_summaries, annotations_df


def create_hero_section(stats):
    """Create hero/landing section"""
    return f"""
# 🛡️ Counterforce-One
## Community Resilience in Health Misinformation Research

**A computational social science project analyzing how online communities respond to health misinformation**

---

### 📊 Dataset Overview

<div style="display: flex; justify-content: space-around; text-align: center; margin: 30px 0;">
    <div>
        <h2 style="color: #4477ff; margin: 0;">{stats['total_posts']:,}</h2>
        <p>Reddit Posts</p>
    </div>
    <div>
        <h2 style="color: #4477ff; margin: 0;">{stats['total_comments']:,}</h2>
        <p>Comments Analyzed</p>
    </div>
    <div>
        <h2 style="color: #4477ff; margin: 0;">{stats['subreddits']}</h2>
        <p>Communities</p>
    </div>
    <div>
        <h2 style="color: #4477ff; margin: 0;">{stats['languages']}</h2>
        <p>Languages</p>
    </div>
</div>

---

### 🎯 Research Questions

1. **How do online communities self-correct health misinformation?**
2. **Who are the "knowledge brokers" providing accurate health information?**
3. **What patterns of peer support emerge in vulnerable communities?**
4. **Can we detect misinformation early through network analysis?**

---

### 🔬 Focus Communities

- **LGBTQ+ Health:** r/gaybros, r/askgaybros, r/lgbt (HIV/PrEP discussions)
- **Canadian Immigration:** r/ImmigrationCanada, r/toronto (newcomer health)
- **Multilingual Support:** English, French, Tagalog, Spanish content
"""


def create_post_card(post):
    """Create formatted card for a key post"""
    severity_colors = {1: "green", 2: "yellow", 3: "orange", 4: "red", 5: "darkred"}
    severity_color = severity_colors.get(post["severity"], "gray")

    accuracy_emoji = {
        "accurate": "✅",
        "partially_accurate": "⚠️",
        "inaccurate": "❌",
        "not_applicable": "➖",
    }
    emoji = accuracy_emoji.get(post["accuracy_label"], "")

    return f"""
### {emoji} {post['title']}

**Post ID:** `{post['post_id']}` | **Score:** {post['score']:,} upvotes | **Comments:** {post['comments']}

**Type:** {post['annotation_type']}
**Accuracy:** {post['accuracy_label']}
**Severity:** <span style="color: {severity_color};">●</span> {post['severity']}/5
**Community Response:** {post['community_response']}

**Analysis Notes:**
> {post['notes']}

---
"""


def create_methodology_section():
    """Explain research methodology"""
    return """
## 🔬 Methodology

### Data Collection
- **Source:** Reddit API (PRAW)
- **Time Period:** 2024-2025
- **Selection Criteria:** Health-related discussions in target communities
- **Ethical Approval:** Public data, de-identified analysis

### Analysis Pipeline

1. **Scraping & Storage**
   - PostgreSQL database with pgvector extension
   - Multilingual content support
   - Vector embeddings for semantic search

2. **Content Classification**
   - LGBTQ+ content classifier
   - Health misinformation scorer
   - Language detection

3. **Network Analysis**
   - User interaction graphs
   - Community detection algorithms
   - Centrality metrics (knowledge brokers)

4. **Human Annotation**
   - Ground truth dataset (4 key posts)
   - Accuracy labeling
   - Severity assessment
   - Community response coding

### Technologies Used

- **Backend:** Python, PostgreSQL, pgvector
- **ML/NLP:** Transformers, sentence-transformers
- **Network Analysis:** NetworkX
- **Visualization:** Plotly, Gradio
- **Data Collection:** PRAW (Reddit API)
"""


def create_findings_section():
    """Highlight key findings"""
    return """
## 💡 Key Findings (Preliminary)

### 1. Community Self-Correction is Common

Even when misinformation is posted, communities often correct it organically:

- **Example:** The "U=U" post (2,268 upvotes) accurately describes HIV science, but the top comment (1,818 upvotes) adds important nuance about trust and adherence
- **Pattern:** High-quality information gets amplified, with community adding protective context

### 2. Subtle Misinformation is Harder to Combat

The "HIV is life altering" post shows how partially accurate information can be misleading:

- ✅ Contains real science (gut damage, lymphatic effects)
- ⚠️ Legitimate PubMed citations
- ❌ But: alarmist framing suggests treatment doesn't work well
- **Community Response:** Mixed - some validate lived experience, some question authenticity

### 3. Peer Support Networks Are Strong

The "recently diagnosed" post (523 upvotes, 68 comments) demonstrates:

- Overwhelmingly supportive responses
- Knowledge brokers (30+ year survivors) educate newly diagnosed
- Practical advice flows naturally
- Emotional support + accurate health info combined

### 4. Knowledge Gaps Persist

The PrEP/condoms discussion reveals:

- Some community members don't understand PrEP limitations (only prevents HIV, not other STIs)
- But: Community self-corrects with education about gonorrhea, other risks
- Demonstrates need for ongoing health education

---

## 🎯 Research Impact

### For Public Health
- Understand how health information spreads in online communities
- Identify influential community members for health promotion
- Design better interventions that work WITH community dynamics

### For Platform Design
- Detect misinformation patterns early
- Amplify accurate peer education
- Support community resilience features

### For Vulnerable Communities
- Document community strengths (not just vulnerabilities)
- Validate peer support as health resource
- Inform culturally competent health communication
"""


def create_demo_interface():
    """Create the main Gradio showcase interface"""
    logger.info("Building demo showcase interface")

    stats, post_summaries, annotations_df = load_project_data()

    with gr.Blocks(
        title="Counterforce-One Research Showcase",
        theme=gr.themes.Soft(),
        css="""
        .gradio-container {max-width: 1200px !important}
        h1 {color: #2c3e50;}
        h2 {color: #34495e; margin-top: 30px;}
        .post-card {background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 15px 0;}
        """,
    ) as demo:
        # Hero section
        gr.Markdown(create_hero_section(stats))

        # Dataset distribution
        gr.HTML("<h2>📈 Subreddit Distribution</h2>")
        gr.HTML(
            (VIZ_DIR / "subreddit_distribution.html").read_text(),
            label="Top Subreddits",
        )

        # Key posts section
        gr.Markdown("## 🔍 Featured Case Studies: 4 Key Posts")
        gr.Markdown(
            """
            These posts were carefully selected to demonstrate different types of health information challenges:

            1. **Accurate info with community nuance** (U=U)
            2. **Subtle misinformation** (HIV life altering)
            3. **Peer support** (recently diagnosed)
            4. **Knowledge gaps & education** (PrEP/condoms)
            """
        )

        # Tabs for each post
        with gr.Tabs():
            for post in post_summaries:
                with gr.Tab(
                    f"Post {post_summaries.index(post) + 1}: {post['title'][:50]}..."
                ):
                    gr.Markdown(create_post_card(post), elem_classes="post-card")

                    # Network visualization
                    gr.Markdown("### 🕸️ Comment Network Visualization")
                    gr.Markdown(
                        """
                        This network shows how users interact through comments:
                        - **Red node:** Original post
                        - **Blue nodes:** Comments (size = comment score)
                        - **Edges:** Reply relationships
                        """
                    )
                    network_path = VIZ_DIR / f"network_{post['post_id']}.html"
                    if network_path.exists():
                        gr.HTML(network_path.read_text(), label="Network Graph")

        # Methodology
        gr.Markdown(create_methodology_section())

        # Findings
        gr.Markdown(create_findings_section())

        # Next steps
        gr.Markdown(
            """
## 🚀 Next Steps

### Immediate (Next 2-4 Weeks)
- [ ] Annotate 20-30 posts for robust ground truth
- [ ] Train ML classifier on annotated data
- [ ] Expand network analysis to all 30 top posts
- [ ] Calculate inter-rater reliability

### Short Term (1-2 Months)
- [ ] Temporal analysis: how does misinformation spread over time?
- [ ] Knowledge broker analysis: who are the key educators?
- [ ] Intervention design: what community features reduce misinformation?

### Long Term (3-6 Months)
- [ ] Cross-platform comparison (Reddit vs other social media)
- [ ] Automated early warning system for misinformation
- [ ] Partnership with public health organizations
- [ ] Academic publication

---

## 💬 Feedback Welcome!

**What would you like to see?**
- More visualizations?
- Different analysis approaches?
- Specific research questions?
- Collaboration opportunities?

**Contact:** [Your contact info here]

---

<div style="text-align: center; margin-top: 50px; padding: 30px; background: #f0f0f0; border-radius: 10px;">
    <h3>🛡️ Counterforce-One</h3>
    <p><strong>Understanding Community Resilience to Health Misinformation</strong></p>
    <p style="font-size: 0.9em; color: #666;">
        Built with Python • PostgreSQL • NetworkX • Gradio<br>
        Generated: October 2025
    </p>
</div>
"""
        )

    return demo


def main():
    """Launch the showcase website"""
    print("=" * 70)
    print("🛡️  Launching Counterforce-One Demo Showcase")
    print("=" * 70)
    print()
    print("🌐 Opening interactive demo website...")
    print("📊 Featuring:")
    print("   • 4 annotated case studies")
    print("   • Network visualizations")
    print("   • Dataset statistics")
    print("   • Research methodology")
    print("   • Key findings")
    print()
    print("🔗 The website will open at: http://localhost:7860")
    print("📤 Share this link for feedback!")
    print()

    demo = create_demo_interface()
    demo.launch(
        server_name="0.0.0.0",  # Allow external access
        server_port=7860,
        share=False,  # Set to True to get public link for sharing
        show_error=True,
    )


if __name__ == "__main__":
    main()
