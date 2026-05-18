# Decision Tree 9: Web Operations (Scraping, Testing, Monitoring)

Use this for web scraping, website testing, monitoring, and browser automation.

---

## Quick Decision Matrix

| Task Type | Scope | Tool | Cost | Time |
|-----------|-------|------|------|------|
| Web scraping (single page) | <100 rows | requests + BeautifulSoup | $0 | 30-60s |
| Web scraping (multi-page) | 100-1000s rows | qwen2.5-coder:7b + scripts | $0 | 1-5 min |
| Screen capture / screenshot | Single page | browser-harness | $0 | 10-30s |
| Form filling / automation | Simple | qwen2.5-coder:1.5b | $0 | 20-30s |
| Complex browser interaction | N/A | qwen2.5-coder:7b + browser-harness | $0 | 1-5 min |
| Website testing | Small site | Selenium + qwen | $0 | 2-5 min |
| Website monitoring | Uptime checks | Simple script + qwen | $0 | 30-60s |
| Headless browser testing | Multiple scenarios | browser-harness + qwen | $0 | 2-5 min |

---

## Decision Flow

```
START: I need to interact with websites
  ↓
What's the task?

A. SCRAPING
  ├─ Scrape single page (extract data)?
  │   └─ Python requests + BeautifulSoup ($0, 30-60s setup)
  │
  ├─ Scrape multiple pages?
  │   └─ qwen2.5-coder:7b generates scraper script ($0, 1-2 min)
  │
  ├─ Scrape with JavaScript rendering?
  │   └─ browser-harness (local Chrome) ($0, 1-3 min)
  │
  └─ Scrape behind authentication?
      └─ browser-harness (session handling) ($0, 2-5 min)

B. BROWSER AUTOMATION
  ├─ Simple form filling?
  │   └─ qwen2.5-coder:1.5b generates script ($0, 20-30s)
  │
  ├─ Multi-step interaction (fill form, click, navigate)?
  │   └─ qwen2.5-coder:7b + browser-harness ($0, 1-3 min)
  │
  ├─ File upload / complex interaction?
  │   └─ browser-harness (Playwright/CDP) ($0, 2-5 min)
  │
  └─ Take screenshot of website?
      └─ browser-harness capture_screenshot() ($0, 10-20s)

C. WEBSITE TESTING
  ├─ Basic HTML/CSS validation?
  │   └─ requests + validators ($0, 20-30s)
  │
  ├─ Test website functionality?
  │   └─ Selenium + qwen2.5-coder:7b ($0, 1-5 min per test)
  │
  ├─ Performance testing (load time)?
  │   └─ browser-harness + Python timer ($0, 30-60s)
  │
  └─ SEO testing (meta tags, structured data)?
      └─ BeautifulSoup + qwen2.5-coder:1.5b ($0, 1-2 min)

D. MONITORING
  ├─ Is my website up (uptime check)?
  │   └─ requests + qwen2.5-coder:1.5b (simple script) ($0, 20s)
  │
  ├─ Monitor prices / content changes?
  │   └─ qwen2.5-coder:7b generates monitoring script ($0, 1 min)
  │
  ├─ Get alerts when content changes?
  │   └─ Script + email integration ($0, 1-2 min)
  │
  └─ Real-time monitoring dashboard?
      └─ qwen2.5-coder:7b (Streamlit) ($0, 2-3 min)
```

---

## Tool Selection

### Python Requests + BeautifulSoup (Simple Scraping)
**Best for:** Extracting data from static HTML pages

**Speed:** Quick (requests is fast, parsing is fast)

**Cost:** $0 (open source, local)

**Examples:**
- "Scrape all product listings from a page"
- "Extract prices and descriptions"
- "Get email addresses from a website"

**Model to generate:** qwen2.5-coder:1.5b (simple scripts)

---

### qwen2.5-coder:7b (Scraper Scripts)
**Best for:** Generating full scraping scripts that handle:
- Multiple pages
- Pagination
- Error handling
- Data transformation
- Rate limiting

**Cost:** $0 (local Ollama)

**Time:** 1-2 minutes per script

---

### browser-harness (JavaScript, Authentication, Interaction)
**Best for:**
- JavaScript-heavy websites (React, Vue, Angular)
- Pages requiring authentication
- Multi-step interactions (form fill, click, navigate)
- Screenshots and visual verification
- Complex interactions (drag-drop, hover effects)

**Cost:** $0 (local Chrome automation via CDP)

**Time:** 1-5 minutes depending on complexity

**Usage pattern:**
```bash
browser-harness -c '
new_tab("https://example.com")
wait_for_load()
click_at_xy(100, 200)  # Click button
type_text("email@example.com")  # Fill form
capture_screenshot()  # Take screenshot
'
```

---

## Real-World Examples

### Example 1: Product Price Scraper
```
Task: Scrape product prices from 5 websites
Approach:
  1. qwen2.5-coder:7b generate Python scraper ($0, 2 min)
     - Loop through sites
     - Extract prices, product names
     - Handle errors
  2. Run scraper (5-10 sec per site)
  3. Save to CSV
Total cost: $0
Total time: 10 minutes
Output: CSV with all prices
Frequency: Can run daily automatically
```

