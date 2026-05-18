# Example: Coding Task Workflow

Real-world example of how to use the decision framework for coding tasks.

---

## Scenario: Build a Data Validation Pipeline

**Goal:** Create a Python script that validates user data from CSV, cleans it, and exports to JSON

**Timeline:** May 18, 2026  
**Model Strategy:** Hybrid local + escalation if needed

---

## Step 1: Classify the Task

### Decision Tree Analysis
```
START: I need to build a data validation pipeline
  ↓
Is this CODING? YES
  ↓
Go to: decision-trees/02-coding-selection.md
  ↓
Task Type: Writing new code
  ↓
Size: ~150-300 lines (feature + error handling)
  ↓
Complexity: Medium (file I/O, validation logic, error handling)
  ↓
Recommendation: qwen2.5-coder:7b ($0, 30-60s)
```

---

## Step 2: Execute with Qwen

### Prompt to Qwen
```
"Write a Python script that:
1. Reads a CSV file with columns: name, email, age, phone
2. Validates each row:
   - Email must be valid format
   - Age must be 18-100
   - Phone must be 10 digits
3. Skips invalid rows and logs them
4. Exports valid rows to JSON

Include error handling and progress output."
```

### Time to First Result
- **Model:** qwen2.5-coder:7b
- **Time to generate:** 45 seconds
- **Token count:** ~380 tokens
- **Cost:** $0

### Generated Output
```python
import csv
import json
import re
from pathlib import Path
from typing import List, Dict

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    digits = re.sub(r'\D', '', phone)
    return len(digits) == 10

def validate_age(age_str: str) -> bool:
    try:
        age = int(age_str)
        return 18 <= age <= 100
    except ValueError:
        return False

def process_csv(input_file: str, output_file: str = 'valid_data.json'):
    valid_rows = []
    invalid_rows = []
    
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=2):
            errors = []
            
            if not validate_email(row.get('email', '')):
                errors.append('Invalid email')
            if not validate_phone(row.get('phone', '')):
                errors.append('Invalid phone')
            if not validate_age(row.get('age', '')):
                errors.append('Invalid age')
            
            if errors:
                invalid_rows.append({'row': idx, 'data': row, 'errors': errors})
            else:
                valid_rows.append(row)
    
    # Export valid rows
    with open(output_file, 'w') as f:
        json.dump(valid_rows, f, indent=2)
    
    # Log summary
    print(f"Processed: {len(valid_rows) + len(invalid_rows)} rows")
    print(f"Valid: {len(valid_rows)}")
    print(f"Invalid: {len(invalid_rows)}")
    
    if invalid_rows:
        print("\nInvalid rows:")
        for row in invalid_rows:
            print(f"  Row {row['row']}: {', '.join(row['errors'])}")
    
    return valid_rows, invalid_rows

if __name__ == '__main__':
    process_csv('input.csv', 'output.json')
```

---

## Step 3: Review & Test

### Review Checklist
- [x] Does it read CSV correctly?
- [x] Are all validations implemented?
- [x] Is error handling included?
- [x] Is output JSON?
- [x] Are there helpful logs?

### Test with Sample Data
```csv
name,email,age,phone
John Doe,john@example.com,30,5551234567
Jane Smith,invalid-email,25,5559876543
Bob Wilson,bob@example.com,120,555
```

**Result:**
```
Processed: 3 rows
Valid: 1
Invalid: 2

Invalid rows:
  Row 2: Invalid email
  Row 3: Invalid age, Invalid phone
```

✓ Works correctly on first try!

---

## Step 4: Log Task Results

```markdown
### Task: Build data validation pipeline
- **Date:** 2026-05-18
- **Type:** Coding
- **Model Used:** qwen2.5-coder:7b
- **Time Taken:** 3 minutes
- **Tokens (approx):** 380
- **Success:** Yes
- **Notes:** Perfect output, no modifications needed. Excellent error handling.
- **Estimated cost:** $0
- **Would escalate next time?** No
```

---

## Step 5: Optimization Opportunity

### Alternative 1: Start with Qwen1.5b
```
Could've used qwen-1.5b for initial quick version ($0, 20s)
Result: Would've gotten 60-70% of the way there
Then use 7b for refinements ($0, 20s)
Time: Same or faster with preview
Savings: N/A (both free)
```

### Alternative 2: Ask Claude for Design Review
```
Prompt: "Is this validation pipeline scalable for 1M records?"
Cost: $0.10-0.15
Value: Strategic feedback on architecture
When: If performance mattered for production
```

---

## Real Workflow: What Actually Happened

### Timeline
```
14:30 — Task received: Build data validation pipeline
14:35 — Check decision tree: qwen-7b recommended
14:35 — Start qwen-7b (takes 45 seconds to generate)
14:36 — Review output (takes 2 minutes)
14:38 — Test with sample data (takes 1 minute)
14:39 — Verify all validations work (takes 1 minute)
14:40 — Task complete: 10 minutes total time
```

**Total cost: $0**  
**Total time: 10 minutes**  
**Success: YES**

---

## Cost Comparison

### Option A: Used Qwen (what we did)
```
Model:         qwen-7b ($0)
Time:          10 minutes
Quality:       Excellent (100% success first try)
Total cost:    $0
```

### Option B: Manual Implementation
```
Time:          60-90 minutes (writing, testing, debugging)
Quality:       Maybe 95% (need testing)
Total cost:    $100/hour rate = $100-150
```

### Option C: Pure Claude
```
Model:         claude-sonnet ($0.15-0.20)
Time:          5 minutes (faster API)
Quality:       Excellent (100% success)
Total cost:    $0.20
Benefit:       Saved 5 min vs qwen
```

**Recommendation:** Qwen-7b was optimal (free, fast enough, perfect quality).

---

## Key Learnings from This Task

1. **Decision tree worked perfectly** — qwen-7b was the right choice
2. **First attempt was successful** — no escalation needed
3. **Time saved vs manual** — 10 min automation vs 90 min manual = 80 min saved
4. **Cost advantage** — $0 vs $0.20 (Claude) or $100-150 (manual)
5. **Quality comparable** — Qwen output was production-ready

---

## How to Apply This Pattern to Your Tasks

1. **Step 1:** Identify task category (coding, data, media, etc.)
2. **Step 2:** Use appropriate decision tree
3. **Step 3:** Select recommended model
4. **Step 4:** Execute and test
5. **Step 5:** Log results and optimize for next time

---

## Escalation Example (What If Something Failed?)

### Hypothetical: What if validation failed?

**Problem:** Regex email validation was too strict/loose

**Escalation Decision:**
```
Did qwen-7b produce mostly correct code? YES
Is the issue a minor logic bug? YES
  → Try to refine with qwen-7b first
  
Prompt to qwen: "The email regex is rejecting valid addresses with '+' 
in them (e.g., user+tag@example.com). Fix the pattern to allow plus signs."

Time: 10-15 seconds
Cost: $0
Result: Fixed regex
```

**If that didn't work:**
```
Should I escalate to Claude? 
  → Only if the email validation logic is critical
  → And I've tried multiple approaches
  → Cost: $0.10 for strategic help
```

---

## Tips for Coding Tasks

1. **Start with qwen-1.5b for quick fixes** (<50 lines)
2. **Use qwen-7b for features** (50-500 lines)
3. **Escalate to Claude for architecture** (design decisions)
4. **Always test before considering done**
5. **Log everything for pattern learning**

---

## Next Steps

See:
- `decision-trees/02-coding-selection.md` — Detailed coding decision tree
- `templates/task-log-template.md` — How to log this task
- `templates/weekly-report-template.md` — Integrate into weekly tracking
