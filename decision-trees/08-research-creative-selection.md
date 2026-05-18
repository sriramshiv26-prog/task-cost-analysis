# Decision Tree 8: Research, Learning & Creative Writing

Use this for tutorials, research, learning materials, blog posts, scripts, and creative content.

---

## Quick Decision Matrix

| Task Type | Length | Complexity | Model | Cost | Time |
|-----------|--------|-----------|-------|------|------|
| Tutorial / how-to | 500-2000 words | Medium | mistral:latest | $0 | 2-3 min |
| Study guide / summary | 200-500 words | Low-medium | gemma4:latest | $0 | 1-2 min |
| Blog post | 1000-3000 words | Medium | mistral:latest | $0 | 3-5 min |
| Research paper outline | 5000+ words | High | Claude Sonnet | $0.20-0.30 | Strategic |
| Script / screenplay | Variable | High | mistral:latest | $0 | Variable |
| Marketing copy | 100-500 words | Medium | mistral:latest | $0 | 1-2 min |
| Product description | 100-200 words | Low-medium | gemma4:latest | $0 | 30-60s |
| Educational content | Variable | Medium-high | gemma4:latest + mistral | $0 | 2-5 min |

---

## Decision Flow

```
START: I need to create content or learn something
  ↓
What's the output type?

A. LEARNING / STUDY MATERIALS
  ├─ Quick summary of topic?
  │   └─ gemma4:latest (concise, well-structured) ($0, 1 min)
  │
  ├─ Study guide for exam?
  │   └─ gemma4:latest (key concepts, summaries) ($0, 2-3 min)
  │
  ├─ Tutorial (how-to guide)?
  │   └─ mistral:latest (step-by-step, examples) ($0, 2-3 min)
  │
  └─ In-depth research paper?
      └─ Claude Sonnet (expert guidance) ($0.20-0.30)

B. BLOG / MARKETING CONTENT
  ├─ Blog post on a topic?
  │   └─ mistral:latest (engaging, well-written) ($0, 3-5 min)
  │
  ├─ Marketing copy (product, service)?
  │   └─ mistral:latest (persuasive, benefit-focused) ($0, 1-2 min)
  │
  ├─ Multiple blog variations?
  │   └─ mistral:latest (different angles/styles) ($0, 2 min each)
  │
  └─ Content strategy / editorial calendar?
      └─ Claude Sonnet (strategic guidance) ($0.15)

C. CREATIVE WRITING
  ├─ Short story or creative piece?
  │   └─ mistral:latest (narrative, engaging) ($0, 3-5 min)
  │
  ├─ Script / screenplay?
  │   └─ mistral:latest (dialogue, scene structure) ($0, Variable)
  │
  └─ Poetry or specialized creative?
      └─ mistral:latest or Claude ($0 - $0.15)

D. TECHNICAL DOCUMENTATION
  ├─ API documentation?
  │   └─ qwen2.5-coder:7b (structured, example code) ($0, 2-3 min)
  │
  ├─ Software architecture documentation?
  │   └─ Claude Sonnet + qwen2.5-coder:7b ($0.15 + $0)
  │
  └─ User guide / manual?
      └─ mistral:latest (clear, task-focused) ($0, 2-3 min)
```

---

## Model Selection

### gemma4:latest → Learning & Summarization
**Best for:**
- Educational summaries
- Key concept extraction
- Study guides
- Research summaries
- Concise explanations

**Examples:**
- "Summarize machine learning for someone new to the field"
- "Create a study guide for this research paper"
- "What are the key concepts in this topic?"
- "Extract main points from these notes"

**Speed:** 45 tokens/sec
**Quality:** Excellent for structured, educational content (95%+ clarity)

---

### mistral:latest → Writing & Creative Content
**Best for:**
- Blog posts (engaging, well-structured)
- Tutorials (step-by-step, clear examples)
- Marketing copy (persuasive, benefit-focused)
- Scripts and creative writing
- Email campaigns and newsletters

**Examples:**
- "Write a tutorial on how to build a REST API"
- "Create a blog post about the benefits of machine learning"
- "Write a product description for this SaaS tool"
- "Script a 2-minute explainer video"
- "Write a short story about [theme]"

**Speed:** 55 tokens/sec
**Quality:** Excellent for prose (95%+ readability and engagement)

---

### Claude Sonnet → Strategic & Complex Content
**Best for:**
- Research paper structure and strategy
- Content strategy and editorial planning
- Complex arguments and analysis
- Expert-level explanations
- Controversial or nuanced topics

**Examples:**
- "How should I structure a research paper on AI ethics?"
- "Help me develop a content strategy for my blog"
- "Explain this complex topic in multiple difficulty levels"

---

## Real-World Examples

### Example 1: Tutorial Generation
```
Task: Write a tutorial on setting up Docker
Approach:
  1. mistral:latest generate tutorial ($0, 3-4 min)
     - Step-by-step instructions
     - Code examples
     - Common pitfalls
  2. qwen2.5-coder:1.5b generate code snippets ($0, 30s)
  3. Add screenshots/diagrams manually
Total cost: $0
Total time: 10-15 minutes
Output: Complete tutorial with code
Quality: Production-ready blog post
```

