# Task Cost Analysis Framework

**A universal model selection and budget optimization system for AI-assisted development**

> Save 93% on AI API costs while maintaining quality. Leverage local Ollama models (FREE) + Claude Sonnet for strategic decisions ($120/month budget).

---

## Overview

This framework covers **110+ use cases** across **12 categories**, enabling you to choose the optimal model for ANY task in under 30 seconds.

**The Formula:**
```
90% local Ollama models ($0) + 10% Claude Sonnet ($0.15-0.30 per decision) = 93% cost savings
```

---

## Quick Start

### 1. Read the Framework (10 minutes)
Start with [`COMPREHENSIVE_COST_ANALYSIS_FRAMEWORK_V2.md`](COMPREHENSIVE_COST_ANALYSIS_FRAMEWORK_V2.md) — the master reference covering all 110+ use cases.

### 2. Choose Your Decision Tree (30 seconds per task)
Use [`decision-trees/`](decision-trees/) to quickly identify the right model:
- `01-what-is-my-task.md` — Top-level task classification
- `02-coding-selection.md` — For development work
- `03-media-selection.md` — For video/audio/images
- `04-data-selection.md` — For data analysis/transformation
- And 6 more for other categories...

### 3. Implement Using Templates
Reference [`templates/`](templates/) for:
- `monthly-cost-report.md` — Track spending
- `task-log-template.md` — Log which model you used
- `budget-planning-template.md` — Set monthly allocations

### 4. See Real Examples
Browse [`examples/`](examples/) for actual project implementations:
- `enterprise-osint-platform-costs.md` — All 8 phases, $1.15 total
- `video-generator-optimization.md` — How to integrate with existing projects
- `data-analysis-workflow.md` — Real data science example

### 5. Calculate & Automate
Use [`tools/`](tools/) for:
- `cost-calculator.py` — Calculate any task's cost
- `budget-tracker.py` — Monthly reconciliation
- `model-selector.py` — Automated model recommendation

---

## The 12 Categories

| # | Category | Use Cases | Typical Model | Cost |
|----|----------|-----------|---------------|------|
| 1 | **Coding & Engineering** | Bug fixes, features, APIs, DevOps | qwen2.5-coder | $0 |
| 2 | **Video/Audio/Media** | Transcription, editing, subtitles | ffmpeg + qwen | $0 |
| 3 | **Image Processing** | Analysis, OCR, manipulation | llava, qwen, Claude | $0-0.30 |
| 4 | **Data Processing** | Transform, validate, analyze | qwen, gemma4, Claude | $0-0.40 |
| 5 | **Compliance & Security** | Scanning, audits, reports | skill-scanner, Claude | $0-0.40 |
| 6 | **Communication & Automation** | Email, Slack bots, notifications | mistral, qwen | $0 |
| 7 | **Business Intelligence** | Dashboards, reports, forecasting | qwen, gemma4, Claude | $0-0.40 |
| 8 | **Research & Learning** | Papers, tutorials, study guides | gemma4, mistral | $0 |
| 9 | **Creative & Content** | Blog posts, scripts, marketing | mistral, gemma4 | $0 |
| 10 | **Web Operations** | Scraping, testing, monitoring | qwen, browser-harness | $0 |
| 11 | **Specialized Domain** | Legal, financial, medical analysis | Claude Sonnet | $0.20-0.40 |
| 12 | **Your Projects** | OSINT, video-gen, skill-scanner, resume | Task-specific | $0-0.30 |

---

## Model Inventory

### Mac M1 Max (Recommended Setup)
Keep 10 models (~50GB):
- **Fast:** qwen2.5-coder:1.5b (1GB)
- **Quality:** qwen2.5-coder:7b (4.7GB), mistral (4.4GB)
- **Analysis:** gemma4:latest (9.6GB), gemma4:26b (17GB)
- **Vision:** llava:latest (7.9GB)
- **Embeddings:** bge:small-en-v1.5 (33MB)
- **Deep:** llama3.3:70b (41GB)

### Windows RTX 5060 Ti (Recommended Setup)
Always loaded (5.4GB / 12GB):
- qwen2.5-coder:1.5b (1GB)
- mistral:latest (3.2GB)
- bge:small-en-v1.5 (33MB)

Load on demand:
- qwen2.5-coder:7b, deepseek-r1:1.5b, gemma4:latest

---

## Cost Comparison

| Approach | Monthly Cost | Speed | Iteration |
|----------|-------------|-------|-----------|
| **Pure Claude Sonnet** | $1,600 | 300 t/sec | Slow (API) |
| **Pure Ollama** | $0 | 10-160 t/sec | Fast (local) |
| **Hybrid (Your choice)** | $120 | 120 t/sec (local) | **Best** ✓ |

**Real example:** Enterprise OSINT platform (8 phases)
- Pure Claude: $1,600
- Hybrid Ollama + Claude: $1.15
- **Savings: 99.93%**

---

## When to Use Each Model

### qwen2.5-coder:1.5b → $0, 120 t/sec
**Use for:** Quick fixes, simple code, format conversions
- "Fix this Python error"
- "Convert JSON to CSV"
- "Generate bash script"

