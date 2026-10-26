# Weekly Model Research — Week of 10/26 - 11/01, 2026

**Research Date:** 2026-10-26
**Researcher:** Claude (scheduled cloud routine)
**Previous report:** `templates/weekly-model-research-2026-10-19.md`

---

## Run Notes / Limitations (read first)

- `tools/model-monitor.py` **still does not exist**. This is the third week running. `python3 tools/model-monitor.py --research` fails with `No such file or directory`.
- Direct access is still blocked. `curl` to ollama.com and huggingface.co gets a proxy `CONNECT 403`, and WebFetch on ollama.com fails with `ENOTFOUND`. **All findings come from web search snippets, mostly third-party aggregators and auto-generated digests. Treat every tag, size and benchmark as unverified** until you check it on https://ollama.com/library or the HF model card.
- There is no Ollama or GPU in the sandbox, so nothing was pulled or benchmarked.

---

## PHASE 1 — New Models Discovered (since 2026-10-19)

### 1. Recursive Flint (40B MoE, ~2.5B active, Apache 2.0) ★ biggest new coding find
- **Sources:** https://www.marktechpost.com/2026/10/21/recursive-flint-local-coding-model/ ; https://aicoder.com/news/news-20261022-recursive-flint-40b-a2-5b-open-weights-local-coding-model ; https://atomicagent.io/blog/recursive-flint/ ; https://www.mindstudio.ai/blog/recursive-flint-local-coding-model ; https://www.developersdigest.tech/blog/recursive-flint-ollama-local-coding-model-claude-code-2026
- **Released:** Oct 21, 2026. Ollama added native support in v0.40.8, macOS first. Linux and Windows reportedly followed in v0.40.9, but sources conflict on this. Reported tag: `flint:40b`.
- **Size:** ~23 GB Ollama download (one source cites a 26 GB int4 GGUF). Observed memory use was ~27–32 GB VRAM. 256K context.
- **Claims (vendor-reported):** SWE-bench Verified 74.2%, Terminal-Bench 2.1 54.9%, LiveCodeBench v6 80.3%. It reportedly runs at 125+ tok/s on an M4 Pro, and one reviewer logged 146 tok/s on an RTX 5090. In one independent agent test it passed 12 of 18 runs, so it is not as clean as the headline numbers suggest.
- **Assessment:** On paper this is far stronger than anything we run locally (qwen2.5-coder:7b is nowhere near 74% SWE-bench). It needs ~32 GB, so it **does not fit a 16 GB Mac and is tight or over on a 24 GB GPU.** It would only suit a 32 GB+ GPU or a 36–48 GB Mac. If we had that hardware, it is the first local model that could plausibly take over **coding/complex** from paid Claude calls.
- **Priority:** MEDIUM (HIGH if a ≥32 GB machine is available). **Value:** candidate for coding/complex on big hardware only. It does not replace `qwen-7b` on the Mac.

### 2. JetBrains Mellum2.1 Thinking (12B-A2.5B) — status update
- **Sources:** https://toolhalla.ai/blog/can-you-run-mellum-2-1-locally ; https://runaihome.com/blog/jetbrains-mellum-2-1-local-coding-llm-gpu-guide-2026/ ; https://llmconfigurator.com/en/models/mellum ; https://www.madebyagents.com/models/mellum2-1
- **Resolved from last week:** an **official GGUF is published** (`JetBrains/Mellum2.1-12B-A2.5B-Thinking-GGUF`). Quants range from BF16 24.3 GB to MXFP4_MOE 7.0 GB, with Q4_K_M recommended. There is **no official Ollama library tag** (`ollama.com/library/mellum2.1` returns 404 per one reviewer). The model runs through:
  `ollama run hf.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking-GGUF:Q4_K_M`
- **Assessment:** Unchanged. It is the best-fit replacement for `qwen-7b` on 16 GB machines, and the only thing blocking it is a local test. **Priority: HIGH.**

### 3. Nemotron 3.5 Bolt E4B (~4 GB) — status unclear
- **Sources:** https://www.datalearner.com/ai-models/pretrained-models/nemotron-3-5-bolt-e4b ; https://letsdatascience.com/news/nvidia-expands-nemotron-35-with-super-vl-and-bolt-ff81d36b ; https://releasebot.io/updates/ollama
- **Details:** It was due Oct 23. One release-notes aggregator describes it under Ollama v0.40.10 as "fast local conversations, image understanding, and tool use, 128K context". No primary source confirms it has shipped. NVIDIA positions it for conversational and physical/device agents. Licence is probably OpenMDW 1.1, unconfirmed.
- **Assessment:** If it really does image understanding at ~4 GB, it would be a **third vision candidate next to qwen3-vl:4b for replacing `llava`**. Wait for independent reviews. **Priority: LOW–MEDIUM. Value: WAITLIST.**

