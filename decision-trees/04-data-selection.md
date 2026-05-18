# Decision Tree 4: Data Processing & Analysis

Use this to choose models for CSV, JSON, databases, data cleaning, and analysis tasks.

---

## Quick Decision Matrix

| Task Type | Size | Complexity | Model | Cost | Time |
|-----------|------|-----------|-------|------|------|
| Validate CSV structure | <1M rows | Simple | qwen2.5-coder:1.5b | $0 | 20-30s |
| Clean/normalize data | 1-10M rows | Medium | qwen2.5-coder:7b | $0 | 1-3 min |
| Data transformation | 10-100M rows | High | qwen2.5-coder:7b | $0 | 2-5 min |
| Statistical analysis | Any size | Medium-high | gemma4:latest | $0 | 1-2 min |
| Detect anomalies | Time series | Complex | gemma4:latest | $0 | 2-5 min |
| Predict trends | Historical data | Complex reasoning | Claude Sonnet | $0.15-0.30 | Strategic |
| Data pipeline design | Architecture | Design | Claude Sonnet | $0.15-0.30 | Strategic |

---

## Decision Flow

```
START: I have a data task
  ↓
What's the data size and task?

A. VALIDATE / INSPECT
  ├─ Check CSV structure (columns, types, duplicates)?
  │   └─ <100K rows → qwen2.5-coder:1.5b ($0, 20s)
  │   └─ >100K rows → use pandas + qwen2.5-coder:7b ($0, 30s script)
  │
  ├─ Find missing values?
  │   └─ qwen2.5-coder:1.5b generates pandas script ($0, 15s)
  │
  └─ Explore data (histograms, correlations)?
      └─ gemma4:latest analyzes structure + recommendations ($0, 1-2 min)

B. CLEAN / NORMALIZE
  ├─ Remove duplicates?
  │   └─ qwen2.5-coder:1.5b writes pandas code ($0, 20s)
  │
  ├─ Handle missing values (imputation)?
  │   └─ qwen2.5-coder:7b (strategy selection) ($0, 1 min)
  │
  ├─ Standardize formats (dates, phone, currency)?
  │   └─ qwen2.5-coder:7b writes transformation script ($0, 1 min)
  │
  └─ Merge multiple datasets?
      └─ qwen2.5-coder:7b (join strategy) ($0, 1 min)

C. TRANSFORM
  ├─ Pivot, group-by, aggregate?
  │   └─ qwen2.5-coder:1.5b (simple aggregations) → qwen2.5-coder:7b (complex) ($0)
  │
  ├─ Feature engineering (create new columns)?
  │   └─ qwen2.5-coder:7b (logic design) ($0, 1-2 min)
  │
  └─ Create derived metrics?
      └─ qwen2.5-coder:7b + gemma4 validation ($0, 1-3 min)

D. ANALYZE
  ├─ Calculate statistics (mean, median, std)?
  │   └─ qwen2.5-coder:1.5b writes pandas code ($0, 20s)
  │
  ├─ Find patterns (clusters, outliers)?
  │   └─ gemma4:latest analyzes structure ($0, 2 min)
  │
  ├─ Time series analysis (trends, seasonality)?
  │   └─ gemma4:latest + visualization recommendation ($0, 2-3 min)
  │
  └─ Predictive modeling?
      ├─ Simple (linear regression)? → qwen2.5-coder:7b + scikit-learn ($0, 2 min)
      ├─ Complex (deep learning)? → Claude Sonnet (strategy) ($0.20)
      └─ Domain-specific (medical, financial)? → Claude ($0.30, expertise needed)

E. PIPELINE DESIGN
  ├─ How should I structure my data pipeline?
  │   └─ Claude Sonnet (architecture decision) ($0.15-0.30)
  │
  ├─ Should I use Airflow, Prefect, or Dagster?
  │   └─ Claude Sonnet ($0.15-0.30, strategic)
  │
  └─ Optimize query performance?
      └─ Claude + qwen2.5-coder:7b ($0.15 design + $0 implementation)
```

---

## Model Details

### qwen2.5-coder:1.5b → Data Validation Scripts
**Best for:** Simple data inspection, validation rules

**Examples:**
- "Check if all email addresses in this CSV are valid"
- "Count missing values in each column"
- "Find duplicate rows in this dataset"

**Output:** Pandas script (15-30 lines)

---

### qwen2.5-coder:7b → Data Transformation
**Best for:** Cleaning, transforming, aggregating data

**Examples:**
- "Normalize date formats from 'Jan 1, 2024' and '01/01/2024' to ISO"
- "Merge these two CSVs on user_id and keep non-duplicates"
- "Create rolling 7-day average of this time series"
- "One-hot encode these categorical columns"

**Performance:** 
- Handles 100M+ rows if SQL-based (generates efficient code)
- 1-2 minutes per task
- Quality: 90%+ correct logic

---

### gemma4:latest → Data Analysis & Pattern Detection
**Best for:** Finding patterns, statistical reasoning, insights

**Examples:**
- "Analyze this sales data and identify seasonal trends"
- "What are the top predictors of customer churn?"
- "Summarize the distribution of this dataset"
- "Detect anomalies in this time series"

**Performance:**
- Speed: 45 tokens/sec (slower but better reasoning)
- Quality: 95%+ insight accuracy
- Good for: Strategic recommendations, not just code

---

### Claude Sonnet → Data Strategy & Complex Reasoning
**Best for:** Architecture decisions, complex analysis, domain expertise

