#!/usr/bin/env python3
"""
Cost Calculator for AI-Assisted Task Cost Analysis Framework

Calculates estimated cost for any task based on:
- Task category (coding, data, media, etc.)
- Model selection (Ollama local vs Claude API)
- Estimated tokens
- Task complexity

Usage:
    python cost-calculator.py --task "Build a React component" --category coding
    python cost-calculator.py --tokens 1500 --model claude-sonnet
"""

import argparse
import json
from enum import Enum
from typing import Dict, Tuple

# Model pricing (per 1M tokens)
MODEL_PRICING = {
    "qwen-1.5b": 0,
    "qwen-7b": 0,
    "mistral": 0,
    "gemma4": 0,
    "llava": 0,
    "deepseek-r1": 0,
    "claude-sonnet": {"input": 3, "output": 15},
}

# Estimated tokens per task category
TASK_TOKENS = {
    "bug-fix": (50, 200),  # (min, max)
    "feature": (200, 1000),
    "api-endpoint": (300, 800),
    "data-pipeline": (400, 2000),
    "dashboard": (500, 1500),
    "blog-post": (300, 1500),
    "tutorial": (500, 2500),
    "analysis": (200, 1000),
    "security-review": (800, 3000),
    "contract-review": (2000, 5000),
}

# Model recommendations by category
MODEL_RECOMMENDATIONS = {
    "coding": {
        "simple": "qwen-1.5b",
        "medium": "qwen-7b",
        "complex": "qwen-7b or Claude",
    },
    "media": {
        "transcription": "whisper.cpp",
        "image": "llava",
        "editing": "ffmpeg + qwen",
    },
    "data": {
        "validation": "qwen-1.5b",
        "transformation": "qwen-7b",
        "analysis": "gemma4",
    },
    "writing": {
        "simple": "gemma4",
        "complex": "mistral",
    },
    "security": {
        "code-scan": "skill-scanner ($0)",
        "compliance": "Claude ($0.15-0.40)",
    },
}


class TaskComplexity(Enum):
    SIMPLE = 1
    MEDIUM = 2
    COMPLEX = 3


def estimate_tokens(task_type: str, complexity: TaskComplexity) -> int:
    """Estimate tokens for a task"""
    if task_type not in TASK_TOKENS:
        return 500  # Default estimate

    min_tokens, max_tokens = TASK_TOKENS[task_type]
    if complexity == TaskComplexity.SIMPLE:
        return int(min_tokens + (max_tokens - min_tokens) * 0.25)
    elif complexity == TaskComplexity.MEDIUM:
        return int(min_tokens + (max_tokens - min_tokens) * 0.5)
    else:  # COMPLEX
        return int(min_tokens + (max_tokens - min_tokens) * 0.75)


def calculate_cost(model: str, tokens: int, output_tokens: int = None) -> float:
    """Calculate cost for a given model and token count"""
    if model in ["qwen-1.5b", "qwen-7b", "mistral", "gemma4", "llava", "deepseek-r1"]:
        return 0.0  # All local Ollama models are free

    if model == "claude-sonnet":
        if output_tokens is None:
            output_tokens = tokens  # Estimate output ~= input
        input_cost = (tokens / 1_000_000) * MODEL_PRICING["claude-sonnet"]["input"]
        output_cost = (output_tokens / 1_000_000) * MODEL_PRICING["claude-sonnet"]["output"]
        return input_cost + output_cost

    return 0.0


def estimate_time(model: str, tokens: int) -> float:
    """Estimate execution time (in minutes)"""
    # Tokens/sec for each model (approximate)
    throughput = {
        "qwen-1.5b": 150,
        "qwen-7b": 50,
        "mistral": 55,
        "gemma4": 45,
        "llava": 15,
        "deepseek-r1": 160,
        "claude-sonnet": 300,  # Via API, much faster
    }

    if model not in throughput:
        return 0.0

    seconds = tokens / throughput[model]
    return seconds / 60  # Convert to minutes


def recommend_model(
    category: str, complexity: TaskComplexity
) -> Tuple[str, str]:
    """Recommend model for a task"""
    if category not in MODEL_RECOMMENDATIONS:
        return "claude-sonnet", "Unknown category"

    complexity_map = {
        TaskComplexity.SIMPLE: "simple",
        TaskComplexity.MEDIUM: "medium",
        TaskComplexity.COMPLEX: "complex",
    }

    complexity_str = complexity_map.get(complexity, "medium")
    rec = MODEL_RECOMMENDATIONS[category].get(complexity_str, "claude-sonnet")
    return rec, f"{category} ({complexity_str})"


