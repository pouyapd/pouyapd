"""
Assets of the animated profile design (assets/v2/):

    banner.svg            animated banner: CSS-only motion (GitHub allows inline CSS in SVG images,
                          no scripts); a map of the real projects with light moving along the links,
                          over a slowly drifting particle network. Without motion it is a complete
                          static image.
    banner-static.svg     the same drawing without motion. Browsers do not pass the reduced-motion
                          preference into an SVG shown as an image, so the README selects this file
                          with <picture><source media="(prefers-reduced-motion: reduce)">.
    cards/*.png           project previews: genuine figures and a screenshot from the project
                          repositories, framed in the profile's style, each with its source.
    cards/safenav-rl.gif  replay of stored SafeNav-RL benchmark trajectories (first expert test
                          scenario, four controllers), drawn from results/benchmark/trajectories.npz.
    cards/groundedai.gif  the GroundedAI live demo recorded in a browser (GroundedAI's
                          scripts/record_demo_preview.py: real screenshots of a real answer), framed
                          like the other cards; cards/groundedai.png is its final frame, for reduced
                          motion.

Only files in pouyapd/assets/v2/ are written; the project repositories are read, never changed.
Run from the folder that contains the repositories:

    python pouyapd/tools/make_profile_v2_assets.py
"""

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "pouyapd" / "assets" / "v2"
FONT = Path("C:/Windows/Fonts/segoeui.ttf")
FONT_SB = Path("C:/Windows/Fonts/seguisb.ttf")

NAVY, NAVY_2, LINE = "#0a1330", "#0e1b3d", "#1d3461"
CYAN, BLUE, INK, INK_2, MUTED = "#5ee7ff", "#5b8cff", "#eef5ff", "#a9bcd8", "#6f86ab"


# ── animated banner ─────────────────────────────────────────────────────────

W, H = 1200, 400
HUB = (950, 198)
PROJECTS = {  # name: (x, y, label anchor, label dx, label dy)
    "SafeTraj-Experiments": (812, 112, "middle", 0, -20),
    "trajectory-failure-analysis": (1072, 98, "middle", 0, -20),
    "SafeTraj-Prototype": (1118, 262, "end", 4, 30),
    "SafeNav-RL": (958, 334, "middle", 0, 34),
    "TrustRAG": (790, 290, "middle", 0, 32),
    "GroundedAI": (742, 204, "middle", 0, -20),
}
# links stated in the projects' READMEs ("the same approach", "the workflow as a toolkit")
RELATED = [("SafeTraj-Experiments", "trajectory-failure-analysis"),
           ("SafeTraj-Experiments", "SafeTraj-Prototype"),
           ("trajectory-failure-analysis", "SafeTraj-Prototype")]


