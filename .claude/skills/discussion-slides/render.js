#!/usr/bin/env node
// Render a seminar discussion deck in the house style (see SKILL.md).
// Usage: NODE_PATH=<dir with pptxgenjs> node render.js content.js out.pptx [path/to/apply_theme.js]
const path = require("path");
const pptxgen = require("pptxgenjs");
const SLIDES = require(path.resolve(process.argv[2]));
const OUT = process.argv[3];
const APPLY_THEME = process.argv[4];

// House style: LMU-green accent (approximation, not the official template), Arial, white content slides.
const S = { font: "Arial", fg: "1A1A1A", accent: "00883A", muted: "5F6368", panel: "F1F3F2", panelA: "E3F1E8", panelB: "ECECEC", onDark: "FFFFFF", onDarkSoft: "E3F1E8" };
const SIZE = { header: 40, titleSlide: 44, section: 48, body: 22, bodyWithStats: 20, question: 26, hook: 18, position: 20, positionLabel: 22, table: 20, foot: 18, stat: 36, statLabel: 18, closing: 48, slideNo: 11 };

const pres = new pptxgen(); pres.layout = "LAYOUT_WIDE"; pres.theme = { headFontFace: S.font, bodyFontFace: S.font };
const M = 0.7, W = 13.333 - 2 * M; let n = 0;
// Content slides: no footer text, slide number only.
pres.defineSlideMaster({ title: "CONTENT", background: { color: "FFFFFF" }, slideNumber: { x: 12.3, y: 6.95, w: 0.6, h: 0.35, fontSize: SIZE.slideNo, color: S.muted, fontFace: S.font }, objects: [] });
pres.defineSlideMaster({ title: "GREEN", background: { color: S.accent } });

const t = (s, x, o) => s.addText(x, Object.assign({ isTextBox: true, fontFace: S.font, color: S.fg, valign: "top", margin: 0 }, o));
const box = (s, x, y, w, h, c) => s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.06, fill: { color: c }, line: { color: c }, objectName: "panel" + (n++) });
const header = (s, h) => t(s, h, { x: M, y: 0.4, w: W, h: 0.9, fontSize: SIZE.header, bold: true, color: S.accent, valign: "middle" });

let section = null;
for (const d of SLIDES) {
  if (["title", "section", "closing"].includes(d.type)) { section = d.type === "title" ? "Opening" : d.type === "closing" ? "Close" : d.title; pres.addSection({ title: section }); }
  const green = ["title", "section", "closing"].includes(d.type);
  const s = pres.addSlide({ masterName: green ? "GREEN" : "CONTENT", sectionTitle: section });
  if (d.type === "title") {
    t(s, d.title, { x: M, y: 2.2, w: W, h: 1.6, fontSize: SIZE.titleSlide, bold: true, color: S.onDark, valign: "bottom" });
    if (d.sub) t(s, d.sub, { x: M, y: 4.0, w: W, h: 1.0, fontSize: 22, color: S.onDark });
    if (d.sub2) t(s, d.sub2, { x: M, y: 5.2, w: W, h: 0.5, fontSize: 16, color: S.onDarkSoft });
  } else if (d.type === "section") {
    t(s, d.title, { x: M, y: 2.4, w: W, h: 1.2, fontSize: SIZE.section, bold: true, color: S.onDark, valign: "bottom" });
    if (d.sub) t(s, d.sub, { x: M, y: 3.8, w: W * 0.85, h: 1.2, fontSize: 20, color: S.onDarkSoft });
  } else if (d.type === "closing") {
    t(s, d.title, { x: M, y: 2.8, w: W, h: 1.5, fontSize: SIZE.closing, bold: true, color: S.onDark, valign: "middle" });
  } else if (d.type === "index") {
    header(s, d.header || "Index");
    d.items.forEach((it, i) => { const y = 1.7 + i * 0.7;
      t(s, String(i + 1).padStart(2, "0"), { x: M, y, w: 0.8, h: 0.55, fontSize: 22, bold: true, color: S.accent, valign: "middle" });
      t(s, it, { x: M + 0.9, y, w: W - 0.9, h: 0.55, fontSize: 22, valign: "middle" }); });
  } else if (d.type === "content") {
    header(s, d.header); let y = 1.6;
    if (d.stats) { d.stats.forEach((st, i) => { const w = (W - 0.6) / 3, x = M + i * (w + 0.3); box(s, x, y, w, 1.15, S.panel);
        t(s, st[0], { x: x + 0.25, y: y + 0.12, w: 1.8, h: 0.9, fontSize: SIZE.stat, bold: true, color: S.accent, valign: "middle" });
        t(s, st[1], { x: x + 2.0, y: y + 0.12, w: w - 2.2, h: 0.9, fontSize: SIZE.statLabel, color: S.muted, valign: "middle" }); }); y += 1.45; }
    t(s, d.bullets.map((b, i) => ({ text: b, options: { bullet: { indent: 22 }, breakLine: i < d.bullets.length - 1, paraSpaceAfter: 10 } })),
      { x: M, y, w: W, h: 6.8 - y, fontSize: d.stats ? SIZE.bodyWithStats : SIZE.body });
  } else if (d.type === "table") {
    header(s, d.header);
    s.addTable(d.rows.map((r, i) => r.map((c, j) => ({ text: c, options: { bold: i === 0 || j === 0, color: i === 0 ? "FFFFFF" : S.fg, fill: { color: i === 0 ? S.accent : (i % 2 ? S.panel : "FFFFFF") }, fontSize: SIZE.table, fontFace: S.font } }))),
      { x: M, y: 1.7, w: W, rowH: 0.7, border: { type: "solid", pt: 1, color: "FFFFFF" }, margin: 0.1 });
    if (d.foot) t(s, d.foot, { x: M, y: 1.7 + d.rows.length * 0.7 + 0.35, w: W, h: 1.0, fontSize: SIZE.foot, color: S.muted });
  } else if (d.type === "question") {
    header(s, d.header);
    t(s, d.question, { x: M, y: 1.45, w: W, h: 0.9, fontSize: SIZE.question, bold: true });
    box(s, M, 2.45, W, 1.3, S.panel); t(s, d.hook, { x: M + 0.3, y: 2.58, w: W - 0.6, h: 1.1, fontSize: SIZE.hook });
    const w = (W - 0.3) / 2;
    [[d.a, S.panelA, S.accent], [d.b, S.panelB, S.fg]].forEach((p, i) => { const x = M + i * (w + 0.3); box(s, x, 3.95, w, 2.65, p[1]);
      t(s, p[0][0], { x: x + 0.3, y: 4.1, w: w - 0.6, h: 0.5, fontSize: SIZE.positionLabel, bold: true, color: p[2] });
      t(s, p[0][1], { x: x + 0.3, y: 4.7, w: w - 0.6, h: 1.7, fontSize: SIZE.position }); });
  }
  if (d.notes) s.addNotes(d.notes);
}
(async () => {
  await pres.writeFile({ fileName: OUT });
  if (APPLY_THEME) { const { applyTheme } = require(path.resolve(APPLY_THEME));
    await applyTheme(OUT, { name: "Seminar Green", headFontFace: S.font, bodyFontFace: S.font, colors: { dk1: S.fg, lt1: "FFFFFF", dk2: S.accent, lt2: S.panel, accent1: S.accent, accent2: S.fg, accent3: S.muted, accent4: S.panelA, accent5: S.panelB, accent6: S.panel, hlink: S.accent, folHlink: S.muted } }); }
  console.log("wrote " + OUT);
})();