### 4. MiniCPM-V-4.7-35B-A3B (OpenBMB, Apache 2.0) — missed in earlier reports
- **Sources:** https://apxml.com/models/minicpm-v-4-7-35b-a3b ; https://www.oflight.co.jp/en/columns/minicpm-v-4-7-35b-a3b-requirements-vram-2026 ; https://llmrun.dev/model/openbmb-minicpm-v-4-7-35b-a3b
- **Released:** Oct 7 or Oct 12, 2026 (sources disagree). 35.2B total / 3B active. Q4_K_M is ~20–22 GB. The Ollama tag is unconfirmed (`hf.co/openbmb/MiniCPM-V-4.7-35B-A3B-gguf:Q4_K_M` or `minicpm-v:35b-a3b`).
- **Assessment:** A strong-looking multimodal MoE that is trending on HF. It needs a 24 GB GPU or 32 GB Mac. It could take **image/complex** (currently `claude-sonnet`) on the NVIDIA box. **Priority: LOW. Value: WAITLIST.**

### 5. Ollama "decision model" wave: pplx-decider 27B, Cloudflare Clef 27B, Bespoke nimble-v3 9B
- **Sources:** https://ollama.com/blog/ollama-now-supports-jev-style-decision-models ; https://releasebot.io/updates/ollama ; https://ollama.com/library?sort=newest (via search snippets)
- **Details:** pplx-decider is a Qwen3.8-27B fine-tune by Perplexity. Clef is Cloudflare's 27B multimodal decision model, dated Oct 19. nimble-v3 is a 9B model for classification, routing and scoring. All three follow on from Liquid d1 last week.
- **Assessment:** These are not task models. **nimble-v3 (9B)** is the most interesting as a possible ML backend for the selector's category/complexity routing, which today is brittle keyword matching. The 27B models are too big for that job. **Value: WAITLIST (selector idea).**

### 6. Ollama speech support (Gradium Phonon), Oct 24
- **Source:** https://ollama.com/blog (via search snippet)
- **Assessment:** Speech models are now in Ollama. This may be relevant to the **media** category, which currently routes audio to `qwen-7b`, a text model, so it can't actually process audio. Not evaluated yet. **Value: note for media category, revisit.**

### 7. Qwen3.8-Flash-Next / Qwen3.8-27B (HF trending)
- **Sources:** https://github.com/datnguyenquy94/news-radar/issues/826 ; https://github.com/datnguyenquy94/news-radar/issues/875 ; https://github.com/Chestnuts-Sisyphus/gittok/issues/1793 ; https://www.yottalabs.ai/post/qwen-4-release-date-what-is-known-how-to-prepare-2026.md
- **Details:** Qwen3.8-27B is still #1 on HF trending (~18.4K likes). Flash-Next shows up in digests but appears to date from **Aug 28**, so it is not new. There is no Qwen 4 and no new small Qwen coder.
- **Assessment:** No change. qwen3.8:27b stays on the WAITLIST for the 24 GB "complex" tier.

### 8. Mistral Large 4 weights — still not released
- **Sources:** https://www.mindstudio.ai/blog/mistral-large-4-pricing-open-weights ; https://www.marktechpost.com/2026/10/06/mistral-ai-releases-mistral-large-4-le-chonk-a-1-05t-parameter-open-weight-multimodal-moe/ ; https://www.developersdigest.tech/blog/mistral-large-4-open-weight-model-2026
- **Details:** Mistral only commits to "end of October". VentureBeat says Oct 27, and the HF page says Oct 31. Expect a custom licence. At 1.05T / 49B active it can't run locally, and no small companion model has been announced.
- **Value:** SKIP for local use. The writing slot (`mistral`) stays unchanged.

### 9. Other items checked
- **LTX-2.5 (Lightricks):** a 4K text-to-video diffusion model trending on HF. It is not an LLM and has no place in the selector. SKIP.
- **Ornith-1.5-122B, Underdog-Saluki-27B:** trending on HF. Too big, or niche (function-calling) with no evidence of a gain. SKIP.
- **Meta Muse Spark Open, Reflection Beam, Nemotron 3.5 Super/Bolt 74B:** covered last week. No change, all SKIP for size.

