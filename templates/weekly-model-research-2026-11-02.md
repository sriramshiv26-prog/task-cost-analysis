# Weekly Model Research — Week of 11/02 - 11/08, 2026

**Research Date:** 2026-11-02
**Researcher:** Claude (scheduled cloud routine)
**Previous report:** `templates/weekly-model-research-2026-10-26.md`

---

## Run Notes / Limitations (read first)

- `tools/model-monitor.py` **still does not exist**. This is the fourth week in a row: `python3 tools/model-monitor.py --research` fails with `No such file or directory`. Either the script should be created or the step dropped from the routine prompt.
- Direct access is still blocked. `curl` to ollama.com and huggingface.co gets a proxy `CONNECT 403`. **Every finding here comes from web search snippets**, many from third-party aggregators and auto-generated digests. Treat sizes, tags and benchmarks as unverified until you check them on https://ollama.com/library or the HF model card.
- The sandbox has no Ollama and no GPU, so nothing was pulled or benchmarked.

---

## PHASE 1 — Findings (since 2026-10-26)

### 1. Liquid AI LFM3 family — now in the Ollama library ★ most relevant new find
- **Sources:** https://x.com/ollama/status/2115147945045864766 ; https://github.com/ollama/ollama/releases ; https://dev.to/madnessbrains_i/ollama-04013-puts-liquid-lfm3-audio-on-windows-local-stttts-that-fits-in-2-gb-586l ; https://www.orcarouter.ai/blog/lfm3-1-7b-ollama-release ; https://www.orcarouter.ai/blog/lfm3-audio-2b-ollama-local-speech ; https://www.youtube.com/watch?v=Xo1ohj1cCy4
- **Released:** ~Oct 27, 2026. Ollama's official account announced it. Ollama v0.40.13 extended the audio and omni variants to Linux and Windows.
- **Lineup (all ~2B):** `lfm3` (1.7B text, 256K context, ~1–1.7 GB), `lfm3-vl` (vision), `lfm3-audio` (STT/TTS, ~1.5–2.4 GB), `lfm3-omni` (text, image and audio), plus d1 decision models.
- **Licence:** **Caution.** One social post claims free commercial use is limited to companies under $10M yearly revenue (the LFM Open License pattern). Not verified against Liquid's terms.
- **Assessment:**
  - **`lfm3-audio`** is the first **small, official-library, cross-platform audio model**. It directly fixes open issue #3 in the selector: `media/medium` routes "video/audio processing" to `qwen-7b`, a text-only coder. **Priority: MEDIUM–HIGH → CONSIDER TESTING.**
  - **`lfm3-vl`** is another small `llava` replacement candidate, alongside qwen3-vl:4b and Bolt E4B.
  - **`lfm3` (1.7B text)** is a possible rival to `qwen-1.5b` for non-coding simple tasks. The OrcaRouter review's "report card that splits in two" suggests mixed results. Low priority.
  - **d1 decision models** carry over last week's WAITLIST idea of ML-based routing in the selector.

### 2. Nemotron 3.5 Bolt E4B — CONFIRMED shipped (resolved from last week)
- **Sources:** https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB ; https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF ; https://build.nvidia.com/nvidia/nemotron-3.5-bolt-e4b.md ; https://docs.nvidia.com/nemo/automodel/model-coverage/vision-language-models/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB-BF16 ; https://pasqualepillitteri.it/en/news/26810/nemotron-3-5-bolt-e4b-nvidia-robots-games
- **Details:** Released 2026-10-23. It is post-trained from **Gemma-4-E4B-it**, and NVIDIA's docs list it under vision-language models, so image understanding is real. There is no official Ollama library tag; the HF route is `ollama run hf.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB:Q4_K_M` (~6.2 GB quant per one source; the "4GB" name may mean the memory target). Licence: OpenMDW-1.1.
- **Assessment:** A valid `llava` replacement candidate, but it targets robotics and game agents, not OCR or document extraction. qwen3-vl:4b and lfm3-vl are likely better fits for the selector's "image description / OCR" slots. **Moves from WAITLIST to "test if time"; priority LOW–MEDIUM.**

