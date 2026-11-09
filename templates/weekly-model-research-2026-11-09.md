# Weekly Model Research — Week of 11/09 - 11/15, 2026

**Research Date:** 2026-11-09
**Researcher:** Claude (scheduled cloud routine)
**Previous report:** `templates/weekly-model-research-2026-11-02.md`

---

## Run Notes / Limitations (read first)

- `tools/model-monitor.py` **still does not exist** (5th week in a row). `python3 tools/model-monitor.py --research` fails with `No such file or directory`.
- Direct access is still blocked. `curl` to ollama.com and huggingface.co gets `connect_rejected` from the egress proxy, and WebFetch can't resolve ollama.com, orcarouter.ai, releasebot.io or codersera.com. Only github.com fetched. **Every finding here comes from web-search snippets**, many from third-party aggregators and auto-generated digests. Verify tags, sizes and benchmarks on https://ollama.com/library before acting.
- The sandbox has no Ollama and no GPU, so nothing was pulled or benchmarked.
- To unblock this step, allow `ollama.com` and `huggingface.co` in the cloud environment's network settings.

---

## PHASE 1 — Findings (since 2026-11-02)

### 1. MiMo-V2.6-Distill-Qwen-9B (`mimo-v2.6`) — new in the Ollama library ★ most relevant new find
- **Sources:** https://github.com/xBakuganMaster2x/privateai-releases/issues/35 (library monitor, detected 2026-11-05) ; https://www.orcarouter.ai/blog/mimo-v2-6-9b-ollama-tag ; https://codersera.com/blog/xiaomi-mimo-v2-6-flash-distill-9b-guide-2026/ ; https://atomic.chat/blog/guides/how-to-run-mimo-v2-6-9b-locally ; https://www.eesel.ai/blog/xiaomi-mimo-v2-6 ; https://ollama.com/maternion/mimo-v2.6 (older community tag)
- **Details:** Xiaomi's SFT of **Qwen3.5-9B** on MiMo-generated agentic and coding data. One aggregator says Ollama **v0.40.15** added support for it. `ollama run mimo-v2.6` reportedly resolves to the 9B distill (the official tag was detected 2026-11-05; I couldn't confirm it directly).
- **Self-reported scores (base Qwen3.5-9B → MiMo 9B):** SWE-bench Verified 60.0 → 61.1; SWE Pro 32.0 → 44.6; Terminal-Bench 2.1 27.0 → 37.1; in-house MiMo Code (mini) 19.5 → 51.6. There is no independent verification and no comparison against qwen2.5-coder:7b. **Don't confuse it with MiMo-V2.6 Pro / Flash**, which are ~1T-class and not local.
- **Assessment:** This is a second **`qwen-7b` replacement candidate for 8–16 GB machines**, alongside Mellum2.1. It may become the easier one, because it has an official library tag (pending confirmation), while Mellum2.1 is HF-only. A 9B Q4 is roughly 5–6 GB, against ~4.7 GB for qwen2.5-coder:7b. **Priority: HIGH (test). Run it head-to-head with Mellum2.1 and qwen2.5-coder:7b.**

### 2. New decision-model tags: `pplx-decider-flash` and `autotrust-jev`
- **Sources:** https://github.com/xBakuganMaster2x/privateai-releases/issues/35 ; https://ollama.com/library/autotrust-jev:9b/blobs/b446278f757d ; https://www.llmreference.com/model/pplx-decider-flash-v1.2/openrouter ; https://aiweekly.co/alerts/perplexity-open-sources-27b-decider-edges-jev-on-11-test-panel ; https://macaubusiness.com/autotrust-ai-releases-jev-27b-an-open-decision-model-for-self-hosted-ai-agents/ ; https://www.usagepricing.com/blueprint/activity/perplexity-ai-2026-10-23-decider-flash-model-launch ; https://alternativeto.net/news/2026/9/ollama-introduces-support-for-jev-style-decision-models-for-local-ai-processing/
- **Details:** Both were detected in the library on 2026-11-05. `pplx-decider-flash` (v1.2) is Perplexity's **4B multimodal** decision model, fine-tuned from Qwen3.5-4B and distilled from its 27B decider (released ~Oct 16–23). `autotrust-jev` comes in `9b` and `35b` tags, labelled vision + decision (AutoTrust's own benchmarks only).
- **Assessment:** This adds to the existing WAITLIST item "ML-based routing for the selector" (alongside LFM3 d1 and nimble-v3). A 4B decider could in principle replace the selector's keyword matching, which is order-dependent and its weakest part. That's an experiment, not a model swap. **WAITLIST (routing idea).**

