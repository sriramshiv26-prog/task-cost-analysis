# Token Budgeting Guide

Understand token consumption to accurately predict costs.

---

## What are Tokens?

**Token ≈ 4 characters**

```
Word "example" = 2 tokens (ex + ample)
Sentence "The quick brown fox" = 5-7 tokens
Paragraph (200 words) = 250-350 tokens
Page of text = 500-800 tokens
```

---

## Typical Token Counts by Task

### Coding Tasks

| Task | Tokens |
|------|--------|
| Bug fix (< 50 lines) | 100-300 |
| Simple function (< 100 lines) | 200-500 |
| Feature (100-500 lines) | 500-1500 |
| Complex system (500+ lines) | 1500-5000 |
| API endpoint + tests | 800-2000 |
| Full microservice | 3000-10000 |

**Rule of thumb:** ~3-5 tokens per line of code

### Data Tasks

| Task | Tokens |
|------|--------|
| Data validation script | 200-500 |
| Cleaning pipeline | 400-1000 |
| Analysis query | 300-800 |
| ML model code | 1000-3000 |
| Full data pipeline | 2000-5000 |

### Writing Tasks

| Task | Tokens |
|------|--------|
| Short email | 100-200 |
| Product description | 200-400 |
| Blog post (500 words) | 300-600 |
| Tutorial (2000 words) | 800-1500 |
| Research paper outline | 1000-2000 |
| Full research paper | 5000-15000 |

**Rule of thumb:** ~0.75 tokens per word

### Analysis Tasks

| Task | Tokens |
|------|--------|
| Data analysis | 300-800 |
| Trend identification | 200-500 |
| Insights generation | 400-1000 |
| Complex reasoning | 800-2000 |

---

## Token Cost Examples

### Local Models (Ollama) = $0

```
1,000 tokens = $0.00
10,000 tokens = $0.00
100,000 tokens = $0.00

All local models: No per-token cost.
Only hardware cost (CPU/GPU).
```

### Claude Sonnet

```
Input pricing: $3 per 1M tokens
Output pricing: $15 per 1M tokens

Example 1: 1,000 input tokens
  Cost = (1,000 / 1,000,000) × $3 = $0.003

Example 2: 10,000 input tokens + 5,000 output
  Cost = (10,000 / 1,000,000) × $3 + (5,000 / 1,000,000) × $15
  Cost = $0.03 + $0.075 = $0.105

Example 3: Batch analysis (50,000 input tokens)
  Cost = (50,000 / 1,000,000) × $3 = $0.15
```

---

## Budget Scenarios

### Scenario 1: Mostly Local (90% Ollama, 10% Claude)

```
Per month: 100 tasks

Task distribution:
  - 90 tasks with Ollama (free)
    Avg 1,000 tokens per task = 90,000 tokens
    Cost: $0.00

  - 10 tasks with Claude (strategic decisions)
    Avg 2,000 tokens = 20,000 tokens input
    Avg 1,000 tokens = 10,000 tokens output
    Cost per task: (2,000 × $0.000003) + (1,000 × $0.000015) = $0.006 + $0.015 = $0.021
    10 tasks: 10 × $0.021 = $0.21

Total monthly cost: $0.21
Budget: $120/month
Efficiency: 0.17% of budget used
```

### Scenario 2: Balanced (70% Ollama, 30% Claude)

```
Per month: 100 tasks

  - 70 tasks with Ollama
    Cost: $0.00

  - 30 tasks with Claude (avg 1,500 tokens)
    30 × $0.045 (estimated per-task cost)
    Cost: $1.35

Total monthly cost: $1.35
Budget: $120/month
Efficiency: 1.1% of budget used
```

### Scenario 3: Heavy Claude (30% Ollama, 70% Claude)

```
Per month: 100 tasks

  - 30 tasks with Ollama
    Cost: $0.00

  - 70 tasks with Claude (avg 1,000 tokens)
    70 × $0.030
    Cost: $2.10

Total monthly cost: $2.10
Budget: $120/month
Efficiency: 1.75% of budget used
```

**All scenarios stay under $120 budget. Even heavy Claude usage is extremely cheap.**

---

## Token Estimation Techniques

### Technique 1: Word Count Method
**For text/writing tasks:**
```
Tokens ≈ Word Count × 0.75 to 1.0

Example: "Write a 500-word blog post"
Estimated tokens: 500 × 0.75 = 375 tokens (input)
Expected output: 500 words = 375 tokens
Total: ~750 tokens
Cost with Claude: 750 × $0.000003 (avg) = $0.002
```

### Technique 2: Line Count Method
**For code:**
```
Tokens ≈ Lines of Code × 3 to 5

Example: "Generate a 200-line Python script"
Estimated tokens: 200 × 4 = 800 tokens input
Expected output: Same size = 800 tokens
Total: ~1,600 tokens
Cost with Claude: 1,600 × $0.000003 (avg) = $0.005
```

