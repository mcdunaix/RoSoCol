This document captures project state for session continuity. A new agent reading this file should be able to orient and resume work without reading the previous transcript.

## Resume here

### 2026-10-06 — Repository formatting scheme, interactive visual tools, and Obsidian in-note rendering

**Session arc.**
1. Established Top-Down Tri-Layer formatting scheme for dense non-imaging optics theory: (L1) Executive One-Breath principle + 3-tool snapshot table, (L2) CEO plain language business translation with dials/trade-offs, (L3) Interactive visual parameter sliders + bottom-loaded technical vector math derivations.
2. Built interactive parameter explorer `assets/interactive/cpc-explorer.html` (lightweight offline HTML5/Canvas, real-time 2D ray tracing, aspect ratio and concentration calculations).
3. Calibrated and restructured note `02-Geometries/20-CPC-Solid-of-Revolution.md` to pilot the formatting scheme.
4. Attempted in-note rendering via relative iframe and Base64 Data URI; identified that Obsidian's Chromium renderer and CSP block local relative frames and `data:` scripts.
5. Installed and registered Obsidian community plugin `local-html-embed` under `.obsidian/plugins/local-html-embed/` and `.obsidian/community-plugins.json`. Switched note syntax to ```` ```html-embed assets/interactive/cpc-explorer.html``` ```` for native in-note interactive rendering.
6. Investigated Obsidian launch state and verified the process is active with `RoSoCol` vault mounted.

**Decisions pinned.**
- **D-01**: Top-Down Tri-Layer note structure across all technical notes (Executive summary & Rule of 3s snapshot -> CEO plain language & trade-offs -> Interactive tool -> Bottom-loaded math derivations).
- **D-02**: Self-contained offline HTML5/Canvas interactive widgets placed in `assets/interactive/` for spatial/geometric parameter intuition.
- **D-03**: In-note interactive rendering via `local-html-embed` markdown code blocks rather than sandboxed iframes or background HTTP daemons.

**Files produced/changed.**
- `SESSION_STATE.md`: Project continuity and session handoff state document.
- `assets/interactive/cpc-explorer.html`: Offline HTML5/Canvas interactive CPC parameter explorer and ray tracer.
- `02-Geometries/20-CPC-Solid-of-Revolution.md`: Refactored to Tri-Layer standard with embedded `html-embed` widget block.
- `.obsidian/plugins/local-html-embed/`: Community plugin files (`main.js`, `manifest.json`) enabling in-note HTML embeds.
- `.obsidian/community-plugins.json`: Vault configuration registering `local-html-embed`.
- `.obsidian/app.json`: Preserved vault configuration.

**Gotchas.**
- Obsidian's Electron/Chromium security sandbox rejects `<iframe src="data:text/html;base64,...">` execution via its internal CSP and sanitization, rendering blank boxes. Do not attempt inline base64 iframes for scripts inside Obsidian notes.
- Obsidian requires `.obsidian/community-plugins.json` to register installed plugins, and plugins only initialize when Obsidian starts or reloads (`Cmd + R`).

**On the horizon.**
- **Immediate**: Verify visual interactive render of `02-Geometries/20-CPC-Solid-of-Revolution.md` in Obsidian Live Preview/Reading View.
- **Rolled forward**: Roll out the Tri-Layer formatting scheme and interactive tools to remaining core theory notes (`01-Theory/10-Non-Imaging-Optics-Foundations.md`, `01-Theory/11-Rotational-Symmetry-and-Phase-Space.md`, `02-Geometries/21-Dielectric-TIR-Concentrators.md`).
