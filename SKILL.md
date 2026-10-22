---
name: modern-dashboard-ui-skill
description: >-
  Universal Web UI/UX Design System & Single-File Offline SPA Architecture
  Skill. Use when designing or building modern, high-contrast web dashboards,
  interactive tools, knowledge bases, or data applications. Provides a complete
  set of standards for Dual-Theme (Dark Tactical Dashboard & Light Eye-Care
  Mode), typography pairing (Noto Sans TC + JetBrains Mono), anti-wall-of-text
  semantic regex highlighting, step-by-step flowchart nodes, mobile/tablet
  touch optimization (sticky bottom bar, pinch-to-zoom lightbox, 44px tap
  targets, zero tap delay), GAS/PWA mobile home-screen icons, and zero-server
  single-file HTML bundling.
---

# Modern Dashboard UI & Offline SPA Design System (`modern-dashboard-ui-skill`)

## Overview

This skill distills best practices from modern web engineering (`modern-web-guidance`, `building-data-apps`, `a11y-debugging`, `generative_ui`, and `gas-mobile-shortcut-icon`) into a cohesive, shareable **Web UI/UX Design System**.

Activate this skill whenever you want the AI to build a clean, high-contrast, responsive web application or dashboard that works seamlessly across **Desktop, Tablet (iPad), and Mobile** — both online and as a **100% offline single-file `.html` bundle**.

---

## Core Design Pillars (五大設計核心規範)

### 1. Dual-Theme High-Contrast Color System (深色戰情室 ＆ 明亮護眼雙主題)

Always support a 1-click theme toggle (`🌙 深色戰情室` / `☀️ 明亮護眼`) persisted in `localStorage`:

| Semantic Role | Dark Tactical Mode (`html.dark`) | Light Eye-Care Mode (`html.light`) | Usage |
| :--- | :--- | :--- | :--- |
| **Main Canvas** | `#060b14` (Deep Navy Black) | `#f8fafc` (Slate 50) | Page background with subtle radial glow |
| **Panel / Card Surface** | `#0b1323` / `#0f172a` | `#ffffff` / `#f1f5f9` | Main content containers with `1px` border |
| **Sticky Glass Header** | `rgba(7, 13, 25, 0.90)` + `backdrop-blur-md` | `rgba(255, 255, 255, 0.94)` + `backdrop-blur-md` | Top navigation & mobile bottom bar |
| **Primary Info / Focus** | `Cyan-400` (`#22d3ee`) | `Sky-700` (`#0369a1`) | Active tabs, primary actions, key terms |
| **Success / Final Step** | `Emerald-400` (`#34d399`) | `Emerald-700` (`#047857`) | Final decision node, high accuracy (≥70%) |
| **Warning / Highlight** | `Amber-400` (`#fbbf24`) | `Amber-700` (`#b45309`) | Confusion traps, starred items, bold keywords |
| **Danger / Alert** | `Rose-400` (`#fb7185`) | `Rose-700` (`#be123c`) | Low accuracy (<60%), critical contraindications |

---

### 2. Typography Pairing & Responsive Grid (字體雙軌制與黃金響應式排版)

1. **Dual-Track Font Pairing**:
   - **Prose & Headings (`font-sans`)**: `"Noto Sans TC", system-ui, -apple-system, sans-serif` — generous line height (`leading-relaxed`) and never smaller than `12px` (`text-xs`).
   - **Numbers, IDs, Badges, Shortcuts (`font-mono`)**: `"JetBrains Mono", monospace` — ensures KPI numbers, percentages, and timers never jitter when values change.
2. **Desktop Split-Pane + Mobile Stack (`12-Column Grid`)**:
   - Use `max-w-[1600px] mx-auto` container.
   - Top section: Collapsible **KPI / Radar Cards Grid** (`grid-cols-2 md:grid-cols-3 xl:grid-cols-6`).
   - Main workspace: `grid-cols-1 lg:grid-cols-12 gap-5 items-start` — Left pane (`lg:col-span-7`) for primary interactive task/content; Right pane (`lg:col-span-5`) for visual flowcharts, step-by-step breakdowns, and alerts.

---

### 3. Anti-Wall-of-Text Visual Components (拒絕文字牆：三大視覺化元件)

