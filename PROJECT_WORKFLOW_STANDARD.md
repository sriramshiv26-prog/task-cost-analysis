# Project Workflow Standard

**For all future projects using this Task Cost Analysis framework**

This document establishes the standard workflow for implementing, testing, tracking, and maintaining AI-assisted projects with cost optimization.

---

## Overview

### The Standard Workflow

```
PHASE 1: Implementation + Testing
    ↓
PHASE 2: Documentation + Memory Save
    ↓
PHASE 3: GitHub Commit + Push
    ↓
PHASE 4: Memory Workflow Setup (weekly/monthly tracking)
```

### Applies To

All projects using the Task Cost Analysis framework:
- OSINT Platform
- Video Generator
- Skill Scanner
- Resume Generator
- Future projects...

---

## Phase 1: Implementation + Thorough Testing

### Step 1: Build Core Functionality

**Before coding:** Run task cost analysis
```
Task: [What you're building]
Category: [From decision trees]
Model: [From automated selector]
Estimated tokens: [Using token budgeting]
Expected cost: $[X]
Timeline: [Hours needed]
```

**Code requirements:**
- Well-structured, modular code
- Comments only for "why" (not "what")
- No premature abstraction
- Safe by default (especially at system boundaries)

### Step 2: Implement Automated Tests

**For code:**
- Unit tests (if logic-heavy)
- Integration tests (if external systems involved)
- Smoke tests (basic "does it work" tests)

**For scripts:**
- Syntax validation
- Dry-run mode
- Error handling
- Expected input/output checks

**For documentation:**
- Markdown syntax validation
- Link validation
- Example code blocks tested

### Step 3: Manual Testing

**Test on target hardware:**
- Mac M1 / Intel
- Windows RTX / CPU
- Linux GPU / CPU

**Test edge cases:**
- Empty inputs
- Large datasets
- Unexpected formats
- Error conditions

**Test integration:**
- With decision trees
- With task logs
- With monthly reports
- With other components

### Step 4: Document Tests + Results

Create test results file:
```markdown
# [Project] Testing Results

## Automated Tests
[Bash tests, Python tests, syntax checks]
✓ All passed

## Manual Tests
[Edge cases, hardware combinations]
✓ All passed

## Integration Tests
[Interactions with framework]
✓ All passed

## Known Limitations
[Any known issues, workarounds]
```

---

## Phase 2: Documentation + Memory Save

### Step 1: Write Comprehensive Docstrings

**For functions/classes:**
```python
def example_function(param1, param2):
    """One-line summary.
    
    Longer description if needed.
    """
```

**For modules:**
```python
"""Module summary - what this does.

Usage:
    python module.py --arg value
"""
```

### Step 2: Create README (if needed)

For new features/components:
```markdown
# [Feature Name]

## What it does
[Clear description]

## How to use
[Examples]

## Requirements
[Dependencies, hardware, etc.]

## Testing
[How to run tests]
```

### Step 3: Save to Memory

**Create memory file:**
```
/Users/sriram/.claude/projects/-Users-sriram/memory/[project]_[phase]_complete.md
```

**Include:**
- What was built
- What was tested
- Results and status
- How to replicate
- Known issues
- Next steps

**Template:**
```markdown
---
name: [Project] — [Phase] Complete
description: [One-line summary]
type: project
---

## Implementation Complete ✓

**Date:** [YYYY-MM-DD]
**Status:** [IN PROGRESS / COMPLETE / PRODUCTION]
**Repository:** [GitHub URL]

### What Was Built
[List deliverables]

### Testing Results
[Test summary]

### Known Issues
[Any limitations]

### Next Steps
[What's next]

### How to Replicate
[Steps to rebuild this]
```

### Step 4: Update Main Memory Index

Edit: `/Users/sriram/.claude/projects/-Users-sriram/memory/MEMORY.md`

Add pointer to new project memory file:
```markdown
## [Project Name]

- [Brief description](memory_file.md) — One-line hook
```

---

## Phase 3: GitHub Commit + Push

### Step 1: Stage Files

```bash
cd /path/to/project
git status  # Review changes

# Add specific files (not git add -A)
git add file1.py file2.md
git add README.md
git status  # Verify staging
```

### Step 2: Create Commit

**Commit message format:**
```
[Title - what changed]

[Detailed description - why this matters]
[List of changes/benefits]
[Cost/impact analysis if relevant]

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

**Example:**
```
Add automated model selector tool

- Reads task description → recommends optimal model
- Auto-detects category (coding, data, media, etc.)
- Auto-detects complexity (simple/medium/complex)
- Shows cost estimate + alternatives
- Tested ✓ All test cases pass

Impact: 20x faster model selection, ensures cost optimization

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

### Step 3: Verify Commit

```bash
git log --oneline -5  # See recent commits
git show HEAD  # Review what was committed
git diff --cached  # Verify no uncommitted changes
```

### Step 4: Push to GitHub

```bash
git push origin main
# Verify: https://github.com/yourusername/your-repo
```

---

## Phase 4: Establish Tracking Workflow

### Weekly Tasks

**Every Monday (or your chosen day):**

1. **Run model research** (30-60 min)
   ```bash
   cp templates/weekly-model-research.md weekly-model-research-[date].md
   # Fill in new models discovered
   # Test candidates if any
   # Decide: Keep/Skip/Waitlist
   ```