### 3. Kimi K3.1 Pro weights — released, also in the Ollama library
- **Sources:** https://ithome.com/1/022/490.htm ; https://ai-tldr.dev/releases/moonshot-kimi-k3-1-pro-open-weights/ ; https://www.buildmvpfast.com/blog/kimi-k3-1-pro-open-model-coding-pricing-2026 ; https://aiweekly.co/fr/alerts/moonshot-publie-les-poids-de-kimi-k31-pro-moe-28-t-avec-contexte-1-m-et-gated ; https://github.com/xBakuganMaster2x/privateai-releases/issues/35
- **Details:** `moonshotai/Kimi-K3.1-Pro` is a 2.8T MoE (~104B active), MXFP4, ~1.56 TB, with a custom MIT-style licence. It landed ~Nov 5. The Ollama `kimi-k3.1-pro` entry is almost certainly a cloud/proxy tag, given the size.
- **Assessment:** Not runnable locally. **SKIP.** It could be a Claude-tier alternative for "complex" slots via API, but that's out of scope for this framework.

### 4. Ricursive Ripple-65B Preview (Apache 2.0) — new
- **Sources:** https://tech-insider.org/what-ricursive-intelligence-released-on-november-4/ ; https://ai-tldr.dev/releases/ricursive-ripple-65b-preview/ ; https://braindetox.kr/en/posts/ripple_65b_preview_open_weights.html ; https://www.llmreference.com/model/ripple-65b-preview ; https://www.eesel.ai/de/blog/ripple-65b-coding-modell
- **Details:** Released 2026-11-04 as `ricursiveAI/Ripple-65B-Preview`, a 65B **dense** coding model (BF16 ~130 GB, plus NVFP4 and community GGUF). Self-reported scores: Terminal-Bench 2.1 80.5, SWE-bench Pro v2.0 Hard 79.1. The model card claims 1M context; the first hosted API offers 16K. Note: Ricursive (Ripple) is a **different company from Recursive (Flint)**.
- **Assessment:** A Q4 would need ~40 GB, and dense 65B is slow on consumer hardware. **SKIP for local use. Revisit only for a ≥48 GB machine.**

### 5. Recursive Flint (`flint:40b`) — still no independent coding benchmark
- **Sources:** https://www.gradually.ai/en/ai-models/recursive-flint/ ; https://techjacksolutions.com/?p=99389 ; https://www.orcarouter.ai/nl/blog/flint-40b-a2-5b-local-coding
- **Update:** The only third-party data point is a **MathBench** entry (69/300 short-answer, 20/100 Lean), which is math, not code. Artificial Analysis still has no Flint entry. The coding scores (SWE-bench Verified 74.2, etc.) remain vendor-only.
- **Assessment:** Unchanged. Only for ≥32 GB VRAM or ≥36 GB Macs. **Priority: MEDIUM.**

### 6. LFM3 licence — CONFIRMED (resolves last week's caution)
- **Sources:** https://liquid.ai/lfm-license ; https://docs.liquid.ai/lfm/help/model-license ; https://fourweekmba.com/ai-liquid-ai-opens-lfm3-free-to-firms-under-10m-in-revenue/ ; https://scancode-licensedb.aboutcode.org/lfm-open-1.0.yml
- **Details:** LFM Open License v1.0 is Apache-2.0-based. Commercial use is **free for companies under $10M annual revenue**; above that you need a paid licence from Liquid. Research and non-commercial use have no threshold.
- **Assessment:** Fine for personal or small-business use. **`lfm3-audio` stays CONSIDER TESTING** for the `media/medium` audio slot.