Never render long paragraphs of raw text. Always transform explanations into structured visual components:

1. **Step-by-Step Decision Flowchart (`Algorithm Nodes`)**:
   - Render multi-step logic as numbered vertical cards connected by a gradient line (`w-0.5 h-3.5 bg-gradient-to-b from-cyan-400 to-emerald-400`).
   - **Highlight the Final Step (`isLast`)**: Automatically style the final conclusion node with an emerald glowing border (`border-emerald-400/70 bg-emerald-950/70`) so the user's eye immediately locks onto the actionable takeaway.
2. **3-Layer Regex Rich-Text Highlighter (`formatRichText`)**:
   - **Layer 1**: Convert `**bold**` into high-contrast amber highlights (`<strong class="text-amber-300 font-bold">`).
   - **Layer 2**: Convert `` `code` `` into monospace cyan pills (`<code class="px-1.5 py-0.5 rounded bg-cyan-950/80 text-cyan-300 font-mono text-xs border border-cyan-500/30">`).
   - **Layer 3**: Automatically highlight domain-specific keywords from a configurable dictionary (`highlightTerms`).
3. **Tabbed Quick Reference Modal (`Cheat Sheet Drawer`)**:
   - Provide a prominent top-bar button (`⚡ 速查表`) that opens a multi-tab modal containing comparison tables for high-frequency data or rules.

---

### 4. Mobile & Tablet Touch UX Optimization (行動裝置滿分觸控規範)

1. **Mobile Sticky Bottom Action Bar (`lg:hidden fixed bottom-0`)**:
   - On screens `<1024px`, provide a 4-button thumb-zone bar at the bottom of the viewport (`[← 上一頁]`, `[☆ 收藏]`, `[🧠 看解析/詳情]`, `[下一頁 →]`) and add `padding-bottom: 76px` to `body`.
2. **Zero Tap Delay & Accessible Tap Targets**:
   - Apply `touch-action: manipulation; -webkit-tap-highlight-color: transparent;` to all interactive controls.
   - Keep interactive buttons at least `40px–44px` tall on mobile.
3. **Pinch-to-Zoom & 200% Toggle Lightbox**:
   - Set `<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes" />`.
   - Wrap full-screen zoomable diagrams/images in `.pinch-zoom-container { touch-action: pan-x pan-y pinch-zoom; }` and provide a 1-click `🔍 切換 200% 放大` button.
4. **Mobile Home-Screen Shortcut Icon (PWA / GAS Web App)**:
   - For standard web apps, include `<link rel="apple-touch-icon">` and `<link rel="icon">`.
   - For Google Apps Script (GAS) Web Apps, inject `.setTitle()` and `.setFaviconUrl('https://lh3.googleusercontent.com/d/<FILE_ID>')` on `HtmlOutput` in `doGet()` so Android/iOS home-screen shortcuts display custom high-res icons instead of a generic gray icon.

---

### 5. Zero-Server & Single-File Offline HTML Architecture (零伺服器與單一檔案封裝)

1. **Avoid `file://` CORS Failures**:
   - Never rely on `fetch('./data.json')` for local static apps (blocked by browser CORS under `file://`). Instead, load data via `<script src="data.js"></script>` defining `window.APP_DATA = [...]`, or inline directly.
2. **Single-File All-in-One Bundle (`scripts/bundle_single_html.py`)**:
   - For effortless sharing via LINE, AirDrop, Email, or iPad Files App, use `scripts/bundle_single_html.py` to inline the local Tailwind CSS engine, JavaScript data files, and compressed Base64 images (`data:image/jpeg;base64,...`) into a single self-contained `.html` file.

---

## Quick Start & Reference Files

- **Interactive Starter Showcase (`index.html` / `examples/ui_showcase_starter.html`)**:
  Open `index.html` (or `examples/ui_showcase_starter.html`) in any browser to explore a live, interactive kitchen-sink demonstration of all UI components, dual themes, flowchart nodes, and mobile touch bars.
- **Single-File Bundler Script (`scripts/bundle_single_html.py`)**:
  ```bash
  uv run --with pymupdf python scripts/bundle_single_html.py \
    --html index.html \
    --output App_Standalone_Bundle.html
  ```