2. **Log this week's tasks** (10 min)
   ```bash
   cp templates/task-log-template.md task-log-week-[N].md
   # Fill in tasks completed this week
   # Note models used + success rates
   ```

### Monthly Tasks

**First Friday of month:**

1. **Monthly cost analysis** (30 min)
   ```bash
   cp templates/monthly-report-comprehensive.md monthly-report-[month-year].md
   # Aggregate weekly data
   # Analyze trends
   # Project next month
   ```

2. **Model maintenance** (30 min)
   - Review research from past 4 weeks
   - Evaluate any "KEEP" candidates
   - Update decision trees if models changed
   - Commit changes to GitHub

3. **Optimization review** (30 min)
   - Any tasks that could use cheaper models?
   - Any patterns in what worked/didn't?
   - Update task log templates if needed
   - Plan for next month

### Quarterly Tasks

**Every 3 months (Jan/Apr/Jul/Oct):**

1. **Deep dive analysis** (2-3 hours)
   - Review all 12 weeks of data
   - Benchmark all models
   - Identify trends
   - Plan next quarter

2. **Archive & cleanup**
   - Move old logs to archive/
   - Update model performance records
   - Clean up unused files

3. **Commit quarterly review**
   ```bash
   git add quarterly-review-[season].md
   git commit -m "Q[X] [year] review: [summary]"
   git push
   ```

---

## Checklist for Each Project

### Implementation Phase
- [ ] Core functionality built
- [ ] All tests pass (automated + manual)
- [ ] Documentation complete
- [ ] Code reviewed (self-review minimum)
- [ ] Edge cases tested
- [ ] Ready for production

### Documentation Phase
- [ ] Memory file created
- [ ] MEMORY.md updated
- [ ] README written (if needed)
- [ ] Test results documented
- [ ] Known issues listed

### GitHub Phase
- [ ] Files staged
- [ ] Commit message clear
- [ ] Remote verified
- [ ] Push successful
- [ ] GitHub URL confirmed

### Tracking Phase
- [ ] Weekly research template copied
- [ ] Task log template copied
- [ ] Monthly report template copied
- [ ] Calendar reminders set
- [ ] Tracking workflow started

---

## File Organization Standard

```
project-root/
├── README.md
├── setup/
│   ├── installation.sh
│   └── [setup files]
├── src/ (or code directory)
│   ├── main.py
│   ├── [modules]
│   └── tests/
│       ├── test_main.py
│       └── [test files]
├── templates/
│   ├── task-log-template.md
│   ├── weekly-model-research.md
│   └── monthly-report-comprehensive.md
├── reference/
│   ├── model-maintenance.md
│   └── [reference guides]
├── examples/
│   └── [example implementations]
├── tools/
│   ├── cost-calculator.py
│   └── [utility scripts]
├── .gitignore
├── PROJECT_WORKFLOW_STANDARD.md (this file)
└── git/
    ├── [commit history]
    └── [branch structure]
```

---

## Cost Tracking Standard

**Every commit should include cost analysis:**

```
Cost Analysis for [Phase/Feature]:

Build phase:
  - AI assistance: qwen-7b (0 cost) × 5 hours = $0
  - Testing: manual + pytest ($0)
  Total: $0

Documentation:
  - AI writing: mistral (0 cost)
  - Memory save: manual ($0)
  Total: $0

TOTAL PROJECT COST: $0
DEVELOPER TIME: [X] hours (valued at $[X])
```

---

## For Future Projects

### When Starting New Project

1. **Copy this file** to new project repo
2. **Adapt templates** (new file names, specific tools, etc.)
3. **Set calendar reminders:**
   - Weekly: Monday morning (model research)
   - Monthly: 1st Friday (full review)
   - Quarterly: Each quarter start (deep dive)
4. **Initial commit:**
   ```bash
   git add PROJECT_WORKFLOW_STANDARD.md
   git commit -m "Add project workflow standard"
   git push
   ```

### Monitoring & Continuous Improvement

Track workflow effectiveness:
- Time spent on each phase (estimated vs actual)
- Cost accuracy (projected vs actual)
- Model accuracy over time
- Process improvements needed

---

## Template Checklists

### Before Every Commit

- [ ] All tests pass
- [ ] Code formatted consistently
- [ ] No debug statements left in
- [ ] No credentials/secrets in code
- [ ] Documentation updated
- [ ] Memory files saved
- [ ] Commit message clear
- [ ] No large files (>10MB)
- [ ] Remote branch checked
- [ ] Ready for production

### Before Every Push

- [ ] Local branch up-to-date
- [ ] Commits are atomic (one logical change per commit)
- [ ] Commit messages follow format
- [ ] GitHub CI checks pass (if applicable)
- [ ] Code review done (self or peer)
- [ ] No conflicts with remote
- [ ] Push target verified

---

## Support & Questions

**For workflow questions:** See this file (PROJECT_WORKFLOW_STANDARD.md)

**For task-specific decisions:** See decision-trees/01-what-is-my-task.md

**For cost analysis:** See tools/cost-calculator.py

**For model recommendations:** See tools/model-selector-automated.py

**For tracking:** See templates/ directory

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-05-18 | Initial version for task-cost-analysis project |
| 1.1 | TBD | Updates from experience using this workflow |
| 2.0 | TBD | Refinements based on quarterly reviews |

---

**Last Updated:** 2026-05-18  
**Next Review:** 2026-08-18 (Quarterly)  
**Status:** PRODUCTION READY ✓