### qwen2.5-coder:7b → $0, 50 t/sec  
**Use for:** Features, APIs, complex logic
- "Generate FastAPI endpoint"
- "Write data transformation pipeline"
- "Create test suite"

### mistral:latest → $0, 55 t/sec
**Use for:** Writing, documentation, templates
- "Generate blog post"
- "Create email template"
- "Write policy document"

### gemma4:latest → $0, 45 t/sec
**Use for:** Analysis, reasoning, summaries
- "Analyze this dataset for patterns"
- "Summarize meeting notes"
- "Generate study guide"

### llava:latest → $0, 15 t/sec
**Use for:** Image analysis, screenshots, vision
- "Analyze this screenshot"
- "Extract text from image"
- "Describe what's in this photo"

### Claude Sonnet → $0.15-0.30, 300 t/sec
**Use for:** Architecture, security, complex reasoning
- "Design system architecture"
- "Review this for security vulnerabilities"
- "Analyze market trends and forecast"

---

## Setup (5 minutes)

### Mac M1 Max
```bash
# Install Ollama
brew install ollama

# Pull recommended models
ollama pull qwen2.5-coder:1.5b
ollama pull qwen2.5-coder:7b
ollama pull mistral:latest
ollama pull gemma4:latest
ollama pull llava:latest
ollama pull bge:small-en-v1.5

# Start daemon
ollama serve
```

### Windows RTX 5060 Ti
```bash
# Download installer: https://ollama.ai
# Run installer (auto-detects RTX 5060 Ti)

# Pull recommended models
ollama pull qwen2.5-coder:1.5b
ollama pull mistral:latest
ollama pull bge:small-en-v1.5

# Start daemon in separate window
ollama serve
```

### Add ANTHROPIC_API_KEY
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
# Or add to ~/.zshrc / ~/.bashrc for permanence
```

---

## Workflow: Apply Before Every Task

### Step 1: Identify Task Type (5 seconds)
Use the decision tree: "Is this coding? Data? Analysis? Media?"

### Step 2: Choose Model (10 seconds)
Reference the quick matrix above or use `tools/model-selector.py`

### Step 3: Execute (Task dependent)
Run your model, track the outcome

### Step 4: Log Results (2 seconds)
Note: model used, tokens approx, success/failure in `task-log.md`

### Step 5: Monthly Review (30 minutes)
Run `tools/budget-tracker.py` to reconcile actual vs budgeted costs

---

## File Structure

```
task-cost-analysis/
├── README.md                                    # This file
├── COMPREHENSIVE_COST_ANALYSIS_FRAMEWORK_V2.md # Master reference (2,800+ lines, 110+ use cases)
│
├── decision-trees/                              # Quick reference guides
│   ├── 01-what-is-my-task.md                   # Top-level classification
│   ├── 02-coding-selection.md
│   ├── 03-media-selection.md
│   ├── 04-data-selection.md
│   ├── 05-security-selection.md
│   ├── 06-communication-selection.md
│   ├── 07-bi-selection.md
│   ├── 08-research-creative-selection.md
│   ├── 09-web-selection.md
│   ├── 10-specialized-selection.md
│   └── escalation-criteria.md                   # When to use Claude
│
├── templates/                                   # Reusable planning documents
│   ├── monthly-cost-report.md
│   ├── task-log-template.md
│   ├── budget-planning-template.md
│   ├── project-cost-breakdown.md
│   └── skill-assessment-template.md
│
├── examples/                                    # Real-world implementations
│   ├── enterprise-osint-platform-costs.md       # $1.15 for 8-phase project
│   ├── video-generator-optimization.md
│   ├── data-analysis-workflow.md
│   ├── web-scraping-strategy.md
│   ├── compliance-audit-automation.md
│   └── case-studies.md
│
├── tools/                                       # Utilities & calculators
│   ├── cost-calculator.py
│   ├── budget-tracker.py
│   ├── model-selector.py
│   ├── requirements.txt                         # Python deps for tools
│   └── README.md                                # How to use tools
│
├── models/                                      # Detailed specs
│   ├── ollama-models.md                         # All 13 Ollama models (specs, speeds, costs)
│   ├── claude-models.md                         # Claude API models & pricing
│   ├── openai-models.md                         # Optional: GPT-4, GPT-3.5 comparison
│   └── specialization-matrix.md                 # Which model for which task
│
├── reference/                                   # Advanced topics
│   ├── token-budgeting.md                       # How to estimate tokens per task
│   ├── cross-machine-optimization.md            # Mac vs Windows strategy
│   ├── monthly-metrics.md                       # Success metrics to track
│   ├── troubleshooting.md                       # Common issues & solutions
│   ├── model-tuning.md                          # Prompt engineering per model
│   └── scaling-beyond-120.md                    # What to do if you need more budget
│
└── .gitignore                                   # Ignore: .env, API keys, local logs
```

---

## Success Metrics (Track Monthly)

```markdown
## May 2026 — Cost Report

Tasks completed: 50
- Ollama-only: 47 ($0)
- Claude calls: 2 ($0.30)
- Hybrid: 1 ($0.10)

