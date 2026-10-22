# 🎨 Modern Dashboard UI & Offline SPA Design Skill (`modern-dashboard-ui-skill`)

一套可公開分享、跨 AI 工具通用的 **「現代雙主題戰情室網頁設計規範與單檔離線打包技能」**。
將現代網頁工程最佳實踐（`modern-web-guidance`、`building-data-apps`、行動端無障礙觸控、以及零伺服器單一檔案封裝）濃縮為一套隨插即用的設計規範與互動範本。

🔗 **線上互動展示室（Live UI Showcase - 直接體驗深淺主題切換與元件）**：
👉 **[https://snake3210.github.io/modern-dashboard-ui-skill/](https://snake3210.github.io/modern-dashboard-ui-skill/)**

---

## ✨ 五大網頁設計精華規範

1. **🌙 / ☀️ 雙主題高對比配色系統（Dual-Theme Design Tokens）**
   - **深色科技戰情室（Dark Tactical Mode）**：深海藍黑底（`#060b14`）、毛玻璃頂部導覽列（`backdrop-blur-md`）、語義化四色指標（翡翠綠 `#10b981` 達標/終點、醫療青 `#06b6d4` 焦點、琥珀黃 `#f59e0b` 警示、珊瑚紅 `#f43f5e` 危險）。
   - **明亮護眼模式（Light Eye-Care Mode）**：一鍵切換 CSS 變數與類別自動反轉，確保白底環境下依然維持高對比度。

2. **📐 字體雙軌制與 12 欄黃金響應式排版**
   - **內文與標題**：`Noto Sans TC` 無襯線字體，最小字級不低於 `12px`。
   - **數據、題號、百分比、快捷鍵**：強制使用 `JetBrains Mono` 等寬字體，數字跳動時版面零位移。
   - **桌機雙欄 / 行動端單欄**：桌機寬螢幕採 `lg:grid-cols-12`（左 7 欄主內容互動、右 5 欄視覺化流程節點與拆解卡），免除上下來回捲動。

3. **🧠 拒絕文字牆！三大視覺化拆解元件**
   - **漸層進程節點圖（Step-by-Step Flowchart）**：將複雜邏輯拆解為編號節點，最後一個結論節點（`isLast`）自動套用翡翠綠發光邊框。
   - **三層正則表達式自動上色引擎（Regex Highlighter）**：自動將 `**粗體**` 轉為琥珀黃、`` `反引號口訣` `` 轉為青色膠囊框、並自動高亮領域關鍵字。
   - **分頁式速查表抽屜（Tabbed Cheat Sheet Modal）**：將高頻數據或比較表收納於頂部一鍵彈出抽屜。

4. **📱 手機與平板滿分觸控體驗（Mobile/Tablet UX）**
   - **底部常駐懸浮快速操作列（Sticky Bottom Bar）**：符合單手大拇指熱區。
   - **零點擊延遲與雙指無段縮放**：全域套用 `touch-action: manipulation`，圖表燈箱支援原生雙指縮放（Pinch-to-Zoom）與 200% 倍率切換。
   - **手機桌面捷徑圖示（GAS / PWA）**：整合 Google Apps Script `setFaviconUrl` 與 Google Drive 直連 CDN 圖示技巧。

5. **📦 零伺服器依賴（Zero-Server）與單一 HTML 離線封裝**
   - 內附 `scripts/bundle_single_html.py` 自動打包工具，將外部 JS 與圖片轉為最佳化 Base64 內嵌至單一 `.html` 檔，透過 LINE / AirDrop 傳到手機或 iPad 點開即用。

---

## 🚀 如何安裝與分享給朋友使用？

### 方式 A：安裝為 Antigravity / Claude Code / Cursor 全域技能
```bash
git clone https://github.com/snake3210/modern-dashboard-ui-skill.git "$HOME/.gemini/config/skills/modern-dashboard-ui-skill"
```

### 方式 B：直接打開線上展示室複製 Prompt 貼給任何 AI（ChatGPT / Gemini / Claude）
直接開啟 **[線上展示室網址](https://snake3210.github.io/modern-dashboard-ui-skill/)**，點擊右上角 **「⚡ 一鍵複製 AI 設計指令」**，貼給你的 AI 即可！