### 7. Mellum2.1 Thinking (12B-A2.5B) — no new head-to-head
- **Sources:** https://benchlm.ai/compare/mellum2-12b-a2-5b-thinking-vs-qwen2-5-coder-32b-instruct ; https://dev.to/thegatewayguy/jetbrains-just-open-sourced-the-missing-piece-of-self-hosted-ai-pipelines-3oe1 ; https://runaihome.com/blog/jetbrains-mellum-2-1-local-coding-llm-gpu-guide-2026/ ; https://tech-insider.org/?p=42696
- **Details:** BenchLM shows **0 shared benchmarks** with Qwen2.5-Coder. New vendor number: EvalPlus 78.4%, against 71.8% for Qwen3.5-9B. A guide claims it fits a 12 GB GPU. Official GGUF reportedly available now.
- **Assessment:** Still a top test candidate, now sharing that spot with MiMo 9B. **Priority: HIGH (test).**

### 8. Ollama runtime
- **Sources:** https://releasebot.io/updates/ollama ; https://www.promptquorum.com/local-llms/top-open-source-models-ollama
- Release feeds now show **v0.40.15** (MiMo V2.6 support), after v0.40.13 (LFM3). Aggregators still disagree on the "latest" version (v0.40.5 / v0.40.14 / v0.40.15). The Mac MLX disk-use warning from previous weeks still applies.

### 9. HF trending (2026-11-08 digest)
- **Sources:** https://github.com/datnguyenquy94/news-radar/issues/1023 ; https://huggingface.co/models?sort=trending
- **Qwen3.8-27B** is still #1 (~19.3K likes, ~7.8M downloads), the same as for ~4 weeks. Others: Kimi-K3.1-Pro, a DavidAU Qwen3.8 "Turbo" GGUF (uncensored community fine-tune, ignore), LTX-2.5 (video), Audio8-TTS-Realistic-Air (TTS, new), Mistral-Large-4, LFM3-1.7B. **No new small Qwen coder and no Qwen 4.**

### 10. LMArena leaderboard
- **Sources:** https://lmarena.pages.dev/leaderboard/text ; https://llm-stats.com/benchmarks/lmarena-text ; https://www.developersdigest.tech/benchmarks/lmarena
- No November snapshot was reachable. The latest secondary data (through Oct 15) has Gemini 4 Argon at #1 (preliminary), and the top open-weight model is Kimi K3 at #15. **No impact on local recommendations.**

### 11. Specific candidates from the routine prompt
| Candidate | Status this week |
|---|---|
| qwen2.5-coder:14b | No change. Superseded by MiMo 9B / Mellum2.1 (16 GB class) and Flint (32 GB class). SKIP. |
| deepseek-r1 variants | No new small distills. SKIP. |
| mistral-small/large | No new release since Large 4 (Oct 29). Small 4 (Mar 2026) is 119B-A6B, not small in practice. SKIP. |
| llama3.3 | No new variants. SKIP. |
| gemma4 | No new Google release. KEEP. |
| llava | Replacement candidates unchanged: qwen3-vl:4b, lfm3-vl, Bolt E4B. |
| starcoder2 / granite-code | No updates. SKIP. |
| new code-specific models | **MiMo-V2.6 9B (official tag, new)**; Ripple-65B (too big); Flint (still unverified). |

**Honest summary:** It was a moderately active week, but almost everything new is far too large for local use (Kimi K3.1 Pro 2.8T, Ripple-65B). The one actionable local item is **MiMo-V2.6 9B**, a plausible `qwen-7b` replacement with an official Ollama tag. The rest of the lineup is unchanged from last week.

---

## PHASE 2 — Performance Analysis (task logs)

| Item | Result |
|---|---|
| `templates/task-log-*.md` (excluding template) | **0** |
| Other logs | `task-log-week-1.md` (repo root): unchanged unfilled template copy from 2026-05-18 |
| Real tasks logged in last 4 weeks | **0** |
| Tasks by model / success rate | **N/A** (no data) |