def calculate_monthly_projection(weekly_cost: float) -> Dict[str, float]:
    """Project monthly costs from weekly average"""
    monthly = weekly_cost * 4
    quarterly = monthly * 3
    annual = monthly * 12

    return {
        "weekly": weekly_cost,
        "monthly": monthly,
        "quarterly": quarterly,
        "annual": annual,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Calculate AI task costs using the Task Cost Analysis Framework"
    )

    parser.add_argument(
        "--task",
        help="Task description (e.g., 'Build a React component')",
        type=str,
    )
    parser.add_argument(
        "--category",
        help="Task category (coding, data, media, writing, security, etc.)",
        type=str,
    )
    parser.add_argument(
        "--complexity",
        help="Task complexity (simple, medium, complex)",
        type=str,
        default="medium",
    )
    parser.add_argument(
        "--model",
        help="Model to use (qwen-1.5b, qwen-7b, mistral, gemma4, llava, claude-sonnet)",
        type=str,
    )
    parser.add_argument("--tokens", help="Estimated tokens for the task", type=int)
    parser.add_argument(
        "--output-tokens",
        help="Estimated output tokens (for Claude)",
        type=int,
    )
    parser.add_argument(
        "--weekly-tasks",
        help="Calculate projection from N tasks per week",
        type=int,
    )

    args = parser.parse_args()

    # Parse complexity
    complexity_map = {
        "simple": TaskComplexity.SIMPLE,
        "medium": TaskComplexity.MEDIUM,
        "complex": TaskComplexity.COMPLEX,
    }
    complexity = complexity_map.get(args.complexity, TaskComplexity.MEDIUM)

    print("\n" + "=" * 60)
    print("TASK COST ANALYSIS CALCULATOR")
    print("=" * 60 + "\n")

    # Handle task description
    if args.task:
        print(f"Task: {args.task}")
        if args.category:
            print(f"Category: {args.category}")
        else:
            args.category = "coding"
            print(f"Category: {args.category} (assumed)")

    # Get tokens estimate
    if args.tokens:
        tokens = args.tokens
    elif args.task or args.category:
        tokens = estimate_tokens(args.category, complexity)
        print(f"Estimated tokens: {tokens:,}")
    else:
        tokens = 0

    # Recommend model if not specified
    if not args.model:
        recommended, reason = recommend_model(args.category, complexity)
        args.model = recommended.split()[0]  # Get first word of recommendation
        print(f"Recommended model: {args.model} ({reason})")
    else:
        print(f"Model selected: {args.model}")

    # Calculate costs
    cost = calculate_cost(args.model, tokens, args.output_tokens)
    time_min = estimate_time(args.model, tokens)

    print("\n" + "-" * 60)
    print("COST ESTIMATE")
    print("-" * 60)
    print(f"Model: {args.model}")
    print(f"Input tokens: {tokens:,}")
    if args.output_tokens:
        print(f"Output tokens: {args.output_tokens:,}")
    print(f"Estimated time: {time_min:.1f} minutes")
    print(f"Cost: ${cost:.4f}")

    # Compare with alternatives
    if args.model != "qwen-1.5b":
        alt_cost = calculate_cost("qwen-1.5b", tokens)
        alt_time = estimate_time("qwen-1.5b", tokens)
        print(f"\nLocal alternative (qwen-1.5b):")
        print(f"  Time: {alt_time:.1f} minutes")
        print(f"  Cost: ${alt_cost:.4f} (savings: ${cost - alt_cost:.4f})")

    if args.model != "claude-sonnet":
        claude_cost = calculate_cost("claude-sonnet", tokens)
        claude_time = estimate_time("claude-sonnet", tokens)
        print(f"\nClaude alternative:")
        print(f"  Time: {claude_time:.1f} minutes")
        print(f"  Cost: ${claude_cost:.4f} (difference: ${abs(cost - claude_cost):.4f})")

    # Monthly projection if tasks specified
    if args.weekly_tasks:
        print("\n" + "-" * 60)
        print("MONTHLY PROJECTION")
        print("-" * 60)
        weekly_cost = cost * args.weekly_tasks
        projection = calculate_monthly_projection(weekly_cost)

        print(f"Tasks per week: {args.weekly_tasks}")
        print(f"Cost per task: ${cost:.4f}")
        print(f"Weekly cost: ${weekly_cost:.2f}")
        print(f"Monthly cost: ${projection['monthly']:.2f}")
        print(f"Quarterly cost: ${projection['quarterly']:.2f}")
        print(f"Annual cost: ${projection['annual']:.2f}")

        budget_monthly = 120
        if projection["monthly"] > budget_monthly:
            print(f"\n⚠️  WARNING: Monthly cost exceeds $120 budget by ${projection['monthly'] - budget_monthly:.2f}")
        else:
            print(f"\n✓ Within budget: ${budget_monthly - projection['monthly']:.2f} remaining")

    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
