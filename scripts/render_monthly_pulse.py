"""Render the web-first August 2026 curation pulse into verified sibling repos.
Source snapshots below were checked with GitHub's repository API on 2026-08-03.
"""
from pathlib import Path

ROOT = Path(r"C:/Users/frank/starlight/repos")
DATE = "2026-08-03"
ECOSYSTEM = """## Explore the Full FrankX Awesome Ecosystem (optional)

Companion catalogs are optional; the third-party projects above are this list's primary value.

- [awesome-jarvis](https://github.com/frankxai/awesome-jarvis) · [awesome-hermes-agents](https://github.com/frankxai/awesome-hermes-agents) · [awesome-manifestation-skills](https://github.com/frankxai/awesome-manifestation-skills) · [awesome-ai-coe](https://github.com/frankxai/awesome-ai-coe)
- [awesome-agentic-income](https://github.com/frankxai/awesome-agentic-income) · [awesome-investor-agent-skills](https://github.com/frankxai/awesome-investor-agent-skills) · [awesome-design-agent-skills](https://github.com/frankxai/awesome-design-agent-skills) · [awesome-agent-operating-systems](https://github.com/frankxai/awesome-agent-operating-systems)
- [awesome-music-agent-skills](https://github.com/frankxai/awesome-music-agent-skills) · [awesome-hermes-agent-skills](https://github.com/frankxai/awesome-hermes-agent-skills) · [awesome-gamification-agent-skills](https://github.com/frankxai/awesome-gamification-agent-skills) · [awesome-wealth-agent-skills](https://github.com/frankxai/awesome-wealth-agent-skills)
- [awesome-mind-agent-skills](https://github.com/frankxai/awesome-mind-agent-skills) · [awesome-cosmos-ai-agents](https://github.com/frankxai/awesome-cosmos-ai-agents) · [awesome-automation-agent-skills](https://github.com/frankxai/awesome-automation-agent-skills) · [awesome-payment-agent-skills](https://github.com/frankxai/awesome-payment-agent-skills) · [awesome-motion-design-agent-skills](https://github.com/frankxai/awesome-motion-design-agent-skills)
"""
PILLARS = """## 6-Pillar curation lens

```mermaid
mindmap
  root((Curated agent capability))
    Strategy
      fit and scope
    Governance
      provenance and license
    Talent
      human review
    Technology
      tools and integration
    Data
      evidence and memory
    Ethics
      safety and disclosure
```

This lens is editorial, not an endorsement or a claim that a project satisfies every pillar.
"""
TAIL = f"""## Contribution standard

Open a PR with a primary URL, one-sentence distinct value, current maintenance evidence, license posture, and relevant safety/deployment caveat. Do not submit affiliate links, private workflow exports, unverified claims, or a product pitch in place of a useful third-party resource.

## Research method

This monthly pulse queried GitHub repository metadata on **{DATE}** for identity, approximate stars, archived state, activity, and license posture. `NOASSERTION` means GitHub did not return a standard SPDX identifier; review the repository license before adoption. Counts are dated discovery signals, not rankings. Nothing here is financial, legal, medical, or safety advice.

Maintained as independent, web-first curation by FrankX. Last research pulse: **{DATE}**.
"""

