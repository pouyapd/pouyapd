"""
Record the GroundedAI card animation from the live demo (real interface, real answer).

    python pouyapd/tools/record_groundedai_demo.py [--url https://pouyapd.github.io/GroundedAI/]

Drives https://pouyapd.github.io/GroundedAI/ in Chromium (dark theme, 960 px wide) the way a
visitor would:

1. the start panel: the extractive generator (the default; the optional in-browser model is the
   base Qwen2.5-1.5B-Instruct) and the optional meaning check;
2. the meaning check (an NLI model) is switched on and downloads into the tab;
3. a sample PDF, the Harbourline Ferries Passenger Guide, is chosen and a question is typed;
4. the answer appears with its source label, the quoted sentence and its page, the lexical claim
   check and the meaning check;
5. the "Checks that ran on this answer" table is opened.

Every frame is a screenshot of the page; nothing is drawn in afterwards. The recording stops with
an error, and writes nothing, unless the answer quotes page 2 and the checks table lists the
meaning check and the added-detail rule.

Writes assets/v2/source/groundedai-demo.gif (the first frame repeats the answer, so the image
tells the story before it plays) and assets/v2/source/groundedai-demo.png (the answer frame).
tools/make_profile_v2_assets.py frames them as cards/groundedai.gif and cards/groundedai.png.
Needs ``playwright`` with Chromium and Pillow.
"""

from __future__ import annotations

import argparse
import io
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "v2" / "source"
URL = "https://pouyapd.github.io/GroundedAI/"
DOCUMENT = "Harbourline Ferries Passenger Guide"
QUESTION_PARTS = ("How much does ", "a single adult ", "ticket to Mirrow ", "cost?")
WIDTH, HEIGHT = 960, 860
HEADER = 112  # the site's sticky header covers the top of the viewport


def record(url: str) -> tuple[list[Image.Image], list[int]]:
    from playwright.sync_api import sync_playwright

    shots: list[tuple[bytes, int]] = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": WIDTH, "height": HEIGHT}, color_scheme="dark")
        page.goto(url)
        page.wait_for_selector("button.chip-example", timeout=240_000)

        def show(selector: str, margin: int = HEADER) -> None:
            """Scroll so that the first element matching ``selector`` starts near the top."""
            page.locator(selector).first.evaluate(
                "(el, m) => window.scrollTo(0, el.getBoundingClientRect().top + window.scrollY - m)",
                margin,
            )
            page.wait_for_timeout(150)

        def shot(ms: int) -> None:
            shots.append((page.screenshot(), ms))

        # 1-2: the start panel, then the meaning check switched on while it downloads
        show("#demo-title", margin=HEADER + 50)
        shot(1700)
        page.locator("label.option-card", has_text="Meaning check").locator("input").check()
        page.wait_for_selector(".nli-progress", timeout=30_000)
        page.wait_for_timeout(700)
        shot(900)
        page.wait_for_selector(".nli-progress", state="detached", timeout=600_000)
        if not page.locator("label.option-card", has_text="Meaning check").locator("input").is_checked():
            raise SystemExit("the meaning check did not load; nothing was written")
        shot(900)

        # 3: a sample PDF and the question
        show("form.card")
        page.select_option("#scope", label=DOCUMENT)
        shot(900)
        typed = ""
        for part in QUESTION_PARTS:
            typed += part
            page.fill("#question", typed)
            shot(230)
        page.click("button[type=submit]:has-text('Ask question')")

        # 4: the answer with quote, page, claim check and meaning check
        page.wait_for_selector(".evidence", timeout=120_000)
        page.wait_for_selector("text=Meaning check (NLI)", timeout=300_000)
        page.wait_for_timeout(600)
        if "p. 2" not in page.locator(".evidence").first.inner_text():
            raise SystemExit("the quote does not name page 2; nothing was written")
        show("section[aria-labelledby=answer-heading]")
        shot(4200)

        # 5: the table of checks that ran
        summary = page.locator("summary", has_text="Checks that ran on this answer").first
        summary.click()
        page.wait_for_timeout(400)
        table = summary.locator("xpath=..").inner_text()
        for needed in ("Meaning", "Added detail"):
            if needed.lower() not in table.lower():
                raise SystemExit(f"the checks table does not list {needed!r}; nothing was written")
        show("section[aria-labelledby=answer-heading]")
        shot(5200)
        browser.close()
    frames = [Image.open(io.BytesIO(png)).convert("RGB") for png, _ in shots]
    return frames, [ms for _, ms in shots]


def save(frames: list[Image.Image], durations: list[int]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    poster = frames[-2]  # the answer with its quote, page, claim check and meaning check
    poster.save(OUT / "groundedai-demo.png", optimize=True)
    sequence = [poster, *frames]  # the first frame shows the result
    timing = [2400, *durations]
    palette = frames[-1].quantize(colors=128, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    indexed = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in sequence]
    indexed[0].save(
        OUT / "groundedai-demo.gif",
        save_all=True,
        append_images=indexed[1:],
        duration=timing,
        loop=0,
        optimize=True,
        disposal=1,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().split("\n\n")[0])
    parser.add_argument("--url", default=URL)
    args = parser.parse_args()
    frames, durations = record(args.url)
    save(frames, durations)
    for name in ("groundedai-demo.gif", "groundedai-demo.png"):
        path = OUT / name
        print(f"{path.relative_to(ROOT).as_posix()}: {Image.open(path).size}, {path.stat().st_size / 1024:.0f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
