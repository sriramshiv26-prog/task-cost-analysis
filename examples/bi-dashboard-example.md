# Example: BI Dashboard Generation

Real-world example of creating a dashboard with the framework.

---

## Scenario: Sales Performance Dashboard

**Goal:** Create an interactive dashboard showing sales by region, product, and time period

**Data:** 50,000 rows of sales transactions (CSV)  
**Timeline:** May 18, 2026  
**Budget:** $0 (use free models)

---

## Step 1: Task Classification

```
START: I need a sales dashboard
  ↓
Is this BI/REPORTING? YES → decision-trees/07-bi-selection.md
  ↓
What do you need? Interactive dashboard
  ↓
Technology preference? Python (Streamlit)
  ↓
Recommended model: qwen-7b ($0, 2-3 min)
```

---

## Step 2: Generate Dashboard Code

### Prompt to Qwen
```
"Create a Streamlit dashboard that:

1. Loads sales data from sales.csv (columns: date, region, product, revenue)
2. Shows total revenue by region (pie chart)
3. Shows top 10 products (bar chart)
4. Shows revenue over time (line chart)
5. Add filters for date range and region
6. Show key metrics: total revenue, avg transaction

Make it fast and interactive."
```

### Generation Details
- **Model:** qwen-7b
- **Time:** 2 minutes
- **Tokens:** ~520
- **Cost:** $0

### Generated Dashboard Code
```python
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Set page config
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('sales.csv')
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# Title
st.title("Sales Performance Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
date_range = st.sidebar.date_input(
    "Select date range",
    value=(df['date'].min(), df['date'].max()),
    min_value=df['date'].min(),
    max_value=df['date'].max()
)
selected_regions = st.sidebar.multiselect(
    "Select regions",
    options=df['region'].unique(),
    default=df['region'].unique()
)

# Filter data
mask = (df['date'] >= pd.Timestamp(date_range[0])) & \
       (df['date'] <= pd.Timestamp(date_range[1])) & \
       (df['region'].isin(selected_regions))
filtered_df = df[mask]

# Key metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Revenue", f"${filtered_df['revenue'].sum():,.0f}")
with col2:
    st.metric("Transactions", f"{len(filtered_df):,}")
with col3:
    st.metric("Avg Transaction", f"${filtered_df['revenue'].mean():,.0f}")

# Charts
col1, col2 = st.columns(2)

with col1:
    # Revenue by region
    region_revenue = filtered_df.groupby('region')['revenue'].sum()
    fig_region = px.pie(
        values=region_revenue.values,
        names=region_revenue.index,
        title="Revenue by Region"
    )
    st.plotly_chart(fig_region, use_container_width=True)

with col2:
    # Top 10 products
    top_products = filtered_df.groupby('product')['revenue'].sum().nlargest(10)
    fig_products = px.bar(
        x=top_products.index,
        y=top_products.values,
        title="Top 10 Products",
        labels={'x': 'Product', 'y': 'Revenue'}
    )
    st.plotly_chart(fig_products, use_container_width=True)

# Revenue over time
daily_revenue = filtered_df.groupby(df['date'].dt.date)['revenue'].sum()
fig_time = px.line(
    x=daily_revenue.index,
    y=daily_revenue.values,
    title="Revenue Over Time",
    labels={'x': 'Date', 'y': 'Revenue'}
)
st.plotly_chart(fig_time, use_container_width=True)

# Data table
with st.expander("View Raw Data"):
    st.dataframe(filtered_df, use_container_width=True)
```

---

## Step 3: Setup & Testing

### Installation
```bash
pip install streamlit plotly pandas
```

### Run Dashboard
```bash
streamlit run dashboard.py
```

### Verification
- [x] Loads data correctly
- [x] All charts display
- [x] Filters work properly
- [x] Performance is fast (instant updates)
- [x] Responsive layout

---

## Step 4: Enhancement with Analytics

### Additional Prompt to Gemma4
```
"Analyze the sales data and tell me:
1. Which region has highest growth?
2. Are there seasonal patterns?
3. Which products are declining?
4. What's the customer retention pattern?"
```

