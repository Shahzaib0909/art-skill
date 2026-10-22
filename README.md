# Art Skill

An AI-agent design skill for creating original thumbnails, social posts, carousels, posters, covers, and campaign artwork.

Art Skill turns a brief into a visual concept, selects suitable available tools, and reviews the exported result. It supports focused revisions without restarting the entire creative process.

## What it covers

- Original concepts and practical art direction.
- One final direction by default, with additional options when requested.
- Exact copy, purposeful typography, faithful logos, and identity references.
- Coherent carousel sequences and campaign variations.
- Urdu, Roman Urdu, and right-to-left rendering checks.
- Full-size and small-display inspection, export checks, and honest delivery status.
- Scoped project records without compulsory global personal memory.

## Install

Copy the complete `art-skill` folder into your agent's skills directory. For a local Codex installation, place it at `~/.codex/skills/art-skill`. Keep `SKILL.md`, `agents/`, and `references/` together. The repository root is also the skill folder, so a downloaded repository may be renamed to `art-skill` before installation.

## Use

```text
Use $art-skill to create one YouTube thumbnail for my video about learning Blender.
Audience: Urdu-speaking beginners. Visible copy: "BLENDER SEEKHO".
Use my supplied portrait. Keep the promise truthful and inspect mobile readability.
```

```text
Use $art-skill to create a six-slide Urdu carousel explaining my design service.
Use my supplied brand colors and verify Urdu shaping on every slide.
```

```text
Use $art-skill to correct only the spelling in this supplied poster.
Preserve the rest of the composition.
```

## Requirements

The skill supplies instructions, not an image-generation service. Finished artwork requires the host to expose appropriate image generation, image editing, or layout tools. Browsing is used when research or current facts require it. No API key, Python runtime, Pinterest account, or external reference corpus is required by the skill itself. Provider accounts, usage limits, and charges remain dependent on the tools you use.

## Files

- `SKILL.md`: mode selection, concept development, production, and review.
- `agents/openai.yaml`: Codex display metadata.
- `references/formats.md`: thumbnails, carousels, campaigns, Urdu/RTL, and exports.
- `references/project-records.md`: project continuity and memory boundaries.
- `references/quality.md`: observable acceptance checks and delivery status.

## Validation and limits

Initial version, 22 October 2026. Skill structure and internal reference links were checked. The workflow was desk-reviewed against repair, thumbnail, Urdu carousel, offline, vector, missing-tool, memory, and repeated-render-failure scenarios. These were not executed image-generation benchmarks. Visual quality, platform results, and audience performance are not guaranteed.

## Background

Created after reviewing [BeyondArtist](https://github.com/beyondtahir/beyondartist). Art Skill uses freshly written instructions and its own organization. It does not include BeyondArtist's reference corpus, scripts, branding, artwork, or identity assets and does not claim equivalent library coverage or affiliation.
