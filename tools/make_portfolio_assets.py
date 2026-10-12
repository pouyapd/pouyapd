"""
Presentation graphics for the pouyapd portfolio: README banners (light and dark SVG)
and social-preview images (PNG) for the profile and the four project repositories.

Every line drawing is computed from a committed result file (or the built-in model)
of the project it represents, and each graphic states its source. No number is drawn
that is not in those files.

Run from the folder that contains the repositories (each checked out side by side):

    python pouyapd/tools/make_portfolio_assets.py

Outputs:
    <repo>/docs/assets/banner-light.svg, banner-dark.svg, social-preview.png
    pouyapd/assets/banner-light.svg, banner-dark.svg
"""

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from matplotlib.patches import Circle, FancyBboxPatch  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
plt.rcParams.update({
    "font.family": ["Segoe UI", "DejaVu Sans"],
    "svg.fonttype": "path",          # text as outlines: renders the same in every browser
    "svg.hashsalt": "pouyapd",       # stable ids, so regenerating gives identical files
    "path.simplify": True,
})

THEMES = {
    "dark": dict(bg="#0d1117", panel="#151b23", border="#30363d", ink="#f0f6fc", ink2="#9198a1",
                 muted="#3d444d", faint="#262c36", bad="#f47067"),
    "light": dict(bg="#ffffff", panel="#f6f8fa", border="#d1d9e0", ink="#1f2328", ink2="#59636e",
                  muted="#c8d1da", faint="#e6eaef", bad="#cf222e"),
}
ACCENT = {  # (light, dark)
    "SafeNav-RL": ("#1a7f74", "#3fc1b0"),
    "SafeTraj-Prototype": ("#b06a00", "#e3a33b"),
    "trajectory-failure-analysis": ("#6750d6", "#a493ff"),
    "SafeTraj-Experiments": ("#1f6fcf", "#5aa2f5"),
    "pouyapd": ("#1f6fcf", "#5aa2f5"),
}
SERIES = "POUYA BATHAEI POURMAND  ·  TRUSTWORTHY AI RESEARCH SOFTWARE"


# ── motifs (data → drawing on an axes) ──────────────────────────────────────

def motif_safenav(ax, th, accent):
    sys.path.insert(0, str(ROOT / "SafeNav-RL"))
    from safenav.evaluation.benchmark import load_trajectories
    trajs = load_trajectories(ROOT / "SafeNav-RL" / "results" / "benchmark" / "trajectories.npz")
    seed = sorted({int(t["episode_seed"]) for t in trajs if t["stage"] == "expert"})[0]
    pick = {(t["method"], bool(t["safety_filter"])): t for t in trajs
            if t["stage"] == "expert" and int(t["episode_seed"]) == seed and t["train_seed"] in (0, "0", None, "None")}
    pf, ppo = pick[("PotentialField", True)], pick[("PPO (filter in training)", True)]
    margin = 0.3 + 0.3                                          # robot radius + safety margin
    for x, y, r in pf["obstacles"]:
        ax.add_patch(Circle((x, y), r, color=th["muted"], lw=0))
        ax.add_patch(Circle((x, y), r + margin, fill=False, ec=th["ink2"], lw=0.7, ls=(0, (2, 2)), alpha=0.6))
    p = ppo["trajectory"]
    ax.plot(p[:, 0], p[:, 1], color=th["ink2"], lw=1.6, solid_capstyle="round")
    ax.plot(*p[-1], marker="s", ms=5, color=th["ink2"])
    q = pf["trajectory"]
    ax.plot(q[:, 0], q[:, 1], color=accent, lw=2.4, solid_capstyle="round")
    ax.plot(*q[0], marker="o", ms=6, color=th["ink"])
    ax.plot(*pf["goal"], marker="*", ms=13, color=accent)
    ax.set_xlim(-0.2, 10.2)
    ax.set_ylim(-0.2, 10.2)
    ax.set_aspect("equal")
    return (f"Expert test scenario {seed} (the first), filter on: potential field reaches the goal; "
            f"PPO trained with the filter stalls (grey). results/benchmark")


