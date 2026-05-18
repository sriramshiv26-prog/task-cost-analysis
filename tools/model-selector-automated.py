#!/usr/bin/env python3
"""
Automated Model Selector for Task Cost Analysis Framework

Reads task description and recommends optimal model based on:
- Task category
- Complexity assessment
- Current model performance metrics
- Hardware capabilities

Usage:
    python tools/model-selector-automated.py --task "Build a React component"
    python tools/model-selector-automated.py --task "Analyze sales data for trends" --show-alternatives
"""

import argparse
import json
import os
import sys
from typing import Dict, List, Tuple

# Model recommendations by task category and complexity
MODEL_RECOMMENDATIONS = {
    "coding": {
        "simple": ("qwen-1.5b", 0, "Bug fixes, simple scripts"),
        "medium": ("qwen-7b", 0, "Features, APIs, complex logic"),
        "complex": ("qwen-7b", 0.15, "Architecture decisions, design reviews"),
    },
    "data": {
        "simple": ("qwen-1.5b", 0, "Data validation, inspection"),
        "medium": ("qwen-7b", 0, "Transformation, cleaning"),
        "complex": ("gemma4", 0, "Analysis, pattern detection"),
    },
    "media": {
        "simple": ("qwen-1.5b", 0, "Format conversion, simple editing"),
        "medium": ("qwen-7b", 0, "Complex video/audio processing"),
        "complex": ("claude-sonnet", 0.20, "Complex media analysis"),
    },
    "writing": {
        "simple": ("gemma4", 0, "Summaries, short content"),
        "medium": ("mistral", 0, "Blog posts, tutorials"),
        "complex": ("mistral", 0, "Long-form, complex narratives"),
    },
    "analysis": {
        "simple": ("gemma4", 0, "Basic statistics"),
        "medium": ("gemma4", 0, "Trend analysis, insights"),
        "complex": ("claude-sonnet", 0.20, "Complex reasoning"),
    },
    "image": {
        "simple": ("llava", 0, "Image description"),
        "medium": ("llava", 0, "OCR, content extraction"),
        "complex": ("claude-sonnet", 0.15, "Medical/specialized image analysis"),
    },
    "security": {
        "simple": ("qwen-1.5b", 0, "Dependency audit"),
        "medium": ("qwen-7b", 0, "Code scanning"),
        "complex": ("claude-sonnet", 0.25, "Compliance audit"),
    },
    "specialized": {
        "simple": ("claude-sonnet", 0.15, "Legal/financial/medical guidance"),
        "medium": ("claude-sonnet", 0.25, "Complex specialized analysis"),
        "complex": ("claude-sonnet", 0.40, "Critical specialized decision"),
    },
}

# Keywords to auto-detect category
CATEGORY_KEYWORDS = {
    "coding": [
        "code",
        "bug",
        "feature",
        "api",
        "script",
        "function",
        "class",
        "debug",
        "fix",
        "generate",
        "write",
    ],
    "data": [
        "csv",
        "data",
        "validate",
        "transform",
        "clean",
        "analyze",
        "database",
        "query",
    ],
    "media": [
        "video",
        "audio",
        "transcribe",
        "subtitle",
        "encode",
        "ffmpeg",
    ],
    "writing": [
        "write",
        "blog",
        "article",
        "post",
        "essay",
        "tutorial",
        "documentation",
        "email",
    ],
    "analysis": [
        "analyze",
        "analyze",
        "trend",
        "forecast",
        "trend",
        "report",
        "summary",
        "insight",
    ],
    "image": [
        "image",
        "photo",
        "screenshot",
        "ocr",
        "vision",
        "extract",
    ],
    "security": [
        "security",
        "vulnerability",
        "scan",
        "compliance",
        "audit",
    ],
    "specialized": [
        "legal",
        "financial",
        "medical",
        "health",
        "contract",
    ],
}

# Complexity keywords
SIMPLE_KEYWORDS = ["simple", "quick", "fix", "short", "small", "bug"]
COMPLEX_KEYWORDS = [
    "design",
    "architecture",
    "complex",
    "advanced",
    "enterprise",
    "scale",
    "large",
]


