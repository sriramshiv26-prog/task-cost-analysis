# Decision Tree 6: Communication & Automation

Use this for email templates, Slack bots, notifications, chat automation, and messaging tasks.

---

## Quick Decision Matrix

| Task Type | Complexity | Model | Cost | Time |
|-----------|-----------|-------|------|------|
| Email template | Simple | qwen2.5-coder:1.5b | $0 | 20-30s |
| Email campaign copy | Medium | mistral:latest | $0 | 1-2 min |
| Slack bot response | Simple | gemma4:latest | $0 | 30s |
| Chat conversation script | Medium | mistral:latest | $0 | 1-2 min |
| Notification copy | Short form | qwen2.5-coder:1.5b | $0 | 15s |
| Customer support reply | Context-heavy | mistral:latest | $0 | 1 min |
| Multi-channel automation | Design | Claude Sonnet | $0.15 | Strategic |

---

## Decision Flow

```
START: I need to automate communication
  ↓
What's the output format?

A. EMAIL
  ├─ Simple email template?
  │   └─ qwen2.5-coder:1.5b (HTML or plaintext) ($0, 20s)
  │
  ├─ Email campaign copy (marketing)?
  │   └─ mistral:latest (persuasive, on-brand) ($0, 1-2 min)
  │
  ├─ Multi-part email with complex layout?
  │   └─ qwen2.5-coder:7b (Jinja2 template) ($0, 1 min)
  │
  └─ Email sequence design (multi-email)?
      └─ mistral:latest + Claude feedback ($0 + $0.10 optional)

B. SLACK / CHAT
  ├─ Slack bot response logic?
  │   └─ qwen2.5-coder:1.5b (Python/JS webhook) ($0, 30s)
  │
  ├─ Conversational AI response?
  │   └─ gemma4:latest (context-aware) ($0, 1 min)
  │
  ├─ Generate multiple chat variants?
  │   └─ mistral:latest (tone/style variations) ($0, 30s per variant)
  │
  └─ Complex bot flow (state machine)?
      └─ qwen2.5-coder:7b (design + code) ($0, 1-2 min)

C. NOTIFICATIONS
  ├─ Alert message copy?
  │   └─ qwen2.5-coder:1.5b (clear, concise) ($0, 15s)
  │
  ├─ Multi-channel notification (email + SMS + push)?
  │   └─ qwen2.5-coder:7b (template generation) ($0, 1 min)
  │
  └─ Notification frequency strategy?
      └─ Claude Sonnet (user experience decision) ($0.10)

D. AUTOMATION WORKFLOW
  ├─ How should I automate this process?
  │   └─ Claude Sonnet or qwen2.5-coder:7b (flow design) ($0-0.15)
  │
  └─ Multi-channel automation strategy?
      └─ Claude Sonnet (architecture) ($0.15)
```

---

## Model Selection by Use Case

### qwen2.5-coder Models (Fastest)
- Email templates (HTML, plaintext)
- Notification message copy
- Simple bot responses
- Script generation (Python, JS)

**Speed:** 1.5b at 150 t/s, 7b at 50 t/s

---

### mistral:latest (Best for Writing)
- Email campaign copy (marketing, persuasive)
- Customer support replies (empathetic, professional)
- Chat conversation scripts
- Style variations (formal, casual, friendly)

**Speed:** 55 tokens/sec
**Quality:** Excellent for prose, tone, persuasion

---

### gemma4:latest (Context-Aware)
- Slack bot responses (understanding context)
- Conversational replies that consider history
- Smart notifications (prioritization)

**Speed:** 45 tokens/sec
**Quality:** Good reasoning about conversation context

---

### Claude Sonnet (Strategic Decisions)
- "How should I design my notification system?"
- "Should I use email, SMS, or push for this alert?"
- "What's the optimal cadence for this notification type?"
- "Design a customer onboarding email sequence"

---

## Real-World Examples

### Example 1: Email Template
```
Task: Create HTML email template for password reset
Approach:
  1. qwen2.5-coder:1.5b generate HTML template ($0, 20s)
  2. Add brand colors/logo manually (no model needed)
  3. Test send
Total cost: $0
Total time: 5 minutes
Output: Production-ready email template
```

### Example 2: Slack Bot Response
```
Task: Generate contextual Slack bot responses
Approach:
  1. qwen2.5-coder:1.5b create bot webhook handler ($0, 30s)
  2. gemma4 generate context-aware response logic ($0, 1 min)
  3. Test with sample inputs
Total cost: $0
Total time: 10 minutes
Output: Working Slack bot
```

