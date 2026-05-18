# Decision Tree 10: Specialized Domain Analysis

Use this for legal, financial, medical, compliance, and domain-expert tasks.

---

## Quick Decision Matrix

| Task Type | Domain | Complexity | Model | Cost | Time |
|-----------|--------|-----------|-------|------|------|
| Contract review | Legal | High | Claude Sonnet | $0.20-0.30 | 5-10 min |
| Legal document generation | Legal | High | Claude Sonnet | $0.15-0.25 | 5 min |
| Financial analysis | Finance | High | Claude Sonnet | $0.20-0.40 | 5-10 min |
| Investment decision | Finance | Strategic | Claude Sonnet | $0.30-0.50 | 10-15 min |
| Medical record review | Medical | Critical | Claude Sonnet | $0.30-0.50 | 5-15 min |
| Regulatory compliance check | Compliance | High | Claude Sonnet | $0.25-0.40 | 5-10 min |
| Audit preparation | Compliance | High | Claude Sonnet | $0.30-0.50 | 10-20 min |

---

## Critical Rule: ALWAYS USE CLAUDE FOR SPECIALIZED DOMAINS

Do NOT attempt specialized domain work with local Ollama models, even for seemingly simple tasks. Hallucinations or errors in legal, financial, or medical contexts can have serious consequences.

**Required for all specialized work:**
1. Claude Sonnet (higher accuracy for stakes)
2. Human expert review (final sign-off)
3. Audit trail (log all AI-assisted analysis)
4. Disclaimer (clearly note AI was used)

---

## Decision Flow

```
START: I have a specialized domain task
  ↓
What's the domain?

A. LEGAL TASKS
  ├─ Contract review?
  │   └─ Claude Sonnet ($0.20-0.30, 5-10 min)
  │   └─ REQUIRE: Human lawyer review after
  │
  ├─ Generate legal document?
  │   └─ Claude Sonnet ($0.20-0.25, template generation)
  │   └─ REQUIRE: Human lawyer customization + signature
  │
  ├─ Compliance check (GDPR, CCPA, etc.)?
  │   └─ Claude Sonnet ($0.25-0.40, detailed analysis)
  │   └─ REQUIRE: Legal expert validation
  │
  └─ Intellectual property (patent, trademark)?
      └─ Claude Sonnet ($0.30-0.50, expert analysis)
      └─ REQUIRE: IP attorney review + filing

B. FINANCIAL TASKS
  ├─ Financial data analysis?
  │   └─ Claude Sonnet ($0.20-0.30, analysis + interpretation)
  │   └─ REQUIRE: CFO/auditor review before action
  │
  ├─ Investment analysis?
  │   └─ Claude Sonnet ($0.30-0.50, due diligence)
  │   └─ REQUIRE: Financial advisor consultation
  │
  ├─ Tax strategy / planning?
  │   └─ Claude Sonnet ($0.25-0.40, guidance)
  │   └─ REQUIRE: Tax professional finalization
  │
  └─ Regulatory / compliance (SEC, FINRA)?
      └─ Claude Sonnet ($0.40-0.60, critical stakes)
      └─ REQUIRE: Compliance officer sign-off

C. MEDICAL TASKS
  ├─ Medical record interpretation?
  │   └─ Claude Sonnet ($0.40-0.50, analysis)
  │   └─ REQUIRE: Licensed physician review
  │   └─ LIABILITY: High — document everything
  │
  ├─ Clinical research summary?
  │   └─ Claude Sonnet ($0.30-0.40, literature analysis)
  │   └─ REQUIRE: Medical expert validation
  │
  ├─ Treatment recommendation?
  │   ├─ DO NOT USE AI ALONE
  │   └─ REQUIRE: Licensed physician decision
  │
  └─ Safety / adverse event analysis?
      └─ Claude Sonnet ($0.40-0.50, incident analysis)
      └─ REQUIRE: Medical safety officer review

D. DOMAIN-SPECIFIC EXPERTISE
  ├─ Need specialized analysis?
  │   └─ Claude Sonnet ($0.20-0.50 depending on domain)
  │
  ├─ Unsure if it requires expert?
  │   └─ Ask: "Is this something a layperson could reasonably understand?"
  │   └─ If NO → Use Claude, require expert review
  │
  └─ Critical decision (affects people, money, health)?
      └─ ALWAYS use Claude + human expert sign-off
```