Total cost: $0.40
Budgeted: $120
Remaining: $119.60

Model performance:
- qwen-1.5b: 18 tasks (100% success)
- qwen-7b: 16 tasks (94% success)
- mistral: 8 tasks (100% success)
- gemma4: 5 tasks (100% success)
- Claude: 3 tasks (100% success)

Cost per task: $0.008 (vs $3.20 pure Claude)
Savings: 99.75%
```

See [`reference/monthly-metrics.md`](reference/monthly-metrics.md) for detailed guidance.

---

## Real Examples

### 1. Enterprise OSINT Platform (110+ API integrations)
**All 8 phases:** 42 hours × $0 Ollama + $1.15 Claude = **$1.15 total**
- Phase 1 (core): qwen-7b ($0) + Claude ($0.30) = $0.30
- Phases 2-8: qwen-7b mostly ($0) + Claude ($0.15 per phase) = $0.85
- **Pure Claude equivalent:** $1,600
- **Savings:** 99.93%

See [`examples/enterprise-osint-platform-costs.md`](examples/enterprise-osint-platform-costs.md)

### 2. Video Generator Optimization  
**Transcription + subtitles + batch processing**
- Audio transcription: whisper.cpp ($0)
- Subtitle generation: qwen-7b ($0)
- Batch processing: qwen-7b ($0)
- **Monthly cost: $0**
- **Previous approach:** $150/month on transcription API

See [`examples/video-generator-optimization.md`](examples/video-generator-optimization.md)

### 3. Data Analysis Workflow
**Real estate valuation system**
- Data validation: qwen-1.5b ($0)
- Statistical analysis: gemma4 ($0)
- Business analysis: Claude ($0.20)
- **Per analysis:** $0.20 (vs $2 pure Claude)
- **Savings: 90%**

See [`examples/data-analysis-workflow.md`](examples/data-analysis-workflow.md)

---

## FAQ

### Q: Will Ollama models work for my use case?
**A:** 90% of tasks. Use the decision trees to identify edge cases where Claude is better (architecture, security, complex reasoning).

### Q: What if Ollama gets stuck on a task?
**A:** After 15 minutes, escalate to Claude Sonnet ($0.15-0.30 per call). Track the incident in your monthly report.

### Q: How do I know if I should use qwen-1.5b or qwen-7b?
**A:** Use the coding decision tree. Rule of thumb:
- <50 lines → qwen-1.5b
- 50-500 lines → qwen-7b
- >500 lines or complex → qwen-7b + Claude

### Q: Can I use this framework with other LLMs (GPT-4, Gemini)?
**A:** Yes. The framework is model-agnostic. We default to Claude + Ollama, but you can swap in GPT-4 ($0.30-0.60 per 1K tokens) or Gemini Pro ($0.25 per 1K input).

### Q: What's the setup cost?
**A:** $0. Ollama is free, open source. Claude API is pay-as-you-go ($120/month is the recommendation, but you can start smaller).

### Q: How long does the decision tree take?
**A:** 30 seconds per task. Includes: identify type, reference matrix, select model.

### Q: What if my task doesn't fit the 110 use cases?
**A:** File an issue on GitHub. We'll add it + update the framework. Most edge cases fit into combinations of the 12 categories.

---

## Getting Started Checklist

- [ ] **Read:** COMPREHENSIVE_COST_ANALYSIS_FRAMEWORK_V2.md (30 min)
- [ ] **Setup:** Install Ollama + models for your machine (Mac or Windows) (15 min)
- [ ] **Download:** This repo, save decision-trees/ locally
- [ ] **First task:** Use decision tree to choose model, track outcome in task-log.md
- [ ] **Monthly:** Run tools/budget-tracker.py, fill out monthly-cost-report.md
- [ ] **Optimize:** Review reference/monthly-metrics.md, adjust strategy as needed

---

## Contributing

This framework is **open source** and lives in this GitHub repo. If you:
- Discover a new use case → add it to examples/
- Find a cheaper approach → file an issue with cost comparison
- Create a project using this → share in case-studies/
- Build tools → submit a PR to tools/

**Every contribution helps the community save more on AI costs.**

---

## License

MIT. Use freely for personal and commercial projects.

---

## Support

- **Questions?** Start with the [decision trees](decision-trees/)
- **Get stuck?** Check [reference/troubleshooting.md](reference/troubleshooting.md)
- **New use case?** Add it to [examples/](examples/) and share
- **Bug or suggestion?** Open a GitHub issue

---

## Quick Links

- **Master Framework:** [COMPREHENSIVE_COST_ANALYSIS_FRAMEWORK_V2.md](COMPREHENSIVE_COST_ANALYSIS_FRAMEWORK_V2.md)
- **Decision Trees:** [decision-trees/](decision-trees/)
- **Real Examples:** [examples/](examples/)
- **Tools:** [tools/](tools/)
- **Models Reference:** [models/](models/)

---

**Version:** 2.0  
**Last Updated:** May 18, 2026  
**Maintainer:** Sriram  
**Status:** Production-Ready ✓