### Technique 3: Historical Data Method
**Track your own patterns:**
```
After 10 tasks, calculate your average:

Task 1: 320 tokens
Task 2: 450 tokens
Task 3: 280 tokens
...
Average: 380 tokens per task

Future estimates: Use 380 as your baseline
```

### Technique 4: Model Feedback
**Many tools show token counts:**
```
After using Claude API, you get:
  Input tokens: 1,234
  Output tokens: 567
  Total: 1,801 tokens

Use this for future predictions.
```

---

## Token Optimization Tips

### 1. Be Specific in Prompts
```
Bad: "Write code to process data"
Tokens: Requires clarification, more back-and-forth

Good: "Write Python code to read CSV, validate email column, export valid rows to JSON"
Tokens: Self-contained, fewer iterations

Savings: 50-100 tokens per task (fewer clarifications)
```

### 2. Batch Similar Tasks
```
Instead of:
  Task 1: "Generate email template 1" (300 tokens)
  Task 2: "Generate email template 2" (300 tokens)
  Task 3: "Generate email template 3" (300 tokens)
  Total: 900 tokens

Do this:
  Batch: "Generate 3 email templates for [context]" (600 tokens)
  Total: 600 tokens

Savings: 300 tokens (33%)
```

### 3. Use Code Examples
```
If your task needs context, provide example rather than describe:

Bad: "Generate code that handles user authentication with JWT tokens,
refresh tokens, and session management"
Tokens: ~200 for description

Good: [Provide 50-line example of existing auth code]
"Modify this to add role-based access control"
Tokens: 50 for code + 100 for request = 150 total

Savings: 50 tokens (25%)
```

### 4. Reuse Generated Code
```
First task: "Generate data validation library" (1,000 tokens)
Second task: "Add field X to the validator" (100 tokens)

vs

Second task: "Generate from scratch" (800 tokens)

Savings: 700 tokens (87.5%)
```

---

## Monthly Token Budget

### Sample Budget (100 tasks/month)

```
Local Ollama tasks (90 tasks):
  - Avg 800 tokens per task
  - Total: 72,000 tokens
  - Cost: $0

Claude tasks (10 tasks):
  - Avg 2,000 tokens per task
  - Total: 20,000 tokens
  - Cost: (20,000 / 1,000,000) × $3 (average of input/output mix)
  - Cost: $0.06

Total: $0.06 / month

Budget: $120 / month
Efficiency: 0.05% of budget used
```

---

## Token Counter Tools

### Option 1: Claude API Directly
After calling Claude API, response shows:
```json
{
  "usage": {
    "input_tokens": 1234,
    "output_tokens": 567
  }
}
```

### Option 2: Python Script
```python
import tiktoken

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
text = "Your text here"
tokens = len(encoding.encode(text))
print(f"Token count: {tokens}")
```

### Option 3: Online Counter
https://platform.openai.com/tokenizer (works for most LLMs)

---

## Cost Projection Formulas

### Formula 1: Per-Task Average
```
Cost per task = (input_tokens + output_tokens) × (token_price / 1,000,000)

Example:
  Input: 1,000 tokens
  Output: 500 tokens
  Claude price: $3/M input, $15/M output
  Cost = (1,000 × $0.000003) + (500 × $0.000015)
  Cost = $0.003 + $0.0075 = $0.0105 per task
```

### Formula 2: Monthly Budget
```
Monthly cost = Tasks × Cost per task

If 100 tasks/month at $0.01 average:
  Monthly = 100 × $0.01 = $1.00
  Annual = $12.00

(Well under $120/month budget)
```

### Formula 3: Task Complexity Multiplier
```
Simple task: 1x tokens
Medium task: 2x tokens
Complex task: 4x tokens

If your average is 1,000 tokens:
  Simple: 1,000 tokens
  Medium: 2,000 tokens
  Complex: 4,000 tokens
```

---

## Token Limits by Model

| Model | Max Tokens | Notes |
|-------|-----------|-------|
| qwen-2.5-coder | 32K | Can handle most tasks |
| mistral | 32K | Good for large documents |
| gemma4 | 8K | Sufficient for most analysis |
| llava | 4K | Good for images + context |
| Claude Sonnet | 200K | Can process entire books |

---

## Tracking Token Usage

### Weekly Log Template
```markdown
## Week of [Date]

| Task | Model | Input Tokens | Output Tokens | Cost |
|------|-------|-------------|--------------|------|
| [Task 1] | qwen-7b | N/A | N/A | $0 |
| [Task 2] | Claude | 1,200 | 500 | $0.009 |
| [Task 3] | qwen-7b | N/A | N/A | $0 |

Total tokens: 1,700
Total cost: $0.009
```

Use for accurate budget forecasting.

---

See also:
- `reference/monthly-metrics.md` — How to track metrics
- `tools/cost-calculator.py` — Automated cost calculation