---

## Legal Domain Details

### Contract Review
**When to use:** Reviewing supplier agreements, employment contracts, NDA, service agreements

**Claude's role:** Flag potential risks, suggest amendments

**Process:**
1. Upload contract to Claude ($0.25-0.30, 10-15 min read)
2. Get high-level risk assessment
3. Get specific red flags (liability, payment terms, termination)
4. Get suggested amendments

**Cost:** $0.25-0.30 per contract

**CRITICAL:** Have a lawyer review Claude's analysis before signing

**Example output:**
```
Contract: Supplier Agreement
Risk level: MEDIUM
Key concerns:
  - Payment terms are net-90 (flag: cash flow risk)
  - Auto-renewal clause without 30-day notice (flag: hard to exit)
  - Indemnification clause is one-sided (flag: we assume all risk)
Suggested amendments:
  - Change to net-30 or net-45
  - Add 30-day cancel notice requirement
  - Balance indemnification language
```

---

### Legal Document Generation
**When to use:** Generating templates, standard agreements, policies

**Process:**
1. Describe what you need ($0.15-0.20, 5 min)
2. Claude generates template
3. Customize with your specifics
4. Have lawyer review + sign

**Cost:** $0.15-0.20 per template

**Example:**
```
Prompt: "Generate an NDA template for software development contractors"
Output: Full NDA with:
  - Definition of Confidential Information
  - Obligations and Restrictions
  - Term and Termination
  - Remedies
  - Standard clauses (jurisdiction, severability, etc.)
```

**Disclaimer needed:** "Template generated with AI assistance, reviewed by [Lawyer Name]"

---

## Financial Domain Details

### Financial Analysis
**When to use:** Analyzing financial statements, trends, ratios, performance

**Process:**
1. Provide financial data to Claude ($0.20-0.30)
2. Get analysis of:
   - Key ratios and trends
   - Anomalies or concerns
   - Performance vs benchmarks
3. Interpretation and recommendations
4. CFO validates before acting

**Cost:** $0.20-0.30 per analysis

---

### Investment Due Diligence
**When to use:** Evaluating investment opportunities, companies, sectors

**Process:**
1. Provide company/investment info ($0.30-0.50)
2. Claude analyzes:
   - Business model viability
   - Market opportunity
   - Competitive positioning
   - Financial health
   - Risk factors
3. Get investment thesis
4. Financial advisor or committee reviews

**Cost:** $0.30-0.50 per investment evaluation

**Note:** This is supporting analysis only. Final investment decision is human responsibility.

---

### Tax & Regulatory Compliance
**When to use:** Understanding tax implications, regulatory requirements

**Process:**
1. Describe scenario to Claude ($0.25-0.40)
2. Get analysis of:
   - Applicable tax rules
   - Reporting requirements
   - Potential strategies (within bounds)
   - Risks and considerations
3. Tax professional implements final strategy

**Cost:** $0.25-0.40 per scenario

**Important:** Claude provides educational analysis, not tax advice. Tax professional must make final decisions.

---

## Medical Domain Details

### Medical Record Analysis
**Use case:** Understanding test results, condition summaries, treatment plans

**Process:**
1. Provide anonymized medical information ($0.40-0.50)
2. Claude explains:
   - What results mean
   - Typical implications
   - Common next steps
3. Licensed physician validates + makes clinical decisions

**Cost:** $0.40-0.50 per record

**Critical disclaimers:**
- "This is not medical advice"
- "Reviewed by [Physician Name]"
- "Patient must consult their doctor"
- Document all AI involvement in medical record

**Liability:** HIGH — ensure physician signs off on accuracy

---

### Clinical Research Summary
**Use case:** Summarizing research papers, understanding study outcomes

**Process:**
1. Provide research paper to Claude ($0.30-0.40)
2. Get summary of:
   - Study design and methods
   - Key findings
   - Limitations and caveats
   - Clinical implications
3. Medical expert validates interpretation

**Cost:** $0.30-0.40 per paper

---

## Real-World Examples

