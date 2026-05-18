# Model Maintenance & Updates Guide

Track, evaluate, and update your Ollama model inventory monthly.

---

## Current Model Inventory (As of May 2026)

### Tier 1: Essential (Always Keep)

| Model | Size | Speed | Best For | Status |
|-------|------|-------|----------|--------|
| qwen2.5-coder:1.5b | 1.0GB | 150 t/s | Fast fixes, quick scripts | ✓ Active |
| qwen2.5-coder:7b | 4.7GB | 50 t/s | Features, APIs | ✓ Active |
| mistral:latest | 4.4GB | 55 t/s | Writing, documentation | ✓ Active |
| gemma4:latest | 9.6GB | 45 t/s | Analysis, reasoning | ✓ Active |
| llava:latest | 7.9GB | 15 t/s | Image analysis, OCR | ✓ Active |

**Total Tier 1 Storage:** ~27.6GB  
**Recommended for:** All users (essential for daily workflow)

---

### Tier 2: Recommended (Add if Space Available)

| Model | Size | Speed | Best For | Notes |
|-------|------|-------|----------|-------|
| deepseek-r1:1.5b | 1.1GB | 160 t/s | Complex reasoning, edge cases | High quality reasoning |
| bge:small-en-v1.5 | 33MB | 5ms/embedding | Semantic search, RAG | Essential for embeddings |
| llama3.3:70b | 41GB | 10 t/s | Ultimate reasoning (CPU offload) | For critical decisions |

**Total Tier 2 Storage:** ~42GB  
**Recommended for:** Developers with >100GB storage

---

### Tier 3: Optional (Experimental/Specialized)

| Model | Size | Speed | Best For | When to Try |
|-------|------|-------|----------|------------|
| gemma4:26b | 17GB | 10 t/s | Deep analysis (slower) | When gemma4 insufficient |
| mistral-large | 14GB | 30 t/s | Complex reasoning | Alternative to qwen-7b |
| deepseek-v2 | 8GB | 40 t/s | Advanced reasoning | When available |

**Total Tier 3 Storage:** ~39GB  
**Recommended for:** Power users with >150GB storage

---

## Model Performance Benchmarks

### Speed (tokens/second) on Standard Hardware

| Model | Mac M1 | Mac Intel | Windows RTX5060Ti | Linux A100 |
|-------|--------|-----------|------------------|-----------|
| qwen-1.5b | 150 | 80 | 200 | 300 |
| qwen-7b | 50 | 30 | 80 | 150 |
| mistral | 55 | 35 | 90 | 160 |
| gemma4 | 45 | 25 | 70 | 140 |
| llava | 15 | 8 | 30 | 60 |
| deepseek-r1 | 160 | 90 | 220 | 350 |

### Quality Ranking (by category)

| Category | Rank 1 | Rank 2 | Rank 3 |
|----------|--------|--------|--------|
| Coding | qwen-7b | qwen-1.5b | mistral |
| Analysis | gemma4 | mistral | qwen-7b |
| Writing | mistral | gemma4 | qwen-7b |
| Vision | llava | N/A | N/A |
| Reasoning | deepseek-r1 | gemma4 | mistral |

---

## Monthly Model Update Checklist

### Week 1: Research New Models

**Action Items:**
- [ ] Check Ollama model library for new releases
- [ ] Read HuggingFace trending models (weekly update)
- [ ] Check Reddit r/LocalLLMs for community feedback
- [ ] Review benchmarks on LMSYS Chatbot Arena
- [ ] Look for models in these categories:
  - [ ] Faster alternatives to current models (>20% speed improvement)
  - [ ] Better quality in your most-used category
  - [ ] New specialized models (medical, legal, code-specific)

**Resources:**
- Ollama: https://ollama.ai/library
- HuggingFace: https://huggingface.co/models?sort=trending
- LMSYS: https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard
- Reddit: https://reddit.com/r/LocalLLMs

**Template Log Entry:**
```markdown
### Week 1 Research (May 18-24, 2026)

New models discovered:
1. **mistral-small** (5.1GB, 70 t/s)
   - Speed: +27% vs mistral:latest
   - Quality: Similar
   - Cost-benefit: Worth testing

2. **qwen2.5-coder:32b** (19GB, 25 t/s)
   - Speed: Slower
   - Quality: Better for complex features (+15%)
   - Cost-benefit: Maybe as Tier 2

3. **llama2-uncensored** (7B)
   - Status: Deprecated, skip

Action items:
- [ ] Test mistral-small (replace mistral:latest?)
- [ ] Benchmark qwen-32b for feature generation
- [ ] Add to Tier 2 waitlist if space available
```