def motif_prototype(ax, th, accent):
    sys.path.insert(0, str(ROOT / "SafeTraj-Prototype"))
    from safetraj import SafeTrajEvaluator
    ev = SafeTrajEvaluator()
    goal = (1.0, 0.0)
    ax.add_patch(Circle(goal, 0.50, color=th["faint"], lw=0))
    ax.add_patch(Circle(goal, 0.30, fill=False, ec=accent, lw=1.0))
    for cmd in ((0.0, 0.8, 0.0), (1.6, 1.0, 0.0), (2.9, 0.8, 0.0), (2.9, 2.4, 0.0)):
        res = ev.evaluate(cmd, return_traj=True, goal=goal)
        tr = res["trajectory"]
        xy = np.column_stack([tr.x, tr.y]) if hasattr(tr, "x") else np.asarray(tr)[:, :2]
        ok = res["metrics"]["outcome_soft"] == "success"
        ax.plot(xy[:, 0], xy[:, 1], color=accent if ok else th["bad"], lw=2.2 if ok else 1.8,
                solid_capstyle="round")
        ax.plot(*xy[-1], marker="o", ms=4, color=accent if ok else th["bad"])
    ax.plot(0, 0, marker="o", ms=6, color=th["ink"])
    ax.set_xlim(-1.5, 2.1)
    ax.set_ylim(-1.65, 1.65)
    ax.set_aspect("equal")
    return ("Four commands toward goal (1, 0), built-in goal-seeking predictor (a physics stand-in, "
            "not a learned model); red: ends outside 0.5 m.")


def _risk_grid(df):
    o_edges = np.linspace(-np.pi, np.pi, 9)
    s_edges = np.array([0.0, 0.5, 1.0, 1.5, 2.0, 3.6])
    grid = np.full((len(s_edges) - 1, len(o_edges) - 1), np.nan)
    for i in range(len(s_edges) - 1):
        for j in range(len(o_edges) - 1):
            m = ((df.init_speed >= s_edges[i]) & (df.init_speed < s_edges[i + 1])
                 & (df.init_orientation >= o_edges[j]) & (df.init_orientation < o_edges[j + 1]))
            if m.sum() >= 3:
                grid[i, j] = df.failure[m].mean()
    return grid


def motif_tfa(ax, th, accent):
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("acc", [th["faint"], accent])
    base = ROOT / "trajectory-failure-analysis" / "results" / "reproduction"
    for k, (scene, name) in enumerate((("eth", "ETH"), ("hotel", "Hotel"))):
        grid = _risk_grid(pd.read_csv(base / f"results_{scene}.csv"))
        x0 = k * 9.5
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                v = grid[i, j]
                ax.add_patch(FancyBboxPatch((x0 + j + 0.06, i + 0.06), 0.88, 0.88,
                                            boxstyle="round,pad=0,rounding_size=0.12", lw=0,
                                            color=th["panel"] if np.isnan(v) else cmap(min(1.0, v / 0.6))))
                if np.isnan(v):
                    ax.add_patch(FancyBboxPatch((x0 + j + 0.06, i + 0.06), 0.88, 0.88,
                                                boxstyle="round,pad=0,rounding_size=0.12",
                                                fill=False, ec=th["faint"], lw=0.6))
        ax.text(x0 + 4, -0.55, name, ha="center", va="top", fontsize=9, color=th["ink2"])
    ax.set_xlim(-0.2, 17.7)
    ax.set_ylim(-1.6, 5.2)
    ax.set_aspect("equal")
    return ("Failure rate per initial orientation × speed bin (darker = more failures; empty = fewer than 3 "
            "trajectories). results/reproduction/results_*.csv")