**Honest summary:** This is the 5th week with no data. Every recommendation here rests only on vendor or aggregator claims. The routine can't measure anything until real tasks get logged.

---

## PHASE 3 — Model Recommendations (This Week)

**KEEP (No Changes)**
- qwen-1.5b (qwen2.5-coder:1.5b): simple tasks.
- qwen-7b (qwen2.5-coder:7b): default coder until MiMo 9B / Mellum2.1 are tested.
- mistral: writing.
- gemma4: data/analysis/writing-simple.
- llava: until a vision replacement is tested.

**CONSIDER TESTING** (priority order)
1. **MiMo-V2.6 9B — NEW** → `qwen-7b` slots. `ollama run mimo-v2.6` (check that the tag exists first). ~+1 GB over qwen2.5-coder:7b.
2. **Mellum2.1 Thinking (12B-A2.5B)** → same slots. `ollama run hf.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking-GGUF:Q4_K_M`. ~+2.5 GB. *Tip: test 1 and 2 together on the same 2–3 coding tasks against qwen2.5-coder:7b, so one session settles it.*
3. **`lfm3-audio`** → `media/medium` audio work. The licence is now confirmed (free under $10M revenue). ~2 GB.
4. **qwen3-vl:4b vs `lfm3-vl`** → replace `llava`.
5. **Recursive Flint (`flint:40b`)** → coding/complex, **only on ≥32 GB VRAM / ≥36 GB Mac**.

**WAITLIST**
- **pplx-decider-flash (4B) / autotrust-jev:9b — NEW**, along with LFM3 d1 / nimble-v3: an ML router to replace the selector's keyword matching.
- **Nemotron 3.5 Bolt E4B**: fallback vision candidate.
- **Spark-X2.6-4B**, **lfm3 (1.7B text)**: simple tier.
- **MiniCPM-V-4.7-35B-A3B**, **qwen3.8:27b / Muse Glimmer 30B**: 24 GB tier.
- **Ripple-65B Preview — NEW**: only for a ≥48 GB machine; wait for independent evals.

**SKIP**
- Kimi K3.1 Pro (2.8T), Mistral Large 4 (1T), DeepSeek V4.1 Flash (~750B), MiMo-V2.6 Pro/Flash, Kimi K3, GLM-5.2, LTX-2.5, qwen2.5-coder:14b, granite-code, starcoder2.

**STORAGE OPTIMIZATION**
- Current usage: **unknown** (`ollama list` can't run in the sandbox).
- Potential: llava → qwen3-vl:4b or lfm3-vl saves ~1–2 GB. qwen2.5-coder:7b → MiMo 9B costs ~+1 GB (→ Mellum2.1 costs ~+2.5 GB). Adding lfm3-audio costs ~+2 GB. Only keep one of the coder candidates after testing.

---

## PHASE 4 — Decision Tool Changes

**No changes to `tools/model-selector-automated.py`.** Nothing has been tested locally and there are no task logs.

Candidate changes, pending a local test:
- If MiMo 9B (or Mellum2.1) beats qwen2.5-coder:7b: change `coding/medium`, `coding/complex`, `data/medium` and `security/medium` from `qwen-7b` to the winner.
- If `lfm3-audio` works: change `media/medium` to `("lfm3-audio", 0, "Speech-to-text / text-to-speech")`.

Open tool issues (carried over):
1. Model names (`qwen-1.5b`, `qwen-7b`) are aliases, not real Ollama tags.
2. Keyword detection is order-dependent (the decider models in the WAITLIST are a possible long-term fix).
3. `media/medium` routes audio to a text-only coder.

---

## Next Week Focus
1. **On a local machine (needs the user):** run a three-way coding test of qwen2.5-coder:7b vs `mimo-v2.6` vs Mellum2.1 on 2–3 real tasks, and log the results in `templates/task-log-week-N.md`. This one session would let the routine finally update the selector.
2. **2026-11-16 run:** look for independent evals of MiMo 9B and Flint, and confirm the `mimo-v2.6` library tag and its sizes. Ask the user to allow ollama.com and huggingface.co in the environment, and to create `tools/model-monitor.py` or drop that step from the routine.