### Example 2: Website Form Automation
```
Task: Fill out forms on 100 websites (bulk submission)
Approach:
  1. qwen2.5-coder:7b generate form-filling script ($0, 2 min)
  2. browser-harness with loop for all sites
  3. Handle failures/redirects
Total cost: $0
Total time: 30 minutes (setup + execution)
Output: 100 forms submitted
Frequency: Reusable script for future runs
```

### Example 3: Website Monitoring
```
Task: Monitor competitor's pricing changes daily
Approach:
  1. qwen2.5-coder:1.5b generate scraper + diff checker ($0, 1 min)
  2. Schedule daily with cron + email alerts
  3. Get notified on changes
Total cost: $0
Total time: 5 minutes setup
Output: Automated price tracking
Frequency: Runs daily automatically
```

### Example 4: Complex Browser Interaction
```
Task: Automate account creation across 10 platforms
Approach:
  1. qwen2.5-coder:7b generate form data ($0, 1 min)
  2. browser-harness create account flow ($0, 2-5 min)
  3. Handle CAPTCHA detection (manual or use API)
Total cost: $0-0.50 (CAPTCHA API if needed)
Total time: 15-30 minutes
Output: 10 accounts created
Frequency: Can be repeated or modified
```

---

## Web Scraping Ethics & Legal

**Always verify:**
- Check robots.txt (allowed to scrape?)
- Check Terms of Service
- Don't overload server (use delays)
- Respect rate limits
- Use appropriate User-Agent headers

**When NOT to scrape:**
- Site explicitly forbids it in robots.txt
- Terms of Service prohibit scraping
- Site has an official API (use that instead)
- Personal/private data

**Framework supports authorized scraping:**
- Web data analysis and monitoring (legitimate business)
- Competitive intelligence (within legal bounds)
- Testing and QA (your own sites)

---

## Tools Comparison

| Tool | Best For | Cost | Speed | Complexity |
|------|----------|------|-------|-----------|
| **requests + BeautifulSoup** | Static HTML | $0 | Fast | Low |
| **Selenium** | Testing, interaction | $0 | Slower | Medium |
| **browser-harness** | Complex interaction, screenshots | $0 | Medium | Low (easy API) |
| **Playwright** | Headless testing | $0 | Fast | Medium |
| **Puppeteer (JS)** | Node.js scraping | $0 | Fast | Medium |

**Recommendation:** Use requests + BeautifulSoup for simple scraping, browser-harness for complex interactions.

---

## Performance Monitoring

### Measure website performance:
```python
import time
from browser-harness import browser

start = time.time()
load_page()
elapsed = time.time() - start
print(f"Page load: {elapsed:.2f}s")
```

**Metrics to track:**
- Time to First Contentful Paint (FCP)
- Time to Interactive (TTI)
- Total page load time
- Resource sizes (images, scripts, CSS)

---

## Content Extraction Patterns

### Extract product data:
```
qwen2.5-coder generates:
1. CSS selector for product containers
2. Parse title, price, description
3. Handle variations (missing fields)
4. Output JSON/CSV
```

### Extract article content:
```
browser-harness:
1. Navigate to article URL
2. Extract headline, author, date, body
3. Handle different layouts
4. Save as markdown/JSON
```

---

## Monitoring & Alerts

### Setup automated monitoring:
```
1. qwen2.5-coder:1.5b generates monitoring script ($0, 30s)
2. Schedule with cron (every hour, daily, weekly)
3. On change detected:
   - Send email alert
   - Log to database
   - Trigger webhook
```

**Cost:** $0 (all local)
**Time:** 5 minutes to setup
**Frequency:** Automatic

---

## Rate Limiting & Politeness

**Best practices:**
- Add 1-2 second delays between requests
- Respect robots.txt Crawl-Delay
- Use appropriate User-Agent header
- Identify yourself in requests
- Cache responses to avoid duplicate requests

**qwen2.5-coder:7b generates all of this automatically when you ask for "polite scraper."**

---

## When to Escalate to Claude

| Situation | Cost |
|-----------|------|
| "Is it legal to scrape this site?" | $0.10 |
| "Design complex multi-site scraping strategy" | $0.15 |
| "Handle CAPTCHA/anti-bot detection" | $0.10-0.20 |
| "Optimize scraper for massive scale (1M+ pages)" | $0.20 |

All other tasks: use Ollama models ($0).

---

## Troubleshooting

**Website blocks my scraper:**
- Add delays between requests
- Rotate User-Agent headers
- Use proxy if needed
- Check if site has official API (better alternative)

**JavaScript content not loading:**
- Use browser-harness instead of requests
- Or use Selenium with headless Chrome
- Wait for elements to load: `wait_for_load()`

**Form filling not working:**
- Use browser-harness for precise clicking
- Verify selectors with screenshot
- Handle dynamic content (wait for elements)

---

## Next Steps

1. **Try simple scraper** with requests + BeautifulSoup (30 seconds)
2. **Generate complex scraper** with qwen2.5-coder:7b (2 minutes)
3. **Test with browser-harness** for JavaScript sites (1-3 minutes)
4. **Set up monitoring** for regular data extraction (5 minutes)
5. **Log scraping tasks** — track time saved vs manual

See: `reference/monthly-metrics.md` for tracking web ops costs and time savings.
