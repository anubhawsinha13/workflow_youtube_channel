#!/usr/bin/env python3
"""Write a shared research brief into the YouTube project folder.

The review script still reads facts, sources, and review_status from this file.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path


def project_name_for(topic: str, project_name: str | None) -> str:
    if project_name:
        return project_name
    cleaned = topic.lower().replace(" ", "_").replace("'", "").replace(",", "")[:50]
    return "".join(character for character in cleaned if character.isalnum() or character in "_-") or "topic"


def save_brief(topic: str, num_facts: int, project_name: str | None) -> dict:
    try:
        from aegis_research import research_brief
    except ImportError:
        return {
            "ok": False,
            "error": "aegis-research is not installed. From this repo run: pip install -e ../aegis-research",
        }
    brief = research_brief(topic, profile="youtube")
    if not brief.get("ok"):
        return {"ok": False, "error": brief.get("error") or "Research did not return a primary source.", "brief": brief}
    claims = brief.get("claims") or []
    facts = [str(claim.get("text") or "").strip() for claim in claims if str(claim.get("text") or "").strip()]
    if num_facts:
        facts = facts[:num_facts]
    sources = []
    for claim in claims:
        url = str(claim.get("source_url") or "").strip()
        if url and url not in sources:
            sources.append(url)
    name = project_name_for(topic, project_name)
    folder = Path("projects") / name / "research"
    folder.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = folder / f"research_{stamp}.json"
    payload = {
        "project_name": name,
        "topic": brief.get("topic") or topic,
        "generated_at": datetime.now().isoformat(),
        "status": "generated",
        "review_status": "pending",
        "facts": facts,
        "sources": sources,
        "raw_response": brief.get("summary") or "",
        "brief": brief,
    }
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return {"ok": True, "research_file": str(path), "facts": facts, "sources": sources}


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args:
        print("Usage: python scripts/research_brief.py <topic> [num_facts] [project_name]")
        return 1
    topic = args[0]
    num_facts = int(args[1]) if len(args) > 1 else 8
    project_name = args[2] if len(args) > 2 else None
    result = save_brief(topic, num_facts, project_name)
    if not result.get("ok"):
        print(result.get("error") or "Research failed.")
        return 1
    print(f"Research saved: {result['research_file']}")
    print(f"Next: python execution/review_research.py {result['research_file']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