### 3. Mistral Large 4 ("Le Chonk") weights — CONFIRMED released (resolved)
- **Sources:** https://mistral.ai/news/mistral-large-4-oss/ ; https://huggingface.co/blog/mistral-large4 ; https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B ; https://pasqualepillitteri.it/en/news/28041/mistral-large-4-le-chonk-open-weights-hugging-face ; https://dev.to/gabrielanhaia/mistral-large-4s-1t-weights-are-out-serve-it-as-an-api-to-others-and-you-need-a-license-1pkc
- **Details:** Released ~Oct 29 as `mistralai/Mistral-Large-4-1T-A52B`: 1T total / 52B active (earlier reports said 1.05T / 49B), 1M context, multimodal. Licence is the Mistral Ecosystem Open-Weight License (modified MIT). Internal use is free; offering it as a hosted model service needs a commercial licence. Community GGUF and NVFP4 builds exist.
- **Assessment:** Needs datacenter GPUs and is irrelevant for local use. No small Mistral companion model was announced. **SKIP. The `mistral` writing slot stays.**

### 4. Recursive Flint (`flint:40b`) — still no independent benchmark
- **Sources:** https://ollama.com/library/flint:40b ; https://www.mindstudio.ai/blog/recursive-flint-local-coding-model ; https://www.orcarouter.ai/blog/flint-40b-a2-5b-local-coding ; https://sumus.im/blog/recursive-flint ; https://www.explainx.ai/blog/recursive-flint-40b-open-weight-coding-model-eureka-machine-apache-2-local-2026 ; https://ai-tldr.dev/models/recursive-flint/ ; https://github.com/datnguyenquy94/news-radar/issues/919
- **Update:** The **official Ollama library tag `flint:40b` is confirmed** (the page notes the scores are publisher-reported). Several write-ups say no third party has published an evaluation yet. Measured VRAM is still "just over 32 GB", and one review says llama.cpp speed on an M4 Max "told a more complicated story" than the 125 tok/s claim. Trending on HF (`RecursiveSI/flint`, ~1.2K likes, ~14K downloads).
- **Assessment:** Unchanged. It is only for ≥32 GB GPUs or ≥36 GB Macs. **Priority: MEDIUM (HIGH if such a machine exists).**

### 5. Spark-X2.6-4B (iFLYTEK/SparkLLM, Apache 2.0) — new to this report
- **Sources:** https://aiweekly.co/alerts/sparkllm-ships-spark-x26-on-device-models-in-17b-and-4b ; https://www.llmreference.com/model/spark-x2.6-4b ; https://llmrun.dev/model/xhtoken-spark-x2-6-4b ; https://www.mindstudio.ai/blog/run-spark-x26-4b-locally-ollama ; https://ollama.com/maternion/spark-x2.6 (community tag) ; https://aiwiki.ai/wiki/spark_x2_6_4b
- **Details:** ~Oct 20, 2026. 4B and 1.7B on-device agent models with claimed 1M context. Self-reported average of 63.3, against 52.1 for X2.5-4B and 49.1 for Qwen3.5-9B. A **community** Ollama tag exists (`maternion/spark-x2.6`), not an official one.
- **Assessment:** If the scores hold, a 4B model beating a 9B is interesting for the "simple" tier. But the numbers are vendor-only, the Ollama tag is community-built, and it isn't code-specialised. **WAITLIST** until there is an independent comparison against qwen2.5-coder:1.5b / gemma4.

### 6. DeepSeek V4.1 Flash (1017 snapshot) — trending, not local
- **Sources:** https://huggingface.co/unsloth/DeepSeek-V4.1-Flash-1017-GGUF ; https://huggingface.co/mrfakename/DeepSeek-V4.1-Flash-1017-GGUF ; https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF ; https://github.com/datnguyenquy94/news-radar/issues/931 ; https://aiera.blog/best-open-weight-ai-models-october-2026/
- **Details:** Despite the "Flash" name it is ~750–763B total parameters. The smallest usable GGUF is ~138 GB (IQ2_XXS), and Q4_K_M is ~414 GiB. Mainline llama.cpp support was lagging. It leads HF trending image-text-to-text.
- **Assessment:** **SKIP** for local use. This also covers the routine's "deepseek-r1 variants" check: **no new small DeepSeek distills** this week.

