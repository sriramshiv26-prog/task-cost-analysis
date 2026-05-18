# Decision Tree 3: Video, Audio & Image Processing

Use this to choose the right model and tools for media tasks.

---

## Quick Decision Matrix

| Task Type | Input | Model/Tool | Cost | Time |
|-----------|-------|-----------|------|------|
| Video transcription | MP4/MOV | whisper.cpp | $0 | 5-10 min |
| Generate subtitles | Audio + transcript | qwen2.5-coder:7b | $0 | 30s-2 min |
| Image OCR | PNG/JPG | llava | $0 | 10-30s |
| Image analysis | PNG/JPG with question | llava | $0 | 20-60s |
| Video editing script | Requirements | ffmpeg + qwen2.5-coder:7b | $0 | 1-2 min |
| Audio enhancement | WAV/MP3 | ffmpeg | $0 | 2-5 min |
| Image classification | Images + categories | llava | $0 | 30-60s per image |
| Batch media conversion | 10+ files | ffmpeg + bash | $0 | 1-3 min setup |

---

## Decision Flow

```
START: I have a media task
  ↓
What type of media?

A. VIDEO
  ├─ Transcribe video to text?
  │   └─ YES → whisper.cpp (local, free) → output: .srt or .vtt
  │
  ├─ Generate subtitles from transcript?
  │   └─ YES → qwen2.5-coder:7b (format as SRT) ($0, 30-60s)
  │
  ├─ Trim, resize, or encode video?
  │   └─ YES → ffmpeg command generation
  │       ├─ Simple (cut, resize)? → qwen2.5-coder:1.5b ($0, 20s)
  │       └─ Complex (filters, codec tuning)? → qwen2.5-coder:7b ($0, 60s)
  │
  └─ Edit multiple videos (batch)?
      └─ YES → ffmpeg script + qwen2.5-coder:7b ($0, 1-2 min)

B. AUDIO
  ├─ Transcribe audio to text?
  │   └─ YES → whisper.cpp (free, local) + qwen2.5-coder:1.5b (cleanup) ($0)
  │
  ├─ Remove background noise?
  │   └─ YES → ffmpeg + sox ($0)
  │
  ├─ Convert formats or bitrate?
  │   └─ YES → ffmpeg command by qwen2.5-coder:1.5b ($0, 20s)
  │
  └─ Generate audio from text (TTS)?
      └─ YES → Use external TTS API (not local cost-effective)

C. IMAGE
  ├─ Read text from image (OCR)?
  │   └─ YES → llava:latest ($0, 15-30s per image)
  │
  ├─ Describe image content?
  │   └─ YES → llava:latest with question ($0, 20-40s)
  │
  ├─ Classify images by type?
  │   └─ YES → llava in batch ($0, 30s per image)
  │
  └─ Edit/resize/filter images?
      ├─ Simple? → qwen2.5-coder:1.5b generates Python PIL script ($0, 20s)
      └─ Complex? → qwen2.5-coder:7b generates PIL or ImageMagick ($0, 60s)

D. DOCUMENT IMAGES (PDFs, scans)
  ├─ Extract text from PDF pages?
  │   └─ Use pdfplumber (Python, free) + llava if OCR needed
  │
  └─ Convert PDF to images?
      └─ Use ghostscript or pdftoppm (free, local)
```

---

## Tool Details

### Video & Audio: whisper.cpp
**What it is:** Local, offline speech-to-text (OpenAI Whisper)

**Best for:**
- Transcribing any video/audio (no API calls, privacy)
- Generating subtitles
- Creating transcripts for analysis

**Speed:**
- ~10-30 minutes per hour of audio (M1 Mac is faster)
- Runs locally, no network

**Cost:** $0 (installed locally)

**Typical usage:**
```bash
whisper audio.mp4 --output_format srt
# Output: audio.srt (subtitle file)
```

**When to use Claude instead:**
- Need real-time transcription (whisper takes time)
- Need complex speaker identification
→ Use Claude API ($0.003 per minute of audio = expensive, but real-time option exists)

---

### Images: llava:latest
**What it is:** Local vision model (can read and describe images)

**Best for:**
- OCR (text extraction from images)
- Image analysis/description
- Classification tasks
- Accessibility (describing images)

**Speed:**
- ~15-40 seconds per image (M1 Mac is faster than Windows)
- Batch processing: 30+ images in parallel

**Cost:** $0 (installed locally)

**Typical usage:**
```bash
ollama run llava:latest "Describe what's in this image: [image path]"
ollama run llava:latest "Extract all text from this screenshot"
```

**Quality:**
- Good for general descriptions (85-95% accurate)
- Excellent for OCR on readable text (90-98%)
- Decent for object detection (70-80%)

**When to use Claude instead:**
- Need expert analysis ("is this photo authentic?")
- Need complex reasoning about image content
- Legal/medical image review (needs human-expert-level accuracy)
→ Use Claude ($0.10-0.30 per image)

---

### Video/Audio Editing: ffmpeg
**What it is:** Industry-standard video/audio processing tool

**Cost:** $0 (open source)

