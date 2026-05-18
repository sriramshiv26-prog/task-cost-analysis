# Weekly Model Research & Evaluation Template

Use this template every Monday to track new models discovered and evaluate their potential.

---

## Week of [MM/DD - MM/DD, YYYY]

**Research Date:** [YYYY-MM-DD]  
**Researcher:** [Your name]

---

## New Models Discovered This Week

### Model 1: [Model Name]

**Source:** [Where found: Ollama library / HuggingFace / Reddit / Other]  
**Publication Date:** [If available]  
**Repository:** [Link to GitHub / HuggingFace]

**Specifications:**
- **Size:** [X.X GB]
- **Parameters:** [X.X B if available]
- **Base Model:** [E.g., "based on Llama2" if known]
- **License:** [E.g., MIT, Apache 2.0]

**Initial Assessment:**
```
Category: [Coding | Data | Writing | Analysis | Vision | Reasoning | Other]
Speed estimate: [Based on size, likely X tokens/sec]
Quality promise: [Marketing claim / community feedback]
Current comparison: [E.g., "faster alternative to mistral"]
```

**Reason for Interest:**
- [ ] Faster than existing model in this category
- [ ] Better quality (claims or user reviews)
- [ ] Specialized (e.g., medical, legal, code-specific)
- [ ] Smaller (better for limited storage)
- [ ] Other: [description]

**Priority to Test:** [HIGH / MEDIUM / LOW]  
**Estimated Value:** [Might replace / Might add as Tier 2 / Skip]

---

### Model 2: [Model Name]
[Repeat above format for each new model]

---

## Models to Test This Week

| Model | Tests to Run | Priority | By When |
|-------|-------------|----------|---------|
| [Model] | Download, speed test, quality test (2 sample tasks) | HIGH | By Friday |
| [Model] | Download, speed test | MEDIUM | By end of week |

---

## Testing Results

### Test 1: [Model Name]

**Download & Setup:**
- Download time: [X minutes]
- Disk size: [X.X GB]
- Installation notes: [Any issues?]
- Status: [✓ Success / ⚠ Issues / ✗ Failed]

**Performance Benchmark:**
```
Hardware: [Your hardware, e.g., "Mac M1 Max"]
Test task: "Explain machine learning in 100 words"
Time to generate: [X seconds]
Tokens/sec: [X]
vs [Current model]: [+/- X%]
Quality: [1-10 score]
```

**Quality Test 1 (Easy Task):**
```
Task: [Your typical quick task, e.g., "Fix this Python error: [error]"]
Model response quality: [1-10]
Accuracy: [1-10]
Usefulness: [1-10]
Notes: [Any observations]
```

**Quality Test 2 (Hard Task):**
```
Task: [Your typical complex task, e.g., "Design API for..."]
Model response quality: [1-10]
Accuracy: [1-10]
Usefulness: [1-10]
Notes: [Any observations]
```

**Overall Assessment:**
- Speed: [Faster / Same / Slower than target]
- Quality: [Better / Same / Worse than target]
- Stability: [Stable / Occasional errors / Frequent issues]
- Memory: [Clean shutdown / Memory leaks / Crashes]

**Decision:**
- [ ] KEEP — Replace current model
- [ ] ADD — Keep alongside current (specialized)
- [ ] SKIP — No advantage
- [ ] WAITLIST — Good but no space now

**Why?**
[Explain reasoning]

---

### Test 2: [Model Name]
[Repeat above format for each tested model]

---

## Weekly Summary

### Models to Action This Week
- [ ] [Model X] — KEEP: Update decision trees, replace old model
- [ ] [Model Y] — ADD as Tier 2: Update docs
- [ ] [Model Z] — WAITLIST: Revisit next month

### Models to Skip
- [Model A]: No speed advantage
- [Model B]: Deprecated / Not available in Ollama
- [Model C]: Community feedback negative

### Next Week's Research Plan
- [ ] Check [X source] for new code models
- [ ] Evaluate [Y model] when released
- [ ] Benchmark [Z model] against current

---

## Evaluation Scores

### Comparison Matrix (vs Current Primary Model)

| Criteria | Score (1-10) | Notes |
|----------|-------------|-------|
| Speed | [X] | Faster/slower than current? |
| Quality | [X] | Better/worse accuracy? |
| Stability | [X] | Any crashes or errors? |
| Storage | [X] | Size acceptable? |
| Availability | [X] | Easy to install / maintain? |
| **Overall** | **[X]** | **Keep/Add/Skip/Waitlist?** |

---

## Decision: Keep or Skip?

**KEEP Criteria (must meet at least one):**
- [ ] >20% faster with same quality
- [ ] Significantly better quality (>2 points on scale)
- [ ] Specialized (solves known problem)
- [ ] Better for majority of your tasks

**SKIP Criteria (if any apply):**
- [ ] Slower with no quality advantage
- [ ] Installation issues or instability
- [ ] Community reports serious problems
- [ ] Not actively maintained

**WAITLIST Criteria:**
- [ ] Good candidate but no storage space
- [ ] Emerging but not ready yet
- [ ] Community reviews still pending

---

## Documentation Updates (if KEEP)

If you decided to KEEP this model:

- [ ] Update `reference/model-maintenance.md`
  - Add to appropriate tier
  - Update performance benchmarks
  - Note what it replaces (if applicable)

- [ ] Update decision trees
  - `02-coding-selection.md` if code-related
  - `07-bi-selection.md` if analysis-related
  - etc.

- [ ] Update `tools/model-selector-automated.py`
  - Add model to recommendations
  - Update cost/speed estimates

- [ ] Update `README.md`
  - Update model inventory section
  - Update quick links if relevant

- [ ] Commit to GitHub
  ```bash
  git add -A
  git commit -m "Add model: [Model Name]

  - Speed: [X] tokens/sec
  - Best for: [Category]
  - Replaces: [Optional]
  - Tested: [Date]"
  ```

---

## Monthly Aggregate

**Used by:** `monthly-report-comprehensive.md`

### Models Evaluated This Month
- Total discovered: [N]
- Tested: [N]
- Added (KEEP): [N]
- Waitlisted: [N]
- Skipped: [N]

### Tier Changes
- Added to Tier 1: [List]
- Added to Tier 2: [List]
- Removed: [List]
- Promoted (Tier 2 → 1): [List]

### Cumulative Effectiveness
- Storage used: [X] GB
- Models available: [N]
- Average success rate: [X]%
- Cost: $0/month (all local)

---

## Resource Links

**Model Discovery:**
- Ollama: https://ollama.ai/library
- HuggingFace: https://huggingface.co/models?sort=trending
- LMSYS Arena: https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard
- Reddit: https://reddit.com/r/LocalLLMs

**Benchmarking:**
- Open LLM Leaderboard: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
- LMSYS: https://chat.lmsys.org
- Local benchmark: Use `tools/cost-calculator.py`

---

## Next Week

- Research date: [Next Monday]
- Models to evaluate: [List any from WAITLIST or known upcoming]
- Focus areas: [E.g., "Find faster code model", "Test gemma4 competitors"]

---

**Sign-off:**
- Researcher: [Name]
- Date: [YYYY-MM-DD]
- Changes committed to GitHub: [Yes / No]
- Next review: [Date]