### Example 1: Contract Review
```
Task: Review vendor contract for SaaS platform
Approach:
  1. Copy contract text to Claude ($0.25, 5-10 min)
  2. Request risk analysis + amendments
  3. Share with lawyer for validation
  4. Make amendments to contract
Total cost: $0.25
Total time: 15-30 minutes (+ lawyer time)
Outcome: Identified 3 risk areas, prevented 1 major liability issue
Value: Prevented potential $50K+ exposure
```

### Example 2: Financial Analysis
```
Task: Analyze quarterly financial performance
Approach:
  1. Provide P&L, balance sheet, cash flow ($0.25)
  2. Claude analyzes trends, ratios, concerns
  3. CFO reviews and validates
  4. Share with board
Total cost: $0.25
Total time: 20 minutes (+ CFO review)
Output: Analysis ready for board presentation
```

### Example 3: Compliance Check
```
Task: Check software for GDPR compliance
Approach:
  1. Describe software functionality + data handling ($0.30)
  2. Claude analyzes GDPR requirements
  3. Identifies gaps and recommendations
  4. Legal team implements fixes
Total cost: $0.30
Total time: 30 minutes (+ implementation)
Outcome: Proactive compliance assessment
```

---

## When to Escalate Beyond Claude

**Even Claude should escalate to human experts when:**
- High financial stakes (>$1M decisions)
- Regulatory filing or court involvement
- Criminal or complex legal matters
- Life-threatening medical situations
- Intellectual property disputes
- Insurance or liability claims

**Process:**
1. Get Claude's analysis ($0.20-0.50)
2. Have expert attorney/accountant/doctor review
3. Expert makes final decision + takes responsibility

---

## Documentation Requirements

For all specialized domain work, document:

```markdown
Analysis: [Type of analysis]
Date: [Date performed]
AI model used: Claude Sonnet
Disclaimer: This analysis was AI-assisted and reviewed by [Expert Name]

Analysis summary:
[Claude's output]

Expert review:
[Expert's notes and validation]

Final decision: [Final decision + expert's name]
Responsibility: [Expert assumes responsibility for accuracy]
```

---

## Cost Breakdown by Domain

| Domain | Per Task | Annual (assume 50 tasks) |
|--------|----------|-------------------------|
| Legal review | $0.25 | $12.50 |
| Financial analysis | $0.30 | $15.00 |
| Medical analysis | $0.45 | $22.50 |
| Compliance check | $0.35 | $17.50 |
| General specialized | $0.25-0.50 | $12.50-25.00 |

**Total specialized budget:** $50-100/month covers hundreds of analyses

---

## Quality Assurance Checklist

Before finalizing any specialized domain work:

- [ ] Claude's analysis reviewed by domain expert
- [ ] Expert has signed off on accuracy
- [ ] Disclaimers added ("AI-assisted analysis")
- [ ] Audit trail documented (who reviewed, when, findings)
- [ ] Expert assumes final responsibility
- [ ] Conflicts of interest disclosed
- [ ] Version control (track changes to analysis)

---

## When Claude Might Refuse

Claude will refuse to:
- Provide medical diagnosis or treatment recommendations
- Give legal advice (instead: "Consult a lawyer")
- Make investment recommendations (instead: "Consult a financial advisor")
- Handle highly sensitive medical/legal data without privacy assurance

**These are safety guardrails. Work with them, not around them.**

---

## Cost-Benefit Analysis

**Example: Legal contract review**
- Claude cost: $0.25
- Lawyer manual review: $500-1000
- Savings: 99% cost reduction
- Lawyer time saved: 2-4 hours
- Risk reduced: Claude catches 80%, lawyer validates remaining 20%

**ROI:** Massive. Claude as first pass, human as final validation.

---

## Next Steps

1. **Identify your specialized tasks** — legal, financial, medical, compliance
2. **For each, use Claude first** ($0.20-0.50 per task)
3. **Have expert validate** (essential step)
4. **Document everything** (audit trail)
5. **Log specialized costs** — track Claude usage by domain

See: `reference/monthly-metrics.md` for tracking specialized domain costs and time savings.

---

## Key Takeaway

**Specialized domains are where Claude saves the most value:**
- Not replacing experts (experts always review)
- Accelerating expert analysis (80% of work done by AI, 20% by expert)
- Cost reduction: 90% cheaper than full manual analysis
- Speed increase: 10x faster initial pass

Use Claude strategically in specialized domains, but always validate with human experts.
