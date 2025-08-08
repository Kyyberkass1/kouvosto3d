#!/usr/bin/env python3
"""Update sitemap.xml <lastmod> to current UTC date."""
from datetime import datetime
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

def get_today() -> str:
    """Return current date in YYYY-MM-DD format (UTC)."""
    return datetime.utcnow().date().isoformat()


def update_sitemap(date: str) -> None:
    sitemap = ROOT / "sitemap.xml"
    content = sitemap.read_text(encoding="utf-8")
    updated = re.sub(r"<lastmod>.*?</lastmod>", f"<lastmod>{date}</lastmod>", content)
    sitemap.write_text(updated, encoding="utf-8")


def main() -> None:
    date = get_today()
    update_sitemap(date)

if __name__ == "__main__":
    main()