def detect_category(task: str) -> str:
    """Detect task category from description"""
    task_lower = task.lower()

    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in task_lower for keyword in keywords):
            return category

    return "coding"  # Default


def detect_complexity(task: str) -> str:
    """Detect task complexity from description"""
    task_lower = task.lower()

    if any(keyword in task_lower for keyword in COMPLEX_KEYWORDS):
        return "complex"
    elif any(keyword in task_lower for keyword in SIMPLE_KEYWORDS):
        return "simple"
    else:
        return "medium"


def get_recommendation(
    category: str, complexity: str
) -> Tuple[str, float, str]:
    """Get model recommendation for task"""
    if category not in MODEL_RECOMMENDATIONS:
        category = "coding"

    if complexity not in MODEL_RECOMMENDATIONS[category]:
        complexity = "medium"

    return MODEL_RECOMMENDATIONS[category][complexity]


def get_alternatives(
    category: str, complexity: str
) -> List[Tuple[str, float, str]]:
    """Get alternative model recommendations"""
    if category not in MODEL_RECOMMENDATIONS:
        category = "coding"

    rec = MODEL_RECOMMENDATIONS[category]

    alternatives = []
    if complexity == "simple" and "medium" in rec:
        alternatives.append(rec["medium"])
    if complexity == "medium":
        if "simple" in rec:
            alternatives.append(rec["simple"])
        if "complex" in rec:
            alternatives.append(rec["complex"])
    if complexity == "complex" and "medium" in rec:
        alternatives.append(rec["medium"])

    return alternatives


def format_output(
    task: str,
    category: str,
    complexity: str,
    model: str,
    cost: float,
    reason: str,
    show_alternatives: bool = False,
) -> str:
    """Format output for display"""
    output = []
    output.append("\n" + "=" * 60)
    output.append("MODEL SELECTOR")
    output.append("=" * 60 + "\n")

    output.append(f"Task: {task}\n")

    output.append("-" * 60)
    output.append("ANALYSIS")
    output.append("-" * 60)
    output.append(f"Category:    {category}")
    output.append(f"Complexity:  {complexity}")
    output.append("")

    output.append("-" * 60)
    output.append("RECOMMENDATION")
    output.append("-" * 60)
    output.append(f"Model:  {model}")
    output.append(f"Cost:   ${cost:.2f}")
    output.append(f"Reason: {reason}")

    if show_alternatives:
        alternatives = get_alternatives(category, complexity)
        if alternatives:
            output.append("")
            output.append("-" * 60)
            output.append("ALTERNATIVES")
            output.append("-" * 60)
            for alt_model, alt_cost, alt_reason in alternatives:
                output.append(f"• {alt_model} (${alt_cost:.2f})")
                output.append(f"  {alt_reason}\n")

    output.append("-" * 60)
    output.append("NEXT STEPS")
    output.append("-" * 60)
    output.append(f"1. Prepare your task")
    output.append(f"2. Run: ollama run {model}")
    output.append(f"3. Track in: templates/task-log-template.md")
    output.append(f"4. Analyze monthly: templates/monthly-report-comprehensive.md")

    output.append("\n" + "=" * 60 + "\n")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="Automated model selector for Task Cost Analysis Framework"
    )

    parser.add_argument("--task", help="Task description", type=str, required=True)
    parser.add_argument(
        "--category",
        help="Override category detection (coding, data, media, writing, analysis, image, security, specialized)",
        type=str,
    )
    parser.add_argument(
        "--complexity",
        help="Override complexity detection (simple, medium, complex)",
        type=str,
    )
    parser.add_argument(
        "--show-alternatives",
        help="Show alternative model options",
        action="store_true",
    )

    args = parser.parse_args()

    # Detect category and complexity
    category = args.category or detect_category(args.task)
    complexity = args.complexity or detect_complexity(args.task)

    # Get recommendation
    model, cost, reason = get_recommendation(category, complexity)

    # Display output
    output = format_output(
        args.task,
        category,
        complexity,
        model,
        cost,
        reason,
        show_alternatives=args.show_alternatives,
    )

    print(output)

    # Return exit code based on cost
    if cost > 0:
        return 0  # Claude used (more expensive but strategic)
    else:
        return 0  # Ollama used (free, local)


if __name__ == "__main__":
    sys.exit(main())
