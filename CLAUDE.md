# Task Cost Analysis Framework — Implementation Guide

**For Claude (any session): How to implement this on any user's machine**

---

## What This Is

A universal AI model selection framework for optimizing which model to use for any task. Uses local Ollama models (90%) + Claude strategic calls (10%) = 93% cost savings.

**Status:** Framework complete, tested, production-ready.

---

## One-Command Deployment

```bash
cd task-cost-analysis
bash setup/ollama-installation.sh
```

This automatically:
1. Detects OS (Mac/Windows/Linux)
2. Detects hardware (Apple Silicon/NVIDIA GPU/CPU)
3. Installs Ollama daemon
4. Downloads optimal models for that hardware
5. Verifies everything works
6. Shows next steps

**Time:** ~30 min first time (depends on internet + hardware)

---

## After Setup: Use It

### For any new task, ask:

```bash
python tools/model-selector-automated.py --task "Your task description here"
```

**Example:**
```bash
$ python tools/model-selector-automated.py --task "Fix Python bug in Flask API"

============================================================
MODEL SELECTOR
============================================================

Task: Fix Python bug in Flask API

------------------------------------------------------------
ANALYSIS
------------------------------------------------------------
Category:    coding
Complexity:  simple

------------------------------------------------------------
RECOMMENDATION
------------------------------------------------------------
Model:  qwen-1.5b
Cost:   $0.00
Reason: Bug fixes, simple scripts

------------------------------------------------------------
NEXT STEPS
------------------------------------------------------------
1. Prepare your task
2. Run: ollama run qwen-1.5b
3. Track in: templates/task-log-template.md
4. Analyze monthly: templates/monthly-report-comprehensive.md

============================================================
```

### Weekly Workflow (Every Monday)

1. **Research new models** (30 min)
   ```bash
   cp templates/weekly-model-research.md templates/weekly-model-research-[date].md
   # Fill in discoveries, test if interested
   ```

2. **Log this week's tasks** (10 min)
   ```bash
   cp templates/task-log-template.md templates/task-log-week-[N].md
   # Log models used, success rates
   ```

### Monthly Workflow (First Friday)

```bash
cp templates/monthly-report-comprehensive.md templates/monthly-report-[month-year].md
# Aggregate weekly data, analyze trends, project next month
```

---

## Key Files

| File | Purpose |
|---|---|
| `setup/ollama-installation.sh` | Automated setup (run once) |
| `tools/model-selector-automated.py` | Get model recommendation for any task |
| `decision-trees/01-10/*.md` | Manual decision guides (if tool not available) |
| `templates/task-log-template.md` | Track tasks you complete |
| `templates/weekly-model-research.md` | Track new models discovered |
| `templates/monthly-report-comprehensive.md` | Monthly cost/performance analysis |
| `reference/model-maintenance.md` | How to keep models current |

---

## Machine-Specific Notes

### Mac (Intel or M1/M2/M3)
```bash
# Setup auto-detects and installs for your hardware
bash setup/ollama-installation.sh

# Local models will run on CPU (Intel) or GPU (Apple Silicon)
# Speed: 80-200 tokens/sec typical
```

### Windows (with NVIDIA GPU)
```bash
# Setup auto-detects RTX, Tesla, etc.
bash setup/ollama-installation.sh

# Local models accelerated on GPU
# Speed: 300-500 tokens/sec typical (3-5x faster than Mac CPU)
```

### Linux
```bash
# Setup auto-detects GPU if present
bash setup/ollama-installation.sh

# Works with NVIDIA, AMD, or CPU-only
```

---

## Integration with Claude

**In any Claude conversation:**

Before starting work on a task, use the model selector:
```bash
python tools/model-selector-automated.py --task "describe your task"
```

This tells you:
- Which local model to use (save $$$)
- When Claude is worth calling (strategic decisions only)
- Expected cost
- Estimated speed

---

## Updating Models

Monthly, check for new/better models:

```bash
# Read the guide
cat reference/model-maintenance.md

# Use the weekly research template
cat templates/weekly-model-research.md

# Replace an old model if a new one is better
ollama pull [new_model]
ollama rm [old_model]

# Update decision trees if needed
# (Edit decision-trees/*.md with new model names)
```

---

## Cost Tracking

Every month, fill out the monthly report:

```bash
cat templates/monthly-report-comprehensive.md
```

Typical monthly cost:
- **Local models only:** $0
- **Local models + 6-10 Claude calls:** $120
- **Pure Claude:** $1,600

This framework targets $0-120/month while maintaining full capability.

---

## Architecture

```
TASK INPUT
   ↓
[Model Selector Tool]
   ↓
AUTO-DETECT: Category (coding/data/media/etc) + Complexity (simple/medium/complex)
   ↓
RECOMMEND: Best model + cost estimate
   ↓
USER CHOICE: Run locally or ask Claude?
   ↓
EXECUTE: Run model or call Claude API
   ↓
TRACK: Log results, monitor cost trends
   ↓
MONTHLY REVIEW: Which models worked best? Keep/replace/add?
```

---

## For Multi-Machine Setup

**Mac + Windows + Cloud:** Each can clone this repo and implement locally.

Use the same decision trees across all machines, but each will have different performance:
- Mac: CPU-based, 80-150 tokens/sec
- Windows (GPU): 300-500 tokens/sec
- Cloud: Claude API (strategic calls only)

Route heavy tasks to fastest hardware, strategic decisions to Claude.

---

## Troubleshooting

**"ollama command not found"**
→ Run: `bash setup/ollama-installation.sh` (installs Ollama)

**"No such file or directory: model-selector-automated.py"**
→ Ensure you're in the `task-cost-analysis` directory: `cd task-cost-analysis`

**"Python not found"**
→ Install Python 3.8+: https://python.org

**Setup script fails on your OS**
→ Manual steps in `setup/ollama-installation.sh` (edit and follow the comments for your OS)

---

## Next Steps After Setup

1. ✓ Run setup script
2. ✓ Test model selector on a real task
3. ✓ Copy a decision tree to reference
4. ✓ Start weekly tracking (every Monday)
5. ✓ Monthly review (first Friday)
6. ✓ Quarterly deep-dive (every 3 months)

---

## Questions?

Refer to:
- `PROJECT_WORKFLOW_STANDARD.md` — Full workflow details
- `COMPREHENSIVE_COST_ANALYSIS_FRAMEWORK_V2.md` — 110+ use cases
- `README.md` — Project overview
- `decision-trees/` — Decision logic for your task type

---

**Status:** Ready to deploy. One setup script. Automatic OS/hardware detection. No manual config needed.
