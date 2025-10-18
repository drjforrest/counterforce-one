# Demo Annotation Guide

## Quick Start

You need to annotate **4 key posts** to create ground truth for your demo. This should take 30-60 minutes total.

## Annotation Template

Use the file: `annotation_template_posts.csv`

Open it in Excel/Google Sheets or edit directly in CSV format.

## Annotation Fields

For each of the 4 posts, fill in these columns:

### 1. annotation_type
What kind of content is this?
- `health_info` - Provides health information/advice
- `personal_experience` - Personal story/experience
- `support_seeking` - Asking for help/support
- `community_discussion` - General discussion
- `misinformation` - Contains false health claims

### 2. accuracy_label
How accurate is the health information?
- `accurate` - Scientifically correct
- `partially_accurate` - Contains some truth, some errors
- `misleading` - Technically true but misleading context
- `inaccurate` - Factually wrong
- `not_applicable` - Not a health claim

### 3. misinformation_type (if applicable)
If this contains misinformation, what type?
- `false_claim` - Outright false statement
- `exaggeration` - True but exaggerated
- `outdated_info` - Was true but no longer current
- `missing_context` - True but lacks important context
- `none` - No misinformation

### 4. severity
How severe is the potential harm? (1-5 scale)
- `1` - No harm
- `2` - Minor misinformation, low impact
- `3` - Moderate, could influence decisions
- `4` - Serious, could cause health harm
- `5` - Critical, immediate health risk

### 5. community_response
How did the community respond?
- `corrective` - Community corrected misinformation
- `supportive` - Provided support and accurate info
- `mixed` - Both good and bad responses
- `amplifying` - Made misinformation worse
- `none` - No significant response

### 6. notes
Free text - your observations about:
- Why this post is valuable for demo
- Key points community made
- Patterns you notice
- Demo talking points

## Recommended Approach

### Start with Post 1: "U=U, 100%!" (1ls1tyz)
```
annotation_type: health_info
accuracy_label: accurate
misinformation_type: none
severity: 1
community_response: supportive
notes:
U=U is scientifically accurate (CDC/WHO endorsed).
341 comments show community reinforcing accurate science.
Great demo for: community resilience, accurate info spreading.
Some skeptics in comments - good for showing how community educates.
```

### Post 2: "HIV is life altering..." (1lyphrb)
This is the trickiest one - contains partial truths but may be misleading.

```
annotation_type: health_info, personal_experience
accuracy_label: partially_accurate
misinformation_type: exaggeration
severity: 3
community_response: mixed
notes:
True that HIV has impacts even with treatment (stigma, etc).
But title implies treatment doesn't work well - misleading.
216 comments show debate - some correct, some amplify fear.
Great demo for: detecting subtle misinformation, community debate.
```

### Post 3: "was recently diagnosed with hiv" (1la8c64)
```
annotation_type: support_seeking, personal_experience
accuracy_label: not_applicable
misinformation_type: none
severity: 1
community_response: supportive
notes:
Personal disclosure, seeking support. No health claims.
164 comments mostly supportive, sharing accurate U=U info.
Great demo for: peer support patterns, community resilience.
Shows knowledge brokers educating newly diagnosed person.
```

### Post 4: "prep exists folks are being weird about condoms" (1lhs70z)
```
annotation_type: community_discussion, personal_experience
accuracy_label: not_applicable
misinformation_type: none
severity: 2
community_response: mixed
notes:
Discusses risk perception and PrEP vs condoms.
Some may underestimate STI risks beyond HIV.
156 comments with education about PrEP limitations (doesn't prevent other STIs).
Great demo for: health decision-making, community education.
```

## After Annotation

Once you've annotated all 4 posts:

1. Save the CSV file
2. We'll import it back into the database
3. Use it as ground truth for:
   - ML model validation
   - Demo narratives
   - Visualization labels

## Advanced: Comment-Level Annotation (Optional)

If you want to go deeper, you can also annotate individual comments from the 261 comments in `key_comments.csv`.

Focus on:
- Top-voted comments (highest scores)
- Comments that correct misinformation
- Supportive comments
- Knowledge broker comments (users who educate others)

This gives you fine-grained network analysis data.

## Time Estimate

- Post-level annotation (4 posts): 30-45 minutes
- Reading key comments for context: 15-30 minutes
- Optional comment annotation (20-30 comments): 30-60 minutes

**Total: 1-2 hours for solid ground truth**
