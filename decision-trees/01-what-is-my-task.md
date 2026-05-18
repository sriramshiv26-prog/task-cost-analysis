# Decision Tree 1: What's My Task?

Use this to identify which category your task belongs to, then jump to the specific decision tree.

---

## Quick Classifier

```
START: New task received
    ↓
Is this CODING?
  → YES: Go to decision-trees/02-coding-selection.md
  → NO: Continue...
    ↓
Is this involving VIDEO/AUDIO/IMAGES?
  → YES: Go to decision-trees/03-media-selection.md
  → NO: Continue...
    ↓
Is this DATA-RELATED (transform/analyze)?
  → YES: Go to decision-trees/04-data-selection.md
  → NO: Continue...
    ↓
Is this COMPLIANCE/SECURITY/AUDIT?
  → YES: Go to decision-trees/05-security-selection.md
  → NO: Continue...
    ↓
Is this COMMUNICATION/AUTOMATION?
  → YES: Go to decision-trees/06-communication-selection.md
  → NO: Continue...
    ↓
Is this BUSINESS INTELLIGENCE/REPORTING?
  → YES: Go to decision-trees/07-bi-selection.md
  → NO: Continue...
    ↓
Is this RESEARCH/LEARNING/CREATIVE?
  → YES: Go to decision-trees/08-research-creative-selection.md
  → NO: Continue...
    ↓
Is this WEB OPERATIONS (scraping/testing)?
  → YES: Go to decision-trees/09-web-selection.md
  → NO: Continue...
    ↓
Is this SPECIALIZED (legal/financial/medical)?
  → YES: Go to decision-trees/10-specialized-selection.md
  → NO: Continue...
    ↓
UNKNOWN TASK?
  → Ask Claude Sonnet for guidance ($0.10)
  → OR add as new use case to examples/
```

---

## Category Quick Reference

| If your task is about... | Go to... | Models | Cost |
|---|---|---|---|
| Writing code, fixing bugs, APIs, DevOps | 02-coding-selection | qwen-1.5b/7b, Claude | $0-0.30 |
| Video, audio, transcription, subtitles | 03-media-selection | ffmpeg, whisper, qwen, Claude | $0-0.50 |
| Images, photos, OCR, vision | 03-media-selection | llava, qwen, Claude | $0-0.30 |
| CSV, JSON, databases, cleaning, analysis | 04-data-selection | qwen, gemma4, Claude | $0-0.40 |
| Security scanning, compliance, audits | 05-security-selection | skill-scanner, Claude | $0-0.40 |
| Slack, email, notifications, chat | 06-communication-selection | qwen, mistral, gemma4 | $0 |
| Dashboards, reports, forecasts, metrics | 07-bi-selection | qwen, gemma4, Claude | $0-0.40 |
| Tutorials, learning, research, summaries | 08-research-creative-selection | gemma4, mistral | $0 |
| Blog posts, scripts, marketing, stories | 08-research-creative-selection | mistral, gemma4 | $0 |
| Web scraping, testing, monitoring | 09-web-selection | qwen, browser-harness | $0 |
| Legal, financial, medical analysis | 10-specialized-selection | Claude Sonnet | $0.20-0.40 |

---

## Examples to Help You Decide

**"I need to fix a Python error"**
→ Is this CODING? YES → See 02-coding-selection.md → Probably qwen-1.5b

**"I need to generate captions for videos"**
→ Is this VIDEO? YES → See 03-media-selection.md → Probably ffmpeg + qwen-7b

**"I need to clean a CSV file"**
→ Is this DATA? YES → See 04-data-selection.md → Probably qwen-7b

**"I need to scan my code for vulnerabilities"**
→ Is this SECURITY? YES → See 05-security-selection.md → Probably skill-scanner ($0)

**"I need to write an email template"**
→ Is this COMMUNICATION? YES → See 06-communication-selection.md → Probably mistral

**"I need to forecast revenue"**
→ Is this BI? YES → See 07-bi-selection.md → Probably Claude Sonnet ($0.20-0.30)

**"I need to write a tutorial"**
→ Is this RESEARCH? YES → See 08-research-creative-selection.md → Probably gemma4

**"I need to scrape a website"**
→ Is this WEB? YES → See 09-web-selection.md → Probably qwen-7b + browser-harness

**"I need legal contract review"**
→ Is this SPECIALIZED? YES → See 10-specialized-selection.md → Definitely Claude Sonnet ($0.20-0.40)

---

## Time-Saving Tip

**If you're in a hurry:** Just use the "Category Quick Reference" table above. Pick the closest match, jump to that decision tree, and execute.

**Total time:** 10 seconds

---

## What If I'm Still Unsure?

1. **Pick the closest category** from the Quick Reference table
2. **Scan the decision tree** for your specific task
3. **If still unsure,** ask Claude Sonnet: "Should I use [Model A] or [Model B] for [task]?" ($0.10)
4. **Add your task** to examples/ with the model you chose + outcome

---

## Next Step

→ Jump to the appropriate decision tree from the list above, or start with **[02-coding-selection.md](02-coding-selection.md)** if you code.

