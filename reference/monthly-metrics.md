# Monthly Metrics Guide

Track these metrics every month to optimize your model selection and stay under budget.

---

## Key Metrics to Measure

### 1. Task Volume & Type Distribution

**Track:** How many tasks of each type you completed

```
| Category | Tasks | % of Total |
|----------|-------|-----------|
| Coding | 25 | 42% |
| Data | 12 | 20% |
| Writing | 10 | 17% |
| BI | 8 | 13% |
| Security | 4 | 7% |
| Other | 1 | 2% |
| TOTAL | 60 | 100% |
```

**Why:** Identifies where most of your time goes. If 42% is coding, optimize your coding workflow first.

---

### 2. Model Success Rates

**Track:** Which models delivered working code first time

```
| Model | Tasks | Successes | Rate |
|-------|-------|-----------|------|
| qwen-1.5b | 15 | 14 | 93% |
| qwen-7b | 25 | 24 | 96% |
| mistral | 10 | 10 | 100% |
| gemma4 | 8 | 8 | 100% |
| Claude | 2 | 2 | 100% |
| TOTAL | 60 | 58 | 97% |
```

**Why:** Shows which models are most reliable for your workflow. If Claude is 100% but costs $X, decide if worth it vs 96% local for $0.

---

### 3. Cost Efficiency

**Track:** Actual cost vs budget projection

```
Budget allocated: $120.00
Spent:
  - Week 1: $12.50 (Claude 5 calls)
  - Week 2: $8.25 (Claude 3 calls + premium)
  - Week 3: $0 (all local)
  - Week 4: $5.00 (Claude 2 calls)
Total spent: $25.75
Remaining: $94.25
Status: ON TRACK (21% of budget used in 4 weeks)

Cost per task: $0.43
Cost if pure Claude: $192 (60 tasks @ $3.20 avg)
Savings: $166 (86% reduction)
```

**Why:** Ensures you stay under $120/month. Alerts you to overspending patterns.

---

### 4. Time Savings

**Track:** Actual time spent vs estimated manual time

```
| Category | Tasks | AI Time | Manual Time | Saved |
|----------|-------|---------|------------|-------|
| Coding | 25 | 45 min | 25 hours | 24h 15m |
| Data | 12 | 20 min | 12 hours | 11h 40m |
| Writing | 10 | 30 min | 15 hours | 14h 30m |
| BI | 8 | 18 min | 8 hours | 7h 42m |
| TOTAL | 55 | 113 min | 60 hours | 58h 7m |

Hourly value (avg $100/h): $5,807 saved
```

**Why:** Quantifies the actual value of automation. Use this in ROI conversations.

---

### 5. Escalation Rate

**Track:** How often you had to move from local to Claude

```
Total tasks: 60
Escalations to Claude: 7 (11.7%)

Reasons:
  - Ambiguous requirements: 2 (0.3% cost impact)
  - Complex logic needed: 3 (0.6% cost impact)
  - Strategic decision: 2 (0.2% cost impact)
  
Cost of escalations: $8.75
Value if all had failed locally: $42 (5 more Claude attempts)
```

**Why:** If escalation rate is >15%, might need to adjust task scoping. If <5%, might be over-using local models.

---

### 6. Model Specialization

**Track:** Which models work best for each task type

```
Coding:
  - qwen-1.5b: Bug fixes only (95% success)
  - qwen-7b: Features (96% success) ✓ PRIMARY
  - Claude: Architecture (100% success) — use strategically

Data:
  - qwen-7b: Transformation (95% success) ✓ PRIMARY
  - gemma4: Analysis (100% success)
  - Claude: Strategy (100% success) — $0.20/call

Writing:
  - mistral: All tasks (100% success) ✓ PRIMARY
  - gemma4: Summaries (98% success)

BI:
  - qwen-7b: Dashboards (96% success) ✓ PRIMARY
  - gemma4: Analysis (100% success)
```

**Why:** Identifies the optimal model for each task type, improving both speed and cost.

---

### 7. Workflow Efficiency

**Track:** Time from task assignment to delivery

```
| Phase | Time | Notes |
|-------|------|-------|
| Classification (decide model) | 20s | Use decision trees |
| Execution (generate code) | 2m | Qwen at 50 t/sec |
| Review & test | 3m | Always verify |
| Deployment | 1m | Push or run locally |
| Logging (document result) | 1m | For future optimization |
| TOTAL per task | 7m | Average across all categories |
```

**Why:** Shows where time is spent. If review takes 10m on average, your models might need adjustment.

---

### 8. Budget Health

**Track:** Your spending trend

