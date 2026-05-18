# Decision Tree 5: Security, Compliance & Audit

Use this for security scanning, compliance checks, vulnerability assessment, and audit tasks.

---

## Quick Decision Matrix

| Task Type | Scope | Tool | Cost | Time |
|-----------|-------|------|------|------|
| Code vulnerability scan | Any codebase | Bandit/Semgrep (local) | $0 | 30-60s |
| Dependency audit | Python/JS package.json | pip-audit / npm audit | $0 | 20-30s |
| SAST scan (all tools) | Full codebase | skill-scanner (local) | $0 | 2-5 min |
| Infrastructure security | AWS/GCP config | Trivy/Checkov (local) | $0 | 1-3 min |
| Compliance check | Code + standards | Claude Sonnet | $0.20-0.40 | 5-10 min |
| Security review (strategic) | Architecture + threat model | Claude Sonnet | $0.20-0.40 | Expert |
| Penetration test (authorized) | System/app | Manual + tooling | $0 | Varies |

---

## Decision Flow

```
START: I have a security task
  ↓
What do I need to secure?

A. SCAN MY CODE
  ├─ Quick code issues (syntax, logic)?
  │   └─ Bandit (Python) or Semgrep (any language) → skill-scanner ($0, 30s)
  │
  ├─ Security vulnerabilities in source?
  │   └─ skill-scanner with all 5 tools ($0, 2-3 min)
  │
  └─ Do a full code audit?
      └─ skill-scanner FULL + Claude review ($0.20 for strategic findings)

B. CHECK DEPENDENCIES
  ├─ Python package vulnerabilities?
  │   └─ pip-audit ($0, 20s)
  │
  ├─ Node.js / npm vulnerabilities?
  │   └─ npm audit ($0, 20s)
  │
  └─ Transitive dependency analysis?
      └─ qwen2.5-coder:7b analyze output ($0, 30s)

C. INFRASTRUCTURE / DEPLOYMENT
  ├─ Scan Dockerfile for security issues?
  │   └─ Trivy ($0, 10s)
  │
  ├─ Scan Kubernetes manifests?
  │   └─ Trivy + Kube-linter ($0, 20-30s)
  │
  ├─ Scan AWS/Terraform configs?
  │   └─ Checkov ($0, 30-60s)
  │
  └─ Check cloud IAM policies?
      └─ Claude Sonnet (strategic review) ($0.20-0.30)

D. COMPLIANCE AUDIT
  ├─ Check if code meets compliance standard?
  │   ├─ GDPR (data handling)?
  │       └─ Claude Sonnet ($0.20-0.30)
  │   ├─ HIPAA (healthcare)?
  │       └─ Claude Sonnet + security expert ($0.40)
  │   ├─ SOC 2 (security controls)?
  │       └─ Claude Sonnet ($0.25)
  │   ├─ PCI-DSS (payment card data)?
  │       └─ Claude Sonnet ($0.30)
  │   └─ ISO 27001 (information security)?
  │       └─ Claude Sonnet ($0.25)
  │
  └─ Audit configuration files?
      └─ Claude + qwen2.5-coder:7b ($0.15 + $0)

E. THREAT MODELING
  └─ Design security strategy?
      └─ Claude Sonnet (expert-level) ($0.25-0.40)
```

---

## Tool Details

### skill-scanner (Unified Local Scanner)
**What it is:** Local security scanning combining 5 tools (Bandit, Semgrep, Trivy, pip-audit, Checkov)

**Cost:** $0 (all local, no API calls)

**Speed:** 2-5 minutes for full codebase scan

**Output:** JSON report with findings by tool and severity

**Use for:**
- "Scan my codebase for security issues"
- "Give me a full security report"
- "Find all vulnerabilities in this repo"

**How to run:**
```bash
skill-scanner scan /path/to/code
skill-scanner scan /path/to/code --format json > report.json
```

**Tools included:**
1. **Bandit** — Python security issues (SQL injection, hardcoded secrets)
2. **Semgrep** — Any language, pattern-based security rules
3. **Trivy** — Container/artifact scanning
4. **pip-audit** — Python dependency vulnerabilities
5. **Checkov** — Infrastructure-as-code (Terraform, Kubernetes, Docker)

---

### Individual Tools (if skill-scanner not available)

**Bandit (Python):**
```bash
pip install bandit
bandit -r /path/to/code -f json > report.json
```

**Semgrep:**
```bash
brew install semgrep
semgrep --config=p/owasp-top-ten /path/to/code --json
```

**Trivy (Container):**
```bash
brew install trivy
trivy image myimage:latest
trivy fs /path/to/code
```

**pip-audit (Python dependencies):**
```bash
pip install pip-audit
pip-audit
```

**Checkov (Infrastructure):**
```bash
pip install checkov
checkov -d /path/to/terraform
```

---

## Real-World Examples

### Example 1: Quick Code Scan
```
Task: Scan Python codebase for security issues
Approach:
  1. skill-scanner scan . --tools bandit,semgrep ($0, 2 min)
  2. Review findings (high priority first)
  3. Fix critical issues
Total cost: $0
Total time: 10-30 minutes
Output: Security report with severities
```