def motif_ste(ax, th, accent):
    df = pd.read_csv(ROOT / "SafeTraj-Experiments" / "results" / "tables" / "exp1_theta_sensitivity.csv")
    df = df[np.isclose(df.GoalX, 1.0) & np.isclose(df.GoalY, 0.0)]
    order = ["DNN_LNA_closs2", "DNN_LNA_on_wheel1", "DNN_LNA_mse", "DNN_LNA_sinu", "DNN_LNA_closs1"]
    for rank, model in enumerate(order):
        d = df[df.Model == model].sort_values("Theta_center")
        strong = model in ("DNN_LNA_closs2", "DNN_LNA_closs1")
        ax.plot(d.Theta_center, d.SuccessRate, color=accent if strong else th["ink2"],
                lw=2.4 if strong else 1.1, alpha=1.0 if strong else 0.7, marker="o", ms=3.5 if strong else 2.5,
                solid_capstyle="round")
        if strong:
            ax.text(d.Theta_center.iloc[-1] + 0.15, d.SuccessRate.iloc[-1], model.replace("DNN_LNA_", ""),
                    fontsize=8, color=accent, va="center")
    ax.axhline(0, color=th["faint"], lw=0.8)
    ax.axhline(100, color=th["faint"], lw=0.8)
    ax.set_xlim(-3.2, 4.2)
    ax.set_ylim(-8, 108)
    return ("Strict success (%) per initial-orientation bin, goal B, five pretrained models. "
            "results/tables/exp1_theta_sensitivity.csv")


PROJECTS = {
    "SafeNav-RL": dict(title="SafeNav-RL", motif=motif_safenav,
                       tagline="Safe reinforcement learning for 2D robot navigation",
                       chips=["PPO", "control barrier function filter", "seeded multi-seed benchmark", "simulation"]),
    "SafeTraj-Prototype": dict(title="SafeTraj-Prototype", motif=motif_prototype,
                               tagline="Trajectory checks, input novelty and failure rules for motion predictors",
                               chips=["Python library", "CLI", "FastAPI", "Streamlit"]),
    "trajectory-failure-analysis": dict(title="Trajectory Failure Analysis", motif=motif_tfa,
                                        tagline="Where and why a pedestrian trajectory predictor fails (ETH dataset)",
                                        chips=["risk maps", "decision-tree rules", "verified preprint reproduction"]),
    "SafeTraj-Experiments": dict(title="SafeTraj-Experiments", motif=motif_ste,
                                 tagline="Black-box failure analysis of five pretrained trajectory predictors",
                                 chips=["MSc thesis", "REXASI-PRO", "42 consistency checks", "SHA-256 manifest"]),
}


# ── layouts ─────────────────────────────────────────────────────────────────

def _panel(fig, th):
    fig.patch.set_alpha(0.0)
    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    bg.add_patch(FancyBboxPatch((0.004, 0.012), 0.992, 0.976, boxstyle="round,pad=0,rounding_size=0.018",
                                transform=bg.transAxes, fc=th["panel"], ec=th["border"], lw=1.0,
                                mutation_aspect=fig.get_figwidth() / fig.get_figheight()))
    return bg


def _chips(fig, x, y, chips, th, size):
    renderer = fig.canvas.get_renderer()
    for c in chips:
        t = fig.text(x, y, c, fontsize=size, color=th["ink2"], va="center", ha="left",
                     bbox=dict(boxstyle="round,pad=0.38,rounding_size=0.8", fc=th["bg"], ec=th["border"], lw=0.8))
        bb = t.get_window_extent(renderer=renderer)
        x += bb.width / fig.bbox.width + 0.012


def _save(fig, out):
    out = Path(out)
    meta = {"Date": None} if out.suffix == ".svg" else {"Software": None}
    fig.savefig(out, transparent=True, metadata=meta)
    plt.close(fig)
    if out.suffix == ".svg":                 # matplotlib leaves trailing spaces in path data
        lines = out.read_text(encoding="utf-8").splitlines()
        out.write_text("\n".join(line.rstrip() for line in lines) + "\n", encoding="utf-8")


def banner(repo, spec, theme, out):
    th = THEMES[theme]
    accent = ACCENT[repo][1 if theme == "dark" else 0]
    fig = plt.figure(figsize=(12, 2.7), dpi=100)
    _panel(fig, th)
    fig.text(0.035, 0.80, SERIES, fontsize=8.2, color=accent, weight="semibold")
    fig.text(0.035, 0.535, spec["title"], fontsize=29, color=th["ink"], weight="bold", va="center")
    fig.text(0.035, 0.33, spec["tagline"], fontsize=12.5, color=th["ink2"], va="center")
    _chips(fig, 0.037, 0.15, spec["chips"], th, 9)
    ax = fig.add_axes([0.62, 0.16, 0.355, 0.74])
    ax.set_axis_off()
    source = spec["motif"](ax, th, accent)
    fig.text(0.975, 0.055, source if len(source) < 150 else source[:147] + "…", fontsize=6.3,
             color=th["ink2"], ha="right", va="center", alpha=0.85)
    _save(fig, out)