---

### Week 2: Evaluate Candidates

**For each new model discovered, test:**

1. **Download & Installation Time**
   ```bash
   time ollama pull [model-name]
   # Record time, disk space
   ```

2. **Speed Benchmark** (on your hardware)
   ```bash
   time ollama run [model-name] "Explain machine learning in 100 words"
   # Time the response
   ```

3. **Quality Test** (pick 2 sample tasks from your workflow)
   ```bash
   Task 1: [Your typical easy task]
   Task 2: [Your typical hard task]
   # Rate 1-10 on accuracy, completeness, usefulness
   ```

4. **Memory Usage**
   ```bash
   ollama list  # Check memory footprint
   ```

5. **Decision: Keep / Skip / Waitlist**
   - KEEP: Faster + same quality, or significantly better quality
   - SKIP: Slower + no quality improvement
   - WAITLIST: Good candidate when you have more storage

**Benchmark Template:**
```markdown
### Model Test: [Model Name]

**Date Tested:** 2026-05-18
**Hardware:** Mac M1 Max / RTX 5060 Ti / Linux

**Specs:**
- Download time: [X minutes]
- Disk size: [X GB]
- Memory usage: [X GB when loaded]

**Speed (100-word response):**
- Time: [X seconds]
- Tokens/sec: [X]
- vs qwen-7b: [+/- X%]

**Quality Score (1-10):**
- Easy task (bug fix): [X]
- Hard task (feature): [X]
- Average: [X]

**Decision:**
- [ ] KEEP (replace current)
- [ ] SKIP (too slow/poor quality)
- [ ] WAITLIST (good but no space)

**Notes:**
[Any special observations]
```

---

### Week 3: Decision & Implementation

**For each KEEP candidate:**

1. **Replace in decision trees** (if relevant)
   - Update `decision-trees/02-coding-selection.md` if better coder
   - Update `decision-trees/07-bi-selection.md` if better analyst, etc.

2. **Update model inventory**
   - Add to `reference/model-maintenance.md`
   - Update templates/README with new model

3. **Test in real workflow**
   - Use new model on 5-10 tasks
   - Log success rate
   - Verify better than old model before removing old one

4. **Remove old model** (if replacing)
   ```bash
   ollama rm [old-model-name]
   # Free up storage
   ```

5. **Update decision trees**
   - Point to new model
   - Update cost estimates if different

**Implementation Checklist:**
```markdown
### Implementation: [New Model]

- [ ] Downloaded and tested successfully
- [ ] Decision trees updated
- [ ] Templates updated
- [ ] Tested in 5+ real workflows
- [ ] Success rate: [X]% (vs [X]% with old model)
- [ ] Old model removed (if replacing)
- [ ] Documented in model-maintenance.md
- [ ] Committed to GitHub
```

---

### Week 4: Monthly Review & Analysis

**Analyze this month's model usage:**

```markdown
## May 2026 Model Review

**Models used:** [List with task counts]
- qwen-1.5b: 15 tasks (92% success)
- qwen-7b: 28 tasks (95% success)
- mistral: 12 tasks (100% success)
- gemma4: 8 tasks (98% success)

**Performance trends:**
- Overall success: 95% (up from 94% in April)
- Speed average: 65 t/s (stable)
- Most reliable: mistral (100%)

**Storage usage:**
- Current: 27.6GB of 100GB available
- Growth: +0GB (no new models)

**New models evaluated:**
- mistral-small: KEEP (faster, same quality)
- qwen-32b: WAITLIST (good but no space)

**Actions taken:**
- Replaced mistral:latest with mistral-small
- Added deepseek-r1 to essential tier
- Removed gemma4:3.3 (redundant)

**Next month goals:**
- Maintain >95% success rate
- Find faster alternative for gemma4
- Evaluate new code-specific models

**Budget impact:**
- No new purchases (all free local models)
- Storage optimized (15.5GB freed)
- Cost savings maintained: $0/month
```

---

## How to Add a New Model

### Step 1: Verify Model Availability
```bash
# Check if model exists in Ollama library
ollama list --all | grep [model-name]
```

### Step 2: Download
```bash
ollama pull [model-name]
# Shows download progress
```

### Step 3: Test
```bash
# Quick test
ollama run [model-name] "Say hello"

# Speed benchmark
time ollama run [model-name] "Explain machine learning in 100 words"

# Memory check
ollama list
```

### Step 4: Update Documentation
- Add to `reference/model-maintenance.md`
- Update decision tree if relevant
- Update README.md with new model info

### Step 5: Integrate into Workflow
- Update `tools/model-selector-automated.py`
- Update decision trees

