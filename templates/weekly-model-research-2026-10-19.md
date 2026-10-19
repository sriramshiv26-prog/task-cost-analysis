# Weekly Model Research — Week of 10/19 - 10/25, 2026

**Research Date:** 2026-10-19
**Researcher:** Claude (scheduled cloud routine)
**Previous report:** `templates/weekly-model-research-2026-10-12.md`

---

## Run Notes / Limitations (read first)

- `tools/model-monitor.py` **still does not exist**. `python3 tools/model-monitor.py --research` fails with `No such file or directory`, which is the second week running.
- Direct access is still blocked. `curl` to ollama.com and huggingface.co gets a proxy `CONNECT 403`, and WebFetch can't resolve DNS for ollama.com, releasebot.io or local-ai-zone.github.io. **All findings come from web search snippets, mostly third-party aggregators. Treat every tag, size and benchmark as unverified** until you check it on https://ollama.com/library.
- There is no Ollama or GPU in the sandbox, so nothing was pulled or benchmarked.

---

## PHASE 1 — New Models Discovered (since 2026-10-12)

### 1. JetBrains Mellum2.1 Thinking (12B MoE, 2.5B active) ★ most relevant new find
- **Source:** https://www.marktechpost.com/2026/10/08/jetbrains-releases-mellum2-1-a-12b-moe-open-model-for-coding-agents/ ; https://benchlm.ai/models/mellum2-1-12b-a2-5b-thinking ; https://toolhalla.ai/blog/can-you-run-mellum-2-1-locally
- **Released:** Oct 8, 2026 (missed last week). Apache 2.0. 64 experts, 8 active per token, 131K context.
- **Size:** ~7.0–7.7 GB at Q4_K_M (community estimates). GGUF repo: `JetBrains/Mellum2.1-12B-A2.5B-Thinking-GGUF` on HF. Sources conflict on whether the GGUF/Ollama builds are live or still "coming soon" (as of Oct 12).
- **Claims (self-reported):** LiveCodeBench v6 82.0, SWE-bench Verified 47.0.
- **Assessment:** This is the first candidate that fits the **same memory class as our `qwen-7b` (qwen2.5-coder:7b, ~4.7 GB)** and runs on 16 GB machines, including the Mac. With 2.5B active parameters it should be *faster* per token than a dense 7B. If the benchmark claims hold, it is a large quality jump over qwen2.5-coder:7b. This is a better test target for coding/medium than last week's qwen3-coder:30b, which needs ~19 GB.
- **Priority:** HIGH. **Value:** Possible replacement for `qwen-7b` on all machines.

### 2. Meta Muse Glimmer 30B (Apache 2.0) — missed in earlier reports
- **Source:** https://phoronix.com/news/Meta-Muse-Glimmer ; https://huggingface.co/meta-models/Muse-Glimmer-30B-GGUF ; https://pasqualepillitteri.it/en/news/10831/meta-muse-glimmer-30b-open-weight-local
- **Released:** Aug 10, 2026. Ollama support since v0.32.7. Q4_K_M GGUF ~15.6 GiB (<20 GB).
- **Assessment:** Meta's first open-weight model since Llama 4, with an agent and general focus. Last week's report said "no new Llama release". That was technically true, but it missed this model. It is in the same weight class as qwen3.8:27b, so it is a 24 GB GPU / 32 GB Mac model only.
- **Priority:** MEDIUM. **Value:** WAITLIST next to qwen3.8:27b as a possible general/analysis "complex" tier on the NVIDIA box. Could reduce `claude-sonnet` calls for analysis/complex.

### 3. Meta Muse Spark Open (816B MoE / 42B active)
- **Source:** https://thenewstack.io/meta-muse-spark-open/ ; https://pasqualepillitteri.it/en/news/24330/meta-muse-spark-open-816b-open-weights
- **Released:** Weights Oct 15, 2026, under the "Muse Model License" (commercial limits). Needs ~300 GB RAM+VRAM even as a GGUF. **SKIP** (not runnable locally).

### 4. NVIDIA Nemotron 3.5 Super (120B/12B active) and Bolt 74B (A9B, 2-bit QAT)
- **Source:** https://pasqualepillitteri.it/en/news/24182/nemotron-3-5-bolt-74b-nvidia-rtx-spark-launch ; https://www.morphllm.com/best-ollama-models
- **Released:** ~Oct 15, 2026. Ollama is a launch runtime. Bolt's weights alone are ~24 GB, so it would not fit a 24 GB card once context memory is added. NVIDIA targets RTX Spark laptops with up to 128 GB. All benchmarks are vendor-stated.
- **Also coming:** **Bolt E4B (~4 GB), due Oct 23**, aimed at game characters, so unlikely to suit our tasks.
- **Priority:** LOW. **Value:** SKIP Super and Bolt 74B (too big). Glance at E4B next week.