### Example 2: Dependency Audit
```
Task: Check for vulnerable dependencies
Approach:
  1. pip-audit (Python) → report vulnerabilities ($0, 20s)
  2. npm audit (Node) → check JS dependencies ($0, 20s)
  3. If critical found: 
     - Escalate to Claude for remediation strategy ($0.15)
Total cost: $0-0.15
Total time: 1-2 minutes
Output: List of vulnerable packages + upgrade guidance
```

### Example 3: Compliance Check
```
Task: Audit code for GDPR compliance (data handling)
Approach:
  1. skill-scanner scan . ($0, 2-3 min)
  2. Manual review of data handling code
  3. Claude Sonnet strategic compliance review ($0.25, 5 min)
     - Are we handling PII correctly?
     - Do we have proper data deletion flows?
     - Is consent/opt-out implemented?
Total cost: $0.25
Total time: 15-20 minutes
Output: Compliance gap report + remediation steps
```

### Example 4: Infrastructure Security
```
Task: Audit Kubernetes manifests for security
Approach:
  1. Trivy scan manifests ($0, 30s)
  2. skill-scanner check for policy violations ($0, 1 min)
  3. Claude review security posture ($0.20, 3 min)
Total cost: $0.20
Total time: 5-10 minutes
Output: Security issues + remediation guidance
```

---

## Common Findings & Quick Fixes

### Python Code Security (Bandit)

| Finding | Severity | Quick Fix |
|---------|----------|-----------|
| Hardcoded password | CRITICAL | Move to environment variable |
| SQL injection risk | CRITICAL | Use parameterized queries |
| Insecure random | HIGH | Use secrets module |
| Assert in production | MEDIUM | Replace with exception handling |
| MD5 hash (weak) | MEDIUM | Use SHA-256 or bcrypt |

### JavaScript/TypeScript (Semgrep)

| Finding | Severity | Quick Fix |
|---------|----------|-----------|
| localStorage for tokens | CRITICAL | Move to httpOnly cookies |
| Eval() usage | CRITICAL | Use safer alternatives |
| Missing CORS headers | HIGH | Add CORS policy |
| XSS vulnerability | HIGH | Sanitize user input |
| No CSP header | MEDIUM | Add Content-Security-Policy |

### Dependencies (pip-audit / npm audit)

| Finding | Severity | Quick Fix |
|---------|----------|-----------|
| Critical CVE in dependency | CRITICAL | Upgrade package immediately |
| No newer version available | CRITICAL | Consider alternatives or vendor the code |
| Pre-release version in prod | MEDIUM | Pin to stable version |

---

## Compliance Framework Mapping

| Compliance | Check | Model | Cost |
|-----------|-------|-------|------|
| **GDPR** | Data handling, deletion, consent | Claude | $0.20-0.30 |
| **HIPAA** | PHI protection, audit logs | Claude | $0.30-0.40 |
| **PCI-DSS** | Payment card data security | Claude | $0.30-0.40 |
| **SOC 2** | Access controls, monitoring | Claude | $0.25-0.30 |
| **ISO 27001** | Information security | Claude | $0.25-0.30 |

**Rule:** For compliance-critical tasks, always use Claude (not local models). Cost is minor compared to compliance breach risk.

---

## Threat Modeling with Claude

**Use when:**
- Designing new system and need security strategy
- Need to identify potential attack vectors
- Planning defense mechanisms

**Example:**
```
Prompt: "Threat model for a web application that handles payment cards 
and user PII. What are the main attack vectors? How should I defend each?"

Cost: $0.25-0.40
Time: 5-10 minutes
Output: STRIDE analysis, attack tree, mitigation strategies
```

---

## Cost Optimization

**Always try local first:**
1. Run skill-scanner on every code push ($0)
2. Run dependency audits weekly ($0)
3. Fix all findings before escalating to Claude
4. Only use Claude for strategic/compliance review ($0.15-0.30)

**Cost savings:**
- Pure Claude security audits: $1.00-2.00 per codebase
- Hybrid local + Claude: $0.20-0.30 per codebase
- Savings: 80-90%

---

## When to Escalate to Claude

| Situation | Cost | Reason |
|-----------|------|--------|
| Compliance audit (GDPR/HIPAA/SOC2) | $0.25-0.40 | Legal/regulatory expertise |
| Threat modeling for new system | $0.25 | Strategic design |
| Complex vulnerability assessment | $0.15-0.25 | Expert reasoning |
| Incident response strategy | $0.20-0.30 | Crisis management |

All other tasks: use skill-scanner ($0).

---

## Authorized Security Testing

This framework supports authorized security testing and penetration testing:
- **Authorized context:** CTF competitions, pentesting engagements, security research
- **Use local tools (all free):** Bandit, Semgrep, Trivy, skill-scanner
- **Strategic guidance:** Claude for threat modeling, complex analysis
- **Documentation:** Log all findings, maintain audit trail

See: Reference documentation for debugging tool errors.

---

## Next Steps

1. **Run skill-scanner** on your current project
2. **Fix all findings** (especially CRITICAL/HIGH)
3. **Set up weekly audits** (free, automated)
4. **Log compliance checks** — audit trail for future reviews

See: `reference/monthly-metrics.md` for tracking security task costs.