### Example 3: Email Campaign Sequence
```
Task: Design 5-email onboarding campaign
Approach:
  1. mistral:latest generate email 1 copy ($0, 1 min)
  2. mistral generate emails 2-5 ($0, 4 min total)
  3. Claude review for flow/consistency ($0.10, optional)
Total cost: $0-0.10
Total time: 5-10 minutes
Output: 5-email sequence ready to send
```

### Example 4: Multi-Channel Notification Strategy
```
Task: Design notification system for user alerts
Approach:
  1. Claude Sonnet design strategy ($0.15, 2 min)
     - When to use push vs email vs SMS?
     - Frequency limits to prevent fatigue?
  2. qwen2.5-coder:7b implement templates ($0, 1 min)
  3. Set up automation logic
Total cost: $0.15
Total time: 15 minutes
Output: Notification strategy + implementation
```

---

## Templates & Patterns

### Email Template Pattern (mistral + qwen)
```
Generate with: mistral for copy tone + qwen for HTML structure

Pattern:
1. Subject line (mistral)
2. Greeting (mistral)
3. Main message (mistral)
4. Call-to-action (mistral)
5. Footer (qwen)

Cost: $0
Time: 1-2 minutes
```

### Slack Bot Pattern (qwen + gemma)
```
Generate with: qwen for webhook code + gemma for response logic

Pattern:
1. Event trigger (webhook)
2. Parse input (qwen generates regex/parser)
3. Generate response (gemma for context)
4. Format output (qwen for JSON)

Cost: $0
Time: 1-2 minutes
```

---

## Common Use Cases & Quick Models

| Use Case | Model | Why |
|----------|-------|-----|
| "Email template" | qwen2.5-coder:1.5b | Fast, structured output |
| "Marketing email copy" | mistral | Persuasive writing |
| "Slack bot response" | gemma4 | Contextual understanding |
| "SMS alert message" | qwen2.5-coder:1.5b | Concise, clear |
| "Chat conversation" | mistral | Natural dialogue |
| "Notification strategy" | Claude Sonnet | Strategic decision |

---

## Automation Integration Examples

### Zapier / Make Automation
- Use qwen2.5-coder:1.5b to generate webhook payloads
- Use mistral to generate response templates
- Cost: $0 (local generation) + Zapier plan (external)

### Custom Python Automation
- Use qwen2.5-coder:7b to generate bot code
- Use gemma4 for response logic
- Cost: $0

### Email Sequence (SendGrid, Klaviyo, etc.)
- Use mistral to generate copy for each email
- Use qwen to format HTML templates
- Cost: $0 (content generation) + email service plan

---

## Tone & Style Variations

Use mistral to generate multiple versions:

```
Prompt: "Generate 3 versions of this email in different tones:
1. Formal and professional
2. Friendly and conversational
3. Urgent and action-focused"

Cost: $0 (1 call)
Time: 1 minute
Output: 3 email versions to choose from
```

---

## When to Use Claude

| Situation | Cost |
|-----------|------|
| "Design my notification strategy" | $0.15 |
| "Email sequence flow (when should I send what?)" | $0.10 |
| "Should I use SMS or email for urgent alerts?" | $0.10 |
| "Review my customer communication tone" | $0.10-0.15 |

All other tasks: use Ollama models ($0).

---

## Cost Optimization Tips

**Batch communication tasks:**
- Generating 10 emails? Use mistral for all ($0)
- Don't use Claude unless you need strategic guidance

**Reuse templates:**
- Generate email template once (mistral, $0)
- Use variations for 5 campaigns (mistral, $0)
- Cost: $0 for all (vs $1.00 if using Claude)

**Automation before manual:**
- Use qwen to generate bot code ($0)
- Automate 100 support replies → savings of hours per week

---

## Troubleshooting

**Email template looks plain:**
- Add styling guidance to prompt
- Use mistral for more sophisticated copy
- Or escalate to Claude for design review ($0.10)

**Slack bot responses aren't contextual:**
- Use gemma4 instead (better reasoning)
- Provide more context in the prompt

**Don't know tone/style to use:**
- Escalate to Claude ($0.10) for guidance
- Or test multiple versions with mistral ($0)

---

## Next Steps

1. **Generate email template** with qwen2.5-coder:1.5b (20 seconds)
2. **Create Slack bot** with qwen + gemma (2 minutes)
3. **Write email copy** with mistral (1-2 minutes)
4. **Log communication tasks** — track what was automated and time saved

See: `reference/monthly-metrics.md` for tracking communication automation savings.