### Example 2: Study Guide
```
Task: Create study guide for machine learning basics
Approach:
  1. gemma4:latest generate outline + key concepts ($0, 1 min)
  2. mistral:latest expand into full guide ($0, 2-3 min)
  3. Add practice questions (manual or generate)
Total cost: $0
Total time: 5-10 minutes
Output: Complete study guide
```

### Example 3: Blog Post Series
```
Task: Write 5-part blog series on React
Approach:
  1. Claude outline series structure ($0.10, 2 min)
  2. mistral generate each post ($0, 5 min per post = 25 min total)
  3. qwen2.5-coder:7b generate code examples ($0, 10 min total)
Total cost: $0.10
Total time: ~45 minutes
Output: 5,000+ word content series
Reach: Can drive 100s of views over time
```

### Example 4: Marketing Copy & Product Description
```
Task: Write product page copy and descriptions
Approach:
  1. mistral generate main description ($0, 1 min)
  2. mistral generate feature descriptions ($0, 2 min)
  3. mistral generate benefits section ($0, 1 min)
Total cost: $0
Total time: 5 minutes
Output: Complete product page copy
Quality: Professional, persuasive
```

---

## Content Types & Recommended Models

| Content Type | Model | Why | Time |
|--------------|-------|-----|------|
| Tutorial | mistral | Step-by-step, examples | 2-3 min |
| Blog post | mistral | Engaging prose | 3-5 min |
| Summary | gemma4 | Concise, structured | 1-2 min |
| Study guide | gemma4 | Educational, clear | 2-3 min |
| Script | mistral | Dialogue, narrative | 3-5 min |
| Marketing copy | mistral | Persuasive | 1-2 min |
| API docs | qwen | Structured, code | 2-3 min |
| Research outline | Claude | Expert structure | Strategic |

---

## Writing Quality Tips

### For mistral (prose writing):
- Be specific about tone (formal, casual, friendly)
- Provide examples or context
- Ask for multiple variations if unsure of direction

### For gemma4 (summaries):
- Ask for specific structure (bullet points, paragraphs, outline)
- Specify difficulty level (beginner, intermediate, advanced)
- Request key takeaways or action items

### For qwen (technical docs):
- Provide code examples
- Specify language and framework
- Request inline comments and explanations

---

## Content Strategy Guidance

**When to escalate to Claude:**
- Developing long-term content strategy ($0.15)
- Complex or controversial topics ($0.10-0.15)
- Research paper structure ($0.20-0.30)
- Multi-part content series planning ($0.10-0.15)

**When to use Ollama:**
- Individual pieces (blog, tutorial, summary) ($0 each)
- Generating variations of content ($0)
- Writing product descriptions ($0)
- Creating study materials ($0)

---

## Reusability & Content Repurposing

One piece of content can become many:

| Original | Derived Content | Cost | Time |
|----------|-----------------|------|------|
| Blog post | Twitter threads | $0 | 10 min |
| Blog post | Email newsletter | $0 | 5 min |
| Blog post | LinkedIn article | $0 | 5 min |
| Blog post | Podcast script | $0 (mistral) | 5 min |
| Blog post | Video script | $0 (mistral) | 5 min |
| Tutorial | Cheat sheet | $0 | 5 min |
| Tutorial | FAQ document | $0 | 5 min |

**Cost savings:** Create once, repurpose for multiple channels ($0 each).

---

## When to Use Claude Instead

| Situation | Cost |
|-----------|------|
| "Help me develop my blog strategy" | $0.15 |
| "Is this topic too controversial?" | $0.10 |
| "Structure a research paper on X" | $0.20-0.30 |
| "Multi-channel content strategy" | $0.15-0.25 |

All other tasks: use Ollama models ($0).

---

## Troubleshooting

**Content isn't engaging:**
- Add specific examples or stories
- Change tone (more casual, more formal)
- Try mistral instead of gemma4

**Summary is too long:**
- Ask for "bullet points only"
- Specify word count limit
- Request "5 key concepts only"

**Tutorial is too technical:**
- Ask for beginner-friendly version
- Request more explanations
- Add "explain like I'm 5" analogies

---

## Quick Templates

### Blog Post Template
```
1. Attention-grabbing intro (mistral)
2. Problem statement (mistral)
3. Solution / main content (mistral)
4. Examples / evidence (mistral + code examples)
5. Call-to-action (mistral)

Cost: $0 (1 mistral call)
Time: 3-5 min
```

### Tutorial Template
```
1. Overview (gemma4 summary)
2. Prerequisites (manual)
3. Step-by-step instructions (mistral)
4. Code examples (qwen2.5-coder)
5. Troubleshooting (manual or Claude $0.10)
6. Next steps (gemma4)

Cost: $0 (3 Ollama calls)
Time: 15-20 min
```

---

## Next Steps

1. **Generate first blog post** with mistral (3-5 minutes)
2. **Create study guide** with gemma4 (2-3 minutes)
3. **Write tutorial** combining mistral + qwen (5-10 minutes)
4. **Log content creation time** — track how much faster than manual writing

See: `reference/monthly-metrics.md` for tracking content creation costs and productivity gains.