def _f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def banner_svg(animated: bool = True) -> str:
    rng = np.random.default_rng(7)
    css = """
      .t{font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,'Helvetica Neue',Arial,sans-serif}
      .d1{animation:d1 46s ease-in-out infinite alternate}
      .d2{animation:d2 34s ease-in-out infinite alternate}
      .d3{animation:d3 25s ease-in-out infinite alternate}
      @keyframes d1{to{transform:translate(-14px,6px)}}
      @keyframes d2{to{transform:translate(-22px,-8px)}}
      @keyframes d3{to{transform:translate(-30px,10px)}}
      .tw{animation:tw 5s ease-in-out infinite alternate}
      @keyframes tw{from{opacity:.12}to{opacity:.75}}
      .pulse{stroke-dasharray:6 194;animation:flow 7s linear infinite}
      @keyframes flow{from{stroke-dashoffset:200}to{stroke-dashoffset:0}}
      .halo{animation:glow 4.5s ease-in-out infinite alternate}
      @keyframes glow{from{opacity:.22}to{opacity:.7}}
      @media (prefers-reduced-motion:reduce){*{animation:none!important}}
    """
    if not animated:                     # same drawing, no motion (the README serves it under reduced motion)
        css = ".t{font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,'Helvetica Neue',Arial,sans-serif}"
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
             f'role="img" aria-labelledby="title desc">',
             '<title id="title">Pouya Bathaei Pourmand: trustworthy AI, ML evaluation, failure analysis</title>',
             '<desc id="desc">Banner with a map of the six projects on this profile, linked to a central '
             'trustworthy-AI node, over a slowly drifting particle network.</desc>',
             f"<style>{' '.join(l.strip() for l in css.strip().splitlines())}</style>",
             "<defs>",
             f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#050a19"/>'
             f'<stop offset=".55" stop-color="{NAVY}"/><stop offset="1" stop-color="{NAVY_2}"/></linearGradient>',
             f'<radialGradient id="glowR" cx="{HUB[0] / W:.3f}" cy="{HUB[1] / H:.3f}" r=".55">'
             f'<stop offset="0" stop-color="{CYAN}" stop-opacity=".20"/>'
             f'<stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>',
             f'<radialGradient id="glowL" cx=".12" cy="1" r=".6"><stop offset="0" stop-color="{BLUE}" '
             f'stop-opacity=".16"/><stop offset="1" stop-color="{BLUE}" stop-opacity="0"/></radialGradient>',
             f'<radialGradient id="halo"><stop offset="0" stop-color="{CYAN}" stop-opacity=".9"/>'
             f'<stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>',
             '<filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.2" '
             'result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
             f'<clipPath id="card"><rect width="{W}" height="{H}" rx="18"/></clipPath>',
             "</defs>",
             '<g clip-path="url(#card)">',
             f'<rect width="{W}" height="{H}" fill="url(#bg)"/>',
             f'<rect width="{W}" height="{H}" fill="url(#glowR)"/>',
             f'<rect width="{W}" height="{H}" fill="url(#glowL)"/>']

    # particle field in three depth layers (fewer particles behind the text)
    for cls, n, r, op in (("d1", 70, 0.9, 0.30), ("d2", 46, 1.3, 0.45), ("d3", 22, 1.9, 0.6)):
        pts = []
        while len(pts) < n:
            x, y = rng.uniform(-30, W + 30), rng.uniform(-20, H + 20)
            if x < 660 and rng.random() > 0.35:
                continue
            pts.append((x, y))
        g = [f'<g class="{cls}">']
        if cls in ("d2", "d3"):
            for i in range(len(pts)):
                for j in range(i + 1, len(pts)):
                    dist = np.hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1])
                    if dist < 110:
                        g.append(f'<line x1="{_f(pts[i][0])}" y1="{_f(pts[i][1])}" x2="{_f(pts[j][0])}" '
                                 f'y2="{_f(pts[j][1])}" stroke="{BLUE}" stroke-opacity="{0.16 * (1 - dist / 110):.3f}" '
                                 f'stroke-width=".7"/>')
        for k, (x, y) in enumerate(pts):
            twinkle = rng.random() < 0.25
            extra = f' class="tw" style="animation-delay:-{rng.uniform(0, 5):.1f}s"' if twinkle else ""
            g.append(f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{r}" fill="#cfe9ff" fill-opacity="{op}"{extra}/>')
        g.append("</g>")
        parts += g

    # project map: satellites, links, pulses, nodes, labels
    hx, hy = HUB
    m = ['<g>']
    for name, (x, y, *_rest) in PROJECTS.items():
        for k in range(4):
            a = rng.uniform(0, 2 * np.pi)
            rr = rng.uniform(26, 44)
            sx, sy = x + rr * np.cos(a), y + rr * np.sin(a)
            m.append(f'<line x1="{_f(x)}" y1="{_f(y)}" x2="{_f(sx)}" y2="{_f(sy)}" stroke="{CYAN}" '
                     f'stroke-opacity=".18" stroke-width=".8"/>')
            m.append(f'<circle cx="{_f(sx)}" cy="{_f(sy)}" r="2" fill="#7fb8ff" fill-opacity=".7"/>')
    for a_name, b_name in RELATED:
        ax_, ay_ = PROJECTS[a_name][:2]
        bx_, by_ = PROJECTS[b_name][:2]
        m.append(f'<line x1="{ax_}" y1="{ay_}" x2="{bx_}" y2="{by_}" stroke="{CYAN}" stroke-opacity=".22" '
                 f'stroke-width="1" stroke-dasharray="3 5"/>')
    for k, (name, (x, y, *_rest)) in enumerate(PROJECTS.items()):
        m.append(f'<line x1="{hx}" y1="{hy}" x2="{x}" y2="{y}" stroke="{CYAN}" stroke-opacity=".32" stroke-width="1.2"/>')
        m.append(f'<path class="pulse" d="M{hx} {hy}L{x} {y}" pathLength="100" stroke="#a8f6ff" stroke-width="2.4" '
                 f'stroke-linecap="round" fill="none" filter="url(#soft)" style="animation-delay:-{k * 1.4:.1f}s"/>')
    m.append(f'<circle class="halo" cx="{hx}" cy="{hy}" r="26" fill="url(#halo)"/>')
    m.append(f'<circle cx="{hx}" cy="{hy}" r="7" fill="#b9f8ff" filter="url(#soft)"/>')
    m.append(f'<text class="t" x="{hx}" y="{hy + 30}" text-anchor="middle" font-size="12.5" fill="{CYAN}" '
             f'letter-spacing="1.2">trustworthy AI</text>')
    for k, (name, (x, y, anchor, dx, dy)) in enumerate(PROJECTS.items()):
        m.append(f'<circle class="halo" cx="{x}" cy="{y}" r="16" fill="url(#halo)" style="animation-delay:-{k * 0.9:.1f}s"/>')
        m.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{INK}" stroke="{CYAN}" stroke-width="1.5"/>')
        m.append(f'<text class="t" x="{x + dx}" y="{y + dy}" text-anchor="{anchor}" font-size="13.5" fill="#d6e6fb">'
                 f'{name}</text>')
    m.append("</g>")
    parts += m

    # text block
    parts += [
        f'<text class="t" x="70" y="118" font-size="13" font-weight="600" fill="{CYAN}" letter-spacing="2.6">'
        f'TRUSTWORTHY AI · ML EVALUATION · FAILURE ANALYSIS</text>',
        f'<rect x="70" y="134" width="54" height="2" rx="1" fill="{CYAN}" fill-opacity=".8"/>',
        f'<text class="t" x="68" y="190" font-size="44" font-weight="700" fill="{INK}">Pouya Bathaei Pourmand</text>',
        f'<text class="t" x="70" y="240" font-size="19.5" fill="{INK_2}">Finding where learned systems fail, and explaining why,</text>',
        f'<text class="t" x="70" y="270" font-size="19.5" fill="{INK_2}">with tested, reproducible research code.</text>',
        f'<text class="t" x="70" y="330" font-size="14" fill="{MUTED}">MSc Computer Engineering · University of Genoa</text>',
        f'<text class="t" x="{W - 24}" y="{H - 16}" text-anchor="end" font-size="11" fill="{MUTED}" fill-opacity=".9">'
        f'map of the projects below</text>',
        "</g>",
        f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="{CYAN}" stroke-opacity=".18"/>',
        "</svg>",
    ]
    return "\n".join(parts) + "\n"


# ── framed project previews ─────────────────────────────────────────────────

def _font(size, semibold=False):
    from PIL import ImageFont
    return ImageFont.truetype(str(FONT_SB if semibold else FONT), size)


def framed(src: Path, out: Path, source: str, width: int = 1000) -> None:
    from PIL import Image, ImageDraw
    pad, radius = 22, 22
    fig = Image.open(src).convert("RGB")
    inner = width - 2 * pad
    fig = fig.resize((inner, round(fig.height * inner / fig.width)), Image.LANCZOS)
    height = pad + fig.height + 58
    card = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle((0, 0, width - 1, height - 1), radius=radius, fill=NAVY, outline=LINE, width=2)
    for x in range(radius, width - radius):            # accent line, cyan to blue
        t = (x - radius) / (width - 2 * radius)
        c = tuple(int(int(CYAN[i:i + 2], 16) * (1 - t) + int(BLUE[i:i + 2], 16) * t) for i in (1, 3, 5))
        d.line([(x, 1), (x, 3)], fill=c + (220,))
    mask = Image.new("L", fig.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, fig.width - 1, fig.height - 1), radius=12, fill=255)
    card.paste(fig, (pad, pad), mask)
    d.text((pad + 2, pad + fig.height + 18), source, font=_font(21), fill="#8ea6c8")
    card.quantize(colors=256, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(out, optimize=True)


def framed_gif(src: Path, out: Path, source: str, width: int = 1000) -> None:
    """Frame every frame of an animated GIF like ``framed`` (transparent corners); keep its timing."""
    from PIL import Image, ImageDraw, ImageSequence
    pad, radius = 22, 22
    raw = [(f.convert("RGB"), f.info.get("duration", 100)) for f in ImageSequence.Iterator(Image.open(src))]
    inner = width - 2 * pad
    cards, durations = [], []
    for fig, ms in raw:
        fig = fig.resize((inner, round(fig.height * inner / fig.width)), Image.LANCZOS)
        height = pad + fig.height + 58
        card = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        d = ImageDraw.Draw(card)
        d.rounded_rectangle((0, 0, width - 1, height - 1), radius=radius, fill=NAVY, outline=LINE, width=2)
        for x in range(radius, width - radius):            # accent line, cyan to blue
            t = (x - radius) / (width - 2 * radius)
            c = tuple(int(int(CYAN[i:i + 2], 16) * (1 - t) + int(BLUE[i:i + 2], 16) * t) for i in (1, 3, 5))
            d.line([(x, 1), (x, 3)], fill=c + (255,))
        mask = Image.new("L", fig.size, 0)
        ImageDraw.Draw(mask).rounded_rectangle((0, 0, fig.width - 1, fig.height - 1), radius=12, fill=255)
        card.paste(fig, (pad, pad), mask)
        d.text((pad + 2, pad + fig.height + 18), source, font=_font(21), fill="#8ea6c8")
        cards.append(card)
        durations.append(ms)
    # one shared palette of 255 colours; index 255 is transparent (the corners outside the frame)
    palette = cards[-1].convert("RGB").quantize(colors=255, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    frames = []
    for card in cards:
        frame = card.convert("RGB").quantize(palette=palette, dither=Image.Dither.NONE)
        transparent = card.getchannel("A").point(lambda a: 255 if a < 128 else 0)
        frame.paste(255, mask=transparent)
        frames.append(frame)
    frames[0].save(out, save_all=True, append_images=frames[1:], duration=durations, loop=0, optimize=True,
                   disposal=1, transparency=255)


# ── SafeNav-RL replay (animated GIF) ────────────────────────────────────────

def safenav_replay(out: Path, step: int = 5) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle
    from PIL import Image

    sys.path.insert(0, str(ROOT / "SafeNav-RL"))
    from safenav.evaluation.benchmark import load_trajectories
    trajs = load_trajectories(ROOT / "SafeNav-RL" / "results" / "benchmark" / "trajectories.npz")
    seed = sorted({int(t["episode_seed"]) for t in trajs if t["stage"] == "expert"})[0]
    pick = {(t["method"], bool(t["safety_filter"])): t for t in trajs
            if t["stage"] == "expert" and int(t["episode_seed"]) == seed and t["train_seed"] in (0, "0", None, "None")}
    panels = [("PPO (filter in training)", True, "PPO trained with filter · filter on", CYAN),
              ("PPO (no filter in training)", False, "PPO trained without filter · filter off", "#8ab4ff"),
              ("PotentialField", True, "Potential field · filter on", "#c4b5fd"),
              ("GoToGoal", False, "Go-to-goal · filter off", "#fbbf24")]
    outcome_text = {"success": "reached goal", "collision": "collision", "timeout": "timeout"}
    end_color = {"success": "#34d399", "collision": "#f87171", "timeout": "#fbbf24"}

    plt.rcParams.update({"font.family": ["Segoe UI", "DejaVu Sans"], "font.size": 9})
    fig, axes = plt.subplots(2, 2, figsize=(7.2, 7.75), dpi=100)
    fig.patch.set_facecolor(NAVY)
    fig.subplots_adjust(left=0.03, right=0.97, top=0.88, bottom=0.07, wspace=0.06, hspace=0.16)
    fig.text(0.03, 0.955, "Same expert test scenario, four controllers", color=INK, fontsize=12.5, weight="semibold")
    fig.text(0.03, 0.925, "Replay of stored SafeNav-RL benchmark trajectories (simulation; dt = 0.1 s)",
             color=INK_2, fontsize=9)
    clock = fig.text(0.97, 0.955, "", color=MUTED, fontsize=9.5, ha="right")
    fig.text(0.03, 0.025, f"results/benchmark/trajectories.npz · expert test scenario {seed} (the first, unselected) "
                          f"· PPO training seed 0", color=MUTED, fontsize=7.6)
    dyn = []
    longest = 0
    for ax, (method, filt, title, color) in zip(axes.flat, panels):
        t = pick[(method, filt)]
        xy = np.asarray(t["trajectory"])
        longest = max(longest, len(xy) - 1)
        ax.set_facecolor("#08102a")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_color(LINE)
        ax.set_title(title, color=INK, fontsize=9.5, loc="left", pad=5)
        for x, y, r in t["obstacles"]:
            ax.add_patch(Circle((x, y), r, facecolor="#22314f", edgecolor="#3a5079", lw=0.8))
            if filt:
                ax.add_patch(Circle((x, y), r + 0.3 + 0.3, fill=False, edgecolor=CYAN, alpha=0.45, lw=0.7,
                                    ls=(0, (2, 2))))
        gx, gy = t["goal"]
        ax.add_patch(Circle((gx, gy), 0.5, facecolor="#34d39922", edgecolor="#34d399", lw=1.0))
        ax.plot(gx, gy, marker="*", ms=11, color="#34d399")
        ax.plot(*xy[0], marker="o", ms=5, color=INK)
        line, = ax.plot([], [], color=color, lw=2.0, solid_capstyle="round")
        robot = Circle(xy[0], 0.3, facecolor=color, edgecolor=INK, lw=0.8, alpha=0.95)
        ax.add_patch(robot)
        status = ax.text(0.03, 0.96, "", transform=ax.transAxes, color=INK_2, fontsize=8.5, va="top")
        end_mark, = ax.plot([], [], marker={"success": "*", "collision": "X", "timeout": "s"}[t["outcome"]],
                            ms=10, color=end_color[t["outcome"]], ls="")
        dyn.append((xy, t["outcome"], line, robot, status, end_mark))

    frames, durations = [], []
    stops = list(range(0, longest + 1, step))
    if stops[-1] != longest:
        stops.append(longest)
    for i in stops:
        for xy, outcome, line, robot, status, end_mark in dyn:
            n = min(i, len(xy) - 1)
            line.set_data(xy[:n + 1, 0], xy[:n + 1, 1])
            robot.center = tuple(xy[n])
            if i >= len(xy) - 1:
                status.set_text(f"{outcome_text[outcome]} · {len(xy) - 1} steps")
                status.set_color(end_color[outcome])
                end_mark.set_data([xy[-1, 0]], [xy[-1, 1]])
            else:
                status.set_text(f"step {n}")
                status.set_color(INK_2)
        clock.set_text(f"t = {i / 10:.1f} s")
        fig.canvas.draw()
        frames.append(Image.frombuffer("RGBA", fig.canvas.get_width_height(), fig.canvas.buffer_rgba()).convert("RGB"))
        durations.append(70)
    durations[-1] = 3000                                  # hold the final state
    plt.close(fig)
    palette_src = frames[-1].quantize(colors=96, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    pal = [f.quantize(palette=palette_src, dither=Image.Dither.NONE) for f in frames]
    pal[0].save(out, save_all=True, append_images=pal[1:], duration=durations, loop=0, optimize=True, disposal=1)


def main() -> int:
    (OUT / "cards").mkdir(parents=True, exist_ok=True)
    (OUT / "banner.svg").write_text(banner_svg(), encoding="utf-8")
    (OUT / "banner-static.svg").write_text(banner_svg(animated=False), encoding="utf-8")
    framed(ROOT / "SafeTraj-Experiments" / "docs" / "figures" / "derived" / "orientation_sensitivity.png",
           OUT / "cards" / "safetraj-experiments.png",
           "Source: SafeTraj-Experiments · results/tables/exp1_theta_sensitivity.csv (derived view)")
    framed(ROOT / "trajectory-failure-analysis" / "docs" / "figures" / "risk_maps_orientation_speed.png",
           OUT / "cards" / "trajectory-failure-analysis.png",
           "Source: trajectory-failure-analysis · binned risk maps from the reproduced results")
    framed(ROOT / "SafeTraj-Prototype" / "docs" / "figures" / "dashboard_evaluate.png",
           OUT / "cards" / "safetraj-prototype.png",
           "Source: SafeTraj-Prototype · dashboard running locally (streamlit run dashboard/app.py)")
    framed(ROOT / "pouyapd" / "assets" / "projects" / "trustrag.png", OUT / "cards" / "trustrag.png",
           "Source: TrustRAG · docs/figures/pipeline_evaluation.png")
    safenav_replay(OUT / "cards" / "safenav-rl.gif")
    demo_source = "Source: GroundedAI live demo, recorded in a browser · extractive generator, sample PDF"
    framed_gif(ROOT / "GroundedAI" / "docs" / "images" / "demo-preview.gif", OUT / "cards" / "groundedai.gif",
               demo_source)
    framed(ROOT / "GroundedAI" / "docs" / "images" / "demo-preview.png", OUT / "cards" / "groundedai.png",
           demo_source)
    for p in sorted(OUT.rglob("*.*")):
        print(f"{p.relative_to(OUT.parent.parent).as_posix():45s} {p.stat().st_size / 1024:7.1f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