# repo: title, scope, decision guide, peer links, [(name,url,snapshot,why), ...]
SPECS = {
"awesome-manifestation-skills": (
 "Awesome Manifestation Skills", "Web-first tools for reflective, observable, human-owned practices—not guarantees of personal outcomes.",
 "Choose private capture, reusable routines, and a review cadence; do not treat an agent as a therapist or authority.",
 "[agentskills/agentskills](https://github.com/agentskills/agentskills) · [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)",
 [("Memos","https://github.com/usememos/memos","MIT · 61,956★","Markdown-native private capture."),("Logseq","https://github.com/logseq/logseq","AGPL-3.0 · 44,214★","Privacy-first linked review notes."),("Obsidian releases","https://github.com/obsidianmd/obsidian-releases","NOASSERTION · 20,387★","Official releases and plugin index."),("Agent Skills","https://github.com/agentskills/agentskills","Apache-2.0 · 23,762★","Portable, inspectable skill packages."),("Anthropic skills","https://github.com/anthropics/skills","NOASSERTION · 165,802★","Public skill collection; inspect boundaries."),("gstack","https://github.com/garrytan/gstack","MIT · 125,927★","Human-reviewed planning and QA loops.")]),
"awesome-agentic-income": (
 "Awesome Agentic Income", "Web-first infrastructure for building, measuring, and governing agent-assisted products—without income promises or affiliate funnels.",
 "Start with customer value, then choose delivery, metering, billing, and attribution. Humans own pricing, claims, permissions, and spend.",
 "[openmeterio/openmeter](https://github.com/openmeterio/openmeter) · [getlago/lago](https://github.com/getlago/lago)",
 [("OpenAI Agents SDK","https://github.com/openai/openai-agents-python","MIT · 28,345★","Bounded multi-agent workflows."),("Vercel AI SDK","https://github.com/vercel/ai","NOASSERTION · 25,965★","Toolkit for AI applications."),("MCP Registry","https://github.com/modelcontextprotocol/registry","NOASSERTION · 7,097★","Community MCP registry; evaluate permissions."),("OpenMeter","https://github.com/openmeterio/openmeter","Apache-2.0 · 2,168★","AI/API usage metering."),("Lago","https://github.com/getlago/lago","AGPL-3.0 · 10,282★","Usage-based billing infrastructure."),("Stripe Node","https://github.com/stripe/stripe-node","MIT · 4,477★","Official API client; compliance stays human-owned."),("Dub","https://github.com/dubinc/dub","NOASSERTION · 24,210★","Disclosed link attribution.")]),
"awesome-ai-coe": (
 "Awesome AI Center of Excellence", "Web-first resources for accountable AI CoE practice: standards, evaluation, skills, orchestration, and operating guardrails.",
 "Assign clear owners for policy, data, architecture, procurement, and releases. Pilot separately from production and measure evidence—not demos.",
 "[microsoft/skills](https://github.com/microsoft/skills) · [agentskills/agentskills](https://github.com/agentskills/agentskills)",
 [("Agent Skills","https://github.com/agentskills/agentskills","Apache-2.0 · 23,762★","Portable capability standard."),("Microsoft skills","https://github.com/microsoft/skills","MIT · 2,853★","Skills, MCP, custom agents, AGENTS.md."),("Agentic Awesome Skills","https://github.com/sickn33/agentic-awesome-skills","MIT · 44,310★","Large peer catalog; curate before install."),("AutoGen","https://github.com/microsoft/autogen","CC-BY-4.0 · 60,169★","Agentic AI framework."),("LangGraph","https://github.com/langchain-ai/langgraph","MIT · 38,702★","Resilient stateful agents."),("gstack","https://github.com/garrytan/gstack","MIT · 125,927★","Product/design/engineering QA workflows."),("OpenAI Agents SDK","https://github.com/openai/openai-agents-python","MIT · 28,345★","Small explicit multi-agent primitives.")]),
"awesome-investor-agent-skills": (
 "Awesome Investor Agent Skills", "Web-first research and analysis tools for investor workflows: educational research and simulation only, never personalized investment advice.",
 "Use public data and reproducible notebooks; separate collection, analysis, backtesting, and any regulated or execution-adjacent action.",
 "[OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) · [microsoft/qlib](https://github.com/microsoft/qlib)",
 [("OpenBB","https://github.com/OpenBB-finance/OpenBB","NOASSERTION · 71,296★","Open data platform for analysts and AI agents."),("Qlib","https://github.com/microsoft/qlib","MIT · 46,947★","AI-oriented quantitative research."),("QuantStats","https://github.com/ranaroussi/quantstats","Apache-2.0 · 7,511★","Portfolio analytics for quants."),("LEAN","https://github.com/QuantConnect/Lean","Apache-2.0 · 21,025★","Execution-adjacent engine; education/backtesting only."),("cvxportfolio","https://github.com/cvxgrp/cvxportfolio","GPL-3.0 · 1,244★","Portfolio optimization/backtesting."),("OpenAI Agents SDK","https://github.com/openai/openai-agents-python","MIT · 28,345★","Bounded research assistants with approval gates.")]),
"awesome-design-agent-skills": (
 "Awesome Design Agent Skills", "Web-first resources for design agents that improve hierarchy, typography, accessibility, interaction quality, and visual QA—not prompt dumps.",
 "Use a concrete brief, inspect actual desktop/mobile output, and retain human ownership of brand, legal, and accessibility decisions.",
 "[bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) · [rohitg00/awesome-claude-design](https://github.com/rohitg00/awesome-claude-design)",
 [("Awesome Design Skills","https://github.com/bergside/awesome-design-skills","license verify · 2,139★","Peer catalog of DESIGN.md/SKILL.md assets."),("Design MD Chrome","https://github.com/bergside/design-md-chrome","license verify · 2,585★","Style extraction and DESIGN.md tooling."),("Awesome Claude Design","https://github.com/rohitg00/awesome-claude-design","license verify · 941★","Peer design skills and teardowns."),("Agent Skills","https://github.com/agentskills/agentskills","Apache-2.0 · 23,762★","Inspectable workflow format."),("gstack","https://github.com/garrytan/gstack","MIT · 125,927★","Design consultation/review tools."),("Motion","https://github.com/motiondivision/motion","MIT · 33,055★","React/JavaScript animation."),("ComfyUI","https://github.com/Comfy-Org/ComfyUI","GPL-3.0 · 123,249★","Modular diffusion; inspect asset provenance.")]),
"awesome-automation-agent-skills": (
 "Awesome Automation Agent Skills", "Web-first automation, orchestration, MCP, and workflow resources with explicit permission, observability, and validation boundaries.",
 "Favor idempotent, least-privilege workflows. Keep discovery read-only and human-gate spend, publishing, credentials, and irreversible actions.",
 "[appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) · [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry)",
 [("n8n","https://github.com/n8n-io/n8n","NOASSERTION/fair-code · 199,086★","Workflow automation with AI capabilities."),("Activepieces","https://github.com/activepieces/activepieces","NOASSERTION · 23,550★","AI/MCP workflow automation."),("Prefect","https://github.com/PrefectHQ/prefect","Apache-2.0 · 23,533★","Resilient Python orchestration."),("Kestra","https://github.com/kestra-io/kestra","Apache-2.0 · 27,537★","Event-driven scheduling."),("MCP Servers","https://github.com/modelcontextprotocol/servers","NOASSERTION · 89,140★","Reference MCP server collection."),("MCP Registry","https://github.com/modelcontextprotocol/registry","NOASSERTION · 7,097★","Community registry."),("OpenMeter","https://github.com/openmeterio/openmeter","Apache-2.0 · 2,168★","Automation cost/capacity metering.")]),
"awesome-cosmos-ai-agents": (
 "Awesome Cosmos AI Agents", "Web-first resources for astronomy, astrodynamics, mission-data exploration, and scientifically grounded agent workflows.",
 "Preserve query provenance, units, timestamps, and uncertainty. Keep computation, interpretation, and visual storytelling separate.",
 "[Astropy](https://github.com/astropy/astropy) · [astroquery](https://github.com/astropy/astroquery)",
 [("Astropy","https://github.com/astropy/astropy","BSD-3-Clause · 5,248★","Core astronomy/astrophysics Python."),("astroquery","https://github.com/astropy/astroquery","BSD-3-Clause · 784★","Online astronomy-data access."),("Skyfield","https://github.com/skyfielders/python-skyfield","MIT · 1,755★","High-precision astronomy calculations."),("NASA Open MCT","https://github.com/nasa/openmct","NOASSERTION · 13,064★","Mission-control visualization layer."),("poliastro","https://github.com/poliastro/poliastro","MIT · 1,016★ · archived","Astrodynamics reference; assess maintenance."),("Jupyter MCP Server","https://github.com/datalayer/jupyter-mcp-server","license verify · 1,234★","Jupyter MCP; apply data safety gates."),("Remotion","https://github.com/remotion-dev/remotion","NOASSERTION · 55,303★","Clearly labeled scientific communication.")]),
"awesome-suno-agent-skills": (
 "Awesome Suno Agent Skills", "Web-first music-structure, audio-analysis, and generative-audio resources; this is not an official Suno catalog.",
 "Separate prompts, analysis, generation, rights review, and distribution. Confirm provider terms before any commercial use.",
 "[facebookresearch/audiocraft](https://github.com/facebookresearch/audiocraft) · [MTG/essentia](https://github.com/MTG/essentia)",
 [("Essentia","https://github.com/MTG/essentia","AGPL-3.0 · 3,673★","Music analysis with Python bindings."),("Muzic","https://github.com/microsoft/muzic","MIT · 4,939★","Music understanding/generation research."),("AudioCraft","https://github.com/facebookresearch/audiocraft","MIT · 23,532★","Audio generation and processing."),("Magenta","https://github.com/magenta/magenta","Apache-2.0 · 19,809★ · archived","Historic ML reference; not default dependency."),("Remotion","https://github.com/remotion-dev/remotion","NOASSERTION · 55,303★","Rights-reviewed visual packaging."),("Agent Skills","https://github.com/agentskills/agentskills","Apache-2.0 · 23,762★","Documented production skills."),("gstack","https://github.com/garrytan/gstack","MIT · 125,927★","QA loops adaptable to asset work.")]),
"awesome-music-agent-skills": (
 "Awesome Music Agent Skills", "Web-first resources for music generation, audio analysis, composition tooling, and rights-aware agent workflows.",
 "Select tools by task—analysis, symbolic composition, audio generation, or packaging—and retain human review over attribution, voice use, and release.",
 "[MTG/essentia](https://github.com/MTG/essentia) · [microsoft/muzic](https://github.com/microsoft/muzic)",
 [("Essentia","https://github.com/MTG/essentia","AGPL-3.0 · 3,673★","Audio/music analysis and synthesis."),("Muzic","https://github.com/microsoft/muzic","MIT · 4,939★","Music understanding/generation."),("AudioCraft","https://github.com/facebookresearch/audiocraft","MIT · 23,532★","Audio processing and generation."),("Agent Skills","https://github.com/agentskills/agentskills","Apache-2.0 · 23,762★","Repeatable production skills."),("Remotion","https://github.com/remotion-dev/remotion","NOASSERTION · 55,303★","Video/visualizer packaging."),("Magenta","https://github.com/magenta/magenta","Apache-2.0 · 19,809★ · archived","Historic reference; assess status.")]),
"awesome-anime-agent-skills": (
 "Awesome Anime Agent Skills", "Web-first resources for agent-assisted anime-style preproduction, image/video workflows, audio, and quality review—not an official studio or rights clearance.",
 "Use original briefs, character bibles, shot lists, and review rubrics. Do not imitate protected franchises or clone voices without consent.",
 "[ComfyUI](https://github.com/Comfy-Org/ComfyUI) · [deforum](https://github.com/deforum/deforum-stable-diffusion)",
 [("ComfyUI","https://github.com/Comfy-Org/ComfyUI","GPL-3.0 · 123,249★","Graph-based diffusion workflows."),("Stable Diffusion WebUI","https://github.com/AUTOMATIC1111/stable-diffusion-webui","AGPL-3.0 · 164,356★","Community UI; assess model provenance."),("Deforum","https://github.com/deforum/deforum-stable-diffusion","NOASSERTION · 2,286★","Animated diffusion workflows."),("Blender","https://github.com/blender/blender","NOASSERTION · 19,467★","Original scene/composite/animation."),("AudioCraft","https://github.com/facebookresearch/audiocraft","MIT · 23,532★","Audio components; no rights implied."),("Remotion","https://github.com/remotion-dev/remotion","NOASSERTION · 55,303★","Reproducible packaging."),("Agent Skills","https://github.com/agentskills/agentskills","Apache-2.0 · 23,762★","Storyboarding/review skills.")]),
"awesome-gamification-agent-skills": (
 "Awesome Gamification Agent Skills", "Web-first resources for ethical progression systems, game-state design, multiplayer coordination, and agent-assisted playtesting.",
 "Design for consent, clarity, and meaningful choice. Avoid dark patterns or autonomous changes to user progression or spending.",
 "[godotengine/godot](https://github.com/godotengine/godot) · [boardgame.io](https://github.com/boardgameio/boardgame.io)",
 [("Godot","https://github.com/godotengine/godot","MIT · 114,953★","Open 2D/3D engine."),("Phaser","https://github.com/phaserjs/phaser","MIT · 40,049★","Web game framework."),("boardgame.io","https://github.com/boardgameio/boardgame.io","MIT · 12,388★","Turn-based game state/multiplayer."),("Colyseus","https://github.com/colyseus/colyseus","MIT · 7,150★","Node multiplayer framework."),("gstack","https://github.com/garrytan/gstack","MIT · 125,927★","Planning/design/QA tools."),("Agent Skills","https://github.com/agentskills/agentskills","Apache-2.0 · 23,762★","Playtest/balance checklists."),("OpenAI Agents SDK","https://github.com/openai/openai-agents-python","MIT · 28,345★","Bounded evaluation workflows.")]),
"awesome-wealth-agent-skills": (
 "Awesome Wealth Agent Skills", "Web-first resources for financial research, reporting, scenario analysis, and governance—educational and analytical only, never personalized financial advice.",
 "Expose sources, dates, currencies, and assumptions. Keep holdings, tax, custody, regulated advice, and decisions with authorized humans/professionals.",
 "[OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) · [ranaroussi/quantstats](https://github.com/ranaroussi/quantstats)",
 [("OpenBB","https://github.com/OpenBB-finance/OpenBB","NOASSERTION · 71,296★","Open analyst/quant data platform."),("QuantStats","https://github.com/ranaroussi/quantstats","Apache-2.0 · 7,511★","Portfolio analytics."),("Qlib","https://github.com/microsoft/qlib","MIT · 46,947★","Quant research platform."),("cvxportfolio","https://github.com/cvxgrp/cvxportfolio","GPL-3.0 · 1,244★","Optimization/backtesting."),("OpenMeter","https://github.com/openmeterio/openmeter","Apache-2.0 · 2,168★","Cost/unit-economics observability."),("Lago","https://github.com/getlago/lago","AGPL-3.0 · 10,282★","Product-finance billing infrastructure."),("OpenAI Agents SDK","https://github.com/openai/openai-agents-python","MIT · 28,345★","Bounded research agents.")]),
"awesome-animation-agent-skills": (
 "Awesome Animation Agent Skills", "Web-first resources for original 2D/3D animation, procedural motion, render pipelines, and agent-assisted review.",
 "Choose the medium first and keep character rights, source assets, and final artistic approval under human control.",
 "[blender/blender](https://github.com/blender/blender) · [remotion-dev/remotion](https://github.com/remotion-dev/remotion)",
 [("Blender","https://github.com/blender/blender","NOASSERTION · 19,467★","Original modeling, rigging, rendering."),("Remotion","https://github.com/remotion-dev/remotion","NOASSERTION · 55,303★","Programmatic video rendering."),("Motion","https://github.com/motiondivision/motion","MIT · 33,055★","Web animation."),("React Three Fiber","https://github.com/pmndrs/react-three-fiber","MIT · 31,609★","Interactive 3D scenes."),("ComfyUI","https://github.com/Comfy-Org/ComfyUI","GPL-3.0 · 123,249★","Generated workflow provenance required."),("Deforum","https://github.com/deforum/deforum-stable-diffusion","NOASSERTION · 2,286★","Animated diffusion experimentation."),("gstack","https://github.com/garrytan/gstack","MIT · 125,927★","Animation QA loop support.")]),
"awesome-motion-design-agent-skills": (
 "Awesome Motion Design Agent Skills", "Web-first resources for interface motion, cinematic web interaction, programmatic video, and motion-design review workflows.",
 "Start with static hierarchy, animate only to clarify state or narrative, provide reduced motion, and verify performance on real devices.",
 "[greensock/GSAP](https://github.com/greensock/GSAP) · [remotion-dev/remotion](https://github.com/remotion-dev/remotion)",
 [("GSAP","https://github.com/greensock/GSAP","NOASSERTION · 27,317★","Modern JavaScript animation."),("Motion","https://github.com/motiondivision/motion","MIT · 33,055★","React/JavaScript animation."),("React Three Fiber","https://github.com/pmndrs/react-three-fiber","MIT · 31,609★","Three.js React renderer."),("Phaser","https://github.com/phaserjs/phaser","MIT · 40,049★","Real-time web interaction patterns."),("Remotion","https://github.com/remotion-dev/remotion","NOASSERTION · 55,303★","Programmatic video rendering."),("gstack","https://github.com/garrytan/gstack","MIT · 125,927★","Design review and QA."),("Agent Skills","https://github.com/agentskills/agentskills","Apache-2.0 · 23,762★","Documented motion review/handoff.")]),
}

def render(repo, title, scope, guide, peers, rows):
    header = f"# {title}\n\n[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Stars](https://img.shields.io/github/stars/frankxai/{repo}?style=flat)](https://github.com/frankxai/{repo}/stargazers) [![Last commit](https://img.shields.io/github/last-commit/frankxai/{repo}?style=flat)](https://github.com/frankxai/{repo}/commits/main)\n\n> {scope}\n\nThis is an independent, **web-first** catalog. It remains useful if every FrankX link is removed: third-party primary sources lead, while companion lists appear only at the end.\n\n## Start here\n\n{guide}\n\n## Peer directories and standards\n\n{peers}\n\n## Curated catalog\n\n| Project | Pulse snapshot | Why it is here |\n| --- | --- | --- |\n"
    table = "\n".join(f"| [{n}]({u}) | {s} | {w} |" for n, u, s, w in rows)
    (ROOT / repo / "README.md").write_text(header + table + "\n\n" + PILLARS + "\n" + ECOSYSTEM + "\n" + TAIL, encoding="utf-8")

for repo, spec in SPECS.items():
    render(repo, *spec)
    print(f"rendered {repo}")