### 7. Mellum2.1 Thinking (12B-A2.5B) — no new evidence
- **Sources:** https://interfaze.ai/models/jetbrainsmellum2-12b-a25b-thinking.md ; https://aiagentstore.ai/ai-models/mellum-2-1-thinking ; https://www.pulse.bot/ai/news/jetbrains-open-sources-mellum2-to-go-where-claude-code-cant-86b4e638-351f-4e62-a61d-b6522c0de23c/
- **Details:** There is still no independent local head-to-head against qwen2.5-coder:7b. JetBrains' "pairwise" win rate is measured against **Qwen2.5-7B-Instruct, not Qwen2.5-Coder**. LiveCodeBench v6 is 69.9 (self-reported). Throughput parity with Qwen2.5-7B (+21% under concurrency) was measured on an H100, not consumer hardware.
- **Assessment:** Still the top test candidate for replacing `qwen-7b` on 16 GB machines, but the evidence is weaker than it looked. JetBrains never directly compared it against our current coder. **Priority: HIGH (test).**

### 8. Ollama runtime
- **Sources:** https://github.com/ollama/ollama/releases ; https://updatify.io/releases/ollama ; https://ollamaherd.com/guides/ollama-release-notes ; https://www.promptquorum.com/local-llms/top-open-source-models-ollama
- Release feeds now show **v0.40.13** (LFM3 audio/omni on Linux/Windows). Aggregators disagree on the "stable" version (one still says v0.40.5). Last week's warning still applies: on Mac, 0.40.x's MLX default can roughly double disk use.

### 9. HF trending (week of Oct 27)
- **Sources:** https://github.com/datnguyenquy94/news-radar/issues/908 ; https://github.com/datnguyenquy94/news-radar/issues/919 ; https://github.com/datnguyenquy94/news-radar/issues/931 ; https://github.com/kakapez/agents-radar/issues/1684
- Qwen3.8-27B is still #1 by likes (~18–19K). DeepSeek-V4.1-Flash-1017 leads by downloads. Flint and Spark-X2.6-4B are rising, and LTX-2.5 (video) is still high. **No new small Qwen coder and no Qwen 4.**

### 10. LMArena leaderboard
- **Sources:** https://manifold.markets/CraigDemel/what-company-will-have-the-top-mode ; https://www.gjopen.com/questions/4792-which-organization-s-large-language-model-llm-will-be-ranked-first-as-of-13-november-2026-according-to-lmarena-s-text-arena ; https://benchlm.ai/stats/open-source-llm ; https://www.swfte.com/fr/ai/lmarena-ai
- No live November snapshot was reachable (the site is now arena.ai). The latest secondary data still shows closed models on top. Open-weight leaders (Kimi K3, GLM-5.2, DeepSeek V4.1 Pro) are all far too large for local use. **No impact on local recommendations.**

### 11. Specific candidates from the routine prompt
| Candidate | Status this week |
|---|---|
| qwen2.5-coder:14b | No change. Superseded by Mellum2.1 (16 GB class) and Flint (32 GB class). SKIP. |
| deepseek-r1 variants | No new small distills. V4.1 Flash is ~750B. SKIP. |
| mistral-small/large | Large 4 weights released (1T, not local). No new small model. SKIP. |
| llama3.3 | No new variants. SKIP. |
| gemma4 | No new Google release. Bolt E4B is an NVIDIA derivative of Gemma-4-E4B. KEEP. |
| llava | Replacement candidates now: qwen3-vl:4b, **lfm3-vl (new)**, Bolt E4B (confirmed). |
| starcoder2 / granite-code | No updates. SKIP. |
| new code-specific models | No new ones this week. Flint now has an official library tag. Mellum2.1 is untested. |

**Honest summary:** It was a quiet week for code models. The only actionable new item is **LFM3**, mainly `lfm3-audio` for the media category. Last week's two open questions (Bolt E4B shipping, Mistral Large 4 weights) are resolved. Neither changes the local lineup.

---

## PHASE 2 — Performance Analysis (task logs)

| Item | Result |
|---|---|
| `templates/task-log-*.md` (excluding template) | **0** |
| Other logs | `task-log-week-1.md` (repo root): byte-identical size to the template, last committed 2026-05-18 |
| Real tasks logged in last 4 weeks | **0** |
| Tasks by model / success rate | **N/A** (no data) |