**Common tasks & qwen model:**

| Task | Command Complexity | Model |
|------|-------------------|-------|
| Cut video (0:30 to 2:00) | Simple | qwen2.5-coder:1.5b |
| Resize video (1080p → 720p) | Simple | qwen2.5-coder:1.5b |
| Change audio bitrate | Simple | qwen2.5-coder:1.5b |
| Convert codec (H264 → VP9) | Medium | qwen2.5-coder:7b |
| Add filters/effects | Complex | qwen2.5-coder:7b |
| Batch process 50 videos | Complex | qwen2.5-coder:7b |

**Example:** "Generate ffmpeg command to cut video from 30s to 2min and resize to 720p"
- Model: qwen2.5-coder:1.5b
- Cost: $0
- Time: 15 seconds
- Output: `ffmpeg -ss 30 -i input.mp4 -t 90 -vf scale=1280:-1 output.mp4`

---

## Real-World Examples

### Example 1: Batch Subtitle Generation
```
Task: Generate subtitles for 10 video files
Approach:
  1. whisper.cpp transcribe each → .srt files ($0, 20 min total)
  2. qwen2.5-coder:7b write cleanup script → fixes timestamps ($0, 1 min)
  3. Run cleanup on all files ($0, 5 sec)
Total cost: $0
Total time: ~25 minutes
Output: 10 subtitle files ready to embed
```

### Example 2: Image Text Extraction
```
Task: Extract text from 100 receipts (JPG scans)
Approach:
  1. Loop with llava:latest on each image ($0, 30s per image)
  2. Parse output with qwen2.5-coder:1.5b ($0, cleanup script)
Total cost: $0
Total time: ~1-2 hours (batch in parallel: 10-20 min)
Output: Structured receipt data (JSON)
Quality: 85-95% accuracy (qwen2.5-coder cleans OCR errors)
```

### Example 3: Video Compression Script
```
Task: Compress 50 video files from 1080p to 720p, reduce bitrate
Approach:
  1. qwen2.5-coder:7b generate ffmpeg batch script ($0, 1 min)
  2. Run script in parallel ($0, 20-30 min execution)
Total cost: $0
Total time: 35 minutes
Savings: Instead of transcoding each manually (2 hours), automated script runs while you work
Quality: Lossless quality reduction, 30-40% file size reduction
```

---

## Cost Comparison

| Approach | Cost | Time | Quality |
|----------|------|------|---------|
| **Pure local (Ollama + ffmpeg)** | $0 | 10-30 min | 85-95% |
| **Hybrid (local + Claude review)** | $0.20 | 15-35 min | 95-99% |
| **Pure API (Whisper API + Claude)** | $0.50-2.00 | 1-5 min | 98-99% |
| **Professional service (Rev.com)** | $1.50-3.00/min | 24 hours | 99%+ |

**Recommendation:** Use pure local (Ollama + ffmpeg) for everything. Only escalate to Claude if quality matters (legal, medical, accessibility) — cost is still negligible.

---

## Setup Checklist

**Mac M1 Max:**
```bash
# Already have Ollama with llava:latest
ollama pull llava:latest

# Install whisper.cpp
brew install whisper-cpp

# Install ffmpeg
brew install ffmpeg

# Verify
whisper-cpp --version
ffmpeg -version
```

**Windows RTX 5060 Ti:**
```bash
# Ollama with llava (auto on GPU)
ollama pull llava:latest

# whisper.cpp
# Download from https://github.com/ggerganov/whisper.cpp or via Chocolatey
choco install whisper-cpp

# ffmpeg
choco install ffmpeg
```

---

## Troubleshooting

**Whisper is too slow:**
- True for long audio (1 hour = 20 minutes on M1)
- Consider batching or parallel processing
- Or use whisper.cpp with GPU acceleration (CUDA on Windows RTX)

**llava OCR isn't accurate enough:**
- Use qwen2.5-coder:7b to post-process llava output
- Or use Tesseract (free, local) for pure text OCR
- Cost still $0, accuracy improves to 95%+

**ffmpeg command too complex:**
- Start with simple task (cut/resize)
- Escalate complex filters to Claude ($0.15)
- Or look up ffmpeg docs + qwen2.5-coder:7b

---

## When to Use Claude Instead

| Situation | Cost | Reason |
|-----------|------|--------|
| "Is this video authentic?" (forensics) | $0.20 | Expert reasoning |
| "Describe medical imaging findings" | $0.30 | Critical accuracy |
| "Legal document OCR with confidence scores" | $0.25 | Audit trail needed |
| "Complex video effects (motion tracking)" | $0.15 | Advanced reasoning |
| "Audio analysis (speaker emotion)" | $0.20 | Complex inference |

All other media tasks: use local tools ($0).

---

## Next Steps

1. **Try whisper.cpp** on next video — measure actual time
2. **Test llava OCR** on a sample image — check accuracy
3. **Generate ffmpeg script** with qwen2.5-coder — verify it works
4. **Log results** — file size savings, time taken, quality

See: `reference/monthly-metrics.md` for tracking media task costs.