### Gemma4 Analysis (1-2 minutes, $0)
```
Key Findings:
- West region: 23% YoY growth (highest)
- Clear seasonality: Peak in Q4, trough in Q2
- Product SKU-042: Down 15% (investigate)
- Monthly repeat rate: 62% (good retention)

Recommendations:
- Invest in West region expansion
- Plan inventory for Q4 spike
- Review Product 042 strategy
```

---

## Step 5: Deployment

### Deploy to Streamlit Cloud (free tier)
```bash
# Push to GitHub
git push origin main

# Go to https://share.streamlit.io
# Connect GitHub account
# Select repo + script
# Dashboard goes live
```

**Dashboard URL:** `https://share.streamlit.io/yourname/yourrepo/main/dashboard.py`

---

## Workflow Summary

| Step | Model | Time | Cost | Output |
|------|-------|------|------|--------|
| 1. Code generation | qwen-7b | 2 min | $0 | Dashboard code |
| 2. Analysis | gemma4 | 1 min | $0 | Business insights |
| 3. Setup | — | 2 min | $0 | Running locally |
| 4. Deployment | — | 3 min | $0 | Public dashboard |
| **TOTAL** | — | **8 min** | **$0** | **Live dashboard** |

---

## Cost Comparison

### Option A: What We Did (Qwen + Gemma)
```
Cost: $0
Time: 8 minutes
Output: Interactive dashboard + analysis
Result: ✓ Perfect
```

### Option B: Pure Claude
```
Cost: $0.30 (dashboard) + $0.15 (analysis) = $0.45
Time: 3 minutes (faster API)
Output: Same quality
Result: More expensive, not faster
```

### Option C: Hire Developer
```
Cost: $150-300 (developer time)
Time: 3-4 hours
Output: Same dashboard
Result: 30x more expensive
```

**Clear winner: Option A (Local models)**

---

## Enhancements for Next Version

### Add Real-Time Updates
```python
# Refresh data every 5 minutes
st.cache_data(ttl=300)
def load_data():
    # Fetches latest from database
```

### Add More Visualizations
```
- Heatmap by region/product
- Funnel chart for sales stages
- Waterfall chart for budget allocation
- Cohort analysis
```

### Add ML Predictions
```python
# Forecast next 30 days
from prophet import Prophet
model = Prophet()
forecast = model.fit(daily_revenue).make_future_dataframe(periods=30)
```

**Cost for enhancements:** $0 (all using local models)

---

## Key Learnings

1. **Qwen-7b is great for UI code** — Generated working dashboard in 2 minutes
2. **Gemma4 is great for analysis** — Identified key insights in 1 minute
3. **Total cost: $0** — No Claude needed for this task
4. **Deployment is free** — Streamlit Cloud is free tier
5. **Time saved** — 8 minutes vs 4+ hours manual development

---

## Tips for Dashboard Tasks

1. **Start with qwen-7b** for dashboard code generation
2. **Use gemma4 for analysis** before building
3. **Test charts locally first** before deploying
4. **Use Streamlit for speed** (faster than building custom UI)
5. **Deploy to Streamlit Cloud** for free hosting

---

## Next Iteration

### Week 2: Add Forecasting
```python
# Prompt: "Add Prophet forecasting to predict next month sales"
Model: qwen-7b
Cost: $0
Time: 5 minutes
Result: Sales forecast added to dashboard
```

### Week 3: Add ML Anomaly Detection
```python
# Prompt: "Detect unusual transactions using Isolation Forest"
Model: qwen-7b (code generation)
Cost: $0
Time: 5 minutes
Result: Anomalies highlighted in dashboard
```

---

## Scaling Considerations

### For 1M+ rows:
```
Problem: Dashboard gets slow with huge datasets
Solution: Aggregate data first (qwen-7b, $0, 2 min)
  - Summarize to daily granularity
  - Pre-compute region totals
  - Cache results

Result: Dashboard still instant, cost still $0
```

---

See also:
- `decision-trees/07-bi-selection.md` — Full BI decision tree
- `examples/coding-workflow-example.md` — Coding pattern
- `templates/weekly-report-template.md` — Track dashboard success