### Step 6: Commit
```bash
git add -A
git commit -m "Add new model: [model-name]

- Added [model-name] to Tier [X]
- Speed: [X] tokens/sec
- Best for: [Category]
- Replaces: [Optional: what it replaces]"
```

---

## How to Remove a Model

### Step 1: Verify Not in Use
```bash
# Check if model appears in decision trees
grep -r "[model-name]" decision-trees/
grep -r "[model-name]" tools/
```

### Step 2: Update Documentation First
- Remove from decision trees
- Remove from `reference/model-maintenance.md`
- Update README.md

### Step 3: Delete Model
```bash
ollama rm [model-name]
# Frees up disk space
```

### Step 4: Commit
```bash
git add -A
git commit -m "Remove model: [model-name]

- Reason: [Replaced / Redundant / Deprecated]
- Freed: [X] GB disk space
- Alternative: [New model if replaced]"
```

---

## Model Lifecycle

```
RESEARCH (Week 1)
    ↓
BENCHMARK (Week 2)
    ↓
DECISION (Week 3)
    ├→ KEEP → UPDATE DOCS → TEST → REPLACE OLD → COMMIT
    ├→ SKIP → LOG REASON → MOVE ON
    └→ WAITLIST → REVISIT NEXT MONTH

MONITOR (Week 4)
    ↓
NEXT MONTH RESEARCH
```

---

## Quarterly Deep Dive (Every 3 Months)

**Full system review:**
- [ ] Compare all Tier 1 models against latest alternatives
- [ ] Benchmark entire workflow (100 tasks)
- [ ] Calculate cost-per-task trends
- [ ] Plan for next quarter's models
- [ ] Archive old benchmarks

**Template:**
```markdown
## Q2 2026 (May-July) Model Review

**Tier 1 Current Status:**
| Model | Tasks | Success | Trend | Replace? |
|-------|-------|---------|-------|----------|
| qwen-1.5b | 50 | 92% | ↑ | No |
| qwen-7b | 120 | 95% | → | No |
| mistral | 45 | 100% | ↑ | No |
| gemma4 | 30 | 98% | → | Maybe |
| llava | 20 | 88% | ↓ | Review |

**Action items for Q3:**
- [ ] Evaluate gemma4 replacement (analyze task, not general)
- [ ] Test llava competitors
- [ ] Add deepseek-v2 when available

**Budget:** $0/month (all local)
**Storage:** 27.6GB of 100GB
**Status:** Healthy ✓
```

---

## Decision Tree: Should I Update This Model?

```
New model found
  ↓
Faster than current? (>20% speed gain)
  ├→ YES → Test quality → KEEP if same/better
  └→ NO: Check next criteria
  ↓
Better quality? (subjective, score test tasks)
  ├→ YES, significantly → Test speed → KEEP if acceptable
  └→ NO: Check next criteria
  ↓
Solving a known problem? (e.g., current model weak on medical)
  ├→ YES → Test in that domain → ADD as specialized
  └→ NO → Skip

DECISION:
- KEEP: Speed better OR quality significantly better
- ADD: Specialized (complements, doesn't replace)
- SKIP: No advantage over current setup
- WAITLIST: Good but no space (add when storage available)
```

---

## Storage Optimization Tips

**Current Usage Analysis:**

```
Essential (Tier 1):  27.6GB
  - qwen-1.5b: 1.0GB
  - qwen-7b: 4.7GB
  - mistral: 4.4GB
  - gemma4: 9.6GB
  - llava: 7.9GB

Recommended (Tier 2): 42GB
  - deepseek-r1: 1.1GB
  - bge: 0.03GB
  - llama3.3: 41GB

Optimization:
  - If space < 50GB: Keep only Tier 1 (27.6GB)
  - If space 50-100GB: Add 1-2 Tier 2 models (50-70GB)
  - If space > 100GB: Add all Tier 2 + selective Tier 3
```

**If running out of space:**
1. Archive rarely-used models (but keep benchmarks)
2. Remove Tier 3 experimental models
3. Remove old duplicate models (e.g., gemma:3.3 if you have gemma4)
4. Test with 1.5B models instead of 7B when possible

---

## Next Actions

- [ ] Run setup/ollama-installation.sh
- [ ] Test all Tier 1 models
- [ ] Schedule weekly research task
- [ ] Set calendar reminders (Weekly: Mon, Monthly: 1st Friday)
- [ ] Track in task-log-template.md
- [ ] Monthly report in monthly-report-comprehensive.md

---

See also:
- `setup/ollama-installation.sh` — Automated setup
- `tools/model-selector-automated.py` — Smart model picker
- `templates/weekly-model-research.md` — Research tracker
