"""
Check that every relative link, image and anchor in README.md resolves inside this repository.

Standard library only and no network access, so the check is fast and does not fail because
an external site is slow. External URLs are not checked.

    python tools/check_readme.py            # exit code 1 if anything is missing
"""

import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent


def slug(heading: str) -> str:
    """GitHub's anchor for a heading: lower case, letters, digits, spaces and hyphens; spaces become hyphens."""
    text = re.sub(r"<[^>]+>", "", heading)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[`*_]", "", text).strip().lower()
    return "".join("-" if ch == " " else ch for ch in text
                   if ch in " -" or unicodedata.category(ch)[0] in "LN")


def anchors(markdown: str) -> set:
    found, seen, in_code = set(), {}, False
    for line in markdown.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m and not in_code:
            s = slug(m.group(2))
            n = seen.get(s, 0)
            found.add(s if n == 0 else f"{s}-{n}")
            seen[s] = n + 1
    return found


def targets(markdown: str) -> list:
    text = re.sub(r"```.*?```", "", markdown, flags=re.S)
    found = re.findall(r"!?\[[^\]]*\]\(([^)\s]+)\)", text)
    found += re.findall(r'(?:src|href)="([^"]+)"', text)
    found += [s.split()[0] for s in re.findall(r'srcset="([^"]+)"', text)]
    return found


def check(readme: Path) -> list:
    text = readme.read_text(encoding="utf-8")
    own = anchors(text)
    problems = []
    for target in targets(text):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        path, _, fragment = target.partition("#")
        if not path:
            if fragment and fragment not in own:
                problems.append(f"missing anchor: #{fragment}")
            continue
        resolved = (readme.parent / unquote(path)).resolve()
        if not resolved.is_relative_to(ROOT):
            problems.append(f"points outside the repository: {target}")
        elif not resolved.exists():
            problems.append(f"missing file: {target}")
    return problems


def main() -> int:
    readme = ROOT / "README.md"
    problems = check(readme)
    count = len([t for t in targets(readme.read_text(encoding="utf-8"))
                 if not t.startswith(("http://", "https://", "mailto:"))])
    for p in problems:
        print(f"README.md: {p}")
    print(f"checked {count} relative links and images: {'OK' if not problems else f'{len(problems)} problem(s)'}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
