# Decision Tree 7: Business Intelligence & Reporting

Use this for dashboards, reports, forecasts, metrics, and business analysis.

---

## Quick Decision Matrix

| Task Type | Data | Complexity | Model | Cost | Time |
|-----------|------|-----------|-------|------|------|
| Generate report (static) | <1M rows | Simple | qwen2.5-coder:7b | $0 | 1-2 min |
| Create dashboard | Any size | Medium | qwen2.5-coder:7b | $0 | 2-5 min |
| Analyze metrics/trends | Time series | Medium | gemma4:latest | $0 | 2-3 min |
| Forecast (simple) | Historical data | Medium | gemma4:latest | $0 | 2 min |
| Forecast (complex) | Multiple variables | Complex | Claude Sonnet | $0.20-0.30 | 5-10 min |
| BI strategy/architecture | N/A | Strategic | Claude Sonnet | $0.15-0.30 | Strategic |

---

## Decision Flow

```
START: I need a report, dashboard, or analysis
  ↓
What's the goal?

A. STATIC REPORTS
  ├─ Generate PDF/HTML report?
  │   └─ qwen2.5-coder:7b (template + code) ($0, 1-2 min)
  │
  ├─ Create summary with key metrics?
  │   └─ gemma4:latest (analysis + summary) ($0, 1-2 min)
  │
  └─ Multi-page report with visuals?
      └─ qwen2.5-coder:7b (generate code) ($0, 2 min)

B. DASHBOARDS
  ├─ Tableau/Power BI dashboard?
  │   └─ qwen2.5-coder:7b (DAX/Tableau script) ($0, 2-3 min)
  │
  ├─ Python dashboard (Plotly, Streamlit)?
  │   └─ qwen2.5-coder:7b (full code) ($0, 2-5 min)
  │
  └─ Dashboard strategy (what metrics to show)?
      └─ Claude Sonnet (business logic) ($0.15-0.20)

C. ANALYSIS
  ├─ Analyze sales trends?
  │   └─ gemma4:latest (statistical analysis) ($0, 2 min)
  │
  ├─ Find anomalies in metrics?
  │   └─ gemma4:latest (pattern detection) ($0, 2-3 min)
  │
  ├─ Compare performance (A/B test)?
  │   └─ qwen2.5-coder:7b (statistical test) ($0, 1 min)
  │
  └─ Deep business analysis?
      └─ Claude Sonnet (expert reasoning) ($0.20-0.30)

D. FORECASTING
  ├─ Simple trend forecast (moving average)?
  │   └─ qwen2.5-coder:7b (code) ($0, 1 min)
  │
  ├─ Time series forecast (ARIMA, Prophet)?
  │   └─ qwen2.5-coder:7b (code generation) ($0, 2 min)
  │
  └─ Complex forecast (multiple factors)?
      └─ Claude Sonnet (strategy) ($0.20-0.30)
      └─ qwen2.5-coder:7b (implementation) ($0)

E. BI ARCHITECTURE
  └─ How should I structure my BI system?
      └─ Claude Sonnet (strategic) ($0.20-0.30)
```

---

## Model Selection

### qwen2.5-coder:7b → Report & Dashboard Generation
**Best for:** 
- Generating SQL queries for data extraction
- Creating dashboard code (Python, JavaScript)
- Report template generation
- Visualization scripts

**Examples:**
- "Generate a Streamlit dashboard showing sales by region"
- "Create SQL query for monthly revenue report"
- "Write Plotly code for this data"
- "Generate Python script for PDF report"

**Speed:** 50 tokens/sec (2-5 minute tasks typical)

---

### gemma4:latest → Metrics Analysis & Insights
**Best for:**
- Trend analysis (finding patterns)
- Anomaly detection
- Statistical analysis
- Business insight generation
- Summarizing data findings

**Examples:**
- "Analyze this sales data for seasonal trends"
- "What's driving customer churn?"
- "Summarize key metrics from this dataset"
- "Detect anomalies in this time series"

**Speed:** 45 tokens/sec
**Quality:** 95%+ accuracy for insights

---

### Claude Sonnet → Strategic BI Decisions
**Best for:**
- "How should I design my analytics warehouse?"
- "What metrics should my dashboard track?"
- "How to forecast this with multiple variables?"
- "What's the best forecasting model for my use case?"

---

## Real-World Examples

### Example 1: Sales Dashboard
```
Task: Create dashboard showing sales by region, product, time
Approach:
  1. qwen2.5-coder:7b write Streamlit code ($0, 3 min)
     - Load data from CSV/database
     - Create filters (region, product, date)
     - Generate charts
  2. gemma4 suggest additional metrics ($0, 1 min)
  3. Deploy dashboard
Total cost: $0
Total time: 10-15 minutes
Output: Interactive dashboard (Python Streamlit)
```

### Example 2: Metrics Analysis
```
Task: Analyze quarterly sales trends
Approach:
  1. Load data (pandas, qwen2.5-coder:1.5b script) ($0, 20s)
  2. gemma4 analyze trends, seasonality, anomalies ($0, 2 min)
  3. Generate summary with insights
Total cost: $0
Total time: 5 minutes
Output: Trend analysis + business insights
```