```
| Month | Spent | Budget | % Used | Trend |
|-------|-------|--------|--------|-------|
| April | $45 | $120 | 38% | — |
| May | $26 | $120 | 22% | ▼ Decreasing (good!) |
| June (proj) | $20 | $120 | 17% | ▼ Better model selection |

Trend analysis:
- April: High usage while learning framework
- May: Better model selection (mostly $0 local)
- June: Projection based on 2-week actual

Recommendation: If trend continues, can increase to 200+ tasks/month
within same $120 budget.
```

**Why:** Identifies cost improvement trends. Shows if you're getting better at choosing cheap models.

---

## Monthly Reporting Template

Use this to fill in your own metrics at month-end:

```markdown
## [Month Year] — Metrics Summary

### Tasks Completed: [N]
- Coding: [N]
- Data: [N]
- Writing: [N]
- Other: [N]

### Success Rates
- qwen-1.5b: [X]%
- qwen-7b: [X]%
- mistral: [X]%
- gemma4: [X]%
- Claude: [X]%
- Overall: [X]%

### Cost Analysis
- Total spent: $[X]
- Budget remaining: $[X]
- Cost per task: $[X]
- Savings vs pure Claude: $[X]

### Time Savings
- Total AI time: [X]h [X]m
- Equivalent manual time: [X]h
- Hours saved: [X]h
- Value @ $100/h: $[X]

### Escalations
- Total: [N]
- % of tasks: [X]%
- Reasons: [list]
- Cost: $[X]

### Best Performing Model
- Model: [Name]
- Success rate: [X]%
- Best for: [Category]

### Worst Performing Model
- Model: [Name]
- Success rate: [X]%
- Recommendation: [Action]

### Key Insights
- [Insight 1]
- [Insight 2]
- [Insight 3]

### Recommendations for Next Month
- Continue: [What worked]
- Try: [What to test]
- Stop: [What didn't work]
```

---

## Dashboard Visualization (Optional)

If you want to visualize metrics, create a simple dashboard with:

```python
import pandas as pd
import plotly.express as px

# Load monthly data
metrics = pd.read_csv('monthly_metrics.csv')

# Chart 1: Task volume by category
fig1 = px.pie(metrics, values='tasks', names='category', title='Tasks by Category')

# Chart 2: Cost trend
fig2 = px.line(metrics, x='month', y='cost', title='Monthly Spending')

# Chart 3: Success rate by model
fig3 = px.bar(metrics, x='model', y='success_rate', title='Model Success Rates')

# Chart 4: Time savings trend
fig4 = px.line(metrics, x='month', y='hours_saved', title='Hours Saved Over Time')
```

Cost: $0 (use local Python + Plotly)

---

## Quality Gates

Set minimum thresholds for healthy operation:

```
✓ Success rate: >90% (indicates good model selection)
✓ Local model usage: >80% (indicates cost efficiency)
✓ Escalation rate: <15% (indicates good task scoping)
✓ Budget tracking: <$120/month (indicates cost control)
✓ Logging accuracy: >95% (indicates good discipline)
```

If any gate drops below threshold, review your workflow.

---

## Continuous Improvement Cycle

```
Month 1: Establish baseline
  - Track all metrics
  - Identify best/worst performers
  - Establish baseline costs

Month 2: Optimize
  - Promote best models
  - Retrain on worst models
  - Adjust task classification

Month 3: Scale
  - Increase task volume
  - Reduce per-task time
  - Maintain cost control

Month 4+: Maintain
  - Track metrics ongoing
  - Alert on anomalies
  - Quarterly reviews
```

---

## Red Flags to Watch

| Metric | Red Flag | Action |
|--------|----------|--------|
| Success rate < 80% | Models unreliable | Retrain or escalate |
| Cost > $120/month | Budget overrun | Reduce Claude usage |
| Escalation rate > 20% | Tasks unclear | Better scoping |
| Time per task > 10m | Inefficient workflow | Review process |
| Local model usage < 60% | Using Claude too much | Use decision tree strictly |

---

## Annual Review

After 12 months of data, analyze:

1. **Total tasks completed:** [N]
2. **Total cost:** $[X]
3. **Total time saved:** [X] hours
4. **Hourly value:** $[X,XXX]
5. **ROI:** [X]x return
6. **Best model overall:** [Model]
7. **Most common task:** [Category]
8. **Biggest time saver:** [Category]
9. **Areas for improvement:** [List]
10. **Next year targets:** [Goals]

Use this for planning next year's budget and tool investments.

---

See also:
- `templates/monthly-cost-report.md` — Full cost report template
- `templates/task-log-template.md` — Where to log task data
- `templates/weekly-report-template.md` — Weekly tracking
