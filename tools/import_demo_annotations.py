#!/usr/bin/env python3
"""
Import manual annotations from CSV back into the database
Creates ground truth for demo validation
"""

import csv
import os
import sys
from datetime import datetime

# Add project root to path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from loguru import logger
from sqlalchemy import text
from src.data_persistence import DataPersistenceManager


def import_post_annotations(csv_path: str) -> dict:
    """
    Import post-level annotations from CSV into database

    Args:
        csv_path: Path to annotation CSV file

    Returns:
        dict: Import statistics
    """
    db_manager = DataPersistenceManager()
    stats = {
        'imported': 0,
        'updated': 0,
        'errors': 0,
        'skipped': 0
    }

    logger.info(f"Reading annotations from: {csv_path}")

    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            with db_manager.get_session() as session:
                for row in reader:
                    post_id = row['post_id']

                    # Skip if not annotated (empty annotation_type)
                    if not row['annotation_type'].strip():
                        logger.debug(f"Skipping unannotated post: {post_id}")
                        stats['skipped'] += 1
                        continue

                    try:
                        # Check if annotation exists
                        check_query = text("""
                            SELECT id FROM post_annotations
                            WHERE post_id = :post_id
                        """)
                        existing = session.execute(
                            check_query,
                            {'post_id': post_id}
                        ).fetchone()

                        if existing:
                            # Update existing annotation
                            update_query = text("""
                                UPDATE post_annotations
                                SET
                                    annotation_type = :annotation_type,
                                    accuracy_label = :accuracy_label,
                                    misinformation_type = :misinformation_type,
                                    severity = :severity,
                                    community_response = :community_response,
                                    notes = :notes,
                                    updated_at = :updated_at
                                WHERE post_id = :post_id
                            """)
                            session.execute(update_query, {
                                'post_id': post_id,
                                'annotation_type': row['annotation_type'],
                                'accuracy_label': row['accuracy_label'],
                                'misinformation_type': row['misinformation_type'],
                                'severity': int(row['severity']) if row['severity'].strip() else None,
                                'community_response': row['community_response'],
                                'notes': row['notes'],
                                'updated_at': datetime.now()
                            })
                            stats['updated'] += 1
                            logger.info(f"✓ Updated annotation for post {post_id}")

                        else:
                            # Insert new annotation
                            insert_query = text("""
                                INSERT INTO post_annotations (
                                    post_id, annotation_type, accuracy_label,
                                    misinformation_type, severity, community_response,
                                    notes, created_at, updated_at
                                ) VALUES (
                                    :post_id, :annotation_type, :accuracy_label,
                                    :misinformation_type, :severity, :community_response,
                                    :notes, :created_at, :updated_at
                                )
                            """)
                            session.execute(insert_query, {
                                'post_id': post_id,
                                'annotation_type': row['annotation_type'],
                                'accuracy_label': row['accuracy_label'],
                                'misinformation_type': row['misinformation_type'],
                                'severity': int(row['severity']) if row['severity'].strip() else None,
                                'community_response': row['community_response'],
                                'notes': row['notes'],
                                'created_at': datetime.now(),
                                'updated_at': datetime.now()
                            })
                            stats['imported'] += 1
                            logger.info(f"✓ Created new annotation for post {post_id}")

                    except Exception as e:
                        logger.error(f"Error processing post {post_id}: {e}")
                        stats['errors'] += 1
                        continue

                # Commit all changes
                session.commit()
                logger.success("All annotations committed to database")

    except FileNotFoundError:
        logger.error(f"Annotation file not found: {csv_path}")
        raise
    except Exception as e:
        logger.error(f"Error importing annotations: {e}")
        raise

    return stats


def main():
    """Main import workflow"""
    print("=" * 70)
    print("📥 Import Demo Post Annotations")
    print("=" * 70)
    print()

    # Default path to annotation template
    default_path = os.path.join(
        project_root,
        'data/demo_highlight_reel/annotation_template_posts.csv'
    )

    csv_path = sys.argv[1] if len(sys.argv) > 1 else default_path

    if not os.path.exists(csv_path):
        print(f"❌ File not found: {csv_path}")
        print()
        print("Usage:")
        print(f"  {sys.argv[0]} [path/to/annotations.csv]")
        print()
        print(f"Default path: {default_path}")
        sys.exit(1)

    print(f"📁 Importing from: {csv_path}")
    print()

    try:
        stats = import_post_annotations(csv_path)

        print()
        print("=" * 70)
        print("✅ Import Complete!")
        print("=" * 70)
        print()
        print(f"  📊 Statistics:")
        print(f"     • New annotations imported: {stats['imported']}")
        print(f"     • Existing annotations updated: {stats['updated']}")
        print(f"     • Skipped (not annotated): {stats['skipped']}")
        print(f"     • Errors: {stats['errors']}")
        print()
        print(f"  📈 Total processed: {sum(stats.values())}")
        print()

        if stats['imported'] > 0 or stats['updated'] > 0:
            print("🎯 Ground truth annotations ready for:")
            print("   • ML model validation")
            print("   • Demo narratives")
            print("   • Visualization labels")
        else:
            print("⚠️  No annotations were imported. Did you annotate the CSV?")
            print(f"   Check: {csv_path}")

        print()

    except Exception as e:
        logger.error(f"Import failed: {e}")
        print()
        print("❌ Import failed. Check the logs for details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
