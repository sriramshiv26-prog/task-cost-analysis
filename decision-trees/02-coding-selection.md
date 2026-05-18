# Decision Tree 2: Coding & Engineering

Use this to choose the right model for coding, debugging, and development tasks.

---

## Quick Decision Matrix

| Task Type | Size | Complexity | Model | Cost | Time |
|-----------|------|-----------|-------|------|------|
| Bug fix | <50 lines | Simple | qwen2.5-coder:1.5b | $0 | 10-20s |
| Feature | 50-500 lines | Medium | qwen2.5-coder:7b | $0 | 30-60s |
| Complex feature | 500+ lines | Complex logic | qwen2.5-coder:7b + Claude | $0.15-0.30 | 2-5 min |
| Architecture | N/A | Design decisions | Claude Sonnet | $0.15-0.30 | Strategic |
| Security audit | Any | Critical | Claude Sonnet | $0.20-0.40 | Deep review |
| API integration | 100-300 lines | Medium-high | qwen2.5-coder:7b | $0 | 1-2 min |
| Test suite | 100-500 lines | Variable | qwen2.5-coder:7b | $0 | 1-3 min |
| DevOps/Infrastructure | 50-200 lines | Bash/Terraform/YAML | qwen2.5-coder:7b | $0 | 30s-2min |

---

## Decision Flow

```
START: I have a coding task
  ↓
What am I doing?
  ├─ FIXING A BUG?
  │   ├─ Can I describe it in <3 sentences? → qwen2.5-coder:1.5b ($0, 10-20s)
  │   └─ Complex bug with unknown root cause? → qwen2.5-coder:7b ($0, 30-60s)
  │
  ├─ WRITING NEW CODE?
  │   ├─ <50 lines (simple script, one function)? → qwen2.5-coder:1.5b ($0, 10-20s)
  │   ├─ 50-500 lines (feature, module, API endpoint)? → qwen2.5-coder:7b ($0, 30-60s)
  │   └─ 500+ lines (complex system, multiple modules)? → qwen2.5-coder:7b + Claude escalation
  │
  ├─ DESIGNING ARCHITECTURE?
  │   ├─ "Should I use X or Y for this?" → Claude Sonnet ($0.15-0.30)
  │   ├─ "Design me a system that handles..." → Claude Sonnet ($0.20-0.40)
  │   └─ "Review this design for issues" → Claude Sonnet ($0.15-0.30)
  │
  ├─ SECURITY REVIEW?
  │   ├─ "Scan this code for vulnerabilities" → Claude Sonnet ($0.20-0.40, high stakes)
  │   └─ Or use skill-scanner first (free, local SAST) → Claude for strategic findings
  │
  ├─ API INTEGRATION?
  │   ├─ Integration with known API (REST, GraphQL)? → qwen2.5-coder:7b ($0, 60s)
  │   ├─ Unknown/complex API with docs? → qwen2.5-coder:7b + docs → escalate to Claude if stuck
  │   └─ OAuth/auth flow design? → Claude Sonnet ($0.15-0.30)
  │
  ├─ WRITING TESTS?
  │   ├─ Unit tests for existing code? → qwen2.5-coder:7b ($0, 1-2 min)
  │   ├─ Integration tests (multi-component)? → qwen2.5-coder:7b ($0, 2-5 min)
  │   └─ End-to-end test strategy? → Claude Sonnet ($0.15-0.25, strategy)
  │
  └─ DEVOPS / INFRASTRUCTURE?
      ├─ Bash script, small tool? → qwen2.5-coder:1.5b ($0, 20-30s)
      ├─ Terraform, Ansible playbook, Docker setup? → qwen2.5-coder:7b ($0, 30-60s)
      └─ Multi-cloud architecture, security policies? → Claude Sonnet ($0.20-0.40)
```

---

## Model Details

### qwen2.5-coder:1.5b → $0, 150+ tokens/sec

**Best for:** Quick fixes, simple scripts, one-off utilities

**Use when:**
- Bug is clearly scoped ("TypeError on line 42")
- Task is <50 lines (single function, small fix)
- You need it NOW (fastest local model)

**Performance:**
- Speed: 150+ tokens/second (fastest)
- Quality: Good for simple, structured code
- Success rate: 95% for well-scoped bugs, 70% for ambiguous tasks

**Examples:**
- "Fix this Python error: `TypeError: 'NoneType' object is not subscriptable`"
- "Generate a bash script to backup this directory"
- "Convert this CSV to JSON"
- "Write a simple decorator for error handling"

**When to escalate:**
- Task requires design decisions ("should this be a class or function?")
- Needs context across multiple files
- Involves security or complex logic
→ Escalate to qwen2.5-coder:7b or Claude

---

### qwen2.5-coder:7b → $0, 50 tokens/sec

**Best for:** Features, APIs, complex logic, most production code

**Use when:**
- Task is 50-500 lines (feature, module, endpoint)
- Needs multi-file context or API integration
- Involves logic beyond straightforward syntax

**Performance:**
- Speed: 50 tokens/sec (acceptable for 2-5 minute tasks)
- Quality: Excellent for features, APIs, test suites
- Success rate: 90-95% for well-scoped features, 75-80% for ambiguous ones

**Examples:**
- "Write a FastAPI endpoint that queries PostgreSQL and returns JSON"
- "Create a data validation pipeline that cleans CSV files"
- "Write integration tests for the auth module"
- "Build a web scraper using BeautifulSoup"
- "Generate a GraphQL resolver for the User type"