### Example 3: Forecasting
```
Task: Forecast monthly revenue for next 6 months
Approach:
  1. qwen2.5-coder:7b write forecasting code (Prophet/ARIMA) ($0, 2 min)
  2. gemma4 analyze forecast accuracy ($0, 1 min)
  3. Generate forecast with confidence intervals
Total cost: $0
Total time: 10 minutes
Output: 6-month forecast with confidence bands
Quality: 80-90% MAPE (mean absolute percentage error)
```

### Example 4: Strategic BI Architecture
```
Task: Design data warehouse for 100M events/day
Approach:
  1. Claude Sonnet design architecture ($0.25, 5 min)
     - Should we use Snowflake, BigQuery, or Postgres?
     - What's the cost/performance trade-off?
     - How to handle real-time vs batch?
  2. qwen2.5-coder:7b implement infrastructure ($0, 2 min)
Total cost: $0.25
Total time: 15 minutes
Output: Architecture design + cost analysis
```

---

## Dashboard Platforms & Recommendations

| Platform | Model | Cost | Effort |
|----------|-------|------|--------|
| **Streamlit** (Python) | qwen2.5-coder:7b | $0 setup | 2-5 min |
| **Plotly Dash** (Python) | qwen2.5-coder:7b | $0 setup | 3-5 min |
| **Tableau** | qwen2.5-coder:7b (DAX) | $70/user/mo | 2-3 min |
| **Power BI** | qwen2.5-coder:7b (DAX) | $10/user/mo | 2-3 min |
| **Metabase** | qwen2.5-coder:7b (SQL) | Free | 1-2 min |
| **Google Data Studio** | qwen2.5-coder:7b | Free | 2-3 min |

**Recommendation:** Start with Streamlit (free, Python) for development, then move to production platform.

---

## Forecasting Models & Complexity

| Model | Best For | Complexity | Cost |
|-------|----------|-----------|------|
| **Moving Average** | Smoothing noise | Low | $0 (1.5b) |
| **Linear/Polynomial** | Trend detection | Low | $0 (1.5b) |
| **Exponential Smoothing** | Seasonal data | Medium | $0 (7b) |
| **ARIMA** | Time series | Medium | $0 (7b) |
| **Prophet** (Facebook) | Business time series | Medium | $0 (7b) |
| **Machine Learning** | Complex patterns | High | $0 (7b) + $0.15 (Claude strategy) |

---

## Key Metrics to Track by Industry

### SaaS
- Monthly Recurring Revenue (MRR)
- Customer Acquisition Cost (CAC)
- Lifetime Value (LTV)
- Churn Rate
- Net Revenue Retention (NRR)

### E-Commerce
- Revenue by channel/product
- Customer acquisition cost
- Cart abandonment rate
- Average order value (AOV)
- Repeat purchase rate

### Marketplace
- Seller count, buyer count
- Gross Merchandise Value (GMV)
- Take rate (% commission)
- Market concentration
- Transaction volume growth

### B2B SaaS
- Qualified Lead Volume (QLV)
- Sales cycle length
- Win rate
- Deal size distribution
- Customer satisfaction (NPS)

---

## Real-Time vs Batch Reporting

**Batch (faster, easier):**
- Daily/hourly snapshots
- Generated by cron job
- Cost: $0 (qwen generates script)
- Latency: 1-24 hours

**Real-Time (more complex):**
- Live dashboard updates
- Requires streaming pipeline
- Cost: $0 (qwen generates code) + infrastructure
- Latency: Seconds

**Recommendation:** Start with batch, upgrade to real-time only if needed.

---

## When to Escalate to Claude

| Situation | Cost |
|-----------|------|
| "Design my BI architecture" | $0.20-0.30 |
| "Complex forecasting strategy" | $0.20-0.30 |
| "What metrics should I track?" | $0.10-0.15 |
| "Should we buy Tableau or build in-house?" | $0.15 |

All other tasks: use Ollama models ($0).

---

## Cost Optimization Tips

**Generate reports in batch:**
- Monthly report: qwen2.5-coder:7b ($0, 2 min)
- Weekly report: qwen2.5-coder:7b ($0, 2 min)
- Daily dashboard: Streamlit + Ollama ($0, 5 min setup)
- Cost per report: $0 (vs $500+ with manual analyst)

**Reuse visualizations:**
- Create template once → use for 12 months
- Cost: 1x qwen generation ($0)

**Forecast once, run many times:**
- Generate Prophet code once ($0)
- Run daily for 365 days ($0)
- Cost: $0 total

---

## Troubleshooting

**Dashboard is slow:**
- Use caching (qwen2.5-coder:7b generates this)
- Reduce dataset size or aggregate
- Move to faster platform (Tableau vs custom Python)

**Forecast accuracy is poor:**
- Check data quality (outliers, missing values)
- Try different models (Prophet, ARIMA)
- Add more features (external signals)
- Escalate to Claude for strategy ($0.15)

**Don't know what metrics to track:**
- Escalate to Claude ($0.10)
- Or use industry standard templates

---

## Next Steps

1. **Generate first dashboard** with qwen2.5-coder:7b (5 minutes)
2. **Analyze first metrics** with gemma4 (2 minutes)
3. **Set up daily/weekly reports** (automated via cron + qwen scripts)
4. **Log report generation time** — track how much time you save vs manual

See: `reference/monthly-metrics.md` for tracking BI task costs and time savings.