def social(repo, spec, out):
    import textwrap
    th = THEMES["dark"]
    accent = ACCENT[repo][1]
    fig = plt.figure(figsize=(12.8, 6.4), dpi=100)
    fig.patch.set_facecolor(th["bg"])
    bg = fig.add_axes([0, 0, 1, 1])
    bg.set_axis_off()
    bg.add_patch(FancyBboxPatch((0.025, 0.04), 0.95, 0.92, boxstyle="round,pad=0,rounding_size=0.02",
                                transform=bg.transAxes, fc=th["panel"], ec=th["border"], lw=1.2,
                                mutation_aspect=2.0))
    fig.text(0.065, 0.855, SERIES, fontsize=10.5, color=accent, weight="semibold")
    fig.text(0.065, 0.70, textwrap.fill(spec["title"], 20), fontsize=36, color=th["ink"], weight="bold",
             va="center", linespacing=1.05)
    fig.text(0.065, 0.50, textwrap.fill(spec["tagline"], 40), fontsize=16.5, color=th["ink2"], va="center",
             linespacing=1.3)
    _chips(fig, 0.067, 0.30, spec["chips"], th, 12)
    ax = fig.add_axes([0.585, 0.37, 0.36, 0.52])
    ax.set_axis_off()
    spec["motif"](ax, th, accent)
    fig.text(0.065, 0.10, f"github.com/pouyapd/{repo}", fontsize=12.5, color=th["ink2"])
    fig.savefig(out, format="png", facecolor=th["bg"], metadata={"Software": None})
    plt.close(fig)


def profile_banner(theme, out):
    th = THEMES[theme]
    accent = ACCENT["pouyapd"][1 if theme == "dark" else 0]
    fig = plt.figure(figsize=(12, 2.9), dpi=100)
    _panel(fig, th)
    fig.text(0.035, 0.80, "TRUSTWORTHY AI  ·  ML EVALUATION  ·  FAILURE ANALYSIS  ·  RESEARCH SOFTWARE",
             fontsize=8.2, color=accent, weight="semibold")
    fig.text(0.035, 0.55, "Pouya Bathaei Pourmand", fontsize=29, color=th["ink"], weight="bold", va="center")
    fig.text(0.035, 0.36, "Finding where learned systems fail, and explaining why —", fontsize=12.5,
             color=th["ink2"], va="center")
    fig.text(0.035, 0.27, "with tested, reproducible research code.", fontsize=12.5, color=th["ink2"], va="center")
    labels = list(PROJECTS)
    boxes = [[0.555, 0.53, 0.2, 0.36], [0.775, 0.53, 0.2, 0.36], [0.555, 0.11, 0.2, 0.36], [0.775, 0.11, 0.2, 0.36]]
    for repo, box in zip(labels, boxes):
        ax = fig.add_axes(box)
        ax.set_axis_off()
        PROJECTS[repo]["motif"](ax, th, ACCENT[repo][1 if theme == "dark" else 0])
        for t in list(ax.texts):
            t.remove()                       # no in-motif labels at this size
        fig.text(box[0] + box[2] / 2, box[1] - 0.025, PROJECTS[repo]["title"], fontsize=7, color=th["ink2"],
                 ha="center", va="top")
    _save(fig, out)


def main() -> int:
    for repo, spec in PROJECTS.items():
        out = ROOT / repo / "docs" / "assets"
        out.mkdir(parents=True, exist_ok=True)
        for theme in ("light", "dark"):
            banner(repo, spec, theme, out / f"banner-{theme}.svg")
        social(repo, spec, out / "social-preview.png")
        print("wrote", out)
    out = ROOT / "pouyapd" / "assets"
    out.mkdir(parents=True, exist_ok=True)
    for theme in ("light", "dark"):
        profile_banner(theme, out / f"banner-{theme}.svg")
    print("wrote", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