**When to escalate:**
- Code becomes >500 lines across multiple files
- Task requires architectural decisions ("how should I structure this microservice?")
- Security is critical ("design a secure token refresh mechanism")
- You get stuck after 15 minutes of iteration
→ Escalate to Claude Sonnet ($0.15-0.30)

---

### Claude Sonnet → $0.15-0.30, 300+ tokens/sec

**Best for:** Architecture, complex reasoning, security, strategic decisions

**Use when:**
- Task requires design/tradeoff analysis
- Security or compliance is critical
- Qwen gets stuck or produces suboptimal code
- You need an expert review

**Examples:**
- "Design a microservices architecture for a real-time analytics platform"
- "Review this authentication system for security vulnerabilities"
- "How should I structure my FastAPI monolith as it scales?"
- "Build a caching strategy for this high-traffic API"
- "Design an event-driven system using Kafka"

**Cost note:**
- ~$0.15-0.30 per decision
- $120/month budget = 400-800 architectural decisions possible
- Use sparingly — only for decisions that matter

---

## Escalation Triggers

Move to the next tier when:

| Trigger | From | To | Cost |
|---------|------|----|----|
| Task unclear or ambiguous | 1.5b → | 7b | $0 |
| Code getting long/complex (>200 lines) | 1.5b → | 7b | $0 |
| Need multi-file context | 1.5b → | 7b | $0 |
| Qwen can't decide (design choice) | 7b → | Claude | +$0.15 |
| Security/compliance critical | Any → | Claude | +$0.20 |
| Stuck after 15 minutes | Any → | Claude | +$0.15 |
| Need expert code review | 7b → | Claude | +$0.15 |

---

## Real-World Examples

### Example 1: Quick Bug Fix
```
User: "Getting KeyError in my data transform. Line 23 checks if 'age' in data but fails"
Task size: <20 lines
Model choice: qwen2.5-coder:1.5b
Cost: $0
Time: 15 seconds
Output: Check for None before accessing dict key
Outcome: ✓ Fixed
```

### Example 2: API Integration
```
User: "Write a FastAPI endpoint to fetch user data from PostgreSQL and return JSON"
Task size: 80-120 lines (route handler + query)
Model choice: qwen2.5-coder:7b
Cost: $0
Time: 45 seconds
Output: Full endpoint with async/await, error handling, response models
Outcome: ✓ Works, production-ready
```

### Example 3: Architecture Decision
```
User: "Should I use Redis or in-memory cache for my job queue?"
Task size: Design decision
Model choice: Claude Sonnet
Cost: $0.20
Time: 1 minute
Output: Trade-off analysis (persistence, scale, latency), recommendation
Outcome: ✓ Strategic guidance, informs 2 weeks of dev work
```

### Example 4: Security Audit
```
User: "Review my JWT token handling for security issues"
Task size: Security-critical
Model choice: Claude Sonnet
Cost: $0.30
Time: 2 minutes
Output: 5 issues found (expiration, refresh token logic, CORS)
Outcome: ✓ Prevents production vulnerabilities
```

---

## Cost Optimization Tips

**Always try local first:**
1. Start with qwen2.5-coder:1.5b for any well-scoped bug
2. Move to 7b if you need more context or complexity
3. Use Claude only for decisions/reviews/architecture

**Batch similar tasks:**
- Fixing 5 bugs? Use 1.5b for all quick ones, 7b for complex ones
- Cost: $0 vs $1.50 if you used Claude for each

**Reuse patterns:**
- After Claude designs an API endpoint, use 7b to generate variations
- Cost savings: 80% (design once with Claude, generate with 7b)

**Document decisions:**
- When Claude makes an architectural decision, save it
- Next similar task uses 7b instead of Claude
- Cost savings over time: 90%+

---

## Troubleshooting

**Qwen1.5b is too slow:**
- True for code >100 tokens
- Move to 7b (50 t/s is faster for larger outputs)

**Qwen7b produces wrong code:**
- Restart daemon: `ollama serve` (refresh context)
- Add more examples to your prompt
- Escalate to Claude if it's critical

**Don't know if escalate to Claude?**
- Rule of thumb: If the output affects multiple systems or is security-critical, ask Claude
- Cost: $0.15-0.30 per question beats $1000+ in production bugs

---

## Quick Reference by Language

| Language | Best Model | Typical Task | Cost |
|----------|-----------|--------------|------|
| Python | qwen2.5-coder:7b | Data, ML, scripts | $0 |
| JavaScript/TypeScript | qwen2.5-coder:7b | Frontend, Node.js | $0 |
| Go | qwen2.5-coder:7b | Backend, CLI tools | $0 |
| Rust | qwen2.5-coder:7b | Systems, performance | $0 |
| Bash | qwen2.5-coder:1.5b | Scripts, DevOps | $0 |
| SQL | qwen2.5-coder:1.5b | Queries, migrations | $0 |
| Terraform | qwen2.5-coder:7b | Infrastructure | $0 |
| YAML/JSON | qwen2.5-coder:1.5b | Config, templates | $0 |

---

## Next Steps

1. **Try qwen2.5-coder:1.5b** on your next bug — time yourself
2. **Track success rate** — did it fix the issue on first try?
3. **Move to 7b** if you need more lines or context
4. **Save escalations** — when you use Claude, log why (helps next month's analysis)

See: `reference/monthly-metrics.md` for tracking coding task success rates.