### 5. Reflection AI Beam (501B / 23B active, Apache 2.0)
- **Source:** https://dev.to/felipe0liveira/open-weights-go-frontier-class-a-501b-base-model-a-816b-meta-moe-and-gemini-4-argon-land-in-one-4b3b ; https://x.com/ollama/status/2107193986482126883
- **Released:** Weights Oct 16. Ollama offers it as a **cloud** tag only. **SKIP** (too large to run locally).

### 6. Liquid AI d1-omni-600M and d1-3B ("decision" models)
- **Source:** https://www.orcarouter.ai/blog/liquid-ai-d1-omni-ollama-decision-model ; https://huggingface.co/LiquidAI/d1-3B
- **Details:** d1-3B (~3.7 GB on Ollama, unverified) is built on LFM2.5-VL-3B and returns typed, calibrated answers in a single forward pass (~8 ms on an RTX 4090). d1-omni-600M became an Ollama pull on Oct 17 (`ollama pull d1-omni`).
- **Assessment:** These are classifiers, not chat or vision assistants. They don't replace llava or qwen3-vl. They are interesting as a possible **local backend for the model selector's category/complexity detection**, which currently uses brittle keyword matching (see Phase 4).
- **Priority:** LOW. **Value:** WAITLIST as an idea for the selector, not as a task model.

### 7. Aleph Alpha Kolibri-1 (Oct 3, Apache 2.0)
- **Source:** https://aifront-page.com/open-weights-october-2026-ai-model-launches/
- **Assessment:** A "sovereign" EU text LLM. No size or Ollama info found, and nothing suggests it beats current picks. **SKIP**.

