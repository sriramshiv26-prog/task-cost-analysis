# Weekly Model Research — Week of 10/12 - 10/18, 2026

**Research Date:** 2026-10-12
**Researcher:** Claude (scheduled cloud routine)

---

## Run Notes / Limitations (read first)

- `tools/model-monitor.py` **does not exist** in the repo, so `python3 tools/model-monitor.py --research` failed. The routine prompt refers to a tool that was never committed. Either create it or drop the step from the routine.
- The cloud sandbox **cannot reach ollama.com or huggingface.co directly**: the egress proxy rejected `curl`, and WebFetch could not resolve DNS. All findings below come from web search, which mostly returned third-party aggregator and SEO roundups. **Treat every tag name, size and benchmark number as unverified.** Check against https://ollama.com/library before you pull anything.
- No Ollama install or GPU is available in the sandbox, so **nothing was downloaded or benchmarked**. Speed and quality figures are claims from sources, not measurements.

---

## PHASE 1 — New Models Discovered

### 1. Qwen3.8 (27B dense, distilled)
- **Source:** Ollama release notes via Releasebot (https://releasebot.io/updates/ollama); Wikipedia (https://en.wikipedia.org/wiki/Qwen); https://www.morphllm.com/best-ollama-models
- **Tag (unverified):** `qwen3.8:27b` / `ollama pull qwen3.8`
- **License:** Apache 2.0 for the distilled 27B. Larger Qwen3.8 sizes carry a revenue-share clause above US$50M annual revenue.
- **Claims:** ~61.7% SWE-bench (one source). Release date conflicts between sources (Apr 16 vs Aug 14, 2026).
- **Category:** Coding / general reasoning
- **Assessment:** A large step up in quality over our `qwen-7b` (qwen2.5-coder:7b), but ~16–18 GB at Q4. That needs a 24 GB GPU or a 32 GB+ Apple Silicon Mac. Too heavy to be the default.
- **Priority:** MEDIUM. **Value:** Possible "complex coding" tier on GPU machines only.

### 2. Qwen3-Coder 30B-A3B (MoE) and Qwen3-Coder-Next 80B-A3B
- **Source:** https://localaimaster.com/models/best-local-ai-coding-models ; https://www.sitepoint.com/qwen3codernext-local-deployment-a-complete-developer-guide-2026/
- **Tag (unverified):** `qwen3-coder:30b` (~19 GB Q4). Coder-Next needs 64 GB+ of memory.
- **Category:** Coding
- **Assessment:** With only ~3B active parameters, the 30B MoE should run *faster per token* than a dense 14B while scoring well above qwen2.5-coder:7b. This is the most promising answer to the routine's "qwen2.5-coder:14b?" question, because qwen2.5-coder is now two generations old. Memory cost is high (19 GB).
- **Priority:** HIGH to test on the Windows/NVIDIA machine. **Value:** May replace `qwen-7b` for medium/complex coding on GPU hardware.

### 3. qwen2.5-coder:14b (the specific candidate in the routine prompt)
- **Status:** Still in the Ollama library. No new version found. Superseded by the Qwen3-Coder line above.
- **Priority:** LOW. **Value:** SKIP in favour of Qwen3-Coder.

### 4. DeepSeek V4 family
- **Source:** https://artificialanalysis.ai/articles/deepseek-is-back-among-the-leading-open-weights-models-with-v4-pro-and-v4-flash ; https://runtimewire.com/article/deepseek-publishes-v4-flash-vision-open-weights
- **Models:** V4-Pro (1.6T total / 49B active), V4-Flash (284B / 13B active), released Apr 24 2026, MIT. V4-Flash-Vision-Exp (305B) weights released Aug 31 2026.
- **Assessment:** None of these is runnable on our hardware. Nothing new since late August. No new small deepseek-r1 distills found this week.
- **Priority:** LOW. **Value:** SKIP (too large to run locally).

### 5. Mistral Large 4
- **Source:** https://mistral.ai/news/mistral-large-4/ ; https://qz.com/mistral-large-4-open-weight-ai-model-launch-100626
- **Details:** Launched Oct 6, 2026, ~1T parameters. API preview only for now. Open weights are promised for **~Oct 27** (one source says "end of October"). RL phase not finished at launch.
- **Assessment:** Not usable locally. Watch for any smaller "Mistral Small" refresh that may come alongside it, because our writing model (`mistral` 7B) is very old.
- **Priority:** LOW. **Value:** WAITLIST and recheck the week of Oct 26.

### 6. Gemma 4 (current), no Gemma 5
- **Source:** https://codersera.com/blog/open-source-llms-landscape-2026/
- **Assessment:** Gemma 4 is still Google's current open line (Apache 2.0). No October release. We already use `gemma4`. **No change.**

### 7. Llama
- **Source:** https://opper.ai/model-releases ; https://llmgateway.io/timeline
- **Assessment:** No new Llama release found. The most recent is Llama 4 Scout (March 2026, Llama 4 Community licence). llama3.3 has no new variants. **No change.**

### 8. Vision: Qwen3-VL 4B, Qwen2.5-VL 7B, Gemma 3 4B, Moondream 2 (LLaVA replacements)
- **Source:** https://www.promptquorum.com/power-local-llm/local-vision-models-llava-ollama-2026 ; https://localaimaster.com/blog/best-local-vision-models ; https://www.serverman.co.uk/ai/ollama/best-ollama-models-for-vision/
- **Tags (unverified):** `qwen3-vl:4b` (~3.3 GB), `qwen2.5vl:7b`, `gemma3:4b`, `moondream`
- **Claims:** qwen3-vl:4b is smaller than llava:7b (3.3 vs 4.7 GB), has a 256K context against 32K, and does OCR in 32 languages. LLaVA 1.6 is a 2023 architecture that Ollama hasn't updated in ~2 years. qwen2.5vl:7b is reportedly much better on charts, screenshots and scanned docs.
- **Counterpoint:** Serverman still recommends LLaVA 1.6 7B as the default.
- **Assessment:** This is the clearest "known problem" fix of the week. Our image tier runs on the oldest model in the stack, and the replacement is *smaller* and claims better OCR.
- **Priority:** HIGH. **Value:** Likely replaces `llava` for image simple/medium.

### 9. Other open-weight releases noted (not locally runnable or not relevant)
- **MiMo-V2.6-Pro, GLM-5.3, Kimi K3:** top open-weight models on the Artificial Analysis index (https://artificialanalysis.ai/leaderboards/models). All are very large MoEs. SKIP.
- **Celeris-1 Decision** (Oct 8, 2026), mentioned in https://llm-stats.com/ai-news. Nothing verified about size or licence. SKIP.
- **Granite Code** (3B/8B/20B/34B, Apache 2.0): 2024-era, no 2026 refresh (https://github.com/ibm-granite/granite-code-models). SKIP.
- **StarCoder2:** no 2026 update found. SKIP.

### 10. Ollama runtime
- **Source:** https://releasebot.io/updates/ollama
- v0.40.0-rc6 (Oct 6) adds multimodal embeddings, and the v0.40 line makes **MLX the default backend on Apple Silicon**. That could noticeably speed up local models on the Mac with no model change. Worth upgrading once 0.40 goes stable. (Stable version numbers conflict between sources: 0.34.3 / 0.35.1.)

### Leaderboard check (LMArena)
- The live board was unreachable. Aggregators conflict: DeepSeek V4.x Pro is cited as the top open-weight text model (Elo 1410 vs 1467 depending on source), and Kimi K3 is cited as #1 on Frontend Code Arena. None of these runs on our hardware, so there is no impact on local recommendations.
- Sources: https://localaimaster.com/blog/lmarena-chatbot-arena-leaderboard ; https://www.codesota.com/arena/open-weight

---

## PHASE 2 — Performance Analysis (task logs)

| Item | Result |
|---|---|
| Task logs found matching `templates/task-log-*.md` | **0** |
| Other task logs in repo | `task-log-week-1.md` (repo root, committed 2026-05-18) |
| Real tasks logged in last 4 weeks | **0** |

`task-log-week-1.md` is a copy of the template. Its only filled-in entries are 4 **sample** tasks dated 2026-05-18: qwen-2.5-coder:1.5b ×1, qwen-2.5-coder:7b ×1, gemma4 ×1, Claude Sonnet ×1. All are marked successful, which gives 100% across 4 samples. These are illustrative data, not real usage, so **no success-rate conclusions can be drawn**.

**Honest summary:** Nobody has logged any tasks since the framework was created in May (~5 months). The performance analysis step has no data to work with. Until logging resumes, every recommendation below rests on external claims only.

---

## PHASE 3 — Model Recommendations (This Week)

**KEEP (No Changes)**
- qwen-1.5b (qwen2.5-coder:1.5b): fast and fine for simple tasks. No compelling small replacement verified.
- qwen-7b (qwen2.5-coder:7b): stays the default coder on 8–16 GB machines.
- mistral: stays for writing. Recheck after the Mistral Large 4 weight drop (~Oct 27) in case a small model ships with it.
- gemma4: current Google line, no newer release.

**CONSIDER TESTING**
- **qwen3-vl:4b** → replace `llava` (image simple/medium). It is smaller (3.3 vs 4.7 GB), newer, and claims much better OCR. Expected improvement: OCR and document extraction. Size impact: −1.4 GB.
- **qwen3-coder:30b (MoE, 3B active)** → candidate for coding medium/complex **on the NVIDIA box only**. Expected improvement: large quality jump over qwen2.5-coder:7b at similar or better tokens/sec. Size impact: +19 GB.
- **qwen2.5vl:7b**: as a fallback if qwen3-vl:4b's OCR is not enough for charts and scans.

**WAITLIST**
- **qwen3.8:27b**: strong, but ~17 GB dense and slow on CPU or Mac. Revisit if the 30B-A3B coder disappoints.
- **Mistral Large 4**: weights due ~Oct 27, but too large to run locally. Recheck the week of 2026-10-26 for any accompanying small model.
- **Ollama 0.40 (MLX on Apple Silicon)**: upgrade once it is stable.

**SKIP**
- DeepSeek V4 Pro/Flash/Vision, MiMo-V2.6-Pro, GLM-5.3, Kimi K3 (too large); qwen2.5-coder:14b (superseded); Granite Code and StarCoder2 (stale).

**STORAGE OPTIMIZATION**
- Current usage: **unknown**. `ollama list` cannot run in the cloud sandbox. Run it on each machine and paste the output here.
- If qwen3-vl:4b passes testing, `ollama rm llava` frees ~4.7 GB, for a net saving of ~1.4 GB.

---

## PHASE 4 — Decision Tool Changes

**No changes to `tools/model-selector-automated.py` this week.** Nothing was tested locally, and the sources are unverified aggregators. Changing defaults on that basis would be speculation.

Issue found while reviewing the tool: its model names (`qwen-1.5b`, `qwen-7b`, `mistral`, `gemma4`, `llava`) are **aliases, not real Ollama tags**. The tool's "Next steps: `ollama run qwen-1.5b`" would fail unless the user has created matching aliases (for example with `ollama cp qwen2.5-coder:1.5b qwen-1.5b`). Consider mapping each alias to its real tag in the tool.

---

## Next Week Focus
1. **Locally test qwen3-vl:4b against llava** on 2–3 real OCR or screenshot tasks, then update the `image` tier if it wins.
2. **Resume task logging.** With zero real logs, Phase 2 is empty every week. Also add or remove `tools/model-monitor.py` so the routine's first step works.
