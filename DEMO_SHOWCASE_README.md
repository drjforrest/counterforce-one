# 🛡️ Counterforce-One Demo Showcase

## Quick Start

Your demo showcase website is ready! Here's how to launch it:

```bash
python tools/launch_demo_showcase_v2.py
```

Then open your browser to: **http://localhost:7860**

---

## What's Included

### ✅ Completed Setup

1. **Data Curation** ✓
   - 4 key posts selected and exported
   - 261 comments from key posts
   - 30 top posts by engagement (1,632 comments total)

2. **Ground Truth Annotations** ✓
   - All 4 posts fully annotated
   - Accuracy labels, severity scores, community response coded
   - Ready for ML training

3. **Network Visualizations** ✓
   - 4 interactive network graphs (one per key post)
   - Shows comment reply relationships
   - Node size = comment score
   - Location: `data/demo_visualizations/network_*.html`

4. **Showcase Website** ✓
   - Interactive Gradio interface
   - Dataset overview with stats
   - 4 case studies with annotations
   - Network visualizations
   - Methodology explanation
   - Key findings
   - Next steps roadmap

---

## File Locations

```
counterforce-one/
├── data/
│   ├── demo_highlight_reel/          # Curated dataset
│   │   ├── key_posts.csv              # 4 annotated posts
│   │   ├── key_comments.csv           # 261 comments
│   │   ├── top_posts_by_engagement.csv# Top 30 posts
│   │   ├── all_top_comments.csv       # 1,632 comments
│   │   ├── annotation_template_RECOMMENDED.csv  # Your annotations
│   │   ├── FULL_POST_CONTENT.md       # Full text review
│   │   ├── ANNOTATION_GUIDE.md        # Annotation instructions
│   │   └── README.md                  # Dataset documentation
│   │
│   └── demo_visualizations/           # Generated visualizations
│       ├── network_1ls1tyz.html       # U=U network
│       ├── network_1lyphrb.html       # HIV life altering network
│       ├── network_1la8c64.html       # Recently diagnosed network
│       ├── network_1lhs70z.html       # PrEP/condoms network
│       ├── subreddit_distribution.html# Subreddit chart
│       ├── dataset_stats.json         # Stats summary
│       └── post_summaries.json        # Post summaries
│
└── tools/
    ├── launch_demo_showcase_v2.py     # 🚀 LAUNCH THIS
    ├── generate_demo_visualizations.py # Regenerate visuals if needed
    ├── import_demo_annotations.py     # Import CSV annotations
    └── annotate_demo_posts.py         # Annotation UI (optional)
```

---

## Sharing for Feedback

### Option 1: Local Preview (Default)
```bash
python tools/launch_demo_showcase_v2.py
```
Access at: http://localhost:7860
Share your screen or invite people locally.

### Option 2: Public Link (For Remote Feedback)

Edit `tools/launch_demo_showcase_v2.py`:

Change this line:
```python
share=False,  # Change to True for public sharing link
```

To:
```python
share=True,  # Get a public gradio.live link
```

Then run:
```bash
python tools/launch_demo_showcase_v2.py
```

Gradio will generate a **public URL** (e.g., `https://xxxxx.gradio.live`) that you can share via email/Slack for 72 hours.

### Option 3: Deploy to Hugging Face Spaces (Permanent)

For a permanent shareable link:

1. Create account at https://huggingface.co
2. Create new Space (select Gradio)
3. Upload your project files
4. Get permanent URL like: https://huggingface.co/spaces/yourname/counterforce-one

---

## What Reviewers Will See

### 1. Project Overview
- Dataset statistics (505 posts, 11K+ comments)
- Research questions
- Focus communities

### 2. 4 Annotated Case Studies
**Post 1: "U=U, 100%!"**
- ✅ Accurate info with community nuance
- Network shows trust/skepticism balance

**Post 2: "HIV is life altering..."**
- ⚠️ Partially accurate, subtle misinformation
- Shows challenge of debunking half-truths

**Post 3: "was recently diagnosed with hiv"**
- ❤️ Peer support in action
- Knowledge brokers visible in network

**Post 4: "prep exists folks weird about condoms"**
- 📚 Knowledge gaps & community education
- Self-correction around STI risks

### 3. Interactive Networks
Clickable network graphs showing comment reply structures

### 4. Methodology
Research pipeline, technologies, ethical considerations

### 5. Findings
4 key insights with examples

### 6. Next Steps
Roadmap for continued research

---

## Regenerating Content

If you modify annotations or want to refresh visualizations:

```bash
# Regenerate all visualizations
python tools/generate_demo_visualizations.py

# Then restart showcase
python tools/launch_demo_showcase_v2.py
```

---

## Key Demo Talking Points

When presenting, emphasize:

1. **Community Resilience Focus**
   - Not surveillance, studying protective mechanisms
   - Documenting community strengths

2. **Real Data, Real Impact**
   - Actual Reddit discussions from 2024-2025
   - 11,000+ comments analyzed
   - Addresses real public health challenges (HIV misinfo)

3. **Innovative Methods**
   - Network analysis reveals information flow
   - Knowledge brokers identified computationally
   - Multilingual content support

4. **Practical Applications**
   - Public health: partner with community educators
   - Platform design: amplify peer support features
   - Intervention: align with community norms

5. **Next Steps Clear**
   - Annotate more posts (20-30 total)
   - Train ML classifier
   - Scale network analysis
   - Temporal analysis (how misinfo spreads over time)

---

## Troubleshooting

**Gradio won't start:**
```bash
# Check if port 7860 is in use
lsof -i :7860

# Kill any existing process
kill -9 <PID>

# Try different port
# Edit launch_demo_showcase_v2.py, change server_port=7860 to server_port=7861
```

**Network visualizations not showing:**
- Check `data/demo_visualizations/` has .html files
- Regenerate: `python tools/generate_demo_visualizations.py`

**Data errors:**
- Verify database connection: `psql postgresql://drjforrest@localhost:5432/misinformation_research`
- Check CSV files exist in `data/demo_highlight_reel/`

---

## Feedback Questions to Ask

When sharing, consider asking:

1. **Clarity:**
   - Is the research question clear?
   - Are the findings compelling?

2. **Visualizations:**
   - Do the network graphs add value?
   - What other visuals would help?

3. **Impact:**
   - Can you see practical applications?
   - Who else should see this?

4. **Next Steps:**
   - What should be prioritized?
   - Any analysis gaps?

5. **Presentation:**
   - Good for academic conference?
   - Good for public health stakeholders?
   - Good for funding applications?

---

## Session Summary

### What We Built Today:

1. ✅ Curated high-quality demo dataset (4 key posts + 30 top posts)
2. ✅ Fixed database linkage (4,458 comments now properly connected)
3. ✅ Created ground truth annotations with your expert review
4. ✅ Generated 4 interactive network visualizations
5. ✅ Built complete showcase website
6. ✅ Documented everything for sharing

### Time Invested:
- Data curation: ~30 min
- Annotation review: ~20 min
- Visualization generation: ~5 min
- Website building: ~15 min
- **Total: ~70 minutes** for a shareable demo!

### Ready to Share:
- [x] Professional presentation
- [x] Real data with real insights
- [x] Interactive exploration
- [x] Clear next steps
- [x] Easy to launch and share

---

## 🚀 Go Launch It!

```bash
cd /Users/drjforrest/dev/academicdev/counterforce-one
python tools/launch_demo_showcase_v2.py
```

**Then visit:** http://localhost:7860

**To share remotely:** Change `share=False` to `share=True` in the launch script!

---

Good luck with your feedback session! 🎯