**Honest summary:** This is the fourth week with no data. Without logs, Phase 2 can't measure anything, and every recommendation below rests only on vendor or aggregator claims.

---

## PHASE 3 — Model Recommendations (This Week)

**KEEP (No Changes)**
- qwen-1.5b (qwen2.5-coder:1.5b): simple tasks.
- qwen-7b (qwen2.5-coder:7b): default coder until Mellum2.1 is tested.
- mistral: writing. Mistral released nothing small.
- gemma4: data/analysis/writing-simple.
- llava: until a vision replacement is tested.

**CONSIDER TESTING** (priority order)
1. **Mellum2.1 Thinking (12B-A2.5B)** → `qwen-7b` slots. `ollama run hf.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking-GGUF:Q4_K_M`. ~+2.5 GB.
2. **`lfm3-audio` (~2 GB, official library) — NEW** → `media/medium` audio work, which today goes to a text-only model. `ollama run lfm3-audio`. Check the licence's revenue cap first.
3. **qwen3-vl:4b vs `lfm3-vl` — lfm3-vl NEW** → replace `llava`. Run both on the same 2–3 OCR/description images.
4. **Recursive Flint (`flint:40b`)** → coding/complex, **only on ≥32 GB VRAM / ≥36 GB Mac**. ~23 GB.

**WAITLIST**
- **Nemotron 3.5 Bolt E4B** (confirmed shipped, HF-only tag, agent/robotics focus): a fallback vision candidate.
- **Spark-X2.6-4B** (community Ollama tag, vendor-only scores): simple tier.
- **lfm3 (1.7B text)**: simple non-coding tasks; reviews are mixed.
- **MiniCPM-V-4.7-35B-A3B**: image/complex on a 24 GB GPU (carried over).
- **qwen3.8:27b / Muse Glimmer 30B**: 24 GB "complex" analysis tier (carried over).
- **LFM3 d1 / nimble-v3**: ML routing for the selector (carried over).

**SKIP**
- Mistral Large 4 (1T), DeepSeek V4.1 Flash (~750B), Muse Spark Open, Kimi K3, GLM-5.2 (all far too large); LTX-2.5 (video diffusion); qwen2.5-coder:14b, granite-code, starcoder2 (stale or superseded).

**STORAGE OPTIMIZATION**
- Current usage: **unknown**, because `ollama list` can't run in the sandbox.
- Potential: llava→qwen3-vl:4b or lfm3-vl saves ~1–2 GB. qwen2.5-coder:7b→Mellum2.1 Q4_K_M costs ~+2.5 GB. Adding lfm3-audio costs ~+2 GB. Net ≈ +1.5–3 GB if all three are adopted.
- On Mac with Ollama 0.40.x, budget for MLX conversion copies.

---

## PHASE 4 — Decision Tool Changes

**No changes to `tools/model-selector-automated.py`.** Nothing has been tested locally and there is no task-log evidence, so changing defaults on vendor claims would be speculative.

A candidate change for after a test: if `lfm3-audio` works on a real transcription task, change `"media": {"medium": ...}` from `("qwen-7b", 0, "Complex video/audio processing")` to `("lfm3-audio", 0, "Speech-to-text / text-to-speech")`.

Issues still open in the tool (carried over, unfixed):
1. The model names (`qwen-1.5b`, `qwen-7b`, …) are aliases, not real Ollama tags, so `ollama run qwen-1.5b` fails without `ollama cp` aliases.
2. Keyword detection is order-dependent ("write" and "generate" → coding; "analyze" → data; "extract" → image).
3. `media/medium` routes audio to a text-only coder (see above; there is now a concrete fix candidate).

---

## Next Week Focus
1. **On a local machine (needs the user):** this is the fourth week of untested recommendations. Testing just two of them would unblock the routine: Mellum2.1 vs qwen2.5-coder:7b on 2–3 coding tasks, and `lfm3-audio` on one transcription. Log the results in `templates/task-log-week-N.md`.
2. **2026-11-09 run:** look for an independent Flint eval and an LFM3 licence confirmation, and check for any small Mistral or Qwen coder release. Create `tools/model-monitor.py` or drop step 1 from the routine prompt.
