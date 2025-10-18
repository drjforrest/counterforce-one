#!/usr/bin/env python3
"""
Quick launcher for annotating the 4 key demo posts
Filters the annotation interface to show only demo highlight posts
"""

import os
import sys

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from loguru import logger

from gradio_app.enhanced_annotation_interface import EnhancedAnnotationInterface

# The 4 key posts for demo
KEY_DEMO_POSTS = ["1ls1tyz", "1lyphrb", "1la8c64", "1lhs70z"]


def main():
    """Launch annotation interface for demo posts only"""
    print("=" * 70)
    print("🎯 Demo Highlight Reel Annotation Interface")
    print("=" * 70)
    print()
    print("📝 Annotating 4 Key Posts:")
    print("   1. 'U=U, 100%!' - Accurate health info (341 comments)")
    print("   2. 'HIV is life altering...' - Potential misinfo (216 comments)")
    print("   3. 'was recently diagnosed' - Support seeking (164 comments)")
    print(
        "   4. 'prep exists folks weird about condoms' - Risk discussion (156 comments)"
    )
    print()
    print("🌐 Interface will open at: http://localhost:7861")
    print()
    print("💡 Quick Tips:")
    print("   • Focus on accuracy, severity, community response")
    print("   • Read top comments for context")
    print("   • Your annotations = ground truth for demo")
    print()
    print("📚 See ANNOTATION_GUIDE.md for detailed instructions")
    print()

    try:
        # Create custom interface for demo posts
        # Note: We'll need to modify EnhancedAnnotationInterface to support post_id filtering
        # For now, launch standard interface with small limit
        logger.info("Initializing annotation interface...")

        interface = EnhancedAnnotationInterface(
            limit=50,  # Small limit to make finding our posts easier
            filter_criteria={"subreddit": "gaybros"},  # All 4 posts are in gaybros
        )

        print("✅ Interface initialized!")
        print("🔍 Filtering to gaybros subreddit (contains all 4 key posts)")
        print()

        interface.launch(share=False)

    except Exception as e:
        logger.error(f"Failed to launch interface: {e}")
        print()
        print("❌ Error launching Gradio interface")
        print()
        print("📝 Alternative: Use CSV annotation template instead")
        print(
            f"   File: {project_root}/data/demo_highlight_reel/annotation_template_posts.csv"
        )
        print(f"   Guide: {project_root}/data/demo_highlight_reel/ANNOTATION_GUIDE.md")
        sys.exit(1)


if __name__ == "__main__":
    main()