**Examples:**
- "Design a data pipeline for a 10B+ row analytics system"
- "How should I approach this forecasting problem?"
- "What ML model is best for detecting fraud in this dataset?"
- "Optimize this slow SQL query (strategic review)"

---

## Real-World Examples

### Example 1: CSV Validation & Cleaning
```
Task: Validate and clean 500K row customer dataset
Approach:
  1. qwen2.5-coder:1.5b check structure + missing values ($0, 20s)
  2. qwen2.5-coder:7b write cleaning script ($0, 1 min)
     - Remove duplicates
     - Normalize phone/email formats
     - Fill missing values (strategy)
  3. Run script ($0, 30s execution)
  4. gemma4 validate results ($0, 1 min)
Total cost: $0
Total time: ~5 minutes
Output: Clean 500K rows, removed 5% duplicates, 98% complete
```

### Example 2: Feature Engineering for ML
```
Task: Create features for customer churn prediction model
Approach:
  1. qwen2.5-coder:7b write feature engineering script ($0, 2 min)
     - Recency, frequency, monetary (RFM)
     - Engagement metrics
     - Account age in days
  2. gemma4 analyze correlation with target ($0, 1 min)
  3. qwen2.5-coder:7b select top features ($0, 30s)
Total cost: $0
Total time: ~5 minutes
Output: 15 engineered features, ready for model training
```

### Example 3: Time Series Analysis
```
Task: Analyze 2-year daily stock price data for trends
Approach:
  1. qwen2.5-coder:1.5b load + visualize ($0, 1 min)
  2. gemma4 identify patterns (volatility, trends, seasonality) ($0, 2 min)
  3. qwen2.5-coder:7b generate forecast (moving averages) ($0, 1 min)
Total cost: $0
Total time: ~5 minutes
Output: Trend analysis + 30-day forecast
Quality: 85-90% accuracy for short-term forecasts
```

### Example 4: Complex Data Strategy (Escalate)
```
Task: Design analytics pipeline for 100M event log rows per day
Approach:
  1. Claude Sonnet design architecture ($0.25, 3 min)
     - Should we use Kafka → Spark → BigQuery?
     - How to handle late-arriving data?
     - What metrics to pre-aggregate?
  2. qwen2.5-coder:7b implement infrastructure-as-code ($0, 5 min)
Total cost: $0.25
Total time: ~10 minutes
Output: Architecture diagram, cost projections, implementation steps
```

---

## Database Queries

### When to use qwen2.5-coder models:
- Simple SELECT queries with JOINs → qwen2.5-coder:1.5b
- Complex aggregations, window functions → qwen2.5-coder:7b
- Query optimization (add indexes, rewrite logic) → qwen2.5-coder:7b

### When to use Claude:
- "How should I design my schema for 10B rows?" → Claude ($0.15-0.25)
- "Optimize this slow query (performance-critical)" → Claude ($0.15-0.25)

---

## Tool Recommendations

### Python (recommended)
- **pandas:** Data manipulation (qwen2.5-coder generates pandas code)
- **polars:** Faster for large datasets (newer, qwen2.5-coder:7b handles)
- **scikit-learn:** Basic ML (qwen2.5-coder:7b generates models)
- **scipy/numpy:** Statistical analysis (qwen2.5-coder:7b)

### SQL
- **DuckDB:** Fast local analytics on CSV/Parquet
- **SQLite:** Lightweight local database
- **PostgreSQL:** Production analytics (qwen generates SQL)

### Visualization
- **matplotlib/seaborn:** Python plotting (qwen2.5-coder generates)
- **Plotly:** Interactive dashboards (qwen2.5-coder:7b)

---

## Cost Optimization Tips

**For 1M+ rows:**
- Don't try to load all in memory
- Use SQL or streaming approach (qwen2.5-coder:7b generates this)
- Cost: Still $0, but execution is faster

**For repeated analysis:**
- Build pipeline once → run many times
- Cost: First pipeline $0, then $0 per run

**For machine learning:**
- Start with qwen2.5-coder:7b + scikit-learn
- Only escalate to Claude for strategy decisions
- Cost savings: 95% (code generation free, architecture decision $0.15-0.25 once)

---

## Troubleshooting

**Qwen generates slow queries:**
- Run EXPLAIN ANALYZE to see the issue
- Add indexes based on EXPLAIN output
- Re-optimize with qwen2.5-coder:7b or Claude

**Analysis doesn't make sense:**
- Verify data quality first (check for outliers)
- Escalate to Claude for interpretation ($0.10)

**Data too large to fit in memory:**
- Use dask (pandas for big data) — qwen2.5-coder:7b generates this
- Or use SQL streaming approach

---

## When to Escalate to Claude

| Situation | Cost |
|-----------|------|
| "Design data warehouse for 100B rows" | $0.25 |
| "Optimize slow analytics query (performance critical)" | $0.15 |
| "Is this the right statistical test?" (domain expertise) | $0.10 |
| "How to handle imbalanced data in ML?" | $0.15 |

All other tasks: use local Ollama models ($0).

---

## Next Steps

1. **Try qwen2.5-coder:1.5b** on next data validation task
2. **Log cleaning time** — document how long pipeline takes
3. **Track accuracy** — if model generates wrong logic, note it
4. **Escalate strategically** — only use Claude for decisions that recur

See: `reference/monthly-metrics.md` for tracking data task costs.