### 10. Specific candidates from the routine prompt
| Candidate | Status this week |
|---|---|
| qwen2.5-coder:14b | No change. Superseded by Mellum2.1 (16 GB class) and Flint (32 GB class). SKIP. |
| deepseek-r1 variants | No new small distills found. SKIP. |
| mistral-small/large | Large 4 weights still pending (see #8). Nothing small. |
| llama3.3 | No new variants. Meta's focus is the Muse line. |
| gemma4 | No new variant since April 2026. KEEP. |
| llava | Unchanged. Replacement candidates are now qwen3-vl:4b, Bolt E4B if confirmed, and MiniCPM-V-4.7 for big hardware. |
| starcoder2 / granite-code | No updates. SKIP. |
| new code-specific models | **Recursive Flint** (new). Mellum2.1 (GGUF now confirmed). |

### 11. Ollama runtime
- **Source:** https://releasebot.io/updates/ollama ; https://www.developersdigest.tech/blog/ollama-0-40-mlx-default-disk-doubling-2026
- Release notes reportedly reached **v0.40.10/0.40.11**, but I found no primary release notes for those versions. Flint support landed in v0.40.8–0.40.9. Note: one write-up warns that 0.40's MLX default on Mac can **roughly double disk use** (lazy GGUF→MLX conversion). Check free disk before upgrading the Mac.

### Leaderboard check (LMArena)
- I could not reach the live board. A Manifold snapshot from early October shows gemini-4-argon-high #1 (1525), with Anthropic models filling the next places. No open-weight model is near the top: the latest specific figure has GLM-5.1 at ~#27. **No impact on local recommendations.** Sources: https://manifold.markets/Terminator2/which-company-will-have-the-1-model ; https://futuresearch.ai/app/p/a/open-weight-llm-overtaking-closed-weight

---

## PHASE 2 — Performance Analysis (task logs)

| Item | Result |
|---|---|
| `templates/task-log-*.md` (excluding template) | **0** |
| Other logs | `task-log-week-1.md` (repo root), unchanged since 2026-05-18 |
| Real tasks logged in last 4 weeks | **0** |
| Success rate | **N/A** (no data) |

**Honest summary:** This is the third week with no data. Nothing has been logged in ~5 months. Without logs, Phase 2 can't do its job, and every recommendation rests only on vendor or aggregator claims.

---

## PHASE 3 — Model Recommendations (This Week)

**KEEP (No Changes)**
- qwen-1.5b (qwen2.5-coder:1.5b): simple tasks.
- qwen-7b (qwen2.5-coder:7b): default coder until Mellum2.1 is tested.
- mistral: writing. Nothing new and small has appeared.
- gemma4: data/analysis/writing-simple. No newer Google release.
- llava: until a vision replacement is tested.

**CONSIDER TESTING** (priority order)
1. **Mellum2.1 Thinking (12B-A2.5B)** → replace `qwen-7b` (coding medium/complex, data medium, security medium). The GGUF is now confirmed, so pull it with `ollama run hf.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking-GGUF:Q4_K_M`. +~2.5 GB (Q4_K_M) over qwen2.5-coder:7b. It fits 16 GB machines.
2. **qwen3-vl:4b** → replace `llava` (carried over, still untested). −~1.4 GB.
3. **Recursive Flint (`flint:40b`)** → **only on a ≥32 GB GPU or ≥36 GB Mac**. Candidate to move **coding/complex** off `qwen-7b`+Claude ($0.15/task) to $0. ~23 GB on disk. Replaces last week's qwen3-coder:30b idea, since Flint claims much higher scores at the same speed class.

**WAITLIST**
- **Nemotron 3.5 Bolt E4B**: confirm it shipped and that its image understanding is real. Possible ~4 GB llava replacement.
- **MiniCPM-V-4.7-35B-A3B**: image/complex on the 24 GB GPU (would replace claude-sonnet for that slot).
- **Muse Glimmer 30B / qwen3.8:27b**: 24 GB "complex" analysis tier (carried over).
- **nimble-v3 (9B) / Liquid d1**: ML-based routing for the selector instead of keywords.
- **Ollama speech models (Phonon)**: the media category currently has no real audio model.

**SKIP**
- Mistral Large 4, Muse Spark Open, Reflection Beam, Nemotron Super/Bolt 74B, Ornith-1.5-122B (too large); pplx-decider and Clef (27B classifiers, overkill); LTX-2.5 (video diffusion); qwen2.5-coder:14b, granite-code, starcoder2 (stale or superseded).

**STORAGE OPTIMIZATION**
- Current usage: **unknown**, because `ollama list` can't run in the sandbox.
- Potential: llava→qwen3-vl:4b saves ~1.4 GB. qwen2.5-coder:7b→Mellum2.1 Q4_K_M costs ~+2.5 GB. Net ~+1.1 GB if both are adopted. Flint adds ~23 GB on whichever machine runs it.
- If you upgrade the Mac to Ollama 0.40.x, budget for MLX conversion copies, which can roughly double disk use per model.

---

## PHASE 4 — Decision Tool Changes

**No changes to `tools/model-selector-automated.py`.** Nothing has been tested locally, and no task-log evidence exists. Changing the defaults on vendor claims alone would be speculative.

Issues still open in the tool (carried over, unfixed):
1. The model names (`qwen-1.5b`, `qwen-7b`, `llava`, …) are aliases, not real Ollama tags, so `ollama run qwen-1.5b` fails without `ollama cp` aliases.
2. Keyword detection is order-dependent. "write" and "generate" route to coding before writing, "analyze" hits data before analysis, and "extract" sits under image.
3. *(New)* `media/medium` routes "complex video/audio processing" to `qwen-7b`, a text-only coder. Now that Ollama supports speech models, this slot needs a real audio-capable model or an honest Claude fallback.

---

## Next Week Focus
1. **On a local machine (needs the user):** run Mellum2.1 against qwen2.5-coder:7b and qwen3-vl:4b against llava on 2–3 real tasks each. Log the results in `templates/task-log-week-N.md` so Phase 2 finally has data. Three weeks of untested recommendations is the main bottleneck.
2. **2026-11-02 run:** confirm the Mistral Large 4 weight drop and licence, and confirm Bolt E4B shipped. Look for independent Flint reviews. Also either create `tools/model-monitor.py` or remove step 1 from the routine prompt.