### 8. Mistral Large 4 — status update
- **Source:** https://letsdatascience.com/news/mistral-debuts-large-4-open-weight-model-preview-cbf9e0b5 ; https://pasqualepillitteri.it/en/news/21196/mistral-large-4-launches-open-weights-late-october
- **Details:** 1.05T total / 49B active. The weights are still pending and are due **~Oct 27** under a *custom* licence (Large 3 used Apache 2.0). It is a cloud tag on Ollama.
- **Mistral Small 4** (119B MoE / 6B active, Apache 2.0; https://feeds.simonwillison.net/tags/mistral/) is from earlier in 2026, **not new**. At ~119B total it is still too large to replace our 7B `mistral` writer.
- **Priority:** LOW. **Value:** WAITLIST. Recheck on 2026-10-26 for any small model released alongside the weights.

### 9. Specific candidates from the routine prompt — unchanged
| Candidate | Status this week |
|---|---|
| qwen2.5-coder:14b | No change. Superseded by Qwen3-Coder and Mellum2.1. SKIP. |
| deepseek-r1 variants | No new small distills. DeepSeek API aliases now route to V3.2/V4 (https://fireworks.ai/blog/deepseek-models). SKIP. |
| mistral-small/large | See #8. Nothing small and new. |
| llama3.3 | No new variants. Meta's attention has moved to the Muse line (see #2, #3). |
| gemma4 | No new variant since Gemma 4 26B-A4B (Apr 2, 2026). embeddinggemma-2 was reportedly added to Ollama (embeddings only, not relevant). KEEP. |
| llava | Still unchanged on Ollama. Last week's replacement candidate (qwen3-vl:4b) stands. |
| starcoder2 / granite-code | No updates. SKIP. |

### 10. Ollama runtime
- **Source:** https://www.promptquorum.com/local-llms/top-open-source-models-ollama ; https://releases.sh/ollama
- v0.40.5 is reportedly stable as of Oct 14, with v0.40.6 in pre-release on Oct 16. The **v0.40 line makes MLX the default backend on Apple Silicon** (noted last week). It now appears to be stable, so **upgrading the Mac is worth doing this week**. Wikipedia still lists 0.34.3, which conflicts.

### Leaderboard check (LMArena)
- No October snapshot was found. In the latest available data (August), Kimi K3 leads the Frontend Code Arena and GLM-5.2 and DeepSeek V4 Pro are in the frontier band. None of them runs locally, so **there is no impact on local recommendations.** Sources: https://www.swfte.com/fr/ai/lmarena-ai ; https://manifold.markets/CraigDemel/what-company-will-have-the-top-mode
- HuggingFace trending (via digests, not direct): the 27B Qwen VL is the most-downloaded multimodal model, along with d1-3B. Sources: https://github.com/kakapez/agents-radar/issues/1648 ; https://huggingface.co/collections/merve/weekly-releases-oct-09-2026

---

## PHASE 2 — Performance Analysis (task logs)

| Item | Result |
|---|---|
| `templates/task-log-*.md` (excluding template) | **0** |
| Other logs | `task-log-week-1.md` (repo root), unchanged since 2026-05-18 |
| Real tasks logged in last 4 weeks | **0** |
| Success rate | **N/A** (no data) |

**Honest summary:** This is the same as last week. No tasks have been logged in ~5 months. The only entries are 4 sample rows from May (4/4 "success"), and they are illustrative, not real. Every recommendation still rests only on external claims.

---

## PHASE 3 — Model Recommendations (This Week)

**KEEP (No Changes)**
- qwen-1.5b (qwen2.5-coder:1.5b): simple tasks.
- qwen-7b (qwen2.5-coder:7b): default coder until Mellum2.1 is tested.
- mistral: writing. Recheck after ~Oct 27.
- gemma4: no newer Google release.

**CONSIDER TESTING** (priority order)
1. **Mellum2.1 Thinking (12B-A2.5B)** → candidate replacement for `qwen-7b` (coding medium/complex, security medium). Expected improvement: big quality gain (self-reported 47% SWE-bench Verified) with similar or faster speed. Size impact: +~2.5–3 GB over qwen2.5-coder:7b. It fits 16 GB machines, including the Mac. *First check that the GGUF is actually published.*
2. **qwen3-vl:4b** → replace `llava` (carried over from last week, still untested). −1.4 GB.
3. **qwen3-coder:30b (MoE)** → NVIDIA box only (carried over). Lower priority now that Mellum2.1 covers the same need in a smaller footprint.

**WAITLIST**
- **Muse Glimmer 30B** and **qwen3.8:27b**: ~16–17 GB "complex" tier for the 24 GB GPU. Could cut Claude calls for complex analysis. Test one of them only after the items above.
- **Mistral Large 4 weights (~Oct 27)**: too large to run, but watch for a small companion model. Recheck 2026-10-26.
- **Nemotron 3.5 Bolt E4B (Oct 23)**: check whether it is general-purpose or only for game NPCs.
- **Liquid d1 / d1-omni-600M**: idea for an ML-based category classifier in the selector.

**SKIP**
- Muse Spark Open, Reflection Beam, Nemotron 3.5 Super/Bolt 74B, Kimi K3, GLM-5.x, DeepSeek V4 (all too large); Kolibri-1 (no evidence of gain); qwen2.5-coder:14b, granite-code, starcoder2 (stale or superseded).

**STORAGE OPTIMIZATION**
- Current usage: **unknown**, because `ollama list` can't run in the sandbox.
- Potential: replacing llava with qwen3-vl:4b saves ~1.4 GB. Replacing qwen2.5-coder:7b with Mellum2.1 costs ~+3 GB. Net +~1.6 GB if both are adopted.

---

## PHASE 4 — Decision Tool Changes

**No changes to `tools/model-selector-automated.py`.** Nothing has been tested locally, and the claims are unverified.

Issues still open in the tool (carried over and expanded):
1. The model names (`qwen-1.5b`, `qwen-7b`, `llava`, …) are aliases, not real Ollama tags, so `ollama run qwen-1.5b` fails without `ollama cp` aliases.
2. Keyword detection is order-dependent. `"write"` and `"generate"` are coding keywords and are checked before writing, so "Write a blog post" is routed to **coding**. `"analyze"` hits **data** before analysis, and `"extract"` sits under image. This is worth fixing (put more specific categories first, or score by the number of matches) independently of any model change.

---

## Next Week Focus
1. **On a local machine:** check that the Mellum2.1 GGUF is live, then test it against qwen2.5-coder:7b on 2–3 real coding tasks. Test qwen3-vl:4b against llava as well. Log the results with `templates/task-log-template.md` so Phase 2 finally has data.
2. **2026-10-26 run:** check the Mistral Large 4 weight drop and Nemotron Bolt E4B. Also either create `tools/model-monitor.py` or remove step 1 from the routine prompt.
